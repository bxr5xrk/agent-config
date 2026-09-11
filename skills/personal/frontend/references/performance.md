# Rendering, media and motion

Prioritize measured bottlenecks: unnecessary request waterfalls, excessive client JavaScript, expensive server work, image/font delivery and long main-thread work. Do not add memoization, virtualization or a new framework without evidence that its benefit fits the affected workload.

Keep public primary content visible before hydration. Reserve media dimensions and stable skeleton geometry; size responsive assets for their rendered use. Do not lazy-load the LCP image. Avoid loading an animation or third-party SDK globally for one optional interaction.

Use motion to explain state, hierarchy or an approved visual direction. A private admin usually needs restrained transition feedback, not a marketing animation system. CSS/WAAPI are sufficient for simple effects; use an existing animation library for genuine coordination needs. Keep reduced-motion output useful and visible. Clean up listeners, observers, timers and animation loops; pause irrelevant work. Auto-moving content may require pause/stop/hide controls under WCAG conditions.

## Verify

Measure a production build on representative routes and interactions under stated CPU/network conditions. Inspect a trace before choosing an optimization and compare the same scenario afterward. Check first load, a meaningful interaction, layout stability and any repeated animation on the relevant device class.

Current Core Web Vitals good thresholds are field p75 LCP ≤2.5s, INP ≤200ms and CLS ≤0.1. These are outcome targets, not guarantees from a local score. Lighthouse navigation does not measure field INP; TBT is a laboratory proxy. Emulation is not proof of physical-device behavior. Report unavailable field data rather than inventing it. Avoid universal bundle-size, FPS or animation-count rules without a project-specific budget.

Sources checked 2026-09-05: [Core Web Vitals](https://web.dev/articles/vitals), [LCP optimization](https://web.dev/articles/optimize-lcp), [WCAG motion criteria](https://www.w3.org/WAI/WCAG22/quickref/), [Vercel React performance rules](https://github.com/vercel-labs/agent-skills/blob/main/skills/react-best-practices/AGENTS.md). Vercel's impact ordering is a useful hypothesis; measured app behavior determines priority.
