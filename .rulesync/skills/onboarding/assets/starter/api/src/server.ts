import { buildApp } from "./app.js";

const port = Number(process.env.PORT ?? 3001);
if (!Number.isInteger(port) || port < 1 || port > 65535) {
  throw new Error("PORT must be an integer between 1 and 65535");
}
const app = buildApp({ logging: true });
let closing = false;
async function shutdown() {
  if (closing) { return; }
  closing = true;
  const deadline = setTimeout(() => process.exit(1), 10_000).unref();
  try { await app.close(); }
  catch { process.exitCode = 1; }
  finally { clearTimeout(deadline); }
}
process.once("SIGTERM", shutdown);
process.once("SIGINT", shutdown);
try { await app.listen({ port, host: process.env.HOST ?? "127.0.0.1" }); }
catch { app.log.error("Server failed to start"); process.exitCode = 1; }
