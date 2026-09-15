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

    additional_context = """Honor the user's actual requested outcome. Treat examples, references, and background as context unless explicitly requested. Complete every explicit deliverable, but do not add methodology, internal details, alternatives, or next steps. Match length and structure to the requested deliverable: keep ordinary answers as short as completeness allows, but preserve requested articles, research, code, tables, lists, translations, rewrites, and formatting transformations in full. Never truncate required content or require "continue" merely for brevity. Label uncertainty beside the claim and never turn "not found" into "does not exist". For substantive work, follow the global worker-and-reviewer policy."""

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
