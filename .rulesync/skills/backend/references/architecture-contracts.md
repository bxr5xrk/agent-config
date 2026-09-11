# Domain boundaries and observable contracts

Organize around cohesive domain responsibilities and hide decisions behind narrow interfaces. Keep a modular monolith or the existing service boundary unless independent deployment, ownership, isolation or workload requirements justify a split. Avoid mandatory controller/service/repository layers for a trivial operation and avoid a shared generic base framework built for imagined reuse.

For overloaded terms, changed invariants or consequential tradeoffs, use the shared [domain context](../../build/references/domain.md). Compare small concrete interface/caller examples when a boundary is unresolved; select by the real contract and hidden complexity rather than the number of architectural layers.

At external boundaries define accepted fields, parsing/coercion, limits, stable errors and the response projection. In Fastify, use trusted JSON Schema for route validation/serialization. Its schema compiler evaluates generated code: never accept user-provided schemas. Keep database-dependent authorization/business checks out of initial asynchronous validation; perform them at the appropriate later hook/handler stage. Reuse schemas where practical; generate adapters only when duplicated contracts have become a real problem.

Whitelist updates and output fields. Do not pass request bodies as database filters/update operators or return whole internal records. Define pagination bounds and stable order, monetary representation/rounding, UTC instants versus local calendar dates, and absent/null semantics when those distinctions affect the domain. Validate environment configuration during boot without printing secrets.

For simplification, write down the contracts that could change: status/body/errors, authorization, ordering, side effects, transaction boundaries, idempotency and documented timing. Remove unnecessary indirection only after checking callers and failure paths. Fewer lines are not evidence of preserved behavior. Intentional behavior changes need their own acceptance criteria.

## Verify

Exercise the affected API/domain contract with valid input, relevant malformed input and a meaningful failure. Assert externally meaningful results rather than internal helper structure. For a refactor, compare old and new behavior at the existing public boundary; preserve established compatibility fixtures where available. Do not add a full test scaffold for a reversible documentation-only change.

Sources checked 2026-09-05: [Fastify validation/serialization](https://fastify.dev/docs/latest/Reference/Validation-and-Serialization/), [Ousterhout modular design lecture](https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign), [Fowler refactoring definition](https://martinfowler.com/bliki/DefinitionOfRefactoring.html), [Monolith First](https://martinfowler.com/bliki/MonolithFirst.html). Architecture principles guide judgment; the monolith argument is explicitly experience-based, not a universal measured result.
