# Reference evidence

Treat a reference as evidence for a direction, not as a complete specification. Record in project `design.md` what should transfer, what should remain project-specific and which claims are observations, measurements or inferences.

## Screenshot or static mockup

A screenshot shows one rendered state at one unknown capture scale. Exact pixel colors and contrast between sampled pixels are measurable. Relative proportions, repeated rhythms, hierarchy, type category and layer order can be inferred. Exact CSS dimensions, font identity, tokens, framework, breakpoints, motion, interaction behavior and uncaptured states cannot be recovered reliably.

Reconstruct the transferable system rather than claiming to have read the original implementation. Express size and spacing as ratios unless the capture scale is known. Name missing evidence that matters to the requested result, then make the smallest reasonable design decision without stopping for information that would not change it.

## Live page

Inspect both authored sources and the rendered result when access permits. Computed styles show what won at the visited viewport and state; source CSS reveals tokens and responsive rules that may not currently apply. Check pseudo-elements and overlapping layers for visual effects. Observe relevant responsive, hover, focus, active, loading and motion states instead of extrapolating from one frame.

Separate three claim types:

- **Observed:** visible behavior or a value read from the live result.
- **Derived:** a relationship calculated from observed evidence.
- **Inferred:** likely design intent or implementation, stated as uncertain.

Copy the mechanism only when it serves this product. Do not copy brand assets, licensed fonts, distinctive artwork, exact copy or a third-party site's identity into the project.
