# Local lesson storage

This is an internal procedure. The active specialist runs `python3 scripts/lessons.py --help` from this role directory; never ask the user to call `$learn`. The default store is `~/.agents/knowledge/specialists/`, resolved relative to this installed helper. It is shared across projects and remains separate from the five public skills. `--store /absolute/path` supports an isolated evaluation store. No network, Git or external database is used.

```text
propose --candidate candidate.json     Stage a new candidate
revise --candidate candidate.json      Revise an undecided candidate; old batches become stale
review [candidate-id ...]              Save exact batch JSON and a readable Markdown review
approve --batch batch-id --approval-reference "actual user message reference"
reject --batch batch-id --approval-reference "actual user message reference"
recall --role designer                 Return only approved applicable-role lessons
history                               List local versions and operations
rollback --to version-id --approval-reference "actual user message reference"
rollback --to empty --approval-reference "actual user message reference"
```

`review` with no IDs selects all undecided candidates. Split into smaller batches when the user accepts only part of a proposed set. Generic technique candidates cannot be approved while evaluation is pending/failed; preferences may use `not_applicable` with direct user provenance.

The helper stores immutable snapshots and atomically switches the current pointer under a process lock. The batch ID binds its full content; baseline/candidate hashes and comparison with the readable review reject altered or stale approvals. Superseded lesson IDs leave active recall. Rollback creates a new version with an earlier rule set (or the initial empty set) while retaining decision history. A missing current pointer with existing history is a recovery error, not an empty store.

The approval reference is an audit record supplied after real user approval, not a cryptographic permission. An agent or program with ordinary filesystem access could bypass this helper. The workflow therefore forbids other tools from mutating approved knowledge or treating a string as proof of consent. This is an accidental-change safeguard, not an OS security boundary.

Keep candidates/evidence redacted and local. Do not place customer payloads, cookies, credentials or copied private conversations in the store. Native Codex generated memories are separate and are not modified by this helper.

The legacy stored role `team` is recalled by `build` for compatibility; it is not a separate public skill.
