# Verify product

Judge the actual result using the [project context](../../references/context.md) and [evidence contract](references/evidence.md). In a delegated review, begin from requirements and raw artifacts rather than the implementation agent's verdict.

1. Identify the requested behaviors and affected surfaces. Read the selected design, current code and actual verification artifacts; reconcile stale documents before judging.
2. Exercise the relevant journey and important failure/recovery conditions. For UI, open the actual rendered result and compare composition, hierarchy, density, content and states against the approved direction. Use narrow/wide and relevant input modes.
3. For motion, load the [motion specialist](../../../designer/internal/motion/ROLE.md) and its temporal verification guidance. Watch the triggered behavior at normal speed and inspect intermediate states, interruption and reduced motion. Stills alone support only static findings.
4. For public pages, use the frontend SEO/measurement references; for APIs, inspect contract/runtime evidence. Apply only relevant checks, not every possible audit.
5. Return actionable findings with location/trigger, observed effect, requirement, evidence and severity. Separate taste suggestions from failures. Report unverified behavior explicitly. Do not invent an issue to justify the reviewer role.

Review is read-only by default. Send fixes to the owner, then verify the repaired result and final bytes. Do not rewrite an agreed design or weaken acceptance to make the result pass.
