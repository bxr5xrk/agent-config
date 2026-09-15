# Release evidence and reporting

Report by claim, not by command inventory:

- **Verified:** behavior and boundary actually exercised, with environment/version.
- **Failed:** observed mismatch, reproduction, impact, and evidence.
- **Not verified:** exact dependency or permission missing; never translate this
  into “does not work” or “not available”.
- **Residual risk:** important path outside the test scope and why it matters.

Release readiness requires the core journey, consequential negative paths,
configuration/runtime dependencies, data/queue effects, and rollback or disable
path proportionate to risk. A build, lint, types, or unit suite can be necessary
but is never the whole release claim.

On failure, preserve minimal reproduction inputs, timestamps/correlation IDs,
expected versus actual behavior, screenshots/log excerpts, and whether the state
is recoverable. Separate product defects, test defects, environmental failures,
and unavailable external systems before assigning ownership.

Re-run the affected story after a fix and inspect final bytes/configuration, not
only the original test. For visual fixes repeat the actual viewport. For async
fixes observe terminal data and side effects, not only job acceptance.

Keep the final verdict proportional: pass the verified scope, fail the violated
acceptance, and block release only when unresolved risk warrants it. Do not bury
a core failure under a large number of passing low-risk checks.
