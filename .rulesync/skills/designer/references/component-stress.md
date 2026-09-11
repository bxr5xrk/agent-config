# Component stress matrix

Use this for a reusable or stateful component when real variation could expose a defect. Skip it for tiny copy/style corrections and static elements with no material variation.

Read the real component API and retain only applicable axes:

| Axis | Exercise when applicable |
|---|---|
| Content | Empty, typical, long, unbreakable, emoji/diacritics, RTL or mixed direction |
| Quantity | Zero, one, realistic count and a credible large count |
| State | Loading, empty, error, disabled, pending and selected |
| Container | Narrow, squeezed by a sibling, normal and unusually wide |
| Environment | Supported theme, text enlargement/reflow and reduced motion |

Build a temporary route or fixture that imports the production component and uses the application's real fonts, tokens and providers. Add only labels, containers and realistic fixture data; do not restyle the component or replace it with a lookalike. Keep live services and production state out of the harness.

Render applicable cases together where that makes comparison easier. Exercise pointer and keyboard behavior in the real rendered result. Record only observed failures, with the exact scenario and visible consequence. A predicted issue or a source rule is not visual evidence.

When alternatives are genuinely needed, vary one consequential axis such as structure, density, emphasis, type or voice. Show each alternative at full size in the same real context with the same content and viewport. Every option must already meet the same accessibility and interaction floor; a broken option is not a candidate.

Fix relevant failures, rerun the affected cases and remove the temporary harness during closeout unless it belongs in the project's maintained preview or test system.
