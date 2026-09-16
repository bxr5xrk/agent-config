# Persistent agent profile

The agent is a thin stateful wrapper around a reusable skill:

- `config.toml`: Codex discovery metadata and an instruction to load the profile and source skill.
- `AGENTS.md`: precedence, operating contract, and learning destinations.
- `SOUL.md`: stable role identity, judgment, taste, and communication style.
- `MEMORY.md`: local validated cross-project guidance; never commit it.
- `memory/CANDIDATES.md`: local pending guidance; never commit it.
- source `SKILL.md`: reusable method, routing, and domain procedure.

## Model policy

`config.toml` intentionally omits `model` and `model_reasoning_effort`. A
spawned custom agent inherits both values from its parent. Root or standalone
runs, including scheduled tasks, use `gpt-5.6-sol` with `high` reasoning unless
the user explicitly chooses another model or effort; that default belongs in
the native root task or automation configuration, never in the child-agent
profile.

Use this precedence:

1. Current user request and authorization boundaries.
2. Current project's instructions, contracts, and domain documents.
3. Validated cross-project `MEMORY.md`.
4. `SOUL.md` and the source skill.

## Learning destinations

- Apply feedback to the current task first. Persist at most one concise memory item only when it is durable cross-project guidance that materially changes future decisions and either the user explicitly asks to remember it globally or it is corroborated across at least 3 independent projects within 30 days.
- Before writing, inspect existing memory and prefer updating, merging, superseding, or deleting an entry over adding one.
- Keep project-specific knowledge in project documentation. Never store project names, facts, paths, selected directions, temporary task state, one-off praise or corrections, raw evidence, or content better kept in project documents.
- A universal improvement to the domain method is staged as an exact source-skill change; a universal workflow or response-policy correction is staged as an exact global `AGENTS.md` change. Publish either only after the user's batch approval.

Never put speculation, secrets, credentials, employer-private information, or
project-private data in global agent memory. A read-only specialist returns at
most one eligible proposed entry to the primary agent.
