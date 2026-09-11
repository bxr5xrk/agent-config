#!/usr/bin/env python3
"""Find canonical project design context; initialize without overwriting it."""

import argparse
import json
from pathlib import Path

EXCLUDED = {"node_modules", ".git", ".next", ".venv", "dist", "build", "vendor"}


def discover(root):
    root = root.resolve(strict=True)
    if not root.is_dir():
        raise ValueError("Project must be a directory")
    found = {"root_design": [], "nested_design": [], "brief": [], "unresolved_links": []}
    pending = [(root, 0)]
    while pending:
        directory, depth = pending.pop()
        for path in sorted(directory.iterdir()):
            if path.name in EXCLUDED:
                continue
            if path.is_symlink():
                if depth == 0 and path.name.casefold() == "design.md":
                    raise ValueError("Root design is a symlink; inspect its authority manually")
                if path.name.casefold() == "design.md" or path.is_dir():
                    found["unresolved_links"].append(str(path))
                continue
            if path.is_file():
                if path.name.casefold() == "design.md":
                    found["root_design" if depth == 0 else "nested_design"].append(str(path))
                elif path.name.casefold() in {"brief.md", "product-brief.md"}:
                    found["brief"].append(str(path))
            elif path.is_dir():
                pending.append((path, depth + 1))
    found["project"] = str(root)
    found["canonical_design"] = found["root_design"][0] if len(found["root_design"]) == 1 else None
    found["conflict"] = len(found["root_design"]) > 1
    return found


def initialize(root, surface):
    context = discover(root)
    if context["conflict"]:
        raise ValueError("Multiple root design documents; reconcile them before initializing")
    if context["canonical_design"]:
        return {"status": "existing", "path": context["canonical_design"]}
    if context["unresolved_links"]:
        raise ValueError("Unresolved linked design/directory; inspect authority before initializing: "
                         + ", ".join(context["unresolved_links"]))
    if len(context["nested_design"]) > 1:
        raise ValueError("Multiple nested design documents; choose the authority before creating an index")
    root = Path(context["project"])
    path = root / "design.md"
    if context["nested_design"]:
        canonical = Path(context["nested_design"][0]).relative_to(root).as_posix()
        text = ("# Design context\n\nStatus: index; verify current decisions against implementation.\n\n"
                f"Canonical project design: [{canonical}]({canonical})\n\n"
                "Update the canonical document; keep this file as the entry point.\n")
    else:
        template = Path(__file__).resolve().parents[1] / "assets" / "design.md"
        text = template.read_text()
        status = "not-applicable" if surface == "api" else "observed"
        text = text.replace("Status: observed | proposed | approved | not-applicable", f"Status: {status}")
        text = text.replace("## Product and surfaces\n", f"## Product and surfaces\nSurface: {surface}.\n")
        if surface == "api":
            text = ("# Design context\n\nStatus: not-applicable\nSurface: API/worker without a user interface.\n\n"
                    "Keep API/domain behavior in the existing brief or architecture document. "
                    "If a visual surface is added, establish its design direction before broad UI implementation.\n")
    with path.open("x") as stream:
        stream.write(text)
    return {"status": "created", "path": str(path)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["inspect", "init"])
    parser.add_argument("project", type=Path)
    parser.add_argument("--surface", choices=["unknown", "landing", "saas", "admin", "api", "native", "mixed"], default="unknown")
    args = parser.parse_args()
    try:
        value = discover(args.project) if args.command == "inspect" else initialize(args.project, args.surface)
        print(json.dumps(value, ensure_ascii=False, indent=2))
    except (ValueError, OSError) as error:
        parser.exit(2, f"Error: {error}\n")


if __name__ == "__main__":
    main()
