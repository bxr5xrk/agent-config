# Adopted defaults for new projects

These choices carry forward the user's project setup, reviewed 2026-09-04. TypeScript and MongoDB were explicitly approved; the remaining stack choices were adopted under delegated setup. Apply them to genuinely new projects without repeating the stack questionnaire. Current project instructions, an existing stack and later explicit user decisions take precedence.

| Need | Default and boundary |
|---|---|
| Language/tooling | Strict TypeScript, supported Node LTS, pnpm with a pinned lockfile. Keep existing JavaScript and tooling. |
| Web UI | Next.js App Router/React; Tailwind and shadcn/ui using the appropriate available primitive base. Existing design systems win. |
| Server | Fastify only when a separate backend is needed; a small synchronous web boundary can stay in the existing Next app. |
| Data | MongoDB with the official driver when persistence is needed. Keep an existing model layer; revisit storage only for a concrete workload/invariant mismatch. |
| Validation/cache | Runtime boundary validation; trusted JSON Schema for Fastify. TanStack Query when interactive client server-state needs it. |
| Measurement | PostHog with an explicit event plan when useful; EU region for a new setup. Preserve an existing host/region. |
| Operations | Existing compatible hosting and auth providers first. Vercel/Cloud Run and Better Auth are candidates when those needs arise, subject to current compatibility and project constraints. Structured logs; existing error monitoring or Sentry when needed. |
| Verification | Existing runner; Vitest for suitable domain tests, Fastify inject for API behavior, browser/keyboard/axe checks for important UI journeys. The small API seed uses node:test. |

The user's data convention is explicit versioned schema/index migrations: keep provisioning out of request, import, connection and startup paths. Follow [data integrity](../../backend/references/data-integrity.md); this is an adopted convention, not a MongoDB restriction.

Identity, information density and motion follow the surface and agreed design. An internal tool and an expressive public landing need different treatment. An approved direction or delegated choice does not require a fresh options ceremony.

Add auth, billing, queues, analytics SDKs, cloud resources and shared modules only when the brief needs them. Keep all setup local until the user authorizes an external action. Check current compatible package support before creating a new project; the bundled seed is a dated snapshot, not an automatic upgrade policy.
