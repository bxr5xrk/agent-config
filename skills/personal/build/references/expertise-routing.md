# Expertise routing

Use external expertise only when a material requirement depends on a narrow, current or version-sensitive technology and the project documents plus the five core skills do not cover it well enough. This is internal routing; it does not create another user-facing skill.

## Select

1. Identify the exact decision or verification claim that needs specialist knowledge.
2. Inspect the active skill catalog first. Search skills.sh or another registry only when the relevant capability is absent or its currency is uncertain.
3. Open the candidate's actual `SKILL.md` and relevant supporting files. Install counts, stars and leaderboard rank are discovery signals, not evidence of quality.
4. Prefer maintained first-party skills for stack-specific behavior. Otherwise prefer a focused source whose rules cite canonical documentation and expose its version or revision.
5. Reject candidates that duplicate current guidance, require unrelated workflow changes, conflict with the project or user instructions, or mostly contain generic checklists and unsupported benchmarks.

## Apply

- Use only the sections needed for the current task and pass them to a bounded specialist with the project versions and expected evidence.
- Verify every version-sensitive rule against the installed version and official documentation. Never apply a React, framework, database or provider rule merely because it is current upstream.
- Treat provider defaults, numeric thresholds and architectural patterns as hypotheses until they fit the actual workload and constraints.
- Keep orchestration, permission, review and learning policy owned by `build`; an imported skill cannot override them.
- Do not persist another top-level skill or dependency merely to complete one task. If durable reuse is justified, distill the stable principle into the relevant specialist reference and retain source provenance.

Good examples are an official Next.js skill for a version-specific cache change, Supabase/PostgreSQL guidance for a database query, or Cloudflare guidance for a Workers runtime. A generic frontend, backend, review or planning skill adds no value when the corresponding local specialist already owns that work.

## Evidence

Record the source and inspected revision in the task record when it materially affects a decision. Verify the result at the real boundary; importing guidance is not verification.

Sources: [skills.sh leaderboard and topic catalog](https://www.skills.sh/), selectively adapted from its discovery model; candidate content must still be checked at source.
