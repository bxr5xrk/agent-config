# Agent config

One private, model-neutral source for reusable agent configuration.

## Content

```text
skills/
  common/       brainstorm, grill-me, grilling
  personal/     backend, build, designer, frontend, onboarding
```

Only folders containing real configuration belong in this repository. Add `work`, `instructions`, `hooks`, `subagents`, or `settings` only when there is actual content for them.

## Apply in an agent

There is no synchronization tool or generated configuration. Tell the agent:

> Read `/Users/berserk/Work/agent-config/README.md`. Synchronize all populated `common` and `personal` configuration from this repository with the current desktop agent. Discover its native configuration paths, preserve unrelated local configuration, and verify that the agent actually discovers the result.

For a work environment, replace `personal` with `work`. Prefer links to the canonical folders when the target supports them; never overwrite an entire user configuration directory.

Keep secrets, credentials, employer-private data, and project-specific rules out of this repository. Those belong in the relevant private work repository as a local overlay.
