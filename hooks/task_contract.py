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

    additional_context = """Apply the installed `caveman-uk` skill to this turn. For a newly composed ordinary answer, use one short paragraph or at most five bullets and no more than 250 words. Do not apply this envelope when the user explicitly requests different length or detail, or when the requested output is a content-preserving transformation or an artifact whose size or coverage is defined by supplied content or an explicit deliverable. Correctness, safety, and irreversible-action clarity override the envelope. After research, delegation, or review, compress the final draft once more."""

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
