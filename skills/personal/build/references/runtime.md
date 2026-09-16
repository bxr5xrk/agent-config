# Runtime and model policy

These skills use native Codex skills and subagent tools. A skill describes a method; the orchestrator creates the separate specialist context and loads the role's method. `agents/openai.yaml` is skill UI metadata, not a model configuration or a persistent agent memory store.

Every spawned specialist and reviewer inherits the resolved model and reasoning effort from its parent. Keep `model` and `model_reasoning_effort` absent from child-agent profiles and do not pass spawn overrides unless the user explicitly requests a different model or effort. New root or standalone runs, including scheduled tasks, use `gpt-5.6-sol` with `high` reasoning unless the user explicitly chooses otherwise.

With collaboration tools, use fresh/minimal context for reviewers and a concrete SKILL.md or internal ROLE.md path in the prompt. Do not change fork history merely to select a different model. Tool names and fields follow the active runtime schema, not copied pseudocode.

A direct `$designer`/`$frontend` invocation runs on its caller's resolved model and effort. Delegate only when task complexity, specialization, context isolation, or independent review requires another agent; never spawn a worker solely to switch models.

Codex also documents custom agents under `~/.codex/agents/*.toml` and project `.codex/agents/*.toml`. They are optional convenience profiles; these skills do not depend on them or silently alter global `config.toml`. Always-on global instructions should remain small. The specialists' stable methods and approved local knowledge provide continuity across short-lived agents.

ChatGPT Projects can keep a project's chats/files together. Project-only memory deliberately excludes outside memories, so it is not an automatic bridge to this local specialist store. Use the local project documents as the execution source of truth; if using ChatGPT for brainstorming, export the agreed brief/references explicitly. Do not assume local files are visible in a cloud chat.

Sources checked 2026-09-16: [Codex subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents), [skills](https://learn.chatgpt.com/docs/build-skills), [scheduled tasks](https://learn.chatgpt.com/docs/automations), [ChatGPT Projects](https://help.openai.com/en/articles/10169521-projects-in-chatgpt).

Only `brainstorm`, `build`, `designer`, `frontend` and `backend` are public entrypoints in this workflow. Internal procedures use `ROLE.md`, have no discovery metadata, and are loaded or delegated by the owner. Their folders are implementation details, never commands to recommend to the user.
