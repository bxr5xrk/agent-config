# Brand foundation before interface design

For a new public `product_brand`, complete this stage after the product brief and before UI exploration. Skip this reference for `lightweight_site` unless the user explicitly asks for brand work. The aim is not a long agency exercise; it is enough brand clarity to avoid building a generic site around a disposable name.

## Required sequence

1. **Context.** Reuse BRIEF.md and recorded discovery. Capture audience, category, desired perception, personality, values, constraints and anti-references in BRAND.md. Do not ask again for known facts. If `brand-context` creates `.agents/brand-context.md`, treat it as the specialist's working context and keep BRAND.md as the canonical onboarding deliverable.
2. **Competitor evidence.** Inspect current competitor homepages and representative product screens where accessible. Record positioning, promises, vocabulary, visual patterns, interaction patterns and repeated category clichés. Community posts and galleries are discovery aids, not proof of effectiveness.
3. **Positioning.** Choose a credible territory with proof points and explicit refusals. State the category, audience, differentiated promise, reasons to believe and one-sentence positioning. Distinctiveness must still serve the user's actual job.
4. **Naming.** Generate names from 3–5 strategic territories, not one undifferentiated list. Evaluate clarity, memorability, pronunciation, spelling, extensibility, unwanted meanings and fit with positioning. Before final approval, verify current search results, relevant domain options and obvious trademark conflicts in target markets. These checks are screening, not legal clearance.
5. **Verbal identity.** Record value proposition, tagline candidates, core messages, voice traits, vocabulary and examples of what the brand would and would not say.
6. **Visual identity brief.** Define logo directions, type character, palette roles, imagery, iconography, motion and application principles. This is a brief for the visual exploration, not permission to select the final UI unseen.
7. **Brand book.** Consolidate approved decisions and usage rules in BRAND.md. Keep rejected names and territories with short reasons so later agents do not repeat them.

## Required evidence and gates

- Use dated URLs for competitor and trend evidence; distinguish direct observation from inference.
- Show the naming shortlist and checks before asking for the name decision.
- For logo work, show materially different directions at relevant sizes; inspect monochrome and favicon-size legibility. Do not claim trademark clearance.
- `brand.status` must be `approved`, `existing_brand`, `not_applicable` or `user_override` before generating a new frontend scaffold. Use `not_applicable` only for backend-only or genuinely internal tools and record the reason; record the exact reason for an override.
- Brand simplification means one clear promise, progressive disclosure and fewer competing actions. It does not mean removing necessary controls, hiding system state or copying the generic AI landing-page aesthetic.

## Specialist use

When available, route selectively through `brand-context`, `competitor-branding`, `brand-positioning`, `brand-naming`, `brand-identity` and `brand-guidelines`. This onboarding skill owns question order, evidence requirements, persistence and approval gates; specialist instructions do not override them. Use only the specialist needed for the current stage, and read its current SKILL.md before use.
