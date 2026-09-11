# Review the delivered result

Acceptance comes from the user's brief and selected artifacts. Before implementation, derive at least the important happy path and consequential failure/recovery cases; do not let passing implementation-generated tests replace those requirements.

After integration:

1. Record the reviewed file set and content hashes (or an existing exact revision). Reviewers inspect the current code and actual runtime. No Git is required: scoped local before/after copies and ordinary diffs suffice.
2. `verify-product` checks the requested scope: missing, incorrect or unrequested behavior, plus the real journey, appearance, responsiveness, accessibility and temporal motion when applicable. `simplify` checks engineering correctness and documented project standards, including contracts, regression risk and unnecessary complexity. Keep those two verdicts distinct so one cannot mask the other. Add focused security review for changed trust boundaries; do not add another duplicate reviewer pair.
3. Classify findings by observed consequence, evidence and whether they are required fixes or optional suggestions. Do not make all aesthetic preferences release blockers. A failed agreed behavior is a blocker; an untested requirement remains unverified.
4. Resolve disagreements using the brief, reproduction and authoritative constraints. Send accepted fixes to the responsible writer. Simplifier edits occur sequentially after implementation ownership is released.
5. Rerun affected checks and review the final bytes. A review of earlier bytes cannot certify later edits. Keep integration-level checks for interactions between individually correct components.

Do not loop cosmetic changes indefinitely. If successive attempts do not resolve the same defect, reassess the cause and evidence, use focused diagnosis, and isolate the unknown. Continue independent useful work; surface a real missing decision/access only when it blocks progress.

Use [diagnosis](diagnosis.md) for uncertain failures and [behavioral checks](behavior-checks.md) to assess whether tests can actually detect a wrong implementation. Cite the violated project standard or accepted requirement for each relevant finding; distinguish a demonstrated defect from an optional design heuristic.

Return a concise evidence ledger per acceptance ID: verified, failed, unverified, blocked or explicitly deferred. Link the command/result or browser evidence and its conditions. Build/typecheck, fake provider tests, screenshots, sampled animation frames, runtime interaction and live provider behavior are distinct forms of evidence.

The two-reviewer design is a workflow safeguard, not a guarantee of correctness or taste. Correlated model mistakes remain possible. Important acceptance cases should be exercised by executable checks or independently observed behavior, not approved only by two textual opinions.

Basis: [Compound Engineering](https://github.com/EveryInc/compound-engineering-plugin), [StrongDM scenarios](https://factory.strongdm.ai/), [GEPA held-out evaluation](https://gepa-ai.github.io/gepa/guides/gskill/). Adopt scoped independent evidence and evaluation; do not import unrelated autonomous publish/commit behavior or spending prescriptions.

The separate requirements/engineering axes also draw on [AI Hero code-review](https://github.com/mattpocock/skills/blob/3cca18b368ae95cdbdebbff572ccafa662551015/skills/engineering/code-review/SKILL.md); the existing two reviewers own them.
