# Observability, incidents, and runbooks

Instrument the user/system journey: request or job accepted, dependency calls,
state transitions, external effects, and terminal outcome. Use structured logs,
metrics, traces, and durable events with a shared correlation key. Exclude secrets,
message contents, raw tokens, passwords, and unnecessary personal data.

Health should distinguish liveness from readiness. Liveness answers whether the
process should be restarted; readiness answers whether it can safely receive the
intended work. Include critical dependency and worker lag signals without making a
transient optional provider take down unrelated service paths.

Alerts need a user/business impact, threshold/window, routing owner, and linked
runbook. Prefer symptoms such as error ratio, queue age, delivery failure, login
pool exhaustion, or data divergence over raw host noise. Verify that the alert can
fire and that notification failure is itself visible.

Incident flow:

1. declare scope, severity, owner, timeline, and change freeze proportional to risk;
2. preserve evidence and identify last known good/change correlation;
3. contain blast radius with the safest reversible control;
4. restore the critical journey and verify observable outcomes;
5. reconcile data/jobs/external side effects;
6. document cause, contributing conditions, detection gap, and owned follow-ups.

Runbooks contain prerequisites, exact safe checks, decision points, rollback,
verification, and escalation. Test them against the current environment; commands
that once worked are not evidence that the runbook remains valid.
