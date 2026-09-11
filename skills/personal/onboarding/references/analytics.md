# “Connect analytics” means PostHog

Reuse the current project's PostHog project/host. For a new setup prefer EU region; create no account or paid resource without authorization. Missing credentials block live ingestion, not event design, code integration or local tests. Never claim integration verified until an event is observed in the intended project.

Create `docs/analytics.md`: business outcome, event name, trigger, properties, identity, consent policy, owner. Start with page views, primary action started/completed/failed, and one activation event tied to the product's first value. Public marketing and logged-in usage need distinct questions; don't collect events with no decision attached.

Implement one client initialization path with actual current PostHog Next instructions; select either automatic or explicit SPA pageviews and test that navigation does not double count. Use a typed event wrapper. Identify by an internal opaque user ID only when appropriate; reset identity on logout. Successful business events may be server-owned with a deduplication key where needed. Do not infer payment success from a button click.

Default product policy: explicit minimal events, autocapture off, session replay off; decide consent behavior before activating collection. For a consent-gated implementation, no analytics network calls before consent, and revoke/opt-out stops future capture. These are conservative product defaults, not a blanket legal compliance claim. Do not attach email, tokens, free-text form contents, full URLs with sensitive queries, or private documents. Maintain an allowlist for properties.

[PostHog Next.js integration](https://posthog.com/docs/libraries/next-js) is the source for current SDK setup. Do not hardcode the research date as an SDK defaults version. Read the current instructions before copying initialization code.

Verification: allowed vs denied consent, first load, client navigation, refresh/back, login/logout, deduplication and intended region; observe actual events without exposing credentials. If ingestion is unavailable, report “implemented; live ingestion unverified” and preserve the precise missing input in HANDOFF.md.

See [event contract template](../assets/documents/ANALYTICS.md).
