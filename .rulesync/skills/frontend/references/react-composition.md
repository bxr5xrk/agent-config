# React composition

Use this reference for reusable components whose API is becoming hard to understand, produces invalid combinations or couples consumers to internal state. Skip it for a small local component with a clear API.

## Shape the API

- Distinguish independent capabilities from modes. A boolean is fine for an orthogonal state such as `disabled`; several booleans that select mutually exclusive layouts or behaviors should become an explicit variant or separate component.
- Prefer a small stable interface that hides styling and state machinery. Let callers compose content through `children` when the parent does not need to provide render-time data.
- Use compound components when several coordinated parts share state and consumers need flexible layout. Do not introduce context for a component whose direct props remain simpler.
- Keep state ownership explicit. Lift state only when siblings need coordination or the consumer must control it. Expose state, actions and metadata through a narrow interface when the implementation may vary.
- Preserve semantic HTML and accessibility through every variant. Composition cannot weaken labels, focus order, keyboard behavior or disabled/loading semantics.

## Review

Reject an abstraction when it adds more concepts than it removes, exists for a hypothetical second use, or makes the common case harder to read. Check representative combinations, long/empty/localized content, loading/error/disabled states and narrow viewports. Remove impossible combinations rather than documenting them.

For material React performance work, use the active first-party `vercel:react-best-practices` skill when available and verify with measurements. Check the installed React version before using version-specific APIs; do not translate React 19 guidance into a project on an earlier version.

Source: selectively adapted from [Vercel React Composition Patterns](https://github.com/vercel-labs/agent-skills/tree/063bee94c3f4df8453406c830b0a7df0f2860278/skills/composition-patterns). Its compound-component and React 19 recommendations are conditional here rather than defaults.
