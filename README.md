# Agent config

One private, model-neutral source for reusable agent skills and configuration. Content is organized by life context, not by the model or desktop app currently using it.

## Structure

```text
skills/
  common/       used in every context
  personal/     private projects and personal workflows
  work/         reusable work-only skills
instructions/   future always-on instructions, split by the same scopes
hooks/          future lifecycle hooks, split by the same scopes
subagents/      future specialist definitions, split by the same scopes
settings/       future portable settings, split by the same scopes
profiles/       selects scopes for a context
scripts/        safe synchronization adapters
```

Every skill exists once. A desktop agent sees it through a symlink from its native user skill directory to the canonical folder in this repository.

Current profiles:

- `personal` = `common` + `personal`
- `work` = `common` + `work`

Current content:

- `common`: `brainstorm`, `grill-me`, `grilling`
- `personal`: `backend`, `build`, `designer`, `frontend`, `onboarding`
- `work`: empty until work-safe reusable content is added

The profile and the target are independent. Today `personal` can be installed into Codex and `work` into Claude; tomorrow those targets can be swapped without moving or renaming any content folder.

## Synchronize desktop skills

Preview is the default and does not write anything:

```sh
pnpm sync --profile personal --target codex
pnpm sync --profile work --target claude
```

Apply and verify:

```sh
pnpm sync --profile personal --target codex --apply
pnpm sync --profile personal --target codex --check

pnpm sync --profile work --target claude --apply
pnpm sync --profile work --target claude --check
```

To use the work profile in Codex later, only the command changes:

```sh
pnpm sync --profile work --target codex --apply
```

You can also ask either desktop agent:

> In `/Users/berserk/Work/agent-config`, preview and apply the `work` profile to the `claude` target, then run the matching check.

The target names exist only in the adapter command because each desktop app has a different native discovery path:

- Codex: `~/.agents/skills`
- Claude Code: `~/.claude/skills`

The synchronizer never overwrites an unrelated file or directory. It only removes links previously recorded as managed in `~/.config/agent-config/state.json`.

[OpenAI documents the Codex skill discovery paths](https://learn.chatgpt.com/docs/build-skills#where-codex-loads-local-skills). [Anthropic documents that Claude Code Desktop shares the same local configuration and skills](https://code.claude.com/docs/en/desktop#shared-configuration).

## Boundaries

Only skills are synchronized now because they are the only populated artifact type. Instructions, hooks, subagents, and settings remain canonical placeholders until each has a real portable format plus a tested adapter for the target host.

Keep secrets, credentials, employer-private data, and project-specific rules out of this repository. Those belong in the relevant private work repository as a local overlay.
