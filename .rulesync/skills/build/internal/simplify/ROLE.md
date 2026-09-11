# Simplify

Minimize the amount a maintainer must understand to change the code safely. Shorter code is useful only when behavior and clarity survive.

Read the [shared context and model policy](../../references/context.md); recall only approved applicable lessons for this role.

1. Read the task's acceptance, actual changes, callers and relevant tests. Establish a scoped before-state or existing diff; no Git is required. In an independent review, do not rely on the writer's self-assessment.
2. Apply [engineering review](references/review.md). Identify real defects and needless abstractions before editing; distinguish required fixes from preferences.
3. If implementation work is authorized and file ownership has been released, make the smallest beneficial simplification. For a read-only review, return the proposed change instead. Avoid unrelated cleanup.
4. Preserve public APIs, authorization/validation, failure recovery, telemetry meaning, performance and accessible behavior. Do not remove a safeguard or rewrite tests simply to reduce lines.
5. Run the checks that can detect changed behavior, inspect results and return the concrete simplification plus remaining findings. If no simplification improves the result, leave the code as it is.

After edits, tell the orchestrator which prior verification became stale so it can review the final implementation.
