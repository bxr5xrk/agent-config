# Review changed trust boundaries

| Boundary | Trace and validate |
|---|---|
| Identity → action | Server-side authorization for the actual object/action; missing, expired and lower-privilege identity |
| Tenant → data | Tenant/owner constraints in queries, caches, exports, object storage and asynchronous jobs |
| Browser → server | Validation and output encoding; cookie/session and CSRF behavior appropriate to the stack; client checks are not authorization |
| External data → parser/render/command | Bounded input, context-appropriate escaping, parameterized queries/commands, safe file/URL handling |
| Provider callback → state | Signature verification, event identity, replay handling, out-of-order events and idempotent state transitions |
| Request → remote fetch | Allowed destination/redirect policy and network exposure when user-controlled URLs exist |
| Internal state → logs/analytics | Redaction, intentional fields, least necessary identifiers and no credentials/private message bodies |
| Dependency/deploy → runtime | Reachable vulnerable use, privilege/secret exposure and effective production configuration |

Choose cases from the real change; do not create a speculative checklist finding for every row. Include a positive-path test alongside a denied access case to avoid fixing a vulnerability by breaking the product.

Use versioned [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/) requirements when traceability helps (stable release observed: 5.0.0, checked 2026-09-05). Consult the relevant [OWASP Cheat Sheet](https://cheatsheetseries.owasp.org/) for the actual boundary. A selected subset is not an ASVS level claim.
