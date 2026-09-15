# Specialist dispatch

| Work | Owner | Conditional collaborators | Independent check |
|---|---|---|---|
| New product intent | brainstorm | Research/domain exploration | Brief and counterexamples |
| New visual direction | designer | motion for temporal behavior | verify-product against selected artifact |
| Naming, brand or logo | designer with branding reference | Focused research and asset tools | Actual header/favicon/export checks |
| Small UI revision | designer or frontend | Existing direction decides | Focused visual/behavior review |
| Public landing/content | designer + frontend | motion, SEO/analytics references | verify-product + simplify |
| Product/admin flow | frontend | designer, backend | verify-product + simplify |
| API/data/background work | backend | security as relevant | simplify + behavior/contract verification |
| Substantive market or technical evidence | research | Relevant domain owner | Claim and provenance audit |
| Acquisition, activation or revenue experiment | growth | research, frontend/backend for instrumentation | Metric path + decision gate |
| Security-sensitive design or change | security | implementation owner | Authorized negative-path evidence |
| Independent behavior or release verification | qa | Relevant implementation owner for repairs | Acceptance map + scoped release evidence |
| Deploy, migration, runtime or incident | ops | backend, security or qa as risk requires | Observable runtime + rollback state |
| Native app surface | Available platform-specific skill | designer for shared intent; native interaction conventions | verify-product + platform build/runtime checks |
| Auth, tenant or external-input change | implementation owner | security | Negative-path evidence |
| Repeated correction | learn | Original specialist for evidence | Unseen scenario + counterexample, then user batch |

Separate decisions from parallel editing. A designer may establish a direction while backend work proceeds independently. Frontend implementation of that direction waits for the decision it needs. If two agents need the same file, assign one writer and let the other return a patch or review. Shared checkout requires explicit ownership; do not create Git worktrees for this local workflow.

Do not dispatch every specialist for every build. Use the smallest team whose
boundaries match the actual risk: research establishes consequential unknowns,
growth owns commercial experiments, security owns scoped trust-boundary work, QA
independently verifies behavior, and ops owns runtime mutation and recovery.
The internal `security-review` role may still provide a fresh post-implementation
review; it does not replace the security specialist for substantive security work.

Every delegation supplies:

```text
Role and exact instruction path (public SKILL.md or internal ROLE.md):
Orchestration / closeout owner:
User outcome and acceptance IDs:
Canonical brief/design/architecture paths:
Inputs and known constraints:
Approved lesson references, if applicable:
Owned files / read-only files:
Dependencies and other active writers:
Required artifact and evidence:
Explicitly out of scope:
```

Use fresh context for independent reviews: give the agreed requirements, actual files/diff and environment, without the writer's success claim or suggested verdict. Reviewers may see known product constraints; independence does not mean hiding requirements.

Parallelism is bounded by available slots. With four total slots, use implementation workers first, then the two reviewers; there is no requirement to run everyone simultaneously. Do not leave required work in an unawaited agent. Reuse an agent for repair context; use a fresh reviewer when an independent judgment is needed.

Use [one closeout owner](closeout.md). Standalone specialists organize their scoped review/repair/learning; delegated builders return evidence and corrections to the orchestrator for the integrated checks. If delegation is unavailable, perform sequential checks and disclose the lack of independent review instead of pretending multiple agents ran.

Resolve internal instruction paths from the owning skill: motion is `designer/internal/motion/ROLE.md`; product verification, simplify, security and learning are under `build/internal/<role>/ROLE.md`. Pass the resolved absolute path when delegating.
