---
name: ops
description: >-
  Prepare, deploy, observe, and recover application runtimes across environments,
  configuration, secrets, migrations, databases, queues, workers, quotas, and
  incidents. Use for release operations, runtime readiness, and operational repair.
---
# Ops

Make the intended runtime observable, recoverable, and safe to change. Work
directly when invoked; a build orchestrator is optional.

Read the [shared project context](../build/references/context.md), actual deployment
and runbook files, current environment state, and the authorization for any
mutation. Diagnose from observable service/process behavior. A successful build,
deployment record, or health endpoint proves only its own layer; verify the user-
visible or worker outcome when claiming the system is operational.

Prefer the smallest reversible change. Identify target environment, blast radius,
dependencies, data changes, rollback/roll-forward path, and evidence before acting.
Never print or copy secret values. Do not restart, migrate, scale, rotate, delete,
or touch production merely because an operational diagnosis would benefit from it;
use the authority in the current request.

Read only the applicable references:

- Environment configuration, secrets, deploy sequence, migrations, rollback, and
  safe smoke tests: [environments and deployments](references/environments-deployments.md).
- Mongo/Postgres, Redis, queues, workers, schedulers, concurrency, and runtime
  readiness: [data, queues, and workers](references/data-queues-workers.md).
- Health, logs, metrics, traces, alerts, incidents, and runbooks:
  [observability and incidents](references/observability-incidents.md).
- Rate limits, quotas, external providers, account/session/proxy pools, and
  capacity safety: [providers and capacity](references/providers-capacity.md).

Keep operational identities and pools separate when their purposes, permissions,
reputation, or external-provider risk differ. Preserve provider delays, quotas,
backoff, and circuit breakers unless an explicitly approved change includes
evidence and a rollback condition.

Update canonical runbooks and environment contracts to match verified behavior.
Finish through the [closeout contract](../build/references/closeout.md): standalone
ops owns post-change observation and repair; delegated ops returns changes,
evidence, rollback state, and unresolved risk. Apply [automatic feedback
learning](../build/references/feedback.md), but keep infrastructure identifiers,
incidents, and secrets in project-local systems.
