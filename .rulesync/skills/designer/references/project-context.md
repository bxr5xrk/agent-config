# Project continuity

An existing application has a design system even when nobody named it. Inspect rendered screens, tokens, components, layout primitives, assets and interaction conventions before inventing replacements. Compare implementation with explicit approved intent; do not preserve a proven defect merely because it repeats.

Use the canonical project `design.md`, respecting its existing capitalization and location. The [shared template](../../build/assets/design.md) is a starting structure, not a requirement to duplicate an established document. A small fix needs only its relevant context; a missing document does not require a full product questionnaire.

Keep three kinds of information distinct:

- Product truth: who uses this surface, their task, real capabilities and accepted content.
- Project design: approved direction, actual tokens/components, density, interaction conventions and known deviations.
- Task intent: exact affected route/state, acceptance criteria, proposed alternatives and verification evidence.

Record actual source paths and token names instead of maintaining a second palette. Mark observations, inferences, proposals and approved decisions explicitly. An implementation screenshot is evidence of what exists, not evidence that the user approved it.

When work creates or materially changes the design system, inspect only the affected layers: foundations, component anatomy and variants, interaction states, responsive behavior, accessibility, theming, content guidance and migration/deprecation. Every documented token and variant needs a real consumer. Link canonical code from `design.md`; do not turn a broad checklist into a completion ritual or duplicate the implementation in prose.

For a new direction, identify the smallest meaningful choice: for example editorial storytelling versus a direct product demonstration. Compare coherent, realistic options at full size only when that choice is unresolved. A fixed number of variants, random style dice, or a question before every correction adds no quality by itself. If the user delegated the choice, make it with a brief rationale.

When alternatives are requested, show actual comparable visuals with the same content and viewport. Explain the consequential differences, preserve stable round/option IDs and link the selected artifact. A text description alone is not a visual comparison; rejected options should not silently return in a later round.

At handoff reconcile changed components, motion contracts, implementation gaps and evidence in `design.md`. Keep project-specific colors, names and screenshots local. Generalize only through [learn](../../build/internal/learn/ROLE.md); a pending proposal is not a global rule.
