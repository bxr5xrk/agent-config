# Checks that can disagree with the implementation

Derive the expected outcome from the accepted behavior, a known fixture or an independently worked example. An assertion that repeats the implementation's formula or copies its current output cannot independently establish correctness.

Choose an existing meaningful boundary: user action, public module/API, persisted invariant or external effect. Check the layer that actually enforces the claim. Mocks can isolate failure handling; real database/provider behavior is required for claims about concurrency, queries, migrations or live integrations. Preserve useful tests even when their current placement is imperfect.

For a real bug or explicitly requested test-first feature, work one useful behavior at a time: observe the relevant failing check, implement the minimum change that passes it, then continue. A failure caused only by broken setup is not the required behavioral failure. Small necessary restructuring is allowed while retaining the behavior checks. Do not write a large imagined suite before learning from the first slice.

For a narrow reversible presentation/documentation change, use an appropriate direct or visual check instead of adding tests that mirror the edit. Derive test boundaries from the brief and existing code; routine test design does not require another permission question. Ask only when an unresolved product contract materially changes the expected result.

Keep relevant failure/recovery cases and run integration checks after independently built parts meet. Recheck affected behavior after simplification or repair. Label checks as observed, simulated or unavailable so a mock success cannot become a live-provider claim.

Adapted from [AI Hero TDD](https://github.com/mattpocock/skills/blob/3cca18b368ae95cdbdebbff572ccafa662551015/skills/engineering/tdd/SKILL.md) and its [test examples](https://github.com/mattpocock/skills/blob/3cca18b368ae95cdbdebbff572ccafa662551015/skills/engineering/tdd/tests.md), with project-appropriate boundaries and verification effort.
