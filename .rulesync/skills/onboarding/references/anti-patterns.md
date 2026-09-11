# Failure → replacement → evidence

| Avoid | Use instead | Observable check |
|---|---|---|
| Silent 5-second navigation | Pending cue + persistent shell + streaming/loading boundary | Cold route with 3-second delayed dependency |
| Await in parent before its Suspense | Await inside bounded subtree | Shell appears before response |
| Root layout waits for unrelated data | Minimal shell; independently gated content | Slow one query doesn't freeze navigation |
| Spinner forever / generic “error” | Timeout, contextual error, retry preserving input | Disconnect provider and recover |
| Request/startup createIndex/syncIndexes | Explicit versioned migration job | Runtime dependency path never provisions indexes |
| Delete applied migration code | Immutable migration history | New isolated environment reproducible |
| Full DB document serialized | Explicit response contract/projection | Sensitive fields absent from response |
| Type assertion on external JSON | Runtime schema validation | Malformed provider payload rejected |
| Unbounded lists/queries | Pagination and limits | Oversize limit cannot exhaust service |
| Retry every POST | Idempotency/dedupe + selective retry | Duplicate request creates one effect |
| Client-only authorization | Data-owner authorization | Wrong-tenant test fails safely |
| Clickable div / no focus | Semantic controls + visible focus | Keyboard-only journey completes |
| Pointer/hover considered all a11y | Names, roles, contrast, focus, states | axe + manual checks |
| Six recolors called six options | Different composition/hierarchy/type/navigation | Side-by-side comparison explains differences |
| shadcn default called a brand | Chosen semantic tokens and visual identity | Screens match selected reference |
| Optimistic destructive success | Confirm server result; reversible optimism only | Failure rolls back honest state |
| Blanket `use client` / global fetch waterfalls | Small client islands / parallel independent reads | Inspect bundle and request timeline |
| PostHog in two initialization paths | Single owner, pageview policy | One event per intended trigger |
| Full URLs/free text in analytics | Allowlisted properties | Payload inspection contains no private values |
| HTTP health = whole product done | Actual happy/failure user journey | Browser/API integration evidence |
