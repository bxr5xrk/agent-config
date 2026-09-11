# Deliver substantial work in verifiable slices

Use when work spans several owners or sessions. A small exact change needs no ticket system. Start from the agreed brief and verified current state; keep the original outcome and exclusions intact.

Split by observable behavior that can be demonstrated through the necessary layers. For example, an input that reaches an API and returns a useful result is a slice; all database files followed by all UI files are implementation layers. Record each slice's acceptance IDs, affected contracts, owner, evidence and only genuine blocking dependencies in the existing task record. Independent slices can proceed together.

An expand → migrate → contract sequence is appropriate when a schema/interface transition must keep old and new consumers working. Label necessary preparatory work honestly instead of pretending every mechanical step provides standalone user value. Avoid speculative platform work.

Before dispatch, verify assumptions against the current code and provide concrete input/output contracts. Preserve useful current file paths and any compact state/schema snippet that captures an agreed decision. Task granularity and ordinary file ownership are implementation choices, not another user approval ceremony.

At a pause or transfer, keep one compact continuation record: current versus desired behavior, completed slices and evidence, unresolved decisions and real blockers, affected contracts, canonical artifact pointers and the next executable slice. Distinguish a temporary deferral from a durable rejection with a reason. Resume from those records without replaying the interview or forcing a new conversation.

Adapted from AI Hero [to-tickets](https://github.com/mattpocock/skills/blob/3cca18b368ae95cdbdebbff572ccafa662551015/skills/engineering/to-tickets/SKILL.md), [to-spec](https://github.com/mattpocock/skills/blob/3cca18b368ae95cdbdebbff572ccafa662551015/skills/engineering/to-spec/SKILL.md), [handoff](https://github.com/mattpocock/skills/blob/3cca18b368ae95cdbdebbff572ccafa662551015/skills/productivity/handoff/SKILL.md) and [triage](https://github.com/mattpocock/skills/blob/3cca18b368ae95cdbdebbff572ccafa662551015/skills/engineering/triage/SKILL.md). Records stay local; no tracker setup, issue publication or Git operation is implied.
