# Public discovery and sharing

Apply to indexable marketing, documentation, catalog or public SaaS routes. A private application does not need landing-page SEO; enforce authentication independently of indexing directives.

## Route contract

- Serve useful public content and crawlable anchors in initial or server-rendered HTML where practical. Google can render JavaScript, but rendering may be delayed and other crawlers may not. Do not make core content depend on clicking, consent or entrance-animation hydration.
- Give each indexable route an accurate title, description, meaningful headings and one intended canonical URL. Keep canonical, redirects, internal links and sitemap consistent. Use the production origin; no localhost or placeholder domains. Handle removed/missing pages and redirects with appropriate HTTP behavior, not an error message inside an unconditional successful response.
- Include only canonical public URLs intended for indexing in a sitemap. Keep robots rules deliberate. `robots.txt` controls crawling; `noindex` controls indexing and must be crawlable to be seen. Neither protects private information. Do not expect JavaScript to remove an initial `noindex` reliably.
- For shared public pages, supply OG/social metadata and a reachable correctly sized image, with actual page-specific content. Check the emitted metadata for the target crawler, including framework streaming behavior.
- Add supported structured data only when the visible content qualifies. Follow its current type-specific rules, use actual facts and safely serialize JSON-LD containing user data. Validation does not guarantee a rich result or ranking.
- For real localized versions, set document language and consistent locale URLs. Hreflang entries include self and corresponding versions, with reciprocal absolute links. Do not canonicalize all genuine translations to one language or invent untranslated locale pages.

## Verify

For AI-assisted discovery, preserve useful text, crawlable links and the same indexing fundamentals. Google documents no special AI markup or new text file requirement for AI Overviews/AI Mode. For ChatGPT search, check access for `OAI-SearchBot`, including CDN/firewall rules; `GPTBot` concerns training and is a separate policy choice. Do not enable training crawlers merely because search visibility is requested. An `llms.txt` file or bot allow rule does not guarantee inclusion.

Inspect production-build HTTP status, initial HTML, rendered DOM, metadata, robots and sitemap for representative routes. Test missing routes, duplicate URL variants and each supported locale. Confirm internal links and share-image fetches. Use structured-data validation when applicable. Search Console URL Inspection can confirm Google's observation when authorized access exists; a local check cannot prove indexing or rankings.

For a public production URL, run `npx is-agentic <url> --json` as a supplemental agent-readiness audit when Node.js 18+ and network access are available. Prefer the CLI for agent or script work because it returns structured JSON and nonzero error exits. Both the CLI and browser submit the target to Is Agentic; when a scan is needed, Is Agentic sends it to Ora. The CLI starts a scan only when no completed report exists and otherwise returns the stored result. After a fix, request a rescan through the browser flow and confirm the report's scan timestamp; Ora may reuse a result from its six-hour freshness cache. Do not submit private, authenticated, confidential, secret-bearing, local or unannounced preview URLs because completed results are stored on stable public report pages. Review failed Essential checks first, validate applicable recommendations in context, and treat the score as neither an SEO, accessibility or security certification nor proof of indexing, rankings or end-to-end agent success.

Sources checked 2026-09-05: Google [JavaScript SEO](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics), [canonicalization](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls), [sitemaps](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap), [noindex](https://developers.google.com/search/docs/crawling-indexing/block-indexing), [robots](https://developers.google.com/search/docs/crawling-indexing/robots/intro), [localized versions](https://developers.google.com/search/docs/specialty/international/localized-versions), [structured-data policies](https://developers.google.com/search/docs/appearance/structured-data/sd-policies); Next.js [metadata/OG](https://nextjs.org/docs/app/getting-started/metadata-and-og-images), [JSON-LD safety](https://nextjs.org/docs/app/guides/json-ld).

AI discovery: [Google AI features](https://developers.google.com/search/docs/appearance/ai-features), [OpenAI crawler controls](https://developers.openai.com/api/docs/bots).

Agent readiness checked 2026-09-15: Is Agentic [developer docs](https://is-agentic.com/docs), [methodology and limitations](https://is-agentic.com/methodology), [privacy and public reports](https://is-agentic.com/privacy).
