#!/usr/bin/env python3
import json
import sys

# Keep this hook domain-agnostic. Do not add keyword- or task-specific branches.


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, OSError):
        return 0

    if payload.get("hook_event_name") != "UserPromptSubmit":
        return 0

    additional_context = """Apply the installed `caveman-uk` skill to this turn. If the prompt appears dictated or loosely structured, silently normalize it into goal, deliverables, constraints, exclusions, and acceptance criteria without changing or dropping the original intent. Answer only what the user asked."""

    print(
        json.dumps(
            {
                "hookSpecificOutput": {
                    "hookEventName": "UserPromptSubmit",
                    "additionalContext": additional_context,
                }
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
