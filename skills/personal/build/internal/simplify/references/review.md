# Engineering review and simplification

Trace behavior across the changed boundary, including the caller and data ownership. Check failure handling and concurrency where the change makes them possible. A typed API can still expose another tenant's data or repeat a side effect after a timeout.

Prefer a direct flow when a wrapper, factory, registry or configuration layer has no current consumer benefit. A small local duplication may be clearer than an abstraction that couples unrelated domains. Keep useful module boundaries that hide real complexity; deleting interfaces just to reduce line count is not simplification.

Check whether deleting an interface removes complexity or merely pushes it into each caller. Base architecture changes on observed change friction and real consumers; compare alternative interfaces only when their shape is materially unresolved. Preserve project terminology and useful tests rather than enforcing a universal layer or vocabulary rule.

Look for:

- Derived state duplicated into mutable state; unnecessary effects, memoization and subscriptions.
- Generic hooks/services/components introduced for a single trivial use case.
- Indirection that moves complexity without encapsulating an invariant.
- Catch-all errors, fake success and silent fallbacks that hide a broken integration.
- Retry/cancellation changes that alter duplicate-write or stale-result behavior.
- Global formatting/dependency churn mixed into a narrow fix.
- Tests that assert mocks or implementation details while missing the promised outcome.

Before removing a branch, read its callers and reason. Before merging paths, verify their ownership, authorization and lifecycle are actually the same. Preserve externally observable statuses, event semantics, stable IDs and recovery paths unless the task changes that contract.

Use behavior checks proportionate to risk: existing tests for a harmless refactor, a targeted negative-path regression for a real bug, runtime/browser checks for UI or integration changes. Do not add a test solely to mirror a short reversible presentation edit. Review code and tests together; a passing test rewritten to match the mistake is weak evidence.

Report defects with a reproduction or concrete argument, not speculative best-practice violations. Optional style changes should not block completion. Scope any verdict to files and behaviors actually reviewed.

Primary reference: [Google's code-review criteria](https://google.github.io/eng-practices/review/reviewer/looking-for.html). The applied goal is understandable, correct code and useful tests, with no speculative abstractions; the bullets above also reflect this workflow's integration and ownership requirements.

Also informed by AI Hero [codebase-design](https://github.com/mattpocock/skills/blob/3cca18b368ae95cdbdebbff572ccafa662551015/skills/engineering/codebase-design/SKILL.md) and [architecture review](https://github.com/mattpocock/skills/blob/3cca18b368ae95cdbdebbff572ccafa662551015/skills/engineering/improve-codebase-architecture/SKILL.md).
