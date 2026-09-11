#!/usr/bin/env python3
"""Create a technical starter after recorded product and design decisions."""
import argparse
import json
from pathlib import Path
import re
import shutil

SKILL = Path(__file__).resolve().parents[1]
PROFILES = {"api": ("api",), "web": ("web",), "fullstack": ("api", "web")}


def validate_state(state, profile):
    if not isinstance(state, dict) or state.get("schema_version") != 1:
        raise ValueError("Expected onboarding state schema_version 1")
    if state.get("profile") != profile:
        raise ValueError("Requested profile must match the agreed state")
    if state.get("brief_agreed") is not True:
        raise ValueError("Agree the product brief before generating the project")
    if "web" in PROFILES[profile]:
        design = state.get("design", {})
        if not isinstance(design, dict):
            raise ValueError("Expected a design decision object")
        selected = design.get("selected_ids")
        if design.get("status") == "selected":
            if not isinstance(selected, list) or not selected or not all(isinstance(x, str) and x.strip() for x in selected):
                raise ValueError("Record the selected visual option IDs")
        elif design.get("status") == "user_override":
            if not isinstance(design.get("override_reason"), str) or not design["override_reason"].strip():
                raise ValueError("Record the user's explicit design override")
        else:
            raise ValueError("Record the agreed visual direction or explicit design delegation first")


def scaffold(destination, name, profile, state, source_documents=None):
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        raise ValueError("Use a lowercase project name with digits and hyphens")
    if profile not in PROFILES:
        raise ValueError("Unknown profile")
    validate_state(state, profile)
    destination = Path(destination).expanduser()
    if destination.exists() or destination.is_symlink():
        raise FileExistsError("Destination already exists; no files changed")
    required_documents = ["BRIEF.md"]
    if "web" in PROFILES[profile] and state["design"]["status"] == "selected":
        required_documents.append("DESIGN.md")
    for filename in required_documents:
        document = Path(source_documents) / filename if source_documents else None
        if document is None or not document.is_file():
            raise ValueError(f"Missing agreed {filename} beside state.json")
        content = document.read_text().strip()
        template = (SKILL / "assets/documents" / filename).read_text().strip()
        if not content or content == template:
            raise ValueError(f"Expected agreed content in {filename}, not a blank document or template")
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.mkdir()
    for component in PROFILES[profile]:
        shutil.copytree(SKILL / "assets/starter" / component, destination / "apps" / component)
    root = {
        "name": name, "private": True, "packageManager": "pnpm@10.33.0",
        "engines": {"node": ">=24 <27"},
        "scripts": {
            "dev": "pnpm -r --parallel --if-present dev",
            "lint": "pnpm -r --if-present lint",
            "typecheck": "pnpm -r --if-present typecheck",
            "test": "pnpm -r --if-present test",
            "build": "pnpm -r --if-present build",
            "verify": "pnpm lint && pnpm typecheck && pnpm test && pnpm build",
        },
    }
    (destination / "package.json").write_text(json.dumps(root, indent=2) + "\n")
    shutil.copyfile(SKILL / "assets/locks" / (profile + ".yaml"), destination / "pnpm-lock.yaml")
    (destination / "pnpm-workspace.yaml").write_text("packages:\n  - 'apps/*'\n")
    (destination / ".gitignore").write_text("node_modules/\n.next/\ndist/\n*.tsbuildinfo\n.env\n.env.*\n!.env.example\n")
    (destination / ".node-version").write_text("24\n")
    docs = destination / "docs/onboarding"
    docs.mkdir(parents=True)
    for source in (SKILL / "assets/documents").glob("*.md"):
        agreed = Path(source_documents) / source.name if source_documents else None
        if source.name in {"LANDING-REVIEW.md", "BRAND.md"} and not (agreed and agreed.is_file()):
            continue  # Created only when a public landing is in scope.
        if source.name == "DESIGN.md" and profile == "api" and not (agreed and agreed.is_file()):
            (docs / source.name).write_text("# Design contract\n\nSurface: API-only.\nVisual design: not applicable.\n")
            continue
        shutil.copyfile(agreed if agreed and agreed.is_file() else source, docs / source.name)
    next_action = "Implement the first real API journey" if profile == "api" else "Apply agreed design and implement the first real journey"
    new_state = {**state, "phase": "scaffold", "next_action": next_action}
    (docs / "state.json").write_text(json.dumps(new_state, ensure_ascii=False, indent=2) + "\n")
    (docs / "STARTER.md").write_text(
        "# Technical starter\n\nRun `pnpm install --frozen-lockfile`, then `pnpm verify`. Start with `pnpm dev`.\n\n"
        "Fullstack: set API_ORIGIN=http://127.0.0.1:3001 for the web process to exercise the status connection.\n\n"
        "Neutral tokens and sample endpoints are technical examples, not the chosen design or business logic. "
        "Replace them from BRIEF.md/DESIGN.md. Public SEO, Mongo domain data, auth and live analytics "
        "are not implemented by this generator. Add only the required modules and verify them.\n"
    )
    return destination


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("destination", type=Path)
    parser.add_argument("--name", required=True)
    parser.add_argument("--profile", required=True, choices=PROFILES)
    parser.add_argument("--state", required=True, type=Path)
    args = parser.parse_args()
    try:
        state = json.loads(args.state.read_text())
        destination = scaffold(args.destination, args.name, args.profile, state, args.state.parent)
    except (ValueError, OSError) as error:
        parser.exit(2, f"Cannot scaffold: {error}\n")
    print(f"Created technical starter: {destination}")


if __name__ == "__main__":
    main()
