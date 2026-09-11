# Evaluate behavior, not prose

For a reusable technique, derive a held-out task with different content/structure from the incident that suggested the rule, plus a case where the rule must not apply. Give a fresh evaluating agent the task, skill/candidate and minimum raw artifacts, without the intended answer or suspected defect. Inspect its actual actions and resulting artifacts.

Compare the current skill with the candidate when claiming an improvement. Keep the task, runtime/model and tools comparable. Repeat enough cases to distinguish an obvious regression from normal model variability; a single success is a smoke test, not a reliability percentage. Preserve failed cases and contradictory outcomes. Do not tune the held-out task after seeing its result and still call it held out.

Useful outcomes include preserved requirements, successful user action, appropriate questions, correctly scoped edits, real runtime evidence, irrelevant-rule avoidance and unchanged privacy boundaries. Do not use output length, number of headings, line count or presence of keywords as a quality metric.

For visual work, use rendered artifacts and selected references; for motion, include triggered temporal behavior. For code changes, use a behavioral oracle whose expected outcome was not rewritten by the implementation. Keep evaluation fixtures and reports out of normal task prompts.

An explicit preference such as “use PostHog unless I choose another tool” is validated by provenance and scope, not a model's aesthetic score. A mechanism claim such as “this fixes duplicate requests” needs behavior evidence.

Record `pending`, `passed` or `failed` truthfully with artifact references. Publishing is a user decision after this evidence, never a model-generated approval token. Later regressions create a revision or a rollback, not a silent mutation of history.
