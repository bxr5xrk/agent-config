---
name: sync-agent-config
description: >-
  Install or update this repository's common plus personal or work agent
  configuration in a requested desktop agent. Use when the user points to this
  file and asks to synchronize skills, instructions, hooks, subagents, or
  settings without a dedicated sync tool.
---
# Sync agent config

Apply the canonical configuration from this repository directly. The repository root is `../../..` from this skill's directory. Do not require a repository script, package dependency, daemon, or model-specific source folder.

## Select the source

Use `common` plus exactly one context scope:

- Personal context: `common` + `personal`.
- Work context: `common` + `work`.

Determine the context from the user's request or reliable project evidence. Do not infer it from the current model or desktop app. Ask one concise question only if the distinction is materially ambiguous.

Apply the selected scopes across the populated top-level artifact directories:

- `skills/`
- `instructions/`
- `hooks/`
- `subagents/`
- `settings/`

Empty directories require no destination changes.

## Apply to the current agent

1. Inspect applicable repository instructions, the selected source files, the target agent's installed version, and its current user-level configuration. Discover the target's native paths and supported formats from its current documentation or local installation; provider names belong only in this destination adapter step.
2. Build the exact source-to-destination mapping. Preserve one canonical source copy. For standalone skill directories, prefer individual symlinks to their canonical repository directories when the target supports symlink discovery. Never symlink or replace an entire user configuration directory.
3. Merge instructions, hooks, subagents, and settings into the target's native format. Preserve unrelated local entries, comments, permissions, credentials, project overlays, and provider-only configuration. Translate only fields whose semantics are understood and supported; report unsupported artifacts instead of approximating them silently.
4. Apply the requested synchronization immediately when the user's message asks to install, update, or synchronize. Refuse to overwrite a conflicting unmanaged path. Remove a stale destination only when it is a symlink into this repository or is otherwise provably an unchanged artifact previously copied from it.
5. Verify both filesystem state and actual discovery by the desktop agent. For skills, inspect the agent's skill or slash-command list. For instructions, hooks, subagents, and settings, use the target's parser, diagnostics, or a harmless observable check. Report what was applied, preserved, unsupported, or still requires an app reload.

Never copy secrets or employer-private project data into this repository. Work-specific project rules remain in their project repository unless the user explicitly promotes a reusable, non-secret rule into the `work` scope.
