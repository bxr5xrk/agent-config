# Environments and deployments

Identify the exact target, revision/artifact, configuration source, dependency
versions, and release mechanism. Compare environment shape without exposing
values: required keys, ownership, scope, rotation path, and whether each component
receives them. Treat missing, empty, stale, and wrong-environment values separately.

Before a consequential deploy establish:

- acceptance and pre-deploy health baseline;
- compatibility order for application, workers, schema, queues, and clients;
- migration runtime, locks, backfill/load, rerun behavior, and recovery;
- feature flag, drain, pause, canary, or other blast-radius control;
- rollback versus roll-forward trigger and responsible owner;
- post-deploy smoke plus observation window.

Schema changes should be backward/forward compatible across mixed versions when
rolling deployment can overlap. Destructive cleanup follows verified migration and
usage removal, not the same release by default. Back up only when the backup and
restore path are actually valid for the risk.

Safe smoke tests use dedicated test identities/data, minimal reversible effects,
and explicit cleanup. Never send real outreach, payments, destructive provider
commands, or broad notifications as a generic health check.

A platform reporting “deployed” proves artifact acceptance. Confirm startup,
dependency connectivity, route/worker readiness, representative transaction, and
the logs/metrics that reveal silent failure.
