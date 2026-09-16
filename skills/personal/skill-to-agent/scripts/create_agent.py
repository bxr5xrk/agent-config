#!/usr/bin/env python3
"""Create or update a persistent Codex agent around an existing skill."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import tomllib
from pathlib import Path


NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
REQUIRED_PROFILE_FILES = (
    "config.toml",
    "AGENTS.md",
    "SOUL.md",
    "MEMORY.md",
    "memory/CANDIDATES.md",
)
INHERITANCE_COMMENT = (
    "# Model policy: omit model and model_reasoning_effort to inherit both from the parent."
)


def parse_args() -> argparse.Namespace:
    repo_root = Path(__file__).resolve().parents[4]
    parser = argparse.ArgumentParser(
        description="Create a thin persistent Codex agent around an existing SKILL.md."
    )
    parser.add_argument("--skill", type=Path, required=True, help="Absolute path to SKILL.md")
    parser.add_argument("--agent-name", help="Lowercase kebab-case name; defaults to <skill-name>-agent")
    parser.add_argument("--description", help="Delegation-oriented custom-agent description")
    parser.add_argument("--agents-root", type=Path, default=repo_root / "agents")
    parser.add_argument("--install-root", type=Path, default=Path.home() / ".codex" / "agents")
    parser.add_argument("--install", action="store_true", help="Hard-link config into the Codex agents directory")
    parser.add_argument("--replace-install", action="store_true", help="Replace a different installed config")
    parser.add_argument("--update", action="store_true", help="Refresh generated files and preserve profile memory")
    return parser.parse_args()


def read_skill_metadata(path: Path) -> tuple[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"{path} has no YAML frontmatter")
    try:
        frontmatter = text.split("---\n", 2)[1]
    except IndexError as exc:
        raise ValueError(f"{path} has incomplete YAML frontmatter") from exc

    name_match = re.search(r"(?m)^name:\s*[\"']?([^\n\"']+)", frontmatter)
    if not name_match:
        raise ValueError(f"{path} frontmatter has no name")
    name = name_match.group(1).strip()

    description = ""
    description_match = re.search(
        r"(?ms)^description:\s*(?:>-?\s*\n(?P<block>(?:[ \t]+.*\n?)+)|[\"']?(?P<line>[^\n\"']+))",
        frontmatter,
    )
    if description_match:
        raw = description_match.group("block") or description_match.group("line") or ""
        description = " ".join(line.strip() for line in raw.splitlines()).strip()
    return name, description


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def create_profile_files(target: Path, agent_name: str, skill_name: str) -> None:
    soul = f"""# Soul

You are the persistent `{agent_name}` specialist. Apply the `{skill_name}` workflow with clear judgment, direct communication, and respect for the current project's constraints.

Do not invent preferences or treat one project decision as a universal rule. Refine this identity only from explicit feedback or repeated evidence.
"""
    memory = """# Validated memory

No cross-project preferences have been validated yet.
"""
    candidates = """# Learning candidates

Keep this local file out of Git. Record at most one concise candidate only when
it materially changes future decisions and is explicitly requested as global
memory or corroborated across at least 3 independent projects within 30 days.
Check existing memory first and prefer updating, merging, superseding, or
deleting. Never store project names, facts, paths, selected directions,
temporary state, one-offs, raw evidence, secrets, or project-document content.

No candidates yet.
"""
    write_text(target / "SOUL.md", soul)
    write_text(target / "MEMORY.md", memory)
    write_text(target / "memory" / "CANDIDATES.md", candidates)


def generated_agents_md(
    agent_name: str, skill_name: str, skill_path: Path, target: Path
) -> str:
    return f"""# {agent_name}

Before working, read `{target / 'SOUL.md'}` and local `{target / 'MEMORY.md'}` when present, then inspect the current project's applicable instructions and domain documents. Follow the canonical `{skill_name}` workflow at `{skill_path}` and load only the references it routes to for the current task.

Use this priority order:

1. The current user request and authorization boundaries.
2. Current-project instructions, contracts, and domain documents.
3. Validated cross-project `MEMORY.md`.
4. `SOUL.md` and the source skill.

Work as a specialist, not as a generic assistant. Keep the source skill canonical; do not duplicate its workflow here.

## Learning

Apply feedback to the current task first. Persist at most one concise memory item only when it is durable cross-project guidance that materially changes future decisions and either the user explicitly asks to remember it globally or it is corroborated across at least 3 independent projects within 30 days.

