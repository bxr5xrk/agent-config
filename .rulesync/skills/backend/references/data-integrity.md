# Persistence, concurrency and migrations

Model the workload and invariants before adding storage layers. For MongoDB, choose document boundaries so common atomic changes stay within a document when practical. Conditional updates, unique constraints and appropriate transactions enforce invariants; a read-then-write check alone cannot prevent a race. Use multi-document transactions for a real cross-document invariant, not as a substitute for schema design. Preserve the existing database when its constraints fit.

Derive indexes from actual filter/sort/uniqueness requirements. Include tenant scope when uniqueness belongs to a tenant. Validate query plans and representative cardinality for a claimed query optimization. Bound result size and pagination; avoid unbounded embedded arrays or full-collection materialization. TTL cleanup is asynchronous, so authorization/expiry logic must check the timestamp itself.

Reuse a MongoClient/pool per process and close it during shutdown. Size connections across replicas/instances against the deployment's connection budget. Bound pool waiting and application concurrency where overload matters; increasing the pool is not a universal fix.

## Schema/index changes

The user's adopted convention is explicit versioned schema/index migrations. Keep provisioning out of requests, imports, connection setup and startup; do not introduce opportunistic boot-time synchronization. Preserve a documented project exception unless changing that policy is in scope. With Mongoose, verify `autoIndex`/`autoCreate` behavior and disable automatic provisioning when explicit migrations own it.

Use versioned immutable migrations with execution history/checksums and a runner that prevents conflicting concurrent execution. Preflight existing data, duplicate values, lock/build impact and old/new application compatibility. Make partial failure observable and retry/resume safe; verify the resulting constraint rather than merely logging completion. Choose expand/backfill/contract when rollout requires coexistence. Keep destructive cleanup separate and plan a credible forward fix or rollback; index operations do not acquire imaginary transactional rollback semantics.

## Verify

For changed invariants, exercise concurrent writes against the actual database engine and assert the final invariant. For migrations, test representative existing data, a second execution, partial failure/restart and relevant version coexistence. Verify duplicate rejection, tenant-specific uniqueness or expiry at the layer enforcing it.

Sources checked 2026-09-05: MongoDB [atomicity](https://www.mongodb.com/docs/manual/core/write-operations-atomicity/), [unique indexes](https://www.mongodb.com/docs/manual/core/index-unique/), [TTL](https://www.mongodb.com/docs/manual/core/index-ttl/), [Node connection pools](https://www.mongodb.com/docs/drivers/node/current/connect/connection-options/connection-pools/); [Mongoose schema options](https://mongoosejs.com/docs/guide.html). Deployment conventions must be adopted deliberately; MongoDB does not forbid startup index creation.
