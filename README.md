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
```

Every artifact has one canonical source. When applying the repository, use `common` plus exactly one context scope:

- Personal context: `common` + `personal`.
- Work context: `common` + `work`.

Current content:

- `common`: `brainstorm`, `grill-me`, `grilling`, `sync-agent-config`
- `personal`: `backend`, `build`, `designer`, `frontend`, `onboarding`
- `work`: empty until work-safe reusable content is added

## Apply in a desktop agent

There is no synchronization script or dependency. Give the target agent this instruction:

> Read `/Users/berserk/Work/agent-config/skills/common/sync-agent-config/SKILL.md` and follow it to apply the `personal` configuration from this repository to the current desktop agent.

Replace `personal` with `work` for a work environment. The skill makes the target-specific mapping at execution time, preserves unrelated local configuration, and verifies actual discovery by that desktop agent.

## Boundaries

Instructions, hooks, subagents, and settings remain canonical placeholders until real content is added. The instruction skill applies only populated artifact types supported by the target agent.

Keep secrets, credentials, employer-private data, and project-specific rules out of this repository. Those belong in the relevant private work repository as a local overlay.
