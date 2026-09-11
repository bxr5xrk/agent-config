# Public SEO versus private app

Public indexable routes get distinct titles/descriptions, correct canonical URL, social previews, favicon, meaningful headings, crawlable links, sitemap/robots behavior and real HTTP not-found handling. Add structured data only for truthful supported entities. Pagination/filter canonical rules should reflect actual content. Render essential public content without waiting on browser-only JavaScript where practical.

Set the production origin from validated configuration. Do not ship localhost/example canonicals. Staging and private routes are not indexable. Private content still requires authentication: robots/noindex is not access control. Never include private/tenant URLs in a public sitemap.

Use Next Metadata and metadata-file conventions appropriate to the installed version. Verify rendered HTML metadata, canonical host, public sitemap URLs and private exclusion; check a crawler-style no-JS request plus browser rendering. Don't claim rankings, rich-result eligibility or “SEO done” just because metadata exists.

Source: [Next metadata and OG](https://nextjs.org/docs/app/getting-started/metadata-and-og-images). Implementation checklist here is our project default; validate any search-provider-specific feature against that provider's documentation.
