# Scope before promotion

| Observation | Destination |
|---|---|
| This project uses a specific brand, provider, route or domain rule | Project design/architecture/brief |
| User explicitly says a preference applies across projects | Candidate tagged `preference`, with exact provenance and exceptions |
| A failure reveals a reusable mechanism | Role-specific candidate, narrow applicability, forward test and counterexample |
| A one-off workaround or unverified guess | Local notes, not an active global rule |

Record a correction after its cause and repair are understood. Distinguish what the user said, what the code/runtime demonstrated, and your interpretation. Repetition strengthens a candidate but does not replace approval. One clear engineering counterexample may justify a narrow rule; do not require an arbitrary occurrence count.

A good candidate says when it applies and what check prevents the failure. Prefer “for an asynchronous destructive action, show pending feedback and prevent accidental duplicate submission” over “all buttons must animate.” Project taste must not become a universal aesthetic ban. A direct global preference still yields to a later explicit project decision when technically valid.

Keep global knowledge small: specialize broad rules, merge duplicates, supersede contradicted lessons, remove stale framework claims, and keep long evidence outside recall. Curate when relevant corrections accumulate or a reviewed lesson proves wrong; do not create an unsolicited background monitor.

When approved maintenance changes a skill or its references, use [skill maintenance](skill-maintenance.md) to keep instructions reachable and test their effect. Automatic candidate capture alone does not authorize rewriting global instructions.

Historical audit candidates in the local knowledge store are proposals. Where a baseline engineering principle is already supported by current docs, the skill can teach that sourced principle; this does not imply that every historical user preference has been globally approved.

Source patterns: [Compound Engineering](https://github.com/EveryInc/compound-engineering-plugin) for capturing verified lessons, [Hermes write approval](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills/) for staged review, [GEPA](https://gepa-ai.github.io/gepa/guides/gskill/) for testing transfer. This implementation uses local snapshots rather than Git.
