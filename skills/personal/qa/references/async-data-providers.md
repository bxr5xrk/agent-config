# Async, data, and provider verification

Trace producer, payload, queue/topic, consumer, state transition, retry, terminal
failure, and user-visible outcome. Test duplicate delivery, delayed/stale jobs,
worker restart, cancellation, partial success, concurrency, and poison input when
those paths could alter data or external effects.

For data consistency verify atomic claims, uniqueness/idempotency, tenant scope,
transaction boundaries, indexes, pagination/order, cache invalidation, and read-
after-write expectations. Observe both stored state and emitted events/jobs; one
without the other can hide divergence.

Classify provider evidence:

- stub/fake: application logic against intentionally simplified behavior;
- mock server/recording: HTTP/protocol contract under controlled responses;
- sandbox/test provider: real provider surface with non-production guarantees;
- authorized live smoke: current credentials, network, policy, and provider behavior.

Never report a fake provider as proof that a real send, login, payment, webhook,
AI response, or platform action works. Live evidence is also bounded by account,
region, plan, quota, and date. Keep external-provider tests safe, minimal, and
explicitly authorized.

For queues and databases, an application build or isolated unit suite does not
prove runtime dependencies are reachable or configured. Confirm process startup,
health, consumption, persistence, and observable completion where release claims
depend on them.
