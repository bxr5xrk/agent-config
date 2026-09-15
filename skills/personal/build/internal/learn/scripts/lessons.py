#!/usr/bin/env python3
"""Stage and publish local lessons after human review; no external dependencies."""

import argparse
from contextlib import contextmanager
from datetime import datetime, timezone
import fcntl
import hashlib
import json
import os
from pathlib import Path
import re
import tempfile
import uuid

ROLES = {"all", "brainstorm", "build", "team", "designer", "motion", "frontend", "backend",
         "verify-product", "simplify", "security-review", "learn"}


def now():
    return datetime.now(timezone.utc).isoformat()


def encode(value):
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode()


def digest(value):
    return hashlib.sha256(encode(value)).hexdigest()


def identifier(value):
    if not isinstance(value, str) or not re.fullmatch(r"[a-z0-9][a-z0-9-]{0,95}", value):
        raise ValueError("Invalid identifier")
    return value


def read(path):
    if path.is_symlink():
        raise ValueError("Store entries must not be symlinks")
    return json.loads(path.read_text())


def atomic(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.is_symlink():
        raise ValueError("Refusing to replace a symlink")
    temp = None
    try:
        with tempfile.NamedTemporaryFile(dir=path.parent, delete=False) as stream:
            temp = Path(stream.name)
            stream.write(encode(value))
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temp, path)
    finally:
        if temp and temp.exists():
            temp.unlink()


@contextmanager
def locked(root):
    root.mkdir(parents=True, exist_ok=True)
    with (root / ".lock").open("a+") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        yield


def current(root):
    pointer = root / "CURRENT.json"
    if not pointer.exists():
        if any((root / "versions").glob("*.json")):
            raise ValueError("CURRENT is missing despite version history; recover the pointer explicitly")
        return {"version": None, "rules": {}, "decisions": {}}
    ref = read(pointer)
    value = read(root / "versions" / (identifier(ref["version"]) + ".json"))
    if value.get("version") != ref["version"] or digest(value) != ref["sha256"]:
        raise ValueError("Current snapshot integrity check failed")
    return value


def strings(value):
    return isinstance(value, list) and all(isinstance(v, str) and v.strip() for v in value)


def validate(candidate):
    identifier(candidate.get("id"))
    if candidate.get("role") not in ROLES or candidate.get("kind") not in {"technique", "preference"}:
        raise ValueError("Invalid role or kind")
    for key in ("scope", "rule", "rationale"):
        if not isinstance(candidate.get(key), str) or not candidate[key].strip():
            raise ValueError(f"Missing {key}")
    for key in ("evidence", "exceptions", "supersedes"):
        if not strings(candidate.get(key, [])):
            raise ValueError(f"Invalid {key}")
    if not candidate.get("evidence"):
        raise ValueError("A candidate needs source evidence")
    for previous in candidate.get("supersedes", []):
        identifier(previous)
    verification = candidate.get("verification", {})
    if verification.get("status") not in {"pending", "passed", "failed", "not_applicable"}:
        raise ValueError("Invalid verification status")
    if not strings(verification.get("evidence", [])):
        raise ValueError("Invalid verification evidence")
    return candidate


def candidate_path(root, name):
    return root / "pending" / (identifier(name) + ".json")


def propose(root, candidate, revise=False):
    validate(candidate)
    active = current(root)
    name = candidate["id"]
    if name in active["decisions"]:
        raise ValueError("Decided candidate IDs are immutable; use a new ID")
    path = candidate_path(root, name)
    if path.exists() and not revise:
        raise ValueError("Candidate exists; use revise")
    if revise and not path.exists():
        raise ValueError("Candidate does not exist")
    if path.exists():
        previous = read(path)
        history_path = root / "candidate-history" / (digest(previous) + ".json")
        if not history_path.exists():
            atomic(history_path, previous)
    atomic(path, candidate)
    return {"candidate": name, "status": "pending", "sha256": digest(candidate)}


def make_id(prefix):
    return prefix + "-" + datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S") + "-" + uuid.uuid4().hex[:12]


def batch_identity(batch):
    return "batch-" + digest({k: v for k, v in batch.items() if k != "id"})[:32]


def review(root, names):
    active = current(root)
    if not names:
        names = [p.stem for p in sorted((root / "pending").glob("*.json"))
                 if p.stem not in active["decisions"]]
    if not names or len(names) != len(set(names)):
        raise ValueError("Select one or more unique undecided candidates")
    candidates = []
    for name in names:
        if name in active["decisions"]:
            raise ValueError("Candidate already decided")
        value = validate(read(candidate_path(root, name)))
        if value["id"] != name:
            raise ValueError("Candidate filename and ID disagree")
        candidates.append({"sha256": digest(value), "candidate": value})
    batch = {"base_version": active["version"],
             "created_at": now(), "candidates": candidates}
    batch["id"] = batch_identity(batch)
    batch_path = root / "batches" / (batch["id"] + ".json")
    atomic(batch_path, batch)
    batch_path.with_suffix(".md").write_text(render_review(batch))
    return {"batch": batch["id"], "review": str(batch_path.with_suffix(".md")),
            "candidates": len(candidates)}


