import assert from "node:assert/strict";
import test from "node:test";
import { buildApp } from "../src/app.js";

test("valid request is projected to the response contract", async (t) => {
  const app = buildApp(); t.after(() => app.close());
  const result = await app.inject({ method: "POST", url: "/echo", payload: { message: "hello", secret: "not returned" } });
  assert.equal(result.statusCode, 200);
  assert.deepEqual(result.json(), { message: "hello" });
});

test("invalid request has a stable client error", async (t) => {
  const app = buildApp(); t.after(() => app.close());
  const result = await app.inject({ method: "POST", url: "/echo", payload: { message: "" } });
  assert.equal(result.statusCode, 400);
  assert.equal(result.json().code, "INVALID_REQUEST");
});

test("internal exceptions do not leak their message", async (t) => {
  const app = buildApp(); t.after(() => app.close());
  app.get("/broken", async () => { throw new Error("private-upstream-detail"); });
  const result = await app.inject("/broken");
  assert.equal(result.statusCode, 500);
  assert.equal(result.json().code, "INTERNAL_ERROR");
  assert.ok(!result.body.includes("private-upstream-detail"));
});

test("liveness is independent of external services", async (t) => {
  const app = buildApp(); t.after(() => app.close());
  const result = await app.inject("/health/live");
  assert.deepEqual(result.json(), { ok: true });
});
