# Agent config

The canonical source for reusable configs, skills, agents, hooks, and scheduled
workflows.

## Content

```text
AGENTS.md      global instructions and orchestration policy
hooks/         active prompt hook configuration and implementation
  claude/       Claude Code answer-review and answer-shape hooks
skills/
  common/       brainstorm, caveman-uk, diagram-design, grill-me, grilling
  work/         gitignored: employer-private skills and data (pr-visual,
                answer-review pairs); never pushed
  personal/     backend, build, designer, frontend, growth, ops,
                qa, research, security, skill-to-agent,
                Emil Kowalski design and animation skills
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
for skill in emil-design-eng animate review-animations improve-animations \
  find-animation-opportunities prototype animation-vocabulary; do
  ln -sfn "/Users/berserk/Work/agent-config/skills/personal/$skill" \
    "$HOME/.agents/skills/$skill"
done
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
and updates only the records affected by verified changes. `advisor-agent`
checks focused, discovery, and delivery answers; fast answers skip it.

Use `$diagram-design` for complex explanatory or presentation-quality diagrams.
Use built-in diagramming for simple diagrams with only a few blocks.

The seven design and animation skills above are preserved from
[emilkowalski/skills](https://github.com/emilkowalski/skills) at commit
`d16ebe60d09a5ba2afcb7054ede9d0a10c9f6128`. Each directory includes its
MIT license. The `designer` and `frontend` skills route relevant work to them;
direct invocation remains available. `apple-design` and `pick-ui-library` are
not installed.

## Claude Code answer hooks

`hooks/claude/` keeps the hooks that shorten Claude Code replies:

- `answer-review.py` — `MessageDisplay` hides a reply longer than 400 characters,
  reviews it with Opus against example pairs, and `PostToolUse`/`Stop` ask the
  agent to rewrite it; state lives in `~/.claude/state/answer-review/`.
- `answer-shape-prefix.py` — prompt prefixes `так/ні:`, `рішення:`, `аудит:` set
  the answer shape.
- `answer-shape-log.py` — logs answer-shape violations without blocking.
- `caveman-mode-tracker.js` — the caveman plugin tracker with the local per-turn
  rule; install caveman first, then replace its tracker.
- `settings.hooks.json` — the matching `hooks` entries for
  `~/.claude/settings.json`; merge them, do not overwrite the file.

The review examples are real work chats, so
`skills/work/answer-review/answer-review-pairs.json` is gitignored. Without it,
build new pairs from rejected («коротше») and accepted replies.

```sh
mkdir -p ~/.claude/hooks ~/.claude/skills
for f in answer-review.py answer-shape-prefix.py answer-shape-log.py \
  caveman-mode-tracker.js; do
  ln -f "/Users/berserk/Work/agent-config/hooks/claude/$f" "$HOME/.claude/hooks/$f"
done
ln -f /Users/berserk/Work/agent-config/skills/work/answer-review/answer-review-pairs.json \
  ~/.claude/hooks/answer-review-pairs.json
ln -sfn /Users/berserk/Work/agent-config/skills/work/pr-visual \
  ~/.claude/skills/pr-visual
```

The Codex port is not done yet; it needs Codex hook events that can hide or
replace a reply.

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
