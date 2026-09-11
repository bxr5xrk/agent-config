# Discovery with Grill Me

Interview in dependency order, not as a long form. Never ask every item automatically. Resolve facts from provided files/code; ask only decisions that materially change the result. Each question includes a recommendation and why it fits. Use one short UI question with 2–3 choices plus free-form input where supported, then wait.

Branches to explore as relevant:

- Person and job: who uses it, what happens today, what meaningful result changes?
- First journey: trigger → steps → outcome; actual sample inputs/outputs; failure/undo path.
- Scope: smallest useful release, explicit exclusions, measurable acceptance.
- Surface: public acquisition site, authenticated product, private admin, API/worker, or combination.
- Domain: entities, ownership, lifecycle, invariants, money/time semantics, search/filter needs.
- Access: actors, roles, tenant boundaries, anonymous capabilities, account recovery.
- Integrations: existing accounts, API limits, authorization ownership, webhooks, background work.
- Design: supplied references and anti-references, content density, devices, audience expectations, brand assets. Ask for a missing reference only if necessary; research otherwise.
- Operations: public/private launch, data region, hosting constraints, budget where spending is involved, failure consequences.

Record accepted answers immediately. Defaults supply Next, TS, Mongo, Fastify and PostHog without another questionnaire. If the user delegates a decision, make it and record `delegated_default`, not `user_approved`.

Before implementation, show a short concrete brief with the first journey, exclusions, architecture, acceptance checks, remaining assumptions. Ask for agreement only if not already given; grilling's agreement is about product intent, not repeated permission for every file edit. Design selection is a separate gate after visible alternatives. A user who says “use your judgment and build” may waive decisions; record their exact override.

Completion: a future agent can continue from `state.json` plus BRIEF.md without asking already answered questions. The state is documentation, not a trusted authorization token: it must reflect the actual conversation.
