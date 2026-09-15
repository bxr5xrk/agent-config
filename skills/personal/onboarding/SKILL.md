---
name: onboarding
description: >-
  Route a new project into a lightweight site or serious product track, then
  create only the proportionate brief, brand, visual exploration, design system
  and verified scaffold. Use for starting or comprehensively onboarding a
  project, not isolated feature edits.
---
# Onboarding

Work in the user's language; retain technical identifiers. Turn the idea into a runnable starting point with a thin real user journey, not merely a proposal or a folder tree. Keep this skill's preferences separate from requirements discovered for the particular product.

## Start and resume

Read [defaults](references/defaults.md), [project track](references/project-track.md) and [discovery](references/discovery.md). Inspect applicable project instructions and existing code before proposing changes. For a new project, prepare the brief/design/state under a temporary `work/onboarding/<project>/` folder before the destination exists; the generator transfers the records to `docs/onboarding`. Create `state.json` from [state template](assets/documents/state.json) and use [brief](assets/documents/BRIEF.md). Existing projects: preserve their stack unless migration is requested; do not run the generator over them.

Use the available `grilling` skill (the user's “Grill Me”) for discovery: load its current SKILL.md from the active skill catalog. Ask one material question at a time with a recommendation, inspect discoverable facts yourself, and wait for each answer. The user's explicit instructions and already accepted defaults override generic interview rules: do not re-ask framework, language, database, or analytics choices. If grilling is unavailable, say so once and use the self-contained interview in discovery.md.

Persist each answer, its status (user-approved / delegated default / assumption), unresolved decisions, current phase, and next action. After every answer or new evidence, reconsider dependencies. Ask the user to settle only material unknowns. Research and reviewable drafts may continue; do not implement the product until the brief is agreed. Resume from state instead of replaying onboarding. Never mark a decision approved because time elapsed.

## Route before depth

Classify the work as `lightweight_site` or `product_brand` before deep discovery. Infer the track without asking when the user's description is clear. Ask one short question only when the difference is material and genuinely ambiguous. Record the selected track and concrete reason in state and BRIEF.md; reassess if later facts change it.

- **`lightweight_site`:** a small informational, personal, event, campaign or utility site with known content, low differentiation stakes and no substantial product workflow. Keep onboarding short. Skip competitor-brand research, positioning exercises, naming workshops, logo exploration, BRAND.md, 5–10 visual directions and a broad design system unless the user explicitly requests one. Record skipped brand/design stages as `skipped_by_track`, not as approved work. Use Codex's normal design judgment, one restrained coherent direction and only the components needed to ship the page well.
- **`product_brand`:** a new SaaS, B2B/consumer product, commercial application or strategically differentiated public brand. Use the full product and brand path below even if the interface itself should feel simple.

Simple visual form does not imply the lightweight track. A focused SaaS with one main screen is still `product_brand` when naming, trust, differentiation, repeat use or product behavior matter.

## Workflow and required outputs

1. **Brief and scope.** Agree audience, job, first useful journey, success measure, boundaries, domain entities, access, integrations, and deployment constraints. Write BRIEF.md and decisions with rationale. Use [architecture](references/architecture.md) only if a backend is needed.
2. **Track-specific design.** For `lightweight_site`, choose one appropriate direction and proceed without ceremony after the brief is agreed. For `product_brand`, follow [brand foundation](references/brand-foundation.md), then [design exploration](references/design-exploration.md) and [design research](references/design-research.md): produce **5–10 genuinely different rendered options, default 6**, and wait for selection before product UI implementation.
3. **Design system and brand application.** For `product_brand`, follow [design system](references/design-system.md), [modern product UI](references/modern-product-ui.md) and [accessibility](references/accessibility.md). Translate BRAND.md and the selected direction into DESIGN.md, semantic tokens, the necessary reusable UI kit and final brand assets. For `lightweight_site`, use only a compact local token set and required components; do not manufacture a brand book or component library. Reuse existing brand when supplied.
4. **Scaffold and first journey.** Follow [scaffold](references/scaffold.md), [frontend](references/frontend.md), [backend](references/backend.md), and [data migrations](references/data-migrations.md) as applicable. Templates are technical seeds, not an approved visual identity. Add only modules needed by the agreed scope. Implement one real end-to-end journey before widening coverage.
5. **Product essentials.** Public frontend: use [SEO](references/seo.md) and [analytics](references/analytics.md). Private app: authentication/authorization and no indexing; analytics only if requested or justified by its success measure. Use [operations](references/operations.md) for environment, logs, deployment and handoff.
6. **Verify.** Execute [acceptance checks](references/verification.md), including real slow-navigation, errors, keyboard interaction and responsive checks for UI. Apply the [anti-pattern matrix](references/anti-patterns.md). Update [handoff](assets/documents/HANDOFF.md) with actual commands/results and limitations. A build or screenshot alone is not end-to-end verification.

Read only relevant references, not the entire library at once. External skills are optional specialists except the explicitly requested grilling workflow; use [routing](references/skill-routing.md). Do not silently install third-party skills or load several conflicting design instruction sets. No subagents by default.

## Non-negotiable user preferences

- Default stack decisions are already made; never restart a stack questionnaire for ordinary onboarding.
- Slow data must not produce a silent multi-second click. Show navigation feedback and the destination shell/loading state while data resolves; keep auth checks intact.
- Create database indexes through versioned explicit operations, never through request handlers, module imports or ordinary app startup. Preserve migrations for rebuilding environments.
- Visible hover, pointer affordance for enabled actions, keyboard focus, pending/disabled/error/empty/success states are part of the UI definition.
- Never turn six options into six recolors of one generic SaaS page. Never select the final visual direction before the user sees the requested alternatives.
- Do not generate a random name or generic AI-style logo and immediately design around it. Competitor evidence, positioning, naming checks and an explicit name decision come first for a new public brand.
- Do not force a small ordinary site through the product-brand workflow. Preserve quality and verification while skipping process that cannot change the result.
- New facts may justify an exception; explain the concrete reason, record it once, and retain all unrelated accepted decisions.
