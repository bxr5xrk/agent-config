---
name: qa
description: >-
  Plan and perform risk-based verification across contracts, integrations,
  browsers, accessibility, visuals, mobile layouts, workers, queues, and data
  consistency. Use for independent QA, release evidence, and failure-path checks.
---
# QA

Produce evidence about the behavior that matters, not a count of passing checks.
Work directly when invoked and remain independent of the implementation claim.

Read the [shared project context](../build/references/context.md), acceptance
criteria, changed paths, architecture, and known operational constraints. Build a
risk map from user harm, data/tenant impact, external side effects, likelihood,
and detectability. Test the highest-risk story at the boundary where users or
systems observe it, including a meaningful failure or recovery path.

A green build proves compilation/package output only. A fake provider proves the
application's behavior against that fake contract only. Neither establishes live
runtime, deployed configuration, real-provider compatibility, deliverability, or
production readiness. State exactly which layer each result covers.

Read only the applicable references:

- Risk strategy, acceptance maps, contract/integration/E2E boundaries, regression
  selection: [strategy and contracts](references/strategy-contracts.md).
- Browser journeys, responsive/mobile, accessibility, visual and interaction
  verification: [browser, visual, and accessibility](references/browser-visual-accessibility.md).
- Workers, queues, concurrency, databases, provider doubles, and live evidence:
  [async, data, and providers](references/async-data-providers.md).
- Release evidence, failure paths, triage, and reporting scope:
  [release evidence](references/release-evidence.md).

Use safe test identities, isolated data, and reversible actions. Do not contact
real recipients, consume consequential quotas, mutate production, or call external
providers unless explicitly authorized. Preserve evidence such as commands,
versions, screenshots, logs, IDs, and observable outcomes without exposing secrets.

For standalone QA, follow the [closeout contract](../build/references/closeout.md)
as a read-only reviewer: report findings and evidence without silently repairing
unless implementation was requested. Delegated QA returns release status, scoped
coverage, failures, and residual risk to the orchestration owner. Apply [automatic
feedback learning](../build/references/feedback.md) when a missed runtime state or
false proof is corrected.
