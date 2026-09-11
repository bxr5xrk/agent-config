# Brand from product intent

Use for a new customer-facing product or requested rebrand. The outcome is a coherent small identity used in real screens, not a speculative brand strategy deck. Internal tools inherit the owning brand and need only the applicable identity notes; an API-only project does not require a logo campaign. Read [naming](naming.md) only when naming is needed and [logo design](logo-design.md) when creating or assessing a mark.

## Establish what is fixed

Inspect supplied assets and existing use before asking. Record exact display name, capitalization, script, logo masters, palette, fonts, usage rights/provenance and what the user considers approved. Keep display name separate from the ASCII repository/package slug. Never rename an approved brand merely because a domain or slug differs.

| Input | Action |
| --- | --- |
| Name and logo | Preserve both; assess readability and available variants, fill missing system rules. Propose a material change only with a concrete reason. |
| Name only | Keep its spelling; explore compatible logo, typography and color directions. |
| Logo only | Inspect the symbol and any embedded wordmark; do not assume ownership or invent the intended reading. Develop a name if missing. |
| Neither | Derive positioning from the agreed product brief, then develop name and visual identity. Absence of assets is not a blocker. |
| Existing brand with inadequate contrast | Retain approved logo colors where practical; create accessible UI color roles. Logo exemption does not exempt buttons or text. |

Resolve material uncertainty through discovery, one decision at a time. A vague request is not permission to invent the audience or code the site. Within an agreed brief, make routine palette/type/export decisions and explain the rationale; do not ask the user to pick every hex value. Preserve explicit delegation of naming or visual choices.

## Lightweight positioning

Write a few concrete lines: audience and situation, promise grounded in actual scope, reason to believe, useful distinction from alternatives, and 3 character traits with their opposites. Example: “calm, precise, human; not clinical, playful or grandiose.” These are project choices, not a universal house style. Define voice with an actual headline, CTA, success message and helpful error; do not invent traction, clients or testimonials.

Names, colors and marks must follow that context. Do not generate a polished identity for an unresolved product assumption just to make discovery feel productive.

## Explore as one identity

When a name is missing, present a reasoned naming shortlist before finalizing a wordmark; a clearly labelled working name can support inexpensive visual exploration. Supply actual visual studies for logo candidates, not descriptions alone. Usually 3 distinct logo concepts are enough before refinement; adapt to supplied assets and user instructions.

When a visual direction is unresolved, explore the smallest useful set of alternatives and honor the requested count. Integrate identity into that exploration: distinct composition, typography, color use and image language, with the same product content. Do not create a Cartesian product of every name × logo × landing. Keep stable IDs for name, logo and UI options so a combination is unambiguous. Preserve approved UI without another comparison; a supplied UI design does not settle an absent name.

Show shortlisted identities in context: header, tiny favicon, a real CTA/form state, and a public social preview where relevant. Compare 2–3 finalists side by side. For animated landings show motion previews using [landing guidance](landing.md) and the [motion procedure](../internal/motion/ROLE.md). Explain fit and weaknesses, recommend one, and wait for selection unless that specific choice was explicitly delegated. Do not interpret “choose a name” as delegation of the whole design gate.

## Minimal brandbook

Fill [BRAND.md](../../build/internal/bootstrap/assets/documents/BRAND.md) with actual chosen values and assets. Keep it short enough to use, but include:

- Positioning, exact name, spelling/pronunciation where useful, tagline only if useful, voice examples and discouraged claims.
- Primary logo/wordmark, small mark, monochrome/reversed variants as applicable; tested clear space and minimum sizes; light/dark background and misuse examples.
- Palette with semantic roles, actual values and permitted text/background contrast pairs; status colors must not rely on hue alone.
- Heading/body fonts, weights, fallback stack, language glyph coverage, source/license and loading strategy. A distinctive heading family is welcome when appropriate; no mandatory novelty font.
- Image/illustration/icon direction, composition rules and bounded motion character, linked to DESIGN.md.
- Master and export locations, source/rights record, selected option IDs, decision status, actual verification and limitations.

Use one source of truth: BRAND.md defines identity intent and approved asset references; DESIGN.md links to the implemented token source and component behavior. Reconcile values with code; do not let two independently maintained palettes drift. Put final project assets in the project's source/public asset tree, documentation at its established project location. No ZIPs, extra delivery folders or separate brand portals unless requested.

## Stress tests before handing off

Check the identity against the intended audience and promise, a competitor reference set, small-size reading, long/short headings, relevant languages, light/dark/monochrome use and real mobile screens. Record observations rather than self-awarded “premium” scores. Ask for real target-user feedback only when available and material; never present an agent's imagined reactions as user research. Fix the weakest meaningful inconsistency and recheck it; avoid infinite subjective polishing.

Deliver a usable wordmark-first identity if that is stronger than the symbol explorations. State any unresolved production limitation; an attractive generated concept is not automatically an editable, tested logo master.

Reference examples, reviewed 2026-09-05: [Mozilla logo usage](https://mozilla.design/mozilla/logo-usage/) documents variants, proportional scaling, small-size rules and spelling; [WCAG 2.2](https://www.w3.org/TR/WCAG22/) distinguishes logo text from ordinary UI contrast requirements. Derive this project's own geometry and sizes; do not copy Mozilla's mark or brand-specific measurements.
