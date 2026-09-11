# PostgreSQL

Use this reference only when the project actually uses PostgreSQL. Inspect the schema, migrations, driver/ORM, deployed PostgreSQL version and representative workload before changing behavior.

## Schema and migrations

- Put invariants in appropriate types, `NOT NULL`, `CHECK`, `UNIQUE`, foreign-key and exclusion constraints as well as application validation.
- PostgreSQL does not automatically index the referencing side of a foreign key. Add such an index when joins, lookups, deletes or cascades need it; derive column order from real query shapes.
- Use versioned, forward-safe migrations. For risky or large changes prefer expand, backfill, verify and contract. Account for locks, table rewrites, mixed application versions and rollback/recovery.
- Verify syntax against the deployed version. For example, PostgreSQL does not support `ADD CONSTRAINT IF NOT EXISTS`.

## Queries and indexes

- Find N+1 access and replace it with a join, batch load or bounded aggregate when it improves the real path.
- Design composite, partial and covering indexes from actual predicates, joins, ordering and selectivity. Include write cost and duplicate-index risk.
- Use `EXPLAIN`; use `EXPLAIN (ANALYZE, BUFFERS)` only with production-like data and safe execution. `ANALYZE` runs the statement, so isolate or roll back mutating queries and avoid unsafe production probes.
- Prefer deterministic keyset pagination for deep or high-volume ordered traversal. Offset pagination remains valid for small result sets or when random page access is a requirement.

## Transactions and connections

- Keep transactions short. Perform external network calls and slow computation outside lock-holding sections when correctness permits.
- Acquire shared locks in a consistent order, make retryable operations idempotent and handle deadlock/serialization retries within a bounded policy.
- Reuse a driver or platform connection pool. Size it from the database connection budget, deployment concurrency, pool mode and observed saturation; do not use a universal formula.

## Authorization

Use row-level security when the database access model relies on it, including Supabase clients or direct multi-tenant access. Test anonymous, authenticated, tenant-crossing, owner and service-role/bypass paths explicitly. Index policy predicates where justified. Keep server authorization even when RLS adds defense in depth, and treat `SECURITY DEFINER` functions as privileged code with fixed `search_path` and restricted execution.

Verify with the real database: constraints reject invalid writes; migrations work on representative data; concurrent cases preserve invariants; query plans support performance claims.

Sources: selectively adapted from [Supabase PostgreSQL Best Practices](https://github.com/supabase/agent-skills/tree/8331f910845103c08d51f6ca1d86ebb7d1f745e3/skills/supabase-postgres-best-practices), checked against the [PostgreSQL constraints](https://www.postgresql.org/docs/current/ddl-constraints.html), [EXPLAIN](https://www.postgresql.org/docs/current/sql-explain.html) and [transaction](https://www.postgresql.org/docs/current/tutorial-transactions.html) documentation.
