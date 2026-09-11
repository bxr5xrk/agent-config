# Scaffold profiles and execution

The provided generator copies a small runnable technical seed, documents and accepted state. It does not invent auth/business logic, create cloud resources or choose a visual identity. Use only for a new destination; apply changes manually to existing repositories.

Profiles: `web` (Next; tiny backend can be added there), `api` (Fastify), `fullstack` (both, independently runnable). Shared packages, Mongo domain modules, analytics/auth SDKs and shadcn components are added only when used by the brief. The default database remains Mongo even though the transport smoke example does not need a database.

1. Agree BRIEF.md and persist honest `state.json` together in `work/onboarding/<project>/` while the final destination is still absent. The CLI carries adjacent BRIEF.md, DESIGN.md, ANALYTICS.md and HANDOFF.md into the new project; preserve or update relative visual artifact links when moving them. Frontend: deliver the visual comparison and record selected IDs or an explicit user override.
2. Run from the skill folder:
   `python3 scripts/scaffold.py /absolute/new-project --name my-project --profile fullstack --state /absolute/state.json`
3. Inspect the generated diff. Run `pnpm install --frozen-lockfile`, then `pnpm verify`; commit the included profile lockfile. The included compatible version snapshot is reviewed 2026-09-04; update from current official docs/release support before future new projects when needed and rerun checks.
4. Fullstack development: `pnpm --filter @starter/api dev`; in another terminal set the non-secret API_ORIGIN or create `apps/web/.env.local` from its example and run `pnpm --filter @starter/web dev`. Next reads its env file; the API reads exported environment variables. Defaults are web 3000/API 3001.
5. Apply selected tokens, add scope-specific shadcn primitives from the current registry, implement the first agreed domain journey and connect Mongo via one server-only pool. Follow data-migrations.md for explicit setup. Add analytics/SEO as the brief requires.
6. Replace technical sample pages/echo route once real paths cover their purpose; do not ship demo text or no-op buttons as the product. Starter `noindex` intentionally remains until public metadata is configured and verified.

The generator validates state shape and refuses existing destinations; it cannot verify that recorded user approval is truthful. State must come from the actual conversation. A technical starter isn't a finished onboarding; use verification.md and HANDOFF.md for scope completion.

Examples outside assets/starter are adaptation patterns, not executed services. No starter calls createIndex at runtime, and no unused database client is added to its hot path.
