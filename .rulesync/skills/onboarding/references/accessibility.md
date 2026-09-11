# Accessibility and interaction

Target WCAG 2.2 AA for applicable UI. This is a verification target, not a certification claim. Check semantic structure, names, reading/focus order, keyboard operation, contrast, zoom/reflow and errors. Source: [W3C quick reference](https://www.w3.org/WAI/WCAG22/quickref/).

Use native button for actions and anchors/Next Link for navigation; no clickable divs. Every form field needs a label, descriptions/errors linked with `aria-describedby`, and errors stated in text. Announce important asynchronous status with a restrained live region. Icon-only controls need an accessible name. Decorational images/icons must not create noise.

Keep visible focus, including against adjacent backgrounds. Test Tab/Shift-Tab, Enter/Space, Escape and focus restoration from dialogs. A modal traps focus only while open. Avoid positive tabIndex. Do not hide essential information or actions behind hover alone. Honor reduced motion and verify zoom to 200% and narrow 320 CSS-pixel reflow where applicable.

Contrast targets: ordinary text 4.5:1, large text 3:1, applicable non-text UI 3:1. WCAG 2.2 AA target size is 24×24 CSS px or qualifying spacing/exceptions; our comfort preference is 44×44 for primary touch actions, not a claim that AA always mandates 44.

User preference beyond WCAG: enabled clickable controls show a pointer cursor and discernible hover feedback; disabled controls show a distinct unavailable state. Hover and cursor alone do not constitute accessibility. Pending buttons retain their label/context, prevent duplicate submissions and announce progress; errors preserve input and provide a recovery action.

[Radix accessibility](https://www.radix-ui.com/primitives/docs/overview/accessibility) informs component selection, but primitives don't verify the surrounding form or app. Run axe on meaningful screens plus manual keyboard checks; a green automated scan cannot prove all criteria.
