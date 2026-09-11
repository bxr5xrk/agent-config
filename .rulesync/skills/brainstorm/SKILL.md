---
name: brainstorm
description: >-
  Develop and stress-test a new product or substantial feature idea into an
  agreed, researched brief before implementation.
targets:
  - codexcli
  - claudecode
codexcli:
  interface:
    display_name: Brainstorm
    short_description: Stress-test an idea into an agreed brief
    default_prompt: Use $brainstorm to clarify my product idea and prepare an agreed brief.
---
# Brainstorm

Turn rough intent into a concrete first journey and decisions that another agent can implement without repeating the interview.

1. Read the supplied material and existing project documents using the [context contract](references/context.md). Separate what the user decided, what the project demonstrates, and what remains unknown.
2. Use the available `grill-me`/`grilling` skill for dependency-ordered questioning; [discovery](references/discovery.md) makes this method self-contained. Ask one material decision at a time, with a recommended answer and reason. Discover facts yourself. Continue independent research while an answer is pending.
3. Research the unfamiliar constraints, strongest alternatives and likely failure modes using [research and challenge](references/research.md). Challenge contradictions with concrete consequences; do not turn a simulated persona into evidence of customer demand.
4. Show the first journey and, when helpful, one compact diagram or comparable visual alternatives. Keep product intent, architecture and art direction as distinct decisions. Honor the user's requested number of options.
5. Write or update the [brief template](assets/brief.md), link references, and record resolved, delegated, deferred and open decisions. Readiness depends on material uncertainty, not a question count. A declared assumption is not user approval.
6. Once intent is agreed or explicitly delegated, hand the brief to the available implementation workflow. If implementation was already requested and authorized, continue into it; otherwise finish with the concrete brief. Reopen only decisions invalidated by later evidence.

Do not scaffold a product while its purpose is still unknown. Exact changes to an established product usually belong directly with the relevant specialist.

Apply [feedback handling](references/feedback.md) when the user corrects your reasoning, demonstrates a better approach or asks to remember. If `$build` exists in the current agent, hand it the agreed brief; otherwise return the brief as the implementation contract.
