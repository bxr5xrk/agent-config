---
name: skill-to-agent
description: >-
  Turn an existing Codex SKILL.md into a persistent custom-agent profile with
  separate identity, validated memory, learning candidates, and a canonical
  source skill. Use when creating or updating a role agent such as a backend,
  frontend, design, or research agent; not for merely editing a skill.
---

# Skill to Agent

Create a thin persistent agent around an existing skill. Keep the skill as the
canonical workflow; do not copy its instructions into the agent profile.

Read [profile structure](references/profile-structure.md) before creating or
updating a profile. Inspect the source `SKILL.md` and any existing target agent
before writing. Derive identity only from the skill and explicit user evidence;
do not invent preferences, history, or project facts.

Use the deterministic scaffold for the filesystem and hard-link mechanics:

```sh
python3 /Users/berserk/Work/agent-config/skills/personal/skill-to-agent/scripts/create_agent.py \
  --skill /absolute/path/to/SKILL.md \
  --agent-name example-agent \
  --description "When this specialist should be delegated work" \
  --install
```

The default agent root is the repository's `agents/` directory. The default
installation root is `~/.codex/agents/`. Use `--update` to refresh generated
`config.toml` and `AGENTS.md` while preserving `SOUL.md`, `MEMORY.md`, and
`memory/CANDIDATES.md`. The command refuses to replace a different installed
file unless `--replace-install` is explicit.

After a first scaffold, tailor `SOUL.md` to stable role judgment and tone. Keep
`MEMORY.md` and `memory/CANDIDATES.md` local and out of Git. Apply feedback to
the current task, but persist at most one concise item only when it meets the
strict cross-project threshold in [profile structure](references/profile-structure.md).
Stage universal skill or global-policy changes for the user's batch approval
instead of silently publishing them. Leave memory empty when the threshold is
not met.

Verify the generated TOML, required files, source-skill path, and installed
hard-link inode. When Codex is available, confirm discovery from a fresh Codex
process rather than assuming that a valid file is loaded.
