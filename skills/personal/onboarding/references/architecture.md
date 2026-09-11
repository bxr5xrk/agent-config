# Architecture choice

Our recommended general Node backend is Fastify, based on first-class route schemas, response serialization, plugin encapsulation and request injection testing. This is a fit judgment, not a universal benchmark winner.

| Option | Good fit | Tradeoff / decision |
|---|---|---|
| Fastify | Standalone Node API with clear contracts | Plugin/validator conventions to learn; default for new service |
| Express 5 | Existing Express code, middleware-dependent integration | Add coherent validation/logging conventions; preserve existing projects |
| Hono | Web-standard APIs on several runtimes, edge deployment | Runtime/library compatibility needs checking; choose for an actual edge need |
| NestJS | Team explicitly wants DI/modules/decorators and broad conventions | More framework structure; no default for a small founder project |
| Next backend | A few synchronous endpoints closely tied to one UI | Keep domain logic outside route components; runtime limits and background work still matter |

[Fastify schemas](https://fastify.dev/docs/latest/Reference/Validation-and-Serialization/), [Express 5 error handling](https://expressjs.com/en/guide/error-handling/), [Hono](https://hono.dev/docs/), [Nest](https://docs.nestjs.com/first-steps).

Choose separate Fastify if there are independent API consumers, webhooks/workers, long-running tasks, non-UI business logic, or independent scaling/deployment. Separation means one modular service first, not a microservice per entity. Prefer one repo with `apps/web`, `apps/api`; add shared contracts only when both actually use them.

Browser → same-origin BFF or explicitly configured API → domain logic → Mongo/external providers. Prefer a same-origin BFF for cookie-based UI access when it simplifies CORS/CSRF. Never proxy arbitrary user-supplied targets. Server components may call the service directly; do not loop through their own HTTP route handler without a reason. Recheck authorization at the data-owning backend even if a UI gate exists.

A backend isn't needed for every landing page. A private admin still needs access control even though SEO is out of scope. Document cost/latency consequences of an extra service; don't add one just to fill a folder.
