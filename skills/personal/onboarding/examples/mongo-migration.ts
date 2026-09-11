// Illustrative explicit deployment job, never imported by the running app.
// PRECONDITION: deployment system serializes migrators for this database.
import { MongoClient } from "mongodb";
const id = "001-items-tenant-slug-unique";
const uri = process.env.MONGODB_URI;
const name = process.env.MONGODB_DATABASE;
if (!uri || !name) { throw new Error("MONGODB_URI and MONGODB_DATABASE are required"); }
const client = new MongoClient(uri, { serverSelectionTimeoutMS: 5_000 });
try {
  await client.connect();
  const db = client.db(name);
  const history = db.collection<{ _id: string; appliedAt: Date }>("_migrations");
  if (!(await history.findOne({ _id: id }))) {
    // Preflight duplicates and rollout impact before applying on existing data.
    await db.collection("items").createIndex({ tenantId: 1, slug: 1 }, {
      name: "items_tenant_slug_unique", unique: true,
    });
    const indexes = await db.collection("items").listIndexes().toArray();
    if (!indexes.some(index => index.name === "items_tenant_slug_unique" && index.unique)) {
      throw new Error("Expected index was not verified");
    }
    await history.insertOne({ _id: id, appliedAt: new Date() });
  }
} finally { await client.close(); }
// Exact index definition is safely retryable after a crash before history insertion.
// A complete production runner also verifies checksums and defines recovery policy.
