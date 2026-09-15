---
name: security
description: >-
  Threat-model, review, and harden application changes across authorization,
  tenants, secrets, sessions, webhooks, queues, AI tools, and third-party
  providers. Use for scoped security analysis or implementation with explicit
  authority; not for unrequested offensive testing.
---
# Security

Protect the system's actual assets and trust boundaries while preserving the
user's requested scope. Work directly when invoked; a build orchestrator is
optional.

Read the [shared project context](../build/references/context.md), applicable
security policy and architecture, then inspect the concrete entrypoints, identity
model, data ownership, secrets, providers, queues, and deployment boundary. State
the authorized target and action before active testing. Read-only code review does
not authorize sending payloads, probing production, rotating credentials, changing
access, or accessing data beyond the user's established authority.

Threat-model the changed or requested path: actor, asset, entrypoint, trust
boundary, abuse case, existing control, bypass condition, impact, and evidence.
Prioritize exploitable paths and violated security properties over generic
hardening lists. Enforce authorization on the resource and tenant at the server
boundary; authentication or hidden UI alone is not authorization.

Read only the applicable references:

- Identity, tenant/resource authorization, roles, object ownership, and threat
  modeling: [threat model and authorization](references/threat-model-authorization.md).
- Credentials, cookies/tokens, sessions, proxies, logs, and provider accounts:
  [secrets, sessions, and providers](references/secrets-sessions-providers.md).
- Webhooks, queues, retries, idempotency, AI/tool calls, and untrusted content:
  [asynchronous and AI boundaries](references/async-ai-boundaries.md).
- Security review, safe validation, severity, remediation, and release decisions:
  [review and release](references/review-release.md).

Prefer controls with observable enforcement and small blast radius. Do not expose
secrets in output, fixtures, logs, patches, or verification. Do not weaken quotas,
rate limits, retries, isolation, or auditability for convenience without explicit
approval and a documented risk decision.

For implementation, verify the security property with an authorized negative
case at the meaningful boundary. Finish through the [closeout contract](../build/references/closeout.md):
standalone security work owns validation and repair; delegated work returns threat
paths, evidence, severity, fixes, and residual risk. Apply [automatic feedback
learning](../build/references/feedback.md) while keeping incidents and secrets in
their project-local records.
