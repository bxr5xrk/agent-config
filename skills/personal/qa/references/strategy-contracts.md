# Risk strategy and contracts

Turn the request into an acceptance map: requirement, observable behavior,
responsible boundary, success evidence, negative/failure evidence, and unresolved
dependency. Add risk ranking for money, permissions, tenant data, irreversible
effects, core journey interruption, and hard-to-detect corruption.

Choose the narrowest layer that can disprove the claim:

- unit tests for isolated deterministic rules;
- contract tests for schemas and caller/provider assumptions;
- integration tests for real database/queue/cache/process boundaries;
- API tests for authorization, validation, state transitions, and errors;
- end-to-end tests for complete user/system journeys;
- deployed smoke tests for target configuration and service reachability.

Do not duplicate the same happy path at every layer. Add regression coverage near
the defect and one higher-level check when integration caused or concealed it.
For authorization and tenant behavior include a denied direct call, not only UI
visibility. For migrations include existing data, rerun/idempotency, partial
failure, and rollback/forward recovery as applicable.

Keep test setup representative. If fixtures bypass required lifecycle, identity,
indexes, or provider constraints, document the resulting gap. Match installed
versions and target environment where the claim depends on them.
