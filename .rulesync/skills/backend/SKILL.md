---
name: backend
description: >-
  Design, implement and repair APIs, domain logic, database changes and
  background integrations. Use when server behavior, data integrity,
  authorization or runtime reliability changes.
targets:
  - codexcli
codexcli:
  interface:
    display_name: Backend
    short_description: Build reliable APIs and data workflows
    default_prompt: Use $backend to implement this server change and verify its contracts.
---
# Backend

Deliver the smallest server change that satisfies the requested behavior and its integrity constraints. Work directly when invoked; a build orchestrator is optional.

Read the [shared context](../build/references/context.md) and recall approved applicable lessons for role `backend` through [learning](../build/internal/learn/ROLE.md); pending historical corrections are not policy. Inspect the affected entrypoint, callers, persisted data, tests, deployment/runtime and project contracts. Establish observable behavior and failure cases before changing structure. Preserve existing language, database, providers and authorization semantics unless a change is required.

For a new project use the [adopted defaults](../build/references/defaults.md); preserve an existing project's stack and explicit choices. Revisit a default only for a concrete workload, invariant or deployment constraint. Tiny synchronous web-server needs may remain in the existing framework. Keep an existing model layer; do not create infrastructure in anticipation of hypothetical scale.

Read only applicable references:

- Bugs, performance regressions or repeated failed fixes: [diagnosis](../build/references/diagnosis.md).
- New behavior, real regressions or test changes: [behavioral checks](../build/references/behavior-checks.md).
- Module/API design or simplification: [architecture and contracts](references/architecture-contracts.md).
- Persistent data, queries, concurrency or schema/index changes: [data integrity](references/data-integrity.md).
- PostgreSQL schema, query plans, migrations, locking, pooling or row-level security: [PostgreSQL](references/postgres.md).
- Protected resources, authentication, tenants or trust boundaries: [authorization](references/authorization.md).
- External APIs, webhooks, jobs, process behavior or diagnostics: [runtime and integrations](references/runtime-integrations.md).

Validate external inputs at runtime; TypeScript alone cannot do this. Enforce business invariants and resource authorization on the server, including direct endpoint calls. Make failure behavior explicit and keep logs/errors safe. A successful request is insufficient when retries, concurrent writes or process interruption can corrupt the result.

Verify the changed contract at its meaningful boundary, including the relevant negative or concurrent case. Use real database/provider behavior when the claim depends on it; distinguish mocks from integration evidence. Follow the [closeout contract](../build/references/closeout.md): standalone builders own independent review, repair and relevant learning candidates; delegated builders return them to the orchestration owner. Update affected contracts and return changed behavior, checks and material gaps. Global lessons require separate approval.

Apply [automatic feedback learning](../build/references/feedback.md) throughout follow-up corrections and “remember” requests; the user does not invoke internal reviewers or learning commands.
