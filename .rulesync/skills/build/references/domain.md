# Domain language and consequential decisions

Read when terms are overloaded, business states/invariants change, or an architectural tradeoff is unresolved. Reuse the project's glossary, brief and decision records. Check concrete actors, examples and code before asking the user to define what the environment already reveals.

Use one name per meaning and separate meanings that happen to share a word. For example, a billing account and a login identity may have different ownership and lifecycle; verify that distinction for this project rather than assuming it. Record terms, relationships, transitions and important invariants alongside the canonical project context, using language developers and product users can recognize.

Capture a consequential choice when its reason would otherwise be surprising or expensive to reconstruct: context, considered alternatives, chosen outcome, consequences and actual decision provenance. Use an existing ADR convention where present; a short section in the brief/architecture document is enough otherwise. A separate glossary or ADR library is earned by recurring need, not required for a small project.

Keep rejected alternatives with their actual reason when future agents are likely to revisit them. Distinguish rejected, deferred and not yet understood. Mark superseded decisions and their replacement; preserve the reasoning without treating old decisions as immutable law.

Adapted from [AI Hero domain-modeling](https://github.com/mattpocock/skills/blob/3cca18b368ae95cdbdebbff572ccafa662551015/skills/engineering/domain-modeling/SKILL.md) and [grill-with-docs](https://github.com/mattpocock/skills/blob/3cca18b368ae95cdbdebbff572ccafa662551015/skills/engineering/grill-with-docs/SKILL.md).
