# Asynchronous, webhook, and AI boundaries

Background execution moves but does not remove authorization. Persist the minimum
trusted identity and authorization context required by the consumer, or re-resolve
it at execution. Validate job payloads and provider events at consumption; assume
queues, retries, delayed messages, and duplicate delivery can occur.

For webhooks verify authenticity on the raw payload, freshness/replay protection,
event ownership, schema/version, and idempotent processing. Acknowledge only after
durable acceptance. Do not let attacker-selected callback URLs or object IDs cross
tenant boundaries.

For queues and workflows check deterministic idempotency keys, atomic claims,
retry/backoff bounds, poison-message handling, cancellation, stale-job behavior,
and audit correlation. Prevent a retry from repeating charges, messages, exports,
privileged changes, or provider-side effects.

Treat model output, retrieved documents, web content, tool results, and user
prompts as untrusted data. A model may propose an action but must not expand its
authorization. Tools need explicit schemas, server-side policy, scoped credentials,
result validation, bounded retries, and confirmation at consequential external
effects. Separate instructions from quoted/retrieved content and prevent secrets
from entering model context unless strictly required and approved.

Rate limits and quotas are security controls when they bound cost, abuse, account
health, or feedback loops. Preserve per-tenant/per-identity isolation and atomic
enforcement under concurrency.