def render_review(batch):
    lines = [f"# Review {batch['id']}", "", f"Baseline: {batch['base_version'] or 'empty'}",
             "", "Pending proposals; approval applies only to this exact batch.", ""]
    for entry in batch["candidates"]:
        c = entry["candidate"]
        lines += [f"## {c['id']} · {c['role']}", "", f"Scope: {c['scope']}", "",
                  c["rule"], "", f"Reason: {c['rationale']}", "",
                  "Exceptions: " + "; ".join(c.get("exceptions", [])), "",
                  "Source: " + "; ".join(c["evidence"]), "",
                  f"Verification: {c['verification']['status']}", "",
                  "Evidence: " + "; ".join(c["verification"].get("evidence", [])), "",
                  "Supersedes: " + ", ".join(c.get("supersedes", [])), "",
                  f"Hash: `{entry['sha256']}`", ""]
    return "\n".join(lines)


def commit(root, active, rules, decisions, operation):
    value = {"schema_version": 1, "version": make_id("v"), "parent": active["version"],
             "parent_sha256": digest(active) if active["version"] else None,
             "created_at": now(), "operation": operation, "rules": rules, "decisions": decisions}
    atomic(root / "versions" / (value["version"] + ".json"), value)
    atomic(root / "CURRENT.json", {"version": value["version"], "sha256": digest(value)})
    return {"version": value["version"], "active_rules": len(rules)}


def decide(root, batch_id, approval_reference, accept):
    if not approval_reference.strip():
        raise ValueError("Record the actual human decision reference")
    active = current(root)
    batch_path = root / "batches" / (identifier(batch_id) + ".json")
    batch = read(batch_path)
    if batch_identity(batch) != batch_id:
        raise ValueError("Batch content or membership changed after review")
    review_path = batch_path.with_suffix(".md")
    if review_path.is_symlink() or review_path.read_text() != render_review(batch):
        raise ValueError("Readable review changed; regenerate and review a fresh batch")
    if batch.get("id") != batch_id or batch["base_version"] != active["version"]:
        raise ValueError("Stale batch: review against the current baseline")
    rules, decisions = dict(active["rules"]), dict(active["decisions"])
    changed = set()
    for entry in batch["candidates"]:
        c = validate(entry["candidate"])
        name = c["id"]
        if name in decisions or digest(c) != entry["sha256"]:
            raise ValueError("Duplicate, decided or changed batch entry")
        if digest(read(candidate_path(root, name))) != entry["sha256"]:
            raise ValueError("Candidate changed after review")
        if accept:
            v = c["verification"]
            tested = v["status"] == "passed" and bool(v.get("evidence"))
            preference = c["kind"] == "preference" and v["status"] == "not_applicable"
            if not (tested or preference):
                raise ValueError("Technique needs passed forward-test evidence before publication")
            for old in c.get("supersedes", []):
                if old not in rules or old in changed or old == name:
                    raise ValueError("Invalid or conflicting superseded lesson")
                rules.pop(old)
                changed.add(old)
            rules[name] = c
        decisions[name] = {"status": "approved" if accept else "rejected",
                           "sha256": entry["sha256"], "batch": batch_id}
    return commit(root, active, rules, decisions,
                  {"type": "approve" if accept else "reject", "batch": batch_id,
                   "approval_reference": approval_reference})


def rollback(root, version, approval_reference):
    if not approval_reference.strip():
        raise ValueError("Record the actual human decision reference")
    active = current(root)
    identifier(version)
    if version == "empty":
        return commit(root, active, {}, active["decisions"],
                      {"type": "rollback", "to": "empty", "approval_reference": approval_reference})
    target = active
    while target["version"] != version:
        previous_id = target.get("parent")
        if not previous_id:
            raise ValueError("Target is not in the published version history")
        previous = read(root / "versions" / (identifier(previous_id) + ".json"))
        if previous.get("version") != previous_id or digest(previous) != target["parent_sha256"]:
            raise ValueError("Historical snapshot integrity check failed")
        target = previous
    return commit(root, active, target["rules"], active["decisions"],
                  {"type": "rollback", "to": version, "approval_reference": approval_reference})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--store",
        type=Path,
        default=Path.home() / ".agents" / "knowledge" / "specialists",
    )
    commands = parser.add_subparsers(dest="command", required=True)
    for command in ("propose", "revise"):
        commands.add_parser(command).add_argument("--candidate", type=Path, required=True)
    commands.add_parser("review").add_argument("ids", nargs="*")
    for command in ("approve", "reject"):
        sub = commands.add_parser(command)
        sub.add_argument("--batch", required=True)
        sub.add_argument("--approval-reference", required=True)
    commands.add_parser("recall").add_argument("--role", choices=sorted(ROLES), required=True)
    commands.add_parser("history")
    sub = commands.add_parser("rollback")
    sub.add_argument("--to", required=True)
    sub.add_argument("--approval-reference", required=True)
    args = parser.parse_args()
    root = args.store.resolve()
    try:
        with locked(root):
            if args.command in {"propose", "revise"}:
                result = propose(root, read(args.candidate), args.command == "revise")
            elif args.command == "review":
                result = review(root, args.ids)
            elif args.command in {"approve", "reject"}:
                result = decide(root, args.batch, args.approval_reference, args.command == "approve")
            elif args.command == "rollback":
                result = rollback(root, args.to, args.approval_reference)
            elif args.command == "history":
                result = [{k: v[k] for k in ("version", "parent", "operation")}
                          for p in sorted((root / "versions").glob("*.json")) for v in [read(p)]]
            else:
                result = [{k: v.get(k) for k in ("id", "role", "scope", "rule", "exceptions")}
                          for v in current(root)["rules"].values() if v["role"] in {"all", args.role, "team" if args.role == "build" else args.role}]
        print(json.dumps(result, ensure_ascii=False, indent=2))
    except (ValueError, KeyError, OSError, TypeError) as error:
        parser.exit(2, f"Error: {error}\n")


if __name__ == "__main__":
    main()
