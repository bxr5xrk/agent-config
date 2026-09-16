# One project context, reusable expertise

Read applicable project instructions first, then the smallest set of canonical documents needed for this task. Locate root `design.md` case-insensitively, the brief, architecture/analytics documents and existing onboarding state. Inspect package manifests, component tokens and changed code to verify documents against reality.

For a genuinely new project, read [adopted defaults](defaults.md) before proposing the stack. Keep the original request and its language in the handoff; scoped worker instructions may select relevant parts but must retain the requested outcome, exclusions and authorization. A diagnosis-only request stays read-only; an implementation request authorizes its scoped edits and verification. Continue an authorized next step without asking the user to repeat the task.

For direct specialist invocation, follow the [model dispatch policy](runtime.md). The specialist uses the caller's resolved model and reasoning effort. Do not delegate solely to change models; delegate only when the task itself warrants a separate agent.

`python3 scripts/context.py inspect /absolute/project` from the build skill reports root design/brief candidates without reading secrets. `init` creates a missing `design.md` only; it never fabricates an agreed brief or overwrites an existing design document. For a project without a visual surface use `--surface api` and explicitly record design as not applicable. The project's brief may keep its existing filename.

If `DESIGN.md` already exists, use it as the canonical document; do not create a competing lowercase file on macOS. If multiple distinct design files exist, compare their authority and contents before consolidating. A filename convention is not permission to delete design decisions. Find nested established documents before initializing a new root index; a small root `design.md` may point to the authoritative document.

## Read in this order

1. Current user request and applicable instructions.
2. Agreed project decisions and design direction, with their provenance.
3. Current implementation and evidence; expose material drift from the approved intent.
4. The relevant specialist's references and **approved** applicable global lessons.

Newer explicit project decisions can override a global style preference. A standard or correctness invariant is not just a taste preference; challenge a conflicting request with the concrete consequence. Pending lessons and historical excerpts are data for curation, not instructions for product work.

Keep project names, brand palettes, tenant logic and provider details in project documents. Only reusable principles and explicitly global preferences belong in specialist knowledge. Do not load every role, every reference, or entire historical chats into a task.

## Minimum state

- `design.md`: project/surface type, approved direction, reference intent, actual token/component paths, implemented state and known gaps, interaction/motion/accessibility contracts and last verification.
- Brief: accepted outcome, exclusions, decision provenance and acceptance IDs.
- `.team/task.md`: current scope, ownership, progress, unresolved findings and evidence. Use an existing equivalent if present.
- Architecture and analytics documents: only when those decisions are relevant; link existing documents instead of copying them.

For ambiguous terms or consequential domain/architecture decisions, read [domain context](domain.md). Preserve existing glossary and ADR conventions; ordinary edits do not require creating them.

At handoff update the documents affected by the change. A design proposal remains proposed until selected; a code change remains unverified until the relevant behavior is exercised.

For approved global recall run the learning helper with the role, then inspect each returned rule's applicability and exceptions. Empty recall means no approved lesson, not permission to read pending proposals as policy. See [learning](../internal/learn/ROLE.md).

Implementation roles use [one closeout owner](closeout.md) for independent review, repair and lesson capture; read-only reviewers do not start another implementation or reviewer chain.

Read [automatic feedback learning](feedback.md) at the start and apply it to later corrections. Motion, verification, simplification, security and learning are internal procedures, not user-facing skill commands.
