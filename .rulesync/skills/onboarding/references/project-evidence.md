# Local project evidence

Observed 2026-09-04; these are references, not a full code/security audit.

| Project type | Observed evidence | Reusable choice |
|---|---|---|
| Next.js application | Next 16, React 19, TypeScript, Tailwind 4, native Mongo driver, Playwright and Vitest | This combination supports the frontend, database and tooling baseline |
| TypeScript service | Express 5 + Mongoose API; Next + Radix + TanStack Query + Zod admin | Existing service boundaries and UI primitives remain valid; do not force a rewrite |
| Legacy JavaScript service | Express 4, JavaScript, Ajv and versioned migration files | JavaScript remains valid in existing services; do not copy old dependency versions into a new starter |
| MongoDB index provisioning | Declarative index module with focused runtime tests | Index declarations can remain reusable while request runtimes avoid provisioning |

No existing project was modified. Package presence is not evidence of production quality or a verified live integration. PostHog was selected as a reusable default, not claimed to be installed in each inspected project. The user explicitly confirmed TypeScript everywhere and MongoDB after this inspection.
