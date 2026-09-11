# Data, navigation and recovery

Keep local UI state, URL state and server state distinct. Derive values during render when possible; use effects for external synchronization, not to mirror derivable state. Put user-triggered logic in its event handler. Use the existing data layer; TanStack Query is the default candidate for substantial interactive authenticated server state, not a requirement for static content.

Represent first load, populated, empty, stale, partial failure, retry and permission states where reachable. Preserve input on recoverable errors. Prevent accidental duplicate submissions; use optimism only when the action is reversible and rollback/reconciliation is defined. Backend integrity must still tolerate duplicate requests.

Place slow work below its Suspense/loading boundary. An earlier await or unrelated root-layout fetch can block that boundary. Show immediate pending feedback at the initiating control when a cold navigation cannot display its destination yet; a prefetched route is insufficient evidence. Do not defer authorization until after protected HTML, RSC payloads or serialized props have been sent.

Treat Server Actions/Route Handlers as callable server endpoints. A hidden control is not authorization. Keep secrets and database access server-only; project only fields the browser needs. Include data-changing parameters and relevant account/tenant scope in cache keys; define invalidation after mutation and account switches. Avoid a second cache of the same server result without a concrete ownership need.

## Verify

For changed data routes, delay the actual data dependency by three seconds and test cold entry, warm navigation, back/forward, a parameter change, failure and recovery. Delay server-to-server requests on the server, not only through browser interception. Check that retry fetches again and that account switches cannot reveal cached prior-user data.

Version check: Next.js `retry()` became stable in 16.3 and refetches; `reset()` clears boundary state without refetching. Use the installed version's supported recovery API. Caching and navigation APIs also vary by version/configuration.

Sources checked 2026-09-05: [React effects](https://react.dev/learn/you-might-not-need-an-effect), [Next navigation](https://nextjs.org/docs/app/getting-started/linking-and-navigating), [error recovery](https://nextjs.org/docs/app/api-reference/file-conventions/error), [data security](https://nextjs.org/docs/app/guides/data-security), [TanStack query keys](https://tanstack.com/query/latest/docs/framework/react/guides/query-keys). The three-second fixture is this workflow's diagnostic convention.
