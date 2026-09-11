# Resolve the decision tree

Start with the highest-consequence unknown. The following are branches to explore when relevant, not a questionnaire to recite.

| Dependency | What must become concrete | Useful challenge |
|---|---|---|
| Audience and job | Who acts, what problem occurs today, what first value changes | Why would they switch from the existing workaround? |
| First journey | Trigger, real input, steps, output and return visit | What if there is no data, an invalid input or a failed dependency? |
| Scope | Useful first release, exclusions, delivery acceptance and later business metric | Which part could be removed while retaining the promised result? |
| Domain | Entities, ownership, states, invariants, money/time semantics | Can two actors update the same thing concurrently? |
| Access and data | Actors, private/public boundaries, sensitive fields, retention | Can one customer read another customer's object? |
| Integration | Existing provider, authorization owner, limits, retry/callback behavior | What happens after a timeout when the remote operation may have succeeded? |
| Surfaces | Landing, product, admin, content site, API, native app, mixed | Is this surface for discovery, repeated work or both? |
| Design and content | Existing brand, approved references, information density, real content, devices | Is the reference attractive because of its photography, layout, product, or motion? |
| Operations | Hosting, runtime, expected load, recovery and launch constraints | What counts as usable when a dependency is unavailable? |

Use a concise UI question when available. One question may compare two or three options plus free text. Wait for the answer to a required decision; elapsed time is not consent. A user can delegate ordinary decisions and the entire direction; record the actual extent of delegation and proceed.

After each answer, update the brief rather than keeping the decision only in chat. If a reference/codebase answers a question, do not ask it. If decisions conflict, state the concrete contradiction and ask only the decision that resolves it. Agreement with a brief does not silently approve a different visual direction, spending, publication, or sending messages.

Before handoff, another agent should be able to describe the first useful outcome, exclusions and acceptance conditions without inventing product intent. A partial brief can still have research or prototypes in progress; mark these honestly.

Use the shared [domain procedure](../../build/references/domain.md) when language or business invariants need sharpening. Capture actual decisions as they land; synthesizing the final brief does not require repeating the interview. Include a compact state/schema example when it expresses an agreed decision more precisely than prose.

For a large uncertain effort, expand the existing decision table with real prerequisites and the next action: research, prototype or a user decision. Resolve currently actionable unknowns first while independent exploration proceeds. Distinguish blocked, still vague, deferred and out of scope. Keep this map local and proportional; a small feature needs no planning framework or ticket system.

When needed facts belong to another person and cannot be discovered, draft a short questionnaire tied to the affected decisions and that person's context. Preserve the draft locally; sending it requires explicit authorization.

These branches adapt AI Hero [wayfinder](https://github.com/mattpocock/skills/blob/3cca18b368ae95cdbdebbff572ccafa662551015/skills/engineering/wayfinder/SKILL.md), [to-spec](https://github.com/mattpocock/skills/blob/3cca18b368ae95cdbdebbff572ccafa662551015/skills/engineering/to-spec/SKILL.md) and [to-questionnaire](https://github.com/mattpocock/skills/blob/3cca18b368ae95cdbdebbff572ccafa662551015/skills/productivity/to-questionnaire/SKILL.md). Preserve the local one-question grilling cadence and existing authorization.
