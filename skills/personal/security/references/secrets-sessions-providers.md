# Secrets, sessions, and providers

Inventory credential classes without printing values: application secrets,
database/queue credentials, API keys, OAuth tokens, session cookies, signing
keys, provider passwords, proxy credentials, webhook secrets, and recovery codes.
Record owner, scope, storage, rotation/revocation path, and where the value can
appear in memory, logs, jobs, exports, or browser state.

Keep server-only secrets out of client bundles and public configuration. Use
least-privilege credentials per environment and purpose. Never copy production
credentials into tests, examples, screenshots, issue text, or agent memory. Mask
structured logs and error objects, not only obvious string fields.

Sessions must bind to the intended identity/context, expire, revoke, and fail
closed. Check fixation, replay, token confusion, stale role/tenant claims, cookie
attributes, CSRF where ambient credentials are used, and logout/revocation across
workers and realtime connections.

Treat proxies and external accounts as credentials plus operational identities.
Separate pools whose purposes, permissions, reputation, or risk differ. Do not
silently reuse parsing/discovery identities for outbound actions, test accounts
for production, or one tenant's provider session for another.

Private/undocumented APIs add contractual, availability, account-ban, and supply-
chain risk. Security review should distinguish exploitability from platform-policy
risk while treating both as release constraints when they affect customer data,
credential safety, or system continuity.
