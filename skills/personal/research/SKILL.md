---
name: research
description: >-
  Investigate repositories, products, markets, competitors, and technical
  mechanisms with source-backed claims. Use when an answer depends on locating
  what actually happens, current external evidence, or a defensible comparison.
---
# Research

Answer the user's actual question at the requested granularity. Work directly
when invoked; a build orchestrator is optional.

Read the [shared project context](../build/references/context.md), applicable
project instructions, and the smallest set of artifacts that can establish the
answer. Do not substitute a product category, README summary, search snippet, or
plausible architecture for the implemented or documented mechanism. When the
question is **what, where, or how**, trace the implementation or data path far
enough to name the real source, transformation, and destination. Preserve a
request for one sentence or a short answer after doing the deeper inspection.

Separate direct observation, sourced fact, calculation, and inference. Keep a
lightweight claim ledger for substantive work so every important conclusion has
evidence, date/freshness where relevant, and a confidence or limitation. Prefer
primary sources and current implementation. A missing result within searched
sources is “not found in this scope”, not proof that it does not exist.

Read only the references relevant to the request:

- Claims, provenance, freshness, citations, conflicting sources, or a research
  report: [evidence and claims](references/evidence-and-claims.md).
- Repository or system questions, mechanism tracing, architecture, or incident
  investigation: [repository investigation](references/repository-investigation.md).
- Market, competitor, pricing, category, recommendation, or opportunity work:
  [market and competitors](references/market-and-competitors.md).
- Choosing between a one-sentence answer, decision memo, comparison, or research
  dossier: [deliverables](references/deliverables.md).

Research is read-only unless the user also asks for implementation or an
external action. Do not sign up, contact people, purchase access, bypass access
controls, or expand authorization merely to obtain evidence. If decisive
evidence is inaccessible, state the bounded gap and answer everything else.

For project work, update only the canonical research/decision document when the
request authorizes it. Finish through the [closeout contract](../build/references/closeout.md):
standalone research owns its evidence audit; delegated research returns claims,
sources, unresolved gaps, and reusable corrections to the orchestration owner.
Apply [automatic feedback learning](../build/references/feedback.md) to material
corrections, especially when a generic summary missed an exact mechanism.
