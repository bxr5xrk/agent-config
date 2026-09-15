# Providers, pools, quotas, and capacity

Model every external provider as a constrained dependency: authentication/session
lifecycle, endpoint/capability, quotas and rate limits, latency, retries, cost,
terms/policy risk, outage behavior, and disable/fallback path. Track current
provider/version/account scope because behavior may differ by region, plan, or
identity.

Keep operational pools separate when they serve different purposes or risk:
discovery/scraping versus outbound sending, test versus production, tenant-owned
versus shared, and low-privilege versus administrative. Separation should exist in
data models, selection logic, metrics, quotas, and runbooks—not only naming.

For account/session/proxy pools observe available, healthy, cooling-down, blocked,
login-required, and exhausted states. Rotate or refresh through the owning provider
contract. Avoid tight retry loops and cross-purpose substitution that can spread a
block, leak tenant activity, or destroy reputation across the pool.

Rate-limit handling uses bounded exponential backoff/jitter, provider-specified
retry timing, atomic quota claims, and circuit breakers where appropriate. Do not
increase concurrency or lower delays until metrics identify capacity rather than
provider protection as the bottleneck.

Plan degraded behavior: queue safely, pause the affected capability, surface a
specific status, and protect unrelated paths. A fallback that repeats the same
external effect or uses an unapproved account is not safe redundancy.
