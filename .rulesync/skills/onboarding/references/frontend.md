# Frontend practice

## Navigation and data boundaries

Use Next Link for internal navigation, persistent layout shells, route `loading.tsx` for dynamic destinations, and Suspense close to slow content. Loading files are nested below their layout: an await above the boundary can still block it. Provide source-link pending feedback for uncached/slow route code too. Prefetch behavior must be checked in a production build. [Next navigation](https://nextjs.org/docs/app/getting-started/linking-and-navigating).

Our acceptance scenario: throttle or delay the data response by 3 seconds; click a cold route; a visible pending cue should appear promptly (project target ~200 ms after the event can be handled), then shell/skeleton before the delayed content. Test warm/cold links, back/forward, query changes and a failure. This target is a local UX budget, not a framework guarantee or WCAG threshold. React may keep previously shown content during transitions; in that case retain content with clear pending feedback. Never fake delay merely to display a skeleton.

Do not await unrelated DB/API requests in the root layout. Public shell can render before private data, but never stream protected content before authorization. Use a gated private subtree and authorized data access. For search/filter/list updates use TanStack Query where client caching is useful, debouncing only where justified, request cancellation and stale-result protection. Don't mark the entire app `use client` for one button.

## State and request behavior

Each data view specifies initial loading, populated, empty, partial/stale, error/retry and permission-denied states. Distinguish refreshing existing data from first load. Keep input/scroll/selection stable where possible. Optimistic UI is for safely reversible actions with rollback; don't display unconfirmed payment or destructive success.

Parallelize independent requests; don't create a fetch waterfall. Bound external calls and check HTTP status before decoding. Validate external data at runtime. Place secrets/server clients behind server-only modules. Cache only when the domain allows it, with explicit invalidation after mutations; never share tenant/private data through a public cache key. Treat current Next caching APIs as version-specific and inspect installed docs.

## Rendering and forms

Render public indexable content on the server or statically. Use client islands for interaction. Reserve image space; use appropriate responsive image sizing and lazy-load below-fold media. Use local or framework-managed licensed fonts with fallbacks. Lazy-load heavy optional editors/maps rather than essential navigation. Avoid unbounded lists; use pagination/virtualization based on actual data size.

Forms have validation at client usability and server trust boundaries; visible field errors; stable pending states; safe retries and preserved input. Never use Server Actions as the default read transport for independent reads. Centralize API contracts and narrowly shared UI primitives, not a universal component with dozens of unrelated modes.

Examples: [streaming pattern](../examples/frontend-patterns.tsx), [starter web](../assets/starter/web). Adapt illustrative snippets; execute the generated app's real acceptance cases.

## Error recovery must fetch again

For the included Next 16.3+ starter, use the error boundary `retry()` prop to re-fetch and render server content; `reset()` only clears the boundary state. For earlier versions inspect the matching API rather than copying this prop. Test recovery with a failed upstream that subsequently becomes healthy, including pending feedback and a second failed retry. [Next error API](https://nextjs.org/docs/app/api-reference/file-conventions/error).
