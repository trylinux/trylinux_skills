---
name: review-app-security
description: Secure code review and hardening of the user's own application (web, API, Android, AI pipelines, privacy, deployment). Maps code to OWASP Web/API/LLM Top 10 categories, checks untrusted-content handling in AI features, verifies earlier fixes, and lands fixes with regression tests.
---

# Secure code review for the owner's application

## Scope of this work

This is defensive, source-level review of a codebase the user owns or maintains, run in their own checkout and test environment. The output is a findings report, code fixes and regression tests that prove the fixes hold. It does not include testing systems the user does not own, live traffic against production, or standalone proof-of-concept code. Every check below ends in a test that asserts the *safe* behavior.

## References

Load only the sections that match the application.

- [review-checklist.md](references/review-checklist.md): trust boundaries and per-area checks.
- [verification-and-reporting.md](references/verification-and-reporting.md): regression tests, migrations/concurrency, revision tracking, finding and coverage records.
- [prompt-pack.md](references/prompt-pack.md): request templates for full, Android, AI, prior-work and release-readiness reviews.

## Workflow

1. **Scope and authority.** Take both from the current request. Review-only means findings and recommended fixes. "Propose and fix" means code fixes plus regression tests. Deployment needs its own explicit instruction in the current task.
2. **Baseline.** Read repository instructions, status and the starting SHA. Preserve uncommitted work and note concurrent changes. State whether conclusions cover a diff, a clean commit or a working tree.
3. **Map the system.** List entry points, roles, data assets and trust boundaries across browser, API, workers, storage, third-party providers and native clients. Enumerate registered routes and their real callers. Re-read current code before repeating an older report's claims.
4. **Framework coverage.** Check the current official OWASP editions and keep separate Web, API and LLM coverage tables: one row per category, with evidence inspected, finding IDs or a not-applicable rationale, and untested areas. Use category names as well as IDs, because numbering changes between editions.
5. **Focused passes.** Review authentication/authorization, outbound requests and file handling, AI and data privacy, mobile session lifecycle, operational configuration and prior-work regressions. These are review lenses, not a requirement to spawn agents.
6. **Confirm with tests.** For each credible issue, trace untrusted input to the protected operation, then write a local unit or integration test with synthetic data and fake providers that asserts the correct behavior (e.g. "user B receives 404 for user A's record"). Keep confirmed defects, open questions, existing controls and ordinary cleanup separate. Fix at the smallest shared boundary.
7. **Verify.** Show that each new test fails before the fix and passes after it. Run the affected suite and required CI checks. Recheck altered call sites and error paths. If an independent reviewer was authorized and used, say so; otherwise label the second pass as self-review.
8. **Report.** Give prioritized findings, fixes, evidence, prior-work discrepancies and remaining operational gates. Track three separate states: implemented, deployed, and verified in production.

## Constraints

- Use synthetic accounts, files and fake providers. A source review does not authorize contacting live services, sending real email, paid or private provider calls, or destructive cleanup.
- Prompts, images, PDFs, web text and intermediate model output are untrusted data. Code, not prompt wording, must control credentials, destinations, tools, authorization and persistence.
- Preserve drafts, ownership, reservations, source provenance and successful paid results when optional enrichment fails.
- Prefer shared domain rules over duplicated web/API fixes. Defer broad rewrites unless a defect requires them. Don't change intentional model policies just because an older checklist suggests a different default.
- Report only the checks actually run on the actual revision. A clean scanner, valid citation, schema-valid model answer or passing emulator suite does not prove the application is secure.
