# Evidence before completion

Do not mechanically run every tool. Execute the checks for the changed scope and record actual results. Structural skill validation only checks packaging; it does not prove future agent behavior.

## Skill package

Run skill-creator's quick_validate, then `python3 scripts/test_scaffold.py`. Generate each supported profile in a temporary empty destination. Install its dependencies; read typecheck, lint/test and production build results. Verify the generator refuses overwrite and missing design/brief decisions. Check all relative links. Examples labelled illustrative must not be reported as integration-tested.

## Generated project

- Clean install with lockfile; selected package lint/typecheck/test/build commands pass.
- API: invalid input, known errors, dependency failure, auth/tenant boundary where present. Confirm safe response/log content.
- Database: isolated migration run and rerun, intended indexes, runtime without DDL rights. If no test DB is available, explicitly mark migration unverified.
- UI: real production browser; desktop/mobile; keyboard and focus; forms; loading/empty/error/success; back/forward and double submit.
- Navigation: inject delayed data below the rendering boundary and separately exercise cold route delivery. Pending feedback or preserved content + progress must precede delayed result. A Playwright intercept can't delay a server-to-server request; use a test upstream or server fixture for that path.
- Accessibility: axe plus manual keyboard/labels/contrast/zoom/reduced-motion checks. No blanket compliance claim.
- Public site: inspect metadata, canonical/robots/sitemap and social image. Private routes: actual auth, not only noindex.
- Analytics: test initialization/pageview count, privacy state and identity; observe event in intended PostHog project if credentials exist.
- Design: display the requested option count before selection; selected identity appears in UI kit and actual screens, including mobile and error states.

Finish only when agreed scope meets its acceptance criteria, or clearly preserve an input-dependent pending stage while completing independent work. Report narrowly: scaffold smoke test, product E2E and real-service integration are different evidence.

Behavioral scenarios to use when the skill changes: API-only idea (no design or frontend packages); public catalog (SEO + visual choice); private admin (access control + no SEO marketing checklist); tiny form (Next-only backend acceptable); existing Express app (no forced migration); analytics-only edit (this skill should not hijack it); user provides selected design (don't repeat six options); user explicitly requests ten (not six); resumed task (retain decisions).
