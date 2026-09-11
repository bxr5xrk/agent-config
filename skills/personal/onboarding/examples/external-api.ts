// Illustrative server-side GET adapter. Adapt schema and provider authentication.
import { z } from "zod";
const providerResult = z.object({ id: z.string(), status: z.enum(["pending", "ready", "failed"]) });
export async function readProviderStatus(baseUrl: URL, id: string, signal?: AbortSignal) {
  const timeout = AbortSignal.timeout(5_000);
  const response = await fetch(new URL(`/items/${encodeURIComponent(id)}`, baseUrl), {
    signal: signal ? AbortSignal.any([signal, timeout]) : timeout,
    headers: { accept: "application/json" },
  });
  if (!response.ok) { throw new Error(`Provider request failed with status ${response.status}`); }
  return providerResult.parse(await response.json());
}
// No automatic POST retries. Never log provider credentials or full response bodies.
