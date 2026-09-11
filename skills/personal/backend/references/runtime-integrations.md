# Runtime, integrations and diagnostics

Bound request bodies, parsing work, dependency calls and concurrency according to the workload. Asynchronous syntax does not move CPU work off Node's event loop. Propagate timeouts/cancellation where supported and distinguish retryable failure from a permanent invalid request. Retry only operations with known idempotency semantics, under a total budget and backoff; reuse the same logical operation key when an outcome is uncertain.

For webhooks, follow the actual provider's signature and raw-body rules before trusting content. Handle duplicate delivery, replay tolerance and out-of-order events as that provider specifies. A transport event ID and a business-operation ID may solve different duplicate problems. Reconcile current source state where ordering cannot be assumed.

Acknowledge success only after the promised work is complete or durably accepted for processing. If durable background work is required, use the existing job system or the smallest suitable durable mechanism. Define retries, terminal failure and recovery. A fire-and-forget promise is not a durable queue. When one operation must commit data and schedule work atomically, use a justified transaction/outbox or equivalent recovery design rather than silently accepting the dual-write gap.

Keep structured logs with safe correlation IDs and actionable operation outcomes. Measure latency/error/queue signals where those failure modes exist; product analytics is not error monitoring. Distinguish readiness from process liveness. Shutdown should stop accepting new work, drain within the deployment deadline and close shared resources without losing acknowledged work.

## Verify

Test the affected failure boundary: slow/unavailable dependency, timeout with uncertain outcome, duplicate delivery, reordered webhook or interruption after durable acceptance. Check the resulting business state, not only HTTP 2xx. Verify signatures against the provider's supported test mechanism where available. A mocked provider proves local handling only; label live integration evidence separately.

Sources checked 2026-09-05: [Node event-loop blocking](https://nodejs.org/learn/asynchronous-work/dont-block-the-event-loop), [Stripe webhooks](https://docs.stripe.com/webhooks), [Stripe idempotent requests](https://docs.stripe.com/api/idempotent_requests), [AWS transactional outbox](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/transactional-outbox.html), [Fastify lifecycle](https://fastify.dev/docs/latest/Reference/Lifecycle/), [Fastify hooks](https://fastify.dev/docs/latest/Reference/Hooks/). Stripe examples establish Stripe behavior; verify another provider's contract separately.
