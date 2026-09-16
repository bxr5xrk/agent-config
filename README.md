# Agent config

The canonical source for reusable configs, skills, agents, hooks, and scheduled
workflows.

## Content

```text
AGENTS.md      global instructions and orchestration policy
hooks/         active prompt hook configuration and implementation
skills/
  common/       brainstorm, caveman-uk, diagram-design, grill-me, grilling
  personal/     backend, build, designer, frontend, growth, ops,
                qa, research, security, skill-to-agent
agents/
  advisor-agent/ persistent final reviewer profile and Codex agent config
  *-agent/      persistent specialist profile and Codex agent config
scheduled/      canonical instructions for recurring workflows
```

Only folders containing real configuration belong in this repository. Add `work`, `instructions`, `hooks`, `subagents`, or `settings` only when there is actual content for them.

This public repository excludes local or generated agent memory, including
`MEMORY.md`, `CANDIDATES.md`, and agent `memory/` directories.

## Apply in an agent

There is no synchronization tool or generated configuration. Tell the agent:

> Read `/Users/berserk/Work/agent-config/README.md`. Synchronize all populated `common` and `personal` configuration from this repository with the current desktop agent. Discover its native configuration paths, preserve unrelated local configuration, and verify that the agent actually discovers the result.

For a work environment, replace `personal` with `work`. Prefer links to the canonical folders when the target supports them; never overwrite an entire user configuration directory.

Keep secrets, credentials, employer-private data, and project-specific rules out of this repository. Those belong in the relevant private work repository as a local overlay.

## Codex configuration

`AGENTS.md`, `hooks/`, and agent `config.toml` files are the canonical sources
for custom global Codex behavior. Install files as hard links so edits stay
synchronized with this repository. Skill directories use symbolic links because
directories cannot be hard-linked:

```sh
cd /Users/berserk/Work/agent-config
mkdir -p ~/.codex/hooks ~/.codex/agents ~/.agents/skills
ln -f /Users/berserk/Work/agent-config/AGENTS.md ~/.codex/AGENTS.md
ln -sfn /Users/berserk/Work/agent-config/skills/common/caveman-uk \
  ~/.agents/skills/caveman-uk
ln -sfn /Users/berserk/Work/agent-config/skills/common/diagram-design \
  ~/.agents/skills/diagram-design
ln -f /Users/berserk/Work/agent-config/hooks/hooks.json ~/.codex/hooks.json
ln -f /Users/berserk/Work/agent-config/hooks/task_contract.py \
  ~/.codex/hooks/task_contract.py
ln -f /Users/berserk/Work/agent-config/agents/advisor-agent/config.toml \
  ~/.codex/agents/advisor-agent.toml
```

The global `AGENTS.md` rule applies the single permanent `caveman-uk` style to every
user-facing chat reply. The skill remains canonical in this repository;
`~/.agents/skills/caveman-uk` is a symbolic link that exposes it to Codex for
implicit invocation. There are no modes or manual activation commands.

When Codex runs inside this repository, it discovers the same hard-linked
`AGENTS.md` once globally and once at project scope. This is the deliberate
tradeoff for keeping the root file as the single canonical source.

The root agent routes work through four depths: fast, focused, discovery, and
delivery. Matching skills are implicit. `brainstorm` handles consequential
discovery; `build` handles substantial delivery; a platform goal is reserved for
long multi-phase delivery. Project work resumes from canonical local documents
and updates only the records affected by verified changes.

Use `$diagram-design` for complex explanatory or presentation-quality diagrams.
Use built-in diagramming for simple diagrams with only a few blocks.

## Codex agents

Keep each agent's canonical files in `agents/<name>/`. Install only its
`config.toml` into `~/.codex/agents/<name>.toml`. For the current Codex client,
use a hard link so the repository remains the single source of truth; ordinary
symbolic links for custom-agent TOML files were not discovered in verification.
Recreate hard links after a Git operation or editor replaces a canonical file's
inode. Verify links with `ls -li`: each canonical/installed pair must share an
inode.

Every custom-agent `config.toml` intentionally omits `model` and
`model_reasoning_effort`, so a spawned agent inherits both from its parent.
New root or standalone runs, including scheduled tasks, use `gpt-5.6-sol` with
`high` reasoning unless the user explicitly chooses another model or effort.
Apply that root-run default in the native Codex configuration or automation;
do not add it to child-agent TOML files.

```sh
ln -f /Users/berserk/Work/agent-config/agents/design-agent/config.toml \
  ~/.codex/agents/design-agent.toml
```

Create the same persistent structure around another canonical skill with
`$skill-to-agent`; its helper preserves profile memory on `--update` and can
install the agent config as a hard link.

## Scheduled workflows

Keep the complete instructions for recurring work in `scheduled/`. The live
Codex automation should point to the canonical file instead of duplicating its
prompt, so repository changes take effect on the next run.

[Daily review](scheduled/daily-review.md) is
the source of truth for the daily review.
