# Security review and release

Scope the review to the actual change and adjacent reachable paths. Start with
changed trust boundaries, new data flows, dependencies, privilege, external
effects, and rollback implications. Use static inspection, existing tests, and
safe local/integration validation before any active network testing.

A finding should include the violated property, affected asset/actor, source-to-
sink path, preconditions, reproducible evidence, impact, existing mitigation,
severity rationale, and minimal remediation. Distinguish validated findings,
plausible concerns needing evidence, hardening opportunities, and platform-policy
risks. Do not inflate severity or claim exploitation from a suspicious pattern.

Remediate at the enforcing boundary, then verify both allowed and denied behavior.
Regression tests should exercise the original bypass condition and avoid embedding
real credentials or attack infrastructure. Recheck logging, migrations, queues,
caches, and alternate routes when they share the property.

Release gates for a relevant change include:

- no unresolved high-impact reachable authorization or secret exposure path;
- scoped credentials and configuration verified for the target environment;
- replay/idempotency/rollback behavior checked for consequential effects;
- dependency/provider risk and emergency disable path understood;
- audit/alert evidence sufficient to detect abuse or failed enforcement.

When a risk is accepted, record owner, scope, rationale, expiry/review date,
compensating controls, and the condition that reopens it. Lack of time is not a
mitigation.
