---
name: frontend
description: >-
  Implement and repair web interfaces, navigation, client data flow, public-page
  SEO, and product analytics. Use for frontend delivery with an existing brief
  or scoped request.
---
# Frontend

Deliver the requested interface with its real states and interactions. Work directly when invoked; a build orchestrator is optional.

Read the [shared context](../build/references/context.md), affected routes, installed versions, project brief and design document. Recall approved applicable lessons for role `frontend` through [learning](../build/internal/learn/ROLE.md); pending historical corrections are not policy. Identify public discovery pages versus authenticated application routes. Preserve the selected visual direction, existing stack, API contracts and authorization boundaries. Resolve missing design decisions proportionally to the change.

For a new project use the [adopted defaults](../build/references/defaults.md); preserve an existing project's stack and explicit choices. Revisit a default only for a concrete brief or deployment constraint. Choose static/server rendering for public content when practical and client components for actual interaction. Add dependencies only for an identified need.

Read only the references relevant to the change:

- Bugs, performance regressions or repeated failed fixes: [diagnosis](../build/references/diagnosis.md).
- New behavior, real regressions or test changes: [behavioral checks](../build/references/behavior-checks.md).
- Data, forms, navigation or recovery: [app state](references/app-state.md).
- Pages intended for discovery or public sharing; changes to indexing policy: [public SEO](references/public-seo.md). Apply per route, not to every route of a SaaS.
- Product measurement: [analytics](references/analytics.md). PostHog remains the default where measurement is useful.
- Reusable React APIs, variant/state complexity or boolean mode growth: [React composition](references/react-composition.md).
- Changed interactive UI: [accessibility and browser safety](references/accessibility-safety.md).
- Rendering, media, scripts, responsiveness or motion: [performance](references/performance.md).

Implement complete applicable states and verify the actual user journey in a browser, including a meaningful failure case. For layout changes inspect the rendered result at relevant sizes; passing types or a build does not establish visual quality. Keep private administration focused on task completion; add discovery metadata or decorative motion only when the product needs it.

Finish using the [closeout contract](../build/references/closeout.md): a standalone builder owns independent review, repair and relevant learning candidates; a delegated builder returns them to its orchestration owner. Update affected project contracts and return changed behavior, verification evidence and material gaps. Global lessons require separate approval.

Apply [automatic feedback learning](../build/references/feedback.md) throughout follow-up corrections and “remember” requests; the user does not invoke internal reviewers or learning commands.
