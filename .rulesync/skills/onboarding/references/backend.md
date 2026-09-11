# Backend practice

Keep transport, domain decisions and persistence distinct where that separation helps testing. Start with small domain modules, not mandatory controller/service/repository classes for every endpoint.

- Parse environment once at startup and fail clearly on missing required values without logging secrets. Reuse one Mongo connection pool per process; close on shutdown.
- Define request schemas for params/query/body and output schemas for public responses. Never accept unrestricted Mongo query objects from clients. Runtime validation remains required with TypeScript.
- Authenticate identity, then authorize the operation and resource ownership/tenant on the server. UI hiding is not authorization; never trust a caller's tenantId independently of identity.
- Paginate collections; bound limit/body size/request timeout; whitelist sort/filter fields. Preserve precise money semantics (minor units + currency) and explicit timezone rules.
- Translate expected domain errors into stable status/code/message; hide internal exceptions. Log safe structured fields, request ID and timing. Avoid full request bodies, authorization headers and database URLs.
- Bound outbound API time and retries, honor rate limits and Retry-After, validate response shape. Retry reads or idempotent operations only; use provider idempotency keys/deduplication for side effects. Do not retry arbitrary POST blindly.
- Webhooks require provider signature verification over the required raw body, timestamp/replay handling, deduplication and durable acknowledgment semantics. A successful acknowledgment must not silently lose the event.
- Long-running work belongs in a durable worker when the brief needs it. A promise launched after sending a response is not a job queue. Add Redis/BullMQ only for actual job requirements.
- Graceful shutdown stops intake and drains/closes resources with a deadline. Separate liveness from readiness: readiness checks required dependencies, not merely process existence.
- Security boundary tests: unauthenticated, forbidden, wrong tenant, invalid payload, duplicate action, unavailable provider. Keep CORS explicit; cookie authentication requires the applicable CSRF protection.

Starter Fastify validates a sample echo endpoint and health; it deliberately contains no invented business/auth logic. Before exposing a real private endpoint implement its actual policy and tests. [Fastify validation](https://fastify.dev/docs/latest/Reference/Validation-and-Serialization/) documents schemas and warns against doing async DB access in initial validation; place authorization/data checks in the appropriate hook/handler.

See [external API example](../examples/external-api.ts) and [data migrations](data-migrations.md).
