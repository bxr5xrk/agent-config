# Trust boundaries and authorization

Use the existing trusted identity provider and server-side session/token verification. Authenticate the caller, then authorize the requested action on the actual resource; UI visibility or a valid login is insufficient. Define an explicit permission boundary and default-deny for protected operations. Revalidate authority on every applicable entrypoint, including jobs and server actions.

For multitenant systems, derive tenant context from verified identity plus membership. Treat caller-supplied tenant IDs as selectors requiring authorization. Scope queries, caches, object storage paths, search and queued work wherever their data varies by tenant. A tenant ID inside a queue message is not proof that its producer or consumer is authorized. Model intentionally global resources explicitly rather than attaching fictitious tenant scope everywhere.

Test ownership and role restrictions as well as tenant separation. Consider membership revocation, account switching and long-lived cached permissions when those paths exist. For shared expensive work, apply proportional request/concurrency limits so one caller or tenant cannot exhaust the service; do not introduce a distributed limiter without a deployment need.

Cookie-authenticated mutations need the framework/provider's appropriate CSRF protections. SameSite and CORS are not replacements for authorization; assess their role in the actual browser/session design. Preserve credential/secret boundaries, redact logs and use narrow response projections. Do not invent authentication or cryptographic mechanisms.

## Verify

For a changed protected operation, call it directly as unauthenticated, authorized and forbidden users. For actual multitenancy, attempt a cross-tenant read/write and cache reuse, plus any affected export, file or job path. Verify failure cannot leak protected data or leave an unauthorized side effect. Add a focused authorization regression case at the enforcing boundary, not merely a test that a button is hidden.

Sources checked 2026-09-05: OWASP [authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html), [multitenant security](https://cheatsheetseries.owasp.org/cheatsheets/Multi_Tenant_Security_Cheat_Sheet.html), [authorization regression testing](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Regression_Testing_Cheat_Sheet.html), [CSRF](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html). Apply the branches the product actually has; this is not a full security audit.
