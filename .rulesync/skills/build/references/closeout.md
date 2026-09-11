# One owner for review, repair and learning

Apply this to implementation by `designer`, `motion`, `frontend` or `backend`. Reading a skill as reference during a read-only review does not start its implementation workflow or another reviewer chain.

- **Delegated builder with an orchestration owner:** perform focused implementation checks, update affected contracts, and return artifacts, evidence, unresolved findings and reusable corrections to that owner. Do not independently spawn the same reviewers. The orchestrator integrates all outputs and owns the final review/repair/learning loop.
- **Standalone builder:** own that same loop for the scoped change. For material behavior/UI changes obtain independent `verify-product` and `simplify` reviews; add `security-review` when trust boundaries change. For API-only work, product verification exercises the contract and consequential failure cases instead of a visual checklist. Wait for the findings, repair accepted issues, and recheck affected final bytes. Small reversible changes use proportionate focused verification.
- **Read-only specialist or reviewer:** return evidence and findings to the requester; do not edit, delegate recursively or promote knowledge merely to complete this workflow.

The delegation prompt identifies the orchestration owner. A strongest-model worker spawned to carry out a direct skill invocation remains a standalone builder unless its caller explicitly owns closeout. The caller must collect and inspect the final result either way. If independent delegation is unavailable, perform sequential checks and report that independent review was unavailable.

After a relevant correction, the owner updates the local decision and uses [learn](../internal/learn/ROLE.md) to stage a justified transferable candidate. Do not invent a lesson after every task or wait for global approval before finishing the current fix. Pending candidates never become product policy. See [review and repair](review-loop.md).
