# Choosing and owning animation

Read the installed library/version and existing components before choosing a mechanism. Use current official documentation for uncertain APIs; these are selection criteria, not frozen implementation recipes.

| Need | Candidate, subject to existing stack |
|---|---|
| A simple state transition | CSS transition/keyframes; JS only where state or control requires it |
| Imperative playback, cancellation or coordination without a framework layer | Web Animations API |
| React presence, layout transitions or gestures | Existing Motion integration or equivalent established component capability |
| Coordinated timelines, SVG or many related DOM elements | Anime.js when its controls solve the task |
| Scroll-driven decoration | Existing/native mechanism with verified browser support, fallback and reduced-motion behavior |

One owner controls a property at a time. A CSS hover transform and a gesture/timeline transform can silently overwrite each other; compose intentionally or give different wrappers clear responsibilities. Avoid adding a second engine for a trivial variant of an existing transition.

Model the interaction before its interpolation. Keep meaningful state in application logic; do not depend on `animationend` alone for saving, cleanup, accessibility state or becoming usable. Decide which actions can interrupt, reverse or queue and which confirmation commits a destructive operation. Preserve focus and pointer ownership when visual elements leave.

Scope selectors and resources to the component. Cancel/revert animations, listeners, observers and timers on cleanup; verify remounts and rapid toggles do not duplicate work. Anime.js scopes support component roots, media-query matching and batch reversion. Confirm the actual version's API. [Official scope documentation](https://animejs.com/documentation/scope/)

Prevent initial hidden states from making essential content unavailable if hydration, an observer or animation setup fails. Animated text clones should not duplicate spoken content or focusable controls. Dragging needs correct cancellation and an appropriate non-drag path; touch gestures must coexist with intended page scrolling.

Prefer inexpensive properties when they produce the intended effect, commonly transform and opacity. Hardware acceleration is property-, engine-, API- and browser-dependent, not guaranteed by choosing CSS, WAAPI or a named library. Layout/filter effects can be valid in bounded cases; measure observed cost on relevant devices rather than banning them or sprinkling `will-change` everywhere. Motion documents these changing limits, including implementation differences for individual transforms. [Official performance guidance](https://motion.dev/docs/performance)

Pause unnecessary offscreen/background work where appropriate. Keep progress tied to real work; decorative timers must not misrepresent completion. Verify the semantic result and the motion together using [temporal QA](temporal-qa.md).
