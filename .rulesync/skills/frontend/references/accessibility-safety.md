# Accessible interactions and browser safety

Use native links for navigation and buttons for actions. Preserve keyboard behavior, accessible names, labels and error associations when composing primitives. Interactive controls need visible focus and clear hover/pressed/disabled/busy states where applicable. Use a pointer for clickable controls under this user's UI convention; a pointer does not establish accessibility.

Dialogs, menus and composite widgets require their actual keyboard model, managed focus and sensible focus restoration. Prefer a verified existing primitive over rebuilding that behavior. Announce important asynchronous status without flooding live regions; errors must be understandable without color alone. Keep controls usable with zoom, reflow, keyboard and touch.

Target WCAG 2.2 AA for applicable web UI: normal text contrast 4.5:1, large text 3:1, relevant control/graphical contrast 3:1. Target-size minimum is 24 CSS pixels with specified exceptions; 44 pixels is a useful comfort target, not the AA rule. Honor reduced-motion preferences, including JavaScript animations.

All client-shipped values are visible to the user. Keep credentials and privileged operations on the server. Render untrusted values as text; rich HTML needs a maintained sanitizer and a defined allowlist, not ad hoc replacement. Validate untrusted navigation/asset URLs for their allowed protocol and destination. Preserve the application's CSP and trusted embedding assumptions when adding scripts.

## Verify

Walk the changed task by keyboard: visible focus, logical order, activation, dismissal and restoration. Test labels/errors with an accessibility tree or assistive technology where relevant. Check 200% zoom, narrow reflow, touch targets and reduced motion. Run axe or equivalent for detectable issues, then inspect manually; an automated pass is not a conformance claim. For changed rich-content or URL handling, use a targeted unsafe-input case and inspect the actual DOM behavior.

Sources checked 2026-09-05: [WCAG 2.2 quick reference](https://www.w3.org/WAI/WCAG22/quickref/), [OWASP DOM XSS](https://cheatsheetseries.owasp.org/cheatsheets/DOM_based_XSS_Prevention_Cheat_Sheet.html), [Next data security](https://nextjs.org/docs/app/guides/data-security). Pointer styling is a user preference.