- Before writing, inspect existing memory and prefer updating, merging, superseding, or deleting an entry over adding one.
- Keep project-specific knowledge in project documentation. Never store project names, facts, paths, selected directions, temporary task state, one-off praise or corrections, raw evidence, speculation, secrets, employer-private information, or content better kept in project documents.
- Stage universal domain-method improvements as exact source-skill changes and universal workflow or response-policy corrections as exact global `AGENTS.md` changes. Publish either only after the user's batch approval.
- If this agent cannot write the canonical destination, return at most one eligible proposed entry to the primary agent.
"""


def generated_config(agent_name: str, description: str, target: Path, skill_path: Path) -> str:
    instruction = (
        f"Before doing specialist work, read and follow {target / 'AGENTS.md'}.\n"
        f"Use {skill_path} as the canonical workflow and load only the references it routes to for the current task."
    )
    return (
        f"name = {json.dumps(agent_name)}\n"
        f"description = {json.dumps(description)}\n"
        f"{INHERITANCE_COMMENT}\n"
        f"developer_instructions = {json.dumps(instruction)}\n"
    )


def install_hard_link(source: Path, destination: Path, replace: bool) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    if destination.exists() or destination.is_symlink():
        if destination.exists() and os.path.samefile(source, destination):
            return
        if not replace:
            raise FileExistsError(
                f"{destination} already exists and is not linked to {source}; use --replace-install"
            )
        destination.unlink()
    os.link(source, destination)


def validate_profile(target: Path, skill_path: Path) -> None:
    missing = [relative for relative in REQUIRED_PROFILE_FILES if not (target / relative).is_file()]
    if missing:
        raise ValueError(f"missing profile files: {', '.join(missing)}")
    with (target / "config.toml").open("rb") as handle:
        config = tomllib.load(handle)
    for key in ("name", "description", "developer_instructions"):
        if not config.get(key):
            raise ValueError(f"config.toml is missing {key}")
    if str(skill_path) not in config["developer_instructions"]:
        raise ValueError("config.toml does not reference the source skill")
    for key in ("model", "model_reasoning_effort"):
        if key in config:
            raise ValueError(f"config.toml must omit {key} so the agent inherits from its parent")
    if INHERITANCE_COMMENT not in (target / "config.toml").read_text(encoding="utf-8"):
        raise ValueError("config.toml does not document parent model inheritance")


def main() -> int:
    args = parse_args()
    if not args.skill.expanduser().is_absolute():
        raise ValueError("--skill must be an absolute path to SKILL.md")
    skill_path = args.skill.expanduser().resolve()
    if skill_path.name != "SKILL.md" or not skill_path.is_file():
        raise ValueError("--skill must point to an existing absolute SKILL.md")
    skill_name, skill_description = read_skill_metadata(skill_path)
    agent_name = args.agent_name or f"{skill_name}-agent"
    if len(agent_name) > 64 or not NAME_RE.fullmatch(agent_name):
        raise ValueError("--agent-name must be kebab-case with at most 64 characters")
    description = args.description or f"Persistent {skill_name} specialist. {skill_description}".strip()

    target = args.agents_root.expanduser().resolve() / agent_name
    existed = target.exists()
    if existed and not args.update:
        raise FileExistsError(f"{target} already exists; use --update to refresh generated files")
    target.mkdir(parents=True, exist_ok=True)

    if not existed:
        create_profile_files(target, agent_name, skill_name)
    else:
        missing_profile = any(
            not (target / relative).exists()
            for relative in ("SOUL.md", "MEMORY.md", "memory/CANDIDATES.md")
        )
        if missing_profile:
            raise ValueError("existing profile is incomplete; repair it explicitly before --update")

    write_text(target / "AGENTS.md", generated_agents_md(agent_name, skill_name, skill_path, target))
    write_text(target / "config.toml", generated_config(agent_name, description, target, skill_path))
    validate_profile(target, skill_path)

    installed = None
    if args.install:
        installed = args.install_root.expanduser().resolve() / f"{agent_name}.toml"
        install_hard_link(target / "config.toml", installed, args.replace_install)
        if not os.path.samefile(target / "config.toml", installed):
            raise ValueError("installed config is not a hard link to the canonical config")

    print(f"agent={target}")
    print(f"skill={skill_path}")
    if installed:
        print(f"installed={installed}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(2)
