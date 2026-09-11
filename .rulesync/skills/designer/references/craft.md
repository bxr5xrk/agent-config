# Visual judgment

Read the existing design before applying these heuristics. They are decision aids, not an aesthetic validator.

**Hierarchy.** Decide what the user should notice, read and do. Adjust grouping, position, weight, size and contrast deliberately; do not make every important item large or filled. Multiple primary actions can be appropriate in independent task contexts. A visible option count is not a working-memory test.

**Typography.** Use the project's type system and real font files/weights. Judge line breaks, measure, hierarchy, numbers and small labels at actual size. Balance short headings, allow unbreakable user content to wrap, keep truncated important content recoverable and use tabular figures where changing numbers must remain aligned. For a new or explicitly revised responsive system, fluid type and spacing may interpolate between verified minimum and maximum values; retain discrete steps when the product's density or existing tokens require them. Font reputation does not determine whether it fits: Inter, a system font or a display face can each be appropriate. Do not replace typography to satisfy a blacklist.

**Composition.** Use spacing to explain relationships before adding containers. Cards, borders, asymmetry, eyebrow labels and gradients need a role, not universal approval or prohibition. Check optical alignment, repeated rhythms, density and neighboring elements. For nested rounded surfaces, reconcile outer radius, inner radius and padding so the geometry reads as one system. Choose scale steps that fit this system rather than imposing a new arithmetic sequence.

**Color and surfaces.** Preserve semantic token roles and actual contrast. A color-space migration, ban on black/white, fixed palette size or fixed hue separation is not automatically an improvement. Match layering, elevation and borders to the task; avoid making critical content depend on translucent backgrounds remaining favorable.

**Interaction.** Active controls need discoverable affordances and visible focus, with appropriate hover, pressed, disabled and pending treatment. This user's web UI convention is `cursor: pointer` on enabled actionable controls, unless an explicit project/platform decision supplies a different convention. Do not infer approval of missing affordances merely because old code omitted them. Cursor shape and animation are separate from accessible names, semantics and keyboard operation. Hover effects should not conceal the only route to an action.

**Content and assets.** Give each graphic a communication job. Inspect crop, resolution, alt treatment and actual rights. Use one coherent icon language per surface; customize stroke, container or color only when it supports the product identity or improves recognition, and preserve the source library's license. Remove false precision, invented proof and copy that repeats a nearby heading. Meaningful labels remain available to assistive technology and forms retain proper labels even when a visual design is compact.

**Product language.** Match the product's established terms and voice, while changing tone with the stakes. Prefer direct verb-first actions and destination-specific links. Confirmations name the consequence; errors state what happened and how to recover; empty states orient the user and offer the relevant next action. Placeholders demonstrate format and never replace labels. Keep variable sentences whole for localization instead of concatenating fragments.

Judge changes against user task, approved direction and rendered evidence. State a preference as a preference; escalate it to a defect only with an observable consequence or an actual requirement. For substantial motion use [motion judgment](../internal/motion/references/judgment.md).

For the underlying hierarchy, spacing, text and image reasoning from the supplied book, use [Refactoring UI foundations](foundations.md), including its contextual and accessibility limits.
