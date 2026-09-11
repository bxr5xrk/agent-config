import { Suspense } from "react";
import { connection } from "next/server";
import { z } from "zod";
import { LoadingState } from "../../components/loading-state";
const statusSchema = z.object({ ok: z.boolean() });
async function ServiceStatus() {
  await connection();
  const origin = process.env.API_ORIGIN;
  if (!origin) { return <p>Web starter is ready. No external service is configured.</p>; }
  const response = await fetch(new URL("/health/live", origin), {
    cache: "no-store", signal: AbortSignal.timeout(5_000),
  });
  if (!response.ok) { throw new Error("Service is unavailable"); }
  const status = statusSchema.parse(await response.json());
  return <p role="status">{status.ok ? "Service is available" : "Service reports a problem"}</p>;
}
export default function StatusPage() {
  return <><h1>Service status</h1><p>The page shell stays available while the service responds.</p>
    <Suspense fallback={<LoadingState />}><ServiceStatus /></Suspense>
  </>;
}
