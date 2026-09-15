# Data, queues, and workers

For Mongo/Postgres and other durable stores verify connectivity, authentication,
database/schema selection, indexes, migration state, pooling, timeouts, disk or
connection capacity, and representative read/write behavior. A TCP check is not
application readiness.

For Redis and queues inspect producer and consumer configuration, queue namespace,
worker concurrency, stalled/failed/delayed jobs, retry/backoff, retention, dead-
letter or poison handling, scheduler ownership, and shutdown/drain behavior. Track
job acceptance separately from consumption and durable completion.

Runtime readiness includes every required process: API/web, background workers,
schedulers, realtime listeners, notification consumers, and provider session
managers. Confirm that only one intended scheduler/leader owns singleton work and
that horizontally scaled workers preserve atomic claims and idempotency.

During deploy or incident, avoid purging queues, editing production documents, or
retrying side effects blindly. Sample payload metadata safely, identify idempotency
and terminal state, then choose retry, quarantine, repair, or discard with explicit
scope. Preserve audit/correlation identifiers.

Capacity checks should cover connection pools, memory, queue age/throughput,
worker saturation, provider quotas, and downstream latency. Scaling consumers can
worsen database or provider overload; change the actual bottleneck and observe it.
