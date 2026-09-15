# Repository and mechanism investigation

Start from the user-visible claim and follow the executing path rather than
inventorying the repository. Inspect applicable project instructions and dirty
state first. Preserve user changes and treat documentation as a map to verify.

For “what does this do?” identify the initiating actor, input, core transformation,
persistent or external effects, and visible output. For “where does it get X?”
trace the source precisely: configuration or curated seeds, API/query, provider,
filter/expansion, storage, and downstream consumption. Name the actual mechanism
in the answer. A label such as “discovery platform”, “AI search”, or “database” is
not enough when the implementation says recommended-profile graph, following
lists, a specific query, cache, queue, or provider endpoint.

Use this trace order selectively:

1. User-facing entrypoint, route, job producer, CLI, or scheduled trigger.
2. Handler/service and direct callers.
3. Provider, query, algorithm, configuration, or external endpoint.
4. Filters, retries, deduplication, authorization, and error paths.
5. Storage/event/queue side effects and the consumer that makes them observable.
6. Tests and runtime evidence that confirm or contradict the inferred path.

Distinguish active code from archived files, unused helpers, legacy aliases,
mocks, comments, and planned documentation. Search for call sites and package
boundaries before declaring a helper part of the real path. When behavior depends
on environment or provider capability, state that condition.

Read-only analysis does not authorize fixes. If asked for a diagnosis, identify
the most supported cause and the evidence needed to close remaining uncertainty;
implement only when the request includes repair.
