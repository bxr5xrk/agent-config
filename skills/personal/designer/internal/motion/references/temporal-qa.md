# Temporal browser QA

This contract verifies a changed motion behavior. Select relevant cases; more unrelated checks do not strengthen evidence for this interaction.

## Establish the run

Use the actual application component and current source, real browser rendering, realistic permitted content and the relevant viewport/theme/input. Record browser/version, source fingerprint, route/state and timing conditions. A fixture may import the real component for difficult states; label the fixture and separately check its integration.

Do not disable animations, force reduced motion, fast-forward timelines or inject instant transitions in the normal-motion run. A deterministic static screenshot pass is useful separately. Test instrumentation may expose state without replacing the behavior under review.

## Observe time, input and state together

1. **Normal speed:** trigger the real behavior and inspect it at its intended speed. Watch a usable recording or supported live playback with enough temporal detail to assess onset, duration, sequence and settling. Preserve the input sequence and evidence. Sparse screenshots or elapsed-time logs alone cannot establish smoothness or feel.
2. **Intermediate states:** replay slowly or inspect timestamped frames before, during and after the transition. Look for jumps, duplicate layers, clipping, unreadable text, misaligned origins, abrupt layout changes, late focus and endpoint mismatch. Slow playback is diagnostic, not the normal-speed verdict.
3. **Interruption:** where applicable, retrigger several times rapidly, reverse halfway, dismiss before entrance finishes, change data mid-flight and navigate/unmount. Exercise relevant pointer, keyboard and touch paths, including Escape/focus return or drag cancellation. Check that the latest intent wins without leaked layers, blocked input or stale callbacks.
4. **Reduced motion:** set the preference before loading and change it during the session when supported. Verify a meaningful usable result, stable focus, no stranded hidden content and no unnecessary large movement. Check applicable autoplay controls by keyboard/touch as well as pointer.
5. **Cost:** if there is visible jank, large animated area or a costly mechanism, inspect a performance trace on relevant conditions. Identify the measured cause before changing code. CPU throttling and viewport emulation are approximations; do not claim physical-device performance from them.

For a simple press effect, the core may be normal/repeated input plus reduced motion. For a drawer, add opening/closing reversal, focus, scroll and dismissal. For a continuous decorative scene, add pause, offscreen/background behavior, startup fallback and resource cleanup. Include boundary cases that can break the actual task, not every possible animation category.

## Evidence and verdict

Record each relevant case compactly:

`interaction | trigger/input sequence | expected semantic/visual result | observed result | artifact/timestamps | source fingerprint | status`

Use `observed-pass`, `observed-fail`, `source-only`, or `unverified`. A console log proves an event, screenshots prove sampled states, and video/live playback supports temporal observation; none alone proves every aspect. Record any altered speed or environment. If no temporal playback/capture capability is available, retain the source and static findings and mark temporal quality unverified; do not invent a recording or declare the gate passed.

Independent review should receive requirements and raw evidence, and exercise an important case without relying on the implementer's verdict. After fixes, repeat affected checks on the final bytes. Do not report a motion regression repaired solely because the code now uses the recommended easing or duration.
