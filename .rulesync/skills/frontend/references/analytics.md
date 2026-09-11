# Product measurement

Use PostHog where the product needs measurement. Reuse its current project, region and integration; for a new project select the region from approved product/data-location requirements. Do not create an account, switch providers or add tracking to an unrelated edit.

Define the decision being measured, event trigger, allowed properties, identity and consent behavior before implementation. Prefer a small explicit event plan. Autocapture and session replay remain off unless the project explicitly needs them. Assign one SDK initialization owner and one pageview owner; framework integration plus manual tracking can double-count.

Identify signed-in users with a stable opaque application identifier when needed; reset identity at logout/account changes. Anonymous visitors retain SDK-generated distinct IDs, not one shared `anonymous` value. Client/server attribution may share an analytics ID; that ID or a tracing header is never evidence of authorization. Record business success from its authoritative server outcome, with an event ID/deduplication policy where retries can repeat delivery.

Allowlist event properties. Exclude credentials, tokens, form free text, personal contact data and private URL/query contents. Check SDK-added properties and server logs as well as explicit payloads.

Apply the approved consent policy. If it requires zero analytics network requests before consent and after withdrawal, the provider's opted-out SDK recipe is not proof of zero traffic. Gate initialization/network-producing functionality as needed; do not enable cookieless tracking to bypass that requirement. Distinguish product policy from a legal compliance determination.

## Verify

Test initial visit, ignored/rejected/accepted/withdrawn consent, route changes, sign-in, logout and a repeated business action. Inspect network payloads, duplication and identity. Confirm an intended test event reaches the correct PostHog project before claiming live ingestion; mocks or a successful SDK call are insufficient. Remove test data only if authorized and supported.

Version check: official docs currently label `@posthog/next` pre-release. Prefer the existing stable integration; verify SDK/framework compatibility and supported `defaults` values rather than inventing a date. Validate CSP against the features actually enabled.

Sources checked 2026-09-05: PostHog [Next.js integration](https://posthog.com/docs/libraries/next-js), [data-collection controls](https://posthog.com/docs/privacy/data-collection). PostHog is the user's current default; consent and data-location requirements come from approved project policy.
