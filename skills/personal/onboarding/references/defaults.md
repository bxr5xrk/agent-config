# Persistent defaults

Version 1; reviewed 2026-09-04. Language and database were explicitly chosen by the user in this task. Other defaults are recommendations adopted under the user's request to select a reusable stack; they are changeable once, not questions repeated for each project.

| Area | Default | When to vary |
|---|---|---|
| Language | TypeScript strict, frontend + backend — user-approved | Existing JS stays JS unless migration requested |
| Runtime/tooling | Supported Node LTS; pnpm workspace; committed lockfile | Existing project's runtime wins |
| Frontend | Next.js App Router + React | Static-only: static rendering/export if its limitations fit; don't add server work unnecessarily |
| Styles/components | Tailwind CSS + shadcn/ui, Radix-backed primitives when available | Existing design system wins; inspect current registry variants |
| Visual identity | `lightweight_site`: one coherent default; `product_brand`: 6 initial directions | User may request 5–10 or provide approved artwork |
| API | Separate Fastify service when backend is needed | Tiny synchronous server needs may live in Next Route Handlers/Server Actions |
| Data | MongoDB, official driver — database user-approved | Mongoose for an existing model layer; relational constraints may justify PostgreSQL |
| Validation | Zod at external boundaries; native JSON Schema for Fastify routes | Keep schemas consistent; add generation only when duplication is real |
| Client server-state | TanStack Query for interactive authenticated data | Server rendering/static data doesn't need a client cache |
| Analytics | PostHog, EU region for a new project; explicit event plan | Reuse the existing project's host/region; no silent migration |
| Logging/errors | Fastify/Pino structured logs; Sentry when error monitoring needed | Reuse current monitoring; analytics is not error monitoring |
| Tests | Vitest for domain logic, Fastify inject for API, Playwright + axe for key UI journeys | Use node:test for the tiny provided API starter |
| Auth | Existing trusted provider; new user-account projects evaluate Better Auth as first candidate | User/tenant model, deployment and provider support determine integration |
| Hosting | Prefer existing compatible account; new Next frontend candidate Vercel, Node API candidate Cloud Run | Costs, background jobs, region, networking can change this; no paid provisioning without authorization |

Do not create auth, payments, queues, email, Redis, Docker, analytics accounts or empty packages unless the brief needs them. If such a need arises, preserve these defaults while resolving only the missing decision.

## TypeScript versus JSDoc

TypeScript is chosen for evolving UI/API contracts and safe refactoring across the scaffold. It does not validate network input at runtime. JSDoc with `checkJs` is a valid checked JavaScript path for existing repos and small scripts; JSDoc without checking is documentation, not enforced correctness. No claim that TypeScript eliminates bugs or that JavaScript is unsuitable.

Source: [TypeScript checkJs](https://www.typescriptlang.org/tsconfig/checkJs.html), [JSDoc support](https://www.typescriptlang.org/docs/handbook/jsdoc-supported-types.html), [Better Auth introduction](https://better-auth.com/docs/introduction).

Local references and the boundaries of their reuse: [project evidence](project-evidence.md).

Keep product/provider choices stable but verify current compatible package releases before a new scaffold. Record versions and validation date; never use floating `latest` in committed manifests or silently upgrade old projects.
