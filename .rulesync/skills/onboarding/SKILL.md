---
name: onboarding
description: >-
  Turn a product idea into an agreed brief, 5-10 visual directions, a selected
  design system, and a verified project scaffold using persistent stack
  defaults. Use for starting or comprehensively onboarding a project, not
  isolated feature edits.
targets:
  - codexcli
codexcli:
  interface:
    display_name: Onboarding
    short_description: 'Idea to brief, design choices and working scaffold'
    default_prompt: >-
      Use $onboarding to onboard my idea, compare visual directions, and build
      the agreed project scaffold.
---
# Onboarding

Work in the user's language; retain technical identifiers. Turn the idea into a runnable starting point with a thin real user journey, not merely a proposal or a folder tree. Keep this skill's preferences separate from requirements discovered for the particular product.

## Start and resume

Read [defaults](references/defaults.md) and [discovery](references/discovery.md). Inspect applicable project instructions and existing code before proposing changes. For a new project, prepare the brief/design/state under a temporary `work/onboarding/<project>/` folder before the destination exists; the generator transfers the records to `docs/onboarding`. Create `state.json` from [state template](assets/documents/state.json) and use [brief](assets/documents/BRIEF.md). Existing projects: preserve their stack unless migration is requested; do not run the generator over them.

Use the available `grilling` skill (the user's “Grill Me”) for discovery: load its current SKILL.md from the active skill catalog. Ask one material question at a time with a recommendation, inspect discoverable facts yourself, and wait for each answer. The user's explicit instructions and already accepted defaults override generic interview rules: do not re-ask framework, language, database, or analytics choices. If grilling is unavailable, say so once and use the self-contained interview in discovery.md.

Persist each answer, its status (user-approved / delegated default / assumption), unresolved decisions, current phase, and next action. After every answer or new evidence, reconsider dependencies. Ask the user to settle only material unknowns. Research and reviewable drafts may continue; do not implement the product until the brief is agreed. Resume from state instead of replaying onboarding. Never mark a decision approved because time elapsed.

## Workflow and required outputs

1. **Brief and scope.** Agree audience, job, first useful journey, success measure, boundaries, domain entities, access, integrations, and deployment constraints. Write BRIEF.md and decisions with rationale. Use [architecture](references/architecture.md) only if a backend is needed.
2. **Visual choice — every new frontend.** Follow [design exploration](references/design-exploration.md) and consult [design research](references/design-research.md). Produce **5–10 genuinely different visual options, default 6**, on comparable content. Show actual rendered mockups/reference screenshots, a side-by-side comparison, sources, and tradeoffs; a list of style names or links is insufficient. Wait for the user's selection or combination before UI-kit/product implementation. If the user supplies a selected design or explicitly delegates the choice, record that override. Backend-only: record design as not applicable.
3. **Design system and brand.** Follow [design system](references/design-system.md) and [accessibility](references/accessibility.md). Write DESIGN.md, semantic tokens, a small reusable UI kit with state examples, and logo/favicon assets for the chosen direction. Reuse existing brand when supplied. Use [design template](assets/documents/DESIGN.md).
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
- New facts may justify an exception; explain the concrete reason, record it once, and retain all unrelated accepted decisions.
