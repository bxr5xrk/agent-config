---
name: build
description: >-
  Implement an agreed brainstorm brief or a substantial project change by
  coordinating design, frontend and backend specialists, integration and
  independent checks.
targets:
  - codexcli
codexcli:
  interface:
    display_name: Build
    short_description: Turn an agreed brief into a verified project
    default_prompt: >-
      Use $build to implement the agreed brief and coordinate specialists,
      reviews, and corrections.
---
# Build

Start implementation from the agreed brainstorm result or a scoped request for an existing project. Own delegation, integration, internal reviews and fixes using the available Codex subagent tools. The user invokes only this skill, not the internal reviewer or learning roles.

1. Resolve the [project context](references/context.md), requested change and actual authorization. For a new idea with consequential unknowns use `brainstorm`; for a bug use [diagnosis](references/diagnosis.md). For an established project ask only the missing decision. Do not restart onboarding for a section or bug fix.
2. Map requirements to observable acceptance and choose the relevant [specialists](references/dispatch.md). When a material part depends on narrow or version-sensitive technology not covered by project instructions, apply [expertise routing](references/expertise-routing.md). Use the strongest currently available model for every role; verify the runtime's supported model/effort values. Do not silently select a cheaper reviewer.
3. Create a compact task record from [the template](assets/task.md). For substantial work use [verifiable slices](references/delivery.md); assign file ownership and dependencies before parallel work. Pass each agent the scoped brief, canonical documents, approved applicable lessons, input artifacts and expected evidence. Delegate independent work and wait for required outputs.
4. Integrate the implementation, then run independent `verify-product` and `simplify` reviews for material UI/behavior changes. Add `security-review` when trust boundaries change. Follow [review and repair](references/review-loop.md); inspect artifacts and rerun affected checks after fixes.
5. Reconcile project documentation with verified behavior. Capture corrections through `learn`: local decision now, generalized candidate later, global activation only after batch approval. Return the result and material verification limits concisely.

Use [project setup and continuity](references/onboarding.md) for a new directory or existing onboarding records. Use [runtime and model policy](references/runtime.md) for dispatch details. Never infer completion from subagent summaries or a green build alone.

Apply [automatic feedback learning](references/feedback.md) on every relevant correction or “remember” request, including later messages. Capture and curate internally; require the agreed batch approval before publishing global lessons.
