# Agent config

Personal, provider-neutral source for reusable agent instructions. Rulesync generates the native files consumed by Codex Desktop and Claude Code Desktop; additional agent hosts can be enabled later.

The repository is named `agent-config`, a common convention for standalone AI-agent configuration repositories. Unlike a general `dotfiles` repository, its scope is intentionally limited to agent behavior and workflows.

## Desktop support

This setup is desktop-first. Rulesync is only the build and synchronization engine; it does not require using either agent through a terminal:

- Codex Desktop loads standalone user skills from `~/.agents/skills` and global instructions from `~/.codex/AGENTS.md`.
- Claude Code Desktop shares `~/.claude` configuration, skills, hooks, permissions, and MCP settings with Claude Code's other local surfaces.

The official references are [OpenAI's skill locations](https://learn.chatgpt.com/docs/build-skills#where-codex-loads-local-skills), [OpenAI's `AGENTS.md` discovery](https://learn.chatgpt.com/docs/agent-configuration/agents-md), and [Anthropic's shared Desktop configuration](https://code.claude.com/docs/en/desktop#shared-configuration).

## Layout

```text
.rulesync/
  skills/<name>/SKILL.md   reusable Agent Skills
  rules/                   shared always-on instructions
  subagents/               shared subagent definitions
  hooks.jsonc              shared lifecycle hooks
  hooks/                   hook scripts
  mcp.jsonc                shared MCP declarations without credentials
  permissions.jsonc        portable permission policy
profiles/                  logical skill collections; not discovery paths
rulesync.jsonc             targets and generation policy
```

`.rulesync/` is the single canonical source because it is Rulesync's default input tree. Skills stay flat under `.rulesync/skills/`; each skill owns its supporting `references/`, `scripts/`, `assets/`, and optional provider metadata.

Generated `.agents/` and `.claude/` directories are not source files and are not committed. Desktop synchronization writes the native outputs directly to the user directories. Do not edit generated files there; edit `.rulesync/` and synchronize again.

The `shared` and `codex-personal` profiles document the intended distribution:

- Shared between Codex and Claude Code: `grilling`, `grill-me`, `brainstorm`.
- Codex only: `backend`, `build`, `designer`, `frontend`, `onboarding`.

The `targets` field in each canonical `SKILL.md` enforces this distribution. `codexcli` is Rulesync's adapter identifier for Codex's local file format; the generated user files are also what Codex Desktop reads.

Only the populated `skills` feature is enabled initially. The canonical directories for rules, subagents, hooks, MCP, and permissions are ready; enable each feature in `rulesync.jsonc` after adding and validating real content.

## Commands

```sh
pnpm install --frozen-lockfile
pnpm desktop:preview
pnpm desktop:apply
pnpm desktop:check
pnpm claude:preview
pnpm claude:apply
pnpm claude:check
```

The `desktop:*` commands update both desktop agents. The `claude:*` and `codex:*` commands update one agent only. Always review the matching `*:preview` command before applying a change.

At present, only skills are enabled. Rules, subagents, hooks, MCP, and permissions remain empty until each shared policy has a real implementation and a verified adapter for both hosts. Provider-specific behavior belongs in an adapter, not in the portable core.

## Scope

- Keep only reusable personal conventions and workflows here.
- Keep employer-specific skills, project context, code style, and secrets in the relevant work repository as a project-local overlay.
- Put provider-specific fields in the matching Rulesync target block instead of forking the whole skill.
- Never commit credentials, OAuth tokens, private work data, or local `rulesync.local.jsonc` overrides.

Models such as DeepSeek are reusable through the host agent that runs them. Add the host target (for example OpenCode or Cline), not a model-name directory.
