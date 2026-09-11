# Operations and handoff

Pin a compatible supported runtime and package versions, commit the lockfile, supply `.env.example` with names/placeholders only, and document clean-install/dev/build/test commands. Never copy another project's secrets. Frontend public variables are public. Keep server environment parsing out of client bundles.

Provide useful liveness/readiness and structured errors. Add Sentry if production error monitoring is in scope, with safe metadata and environment/release tags; don't send personal payloads. Record how to see failures. Choose deployment topology from the actual runtime, data region and hosting access, not a template logo.

CI for the chosen modules: frozen install, lint, typecheck, meaningful tests, build. Add browser journeys when UI behavior is critical. Test configuration under production build, not only development HMR. A repository/PR/deploy is created only when in the user's authorized scope; no automatic purchase or production migration.

For persistent data, define backup/restore responsibility and test recovery when launching real stateful service. For integrations document limits and failure recovery. Health endpoints should avoid environment or credential detail.

Handoff distinguishes: technical scaffold, first implemented user journey, sample/demo data, unconnected services, passed checks, tests not run, and exact remaining input. Remove obsolete scaffolding made unnecessary by this work; preserve user-owned code. Update state with a concrete next action. Never mark onboarding complete while design choice or a required integration is still pending.
