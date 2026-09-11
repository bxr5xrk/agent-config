# Browser evidence for design

Select checks according to the change and credible risks. Do not launch a ceremonial full audit for a spelling correction; do not call a new interactive page complete after looking at its hero.

## Inspect the actual result

Use the project's real route, components and realistic permitted data. Confirm the current build, loaded fonts, assets, theme and intended state. Record source/version or a local file fingerprint so later edits invalidate the right evidence. A rebuilt lookalike fixture cannot prove the production component works.

Inspect relevant narrow, wide and intermediate layouts at 100% screenshot scale, including meaningful overflow and below-the-fold content. For text/layout work exercise text enlargement and reflow: normally 200% text and an effective 320 CSS px width, such as 400% browser zoom on a 1280 CSS px viewport. Account for legitimate two-dimensional content exceptions. Device emulation is not proof on physical hardware.

Compare hierarchy, typography, crops, density and states with the selected direction. Check hover/pressed/pending/error states where changed, keyboard traversal, visible unobscured focus, touch affordances and relevant accessible names/roles. For dialogs, menus and forms exercise the actual behavior, not just attributes. Automated accessibility scans help find defects but do not establish full conformance.

## Measure relevant accessibility

- WCAG 2.2 AA text contrast is generally 4.5:1; large text has a 3:1 threshold at 18pt regular or 14pt bold (24 CSS px or about 18.67 CSS px). Apply documented exceptions and use computed foreground/background colors; screenshot antialiasing is not the calculation. Dynamic imagery/transparency needs checks across relevant states and crops. [SC 1.4.3](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html)
- AA target size is 24 by 24 CSS px or a specified exception, including sufficient spacing. A larger target such as 44px can be a sensible touch goal; it is not the universal AA requirement. Check expanded hit areas for collisions. [SC 2.5.8](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)
- Accessible controls need correct semantics, labels, keyboard operation and visible focus. Contrast and cursor checks alone cannot cover these. Use the applicable standard and established component behavior when a specific uncertainty arises.

## Separate static and temporal evidence

Settled screenshots can support visual comparison. If animations were disabled or fast-forwarded for those captures, say so and run a separate normal-motion pass. A before/after screenshot, DOM attribute, timer log or source rule cannot establish how a transition looks in between. Apply the [temporal QA contract](../internal/motion/references/temporal-qa.md) whenever motion is added or changed.

For each material finding preserve: route/component, viewport/theme/input, trigger and state, expected result, observed effect, evidence path and current source fingerprint. Mark `observed`, `source-only`, or `unverified`; a missing tool is not a pass. Independent review should receive the accepted direction, relevant acceptance criteria and raw evidence before the implementer's verdict. Fix relevant issues and verify the final changed bytes.
