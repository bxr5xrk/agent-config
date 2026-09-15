# Threat model and authorization

Define the protected asset and security property before listing threats. Useful
properties include confidentiality, integrity, availability, tenant isolation,
identity authenticity, non-repudiation, bounded automation, and recoverability.

Trace each sensitive operation through:

1. caller-controlled input and reachable entrypoint;
2. authentication and session/token validation;
3. tenant resolution and role/capability decision;
4. resource lookup and ownership/relationship check;
5. state mutation or external effect;
6. audit record, response, and failure behavior.

Check direct-object access, guessed identifiers, mass assignment, alternate
routes, background jobs, exports, admin/client parity, stale membership, and
cross-tenant caches. Query by both resource and authorized tenant/owner where
possible; a later equality check must fail closed. UI visibility and possession
of an opaque ID do not grant access.

Model actors realistically: unauthenticated user, normal tenant user, privileged
tenant user, compromised session, malicious integration, internal operator,
background worker, and third-party provider. Do not assume every internal network
hop or queue message is trusted.

For each plausible path capture preconditions, source-to-sink flow, existing
mitigations, reproducibility, impact, and uncertainty. Severity follows the
demonstrated path and reachable blast radius, not the category name alone.
