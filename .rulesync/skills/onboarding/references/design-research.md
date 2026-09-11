# Design tools and sources compared

Reviewed 2026-09-04. These are source-backed capabilities and our fit judgments, not a measured ranking or proof of design quality. None of these third-party packages is silently installed by this skill.

| Approach | Useful contribution | Limitation / how to use |
|---|---|---|
| Installed Product Design ideate + image-to-code | Visual alternatives and implementation from a selected reference | User's 5–10 count and selection gate override a narrower default; availability checked at runtime |
| [Anthropic frontend-design](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md) | Deliberate visual direction, composition and subject-specific typography | Primarily creative guidance; does not establish behavior/accessibility correctness |
| [Impeccable](https://github.com/pbakaus/impeccable), [workflow](https://impeccable.style/designing/) | Separate product context/design context; focused refinement vocabulary and anti-pattern awareness | Opinionated defaults can conflict with other design skills; use one design lead and validate results |
| [UI UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | Searchable design references and reusable assets/scripts in a multi-file package | A recommendation catalog cannot select the user's taste or verify an implemented flow |
| [Vercel Web Interface Guidelines](https://vercel.com/design/guidelines) | Concrete interaction and implementation review checklist | Quality floor, not a distinctive identity generator |
| [shadcn/ui](https://ui.shadcn.com/docs) + [Radix](https://www.radix-ui.com/primitives/docs/overview/accessibility) | Owned component code and accessible interaction primitives | Default component styling is not a brand; composition still needs keyboard/label/state checks |

Recommendation: this onboarding workflow owns scope/state/choice; use one available creative specialist for alternatives, then tokens + shadcn primitives, then an independent behavior/accessibility check. Do not concatenate every downloaded skill into a giant prompt. Multi-file structure is useful for selective reading and deterministic helpers, not for file count.

Discovery registry: [skills.sh frontend-design](https://www.skills.sh/anthropics/skills/frontend-design). Registry popularity is not quality evidence.

X research limitation: [an Ivan Leo post linked by Impeccable](https://x.com/ivanleomk/status/2041371674248147047) was reached, but its text did not load in the research tool. Impeccable's own testimonials are vendor-selected; no independent Twitter consensus is claimed.

## Reference pools for future options

- [Curated](https://curated.design/): varied live marketing sites.
- [Lapa Ninja](https://www.lapa.ninja/): landing-page composition and category references.
- [Awwwards](https://www.awwwards.com/): distinctive art direction; recheck usability and performance before borrowing.
- [Mobbin](https://mobbin.com/): product flows and UI states; respect account/paywall limits.
- [shadcn components](https://ui.shadcn.com/docs/components): interaction inventory, not final visual alternatives.

Use reference pools to find the actual five to ten relevant examples for each new product. Their homepages alone are not a completed comparison board.
