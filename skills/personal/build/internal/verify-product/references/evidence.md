# Evidence by claim

| Claim | Evidence needed | What it does not establish |
|---|---|---|
| Requested behavior works | Exercise the journey with realistic inputs and an important failure/recovery case | All possible edge cases |
| Visual direction matches | Actual rendering compared with selected reference at relevant widths/states | Motion quality or usability with assistive technology |
| Animation behaves correctly | Real trigger, normal playback, temporal samples, interruption and reduced-motion checks | Frame pacing on an untested device |
| Accessible interaction | Semantics/automated checks plus keyboard, focus, zoom/reflow and relevant assistive-tech checks | Full WCAG conformance from a clean axe run |
| Runtime integration works | Correct environment, actual dependency path and resulting side effect/read-back | Production behavior from a fake provider |
| Public page is discoverable | Response/status/rendered content/metadata/crawl directives and appropriate indexing evidence | Guaranteed search ranking or inclusion in every AI answer |
| Analytics works | Intended event once, expected schema/identity, actual ingestion where accessible | Vercel logs automatically appearing in PostHog |

Use existing browser/test tooling. For reproducible visual comparisons fix browser/viewport/fonts/data and wait for readiness; inspect baseline images before accepting them. A blindly updated snapshot can normalize a regression. Keep recorded videos/traces for temporal and interaction evidence; save them after the browser context closes. Static screenshot tooling may disable animations, so check its configuration before making a temporal claim.

Test a UI with realistic long labels, empty data, errors and slow responses when those conditions affect the change. Verify feedback appears before a delayed operation finishes; repeat activation should not create accidental duplicate work. Check that solving one visual/runtime defect did not regress a coupled property such as sizing versus frame rate, or skeleton visibility versus content focus.

Motion review should distinguish endpoint geometry, mid-transition continuity and frame timing. Slow playback or contact sheets help spot discontinuities; normal-speed observation judges perceived pacing. A browser performance trace supplies timing evidence that sparse images cannot. Report the tested device/browser/viewport, trigger and timing method. Do not pretend to have watched video when only sampled frames were available.

Record findings as `required-fix`, `optional`, or `unverified`, with an observable consequence. A critical missing behavior cannot be averaged away by high visual scores. When access prevents a live check, preserve the limitation and finish independent checks.

Sources: [W3C evaluation-tool limits](https://www.w3.org/WAI/test-evaluate/tools/selecting/), [Playwright visual comparisons](https://playwright.dev/docs/test-snapshots), [video lifecycle](https://playwright.dev/docs/videos), [Chrome runtime profiling](https://developer.chrome.com/docs/devtools/performance). These sources support testing techniques; visual taste still requires contextual judgment.
