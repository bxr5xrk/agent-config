# Runtime and model policy

These skills use native Codex skills and subagent tools. A skill describes a method; the orchestrator creates the separate specialist context and loads the role's method. `agents/openai.yaml` is skill UI metadata, not a model configuration or a persistent agent memory store.

The user's policy is the strongest available model for every specialist and reviewer. On the inspected host, the task tool catalog exposes `gpt-6-astra` as the strongest option, and supports `max`/`ultra`. Use the strongest supported configuration suitable for the task; check the live catalog rather than permanently treating a model name as latest. Inheritance is appropriate only if the parent is already on that model/configuration. If the parent is Sol, explicitly select the strongest model for spawned specialists. Record an unavailable requested model and the replacement; never silently lower quality to save quota.

With collaboration tools, use fresh/minimal context for reviewers and a concrete SKILL.md or internal ROLE.md path in the prompt. If the runtime forbids model overrides on full-history forks, use a fresh or limited-history fork with the explicit supported model. Tool names and fields follow the active runtime schema, not copied pseudocode.

A direct `$designer`/`$frontend` invocation cannot change its own caller's model merely through YAML. If the caller is not verifiably on the strongest available model, it should dispatch one bounded execution worker with an explicit strongest-model selection, pass `already dispatched as this specialist` in that worker's task, and collect its result. A worker so marked must execute rather than spawning another copy of itself. If model selection or delegation is unavailable, state that limitation instead of claiming the model switched.

Codex also documents custom agents under `~/.codex/agents/*.toml` and project `.codex/agents/*.toml`. They are optional convenience profiles; these skills do not depend on them or silently alter global `config.toml`. Always-on global instructions should remain small. The specialists' stable methods and approved local knowledge provide continuity across short-lived agents.

ChatGPT Projects can keep a project's chats/files together. Project-only memory deliberately excludes outside memories, so it is not an automatic bridge to this local specialist store. Use the local project documents as the execution source of truth; if using ChatGPT for brainstorming, export the agreed brief/references explicitly. Do not assume local files are visible in a cloud chat.

Sources checked 2026-09-05: [Codex subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents), [skills](https://learn.chatgpt.com/docs/build-skills), [ChatGPT Projects](https://help.openai.com/en/articles/10169521-projects-in-chatgpt). Runtime observations take precedence over an older example model name in documentation.

Only `brainstorm`, `build`, `designer`, `frontend` and `backend` are public entrypoints in this workflow. Internal procedures use `ROLE.md`, have no discovery metadata, and are loaded or delegated by the owner. Their folders are implementation details, never commands to recommend to the user.
