# MongoDB lifecycle and index policy

Runtime application code may read/write data; it must not create or reconcile schema/indexes on each request, import, connection, or start. With Mongoose use `autoIndex: false` and `autoCreate: false` in deployed runtime, and do not call `syncIndexes()` there. [Mongoose index guidance](https://mongoosejs.com/docs/guide.html#indexes).

Keep index definitions in versioned `db/migrations` or a dedicated operations package. The user's “create once” means once per relevant environment/change, not deleting the only reproducible definition. Every new environment still needs provisioning. [Mongo createIndex](https://www.mongodb.com/docs/manual/reference/method/db.collection.createIndex/) describes creation behavior; repeating an identical definition is not a substitute for an explicit migration lifecycle.

Migration requirements:

1. Stable ID + checksum/history; explicit CLI or deployment job, never app startup.
2. One migrator per environment (deployment concurrency lock or tested database lock). Don't build a casual expiring lock without renewal/fencing.
3. Preflight collection/data size and duplicate values before unique constraints; define maintenance/online rollout implications.
4. Execute only pending operations; verify `listIndexes()`/expected constraints; record completion after success. If a crash leaves partial work, retry must be safe or require explicit recovery.
5. Preserve immutable applied migrations. Document rollback or forward-fix; don't promise transactional rollback for index builds. Do not automatically drop indexes merely because they are absent from a schema.
6. Keep runtime database privileges separate from migration privileges when hosting supports it.

Do not invent indexes for hypothetical queries. Link each to a query/sort/uniqueness/TTL requirement and inspect query plans when data warrants it. Uniqueness guards correctness; check-then-insert alone races. Tenant filters belong in every applicable access and in compound index design. TTL expiration is not instantaneous authorization expiry: check expiration in application logic too.

The included `examples/mongo-migration.ts` shows a single serialized deployment migration. It explicitly relies on the deployment lock; adapt to your deploy system and test against an isolated database. It is not a general-purpose distributed migration framework.
