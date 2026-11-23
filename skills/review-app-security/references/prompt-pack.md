# Request templates

These templates are synthesized, not quoted from earlier chats. Pick the one that matches the request and narrow the scope to the current project. A template never grants more authority than the user's current request.

Each one names the codebase as the user's own and ends in fixes and tests. Keep that framing when you adapt them.

## Full review with fixes

> Use $review-app-security for a full secure code review of this repository, which I own. Cover ordinary correctness plus the current OWASP Web, API and LLM Top 10 categories; duplicated security logic that has drifted; earlier fixes and whether they still hold; and how AI features handle untrusted document and web content. Map web, workers, mobile client, storage, providers and deployment boundaries. Confirm each issue with a local test using synthetic data, fix confirmed problems and keep the tests as regressions. Leave unrelated work alone. Report severity, file locations, evidence, final-revision checks, open risks and operational gates. This request does not authorize deployment.

For report-only work, replace "fix confirmed problems and keep the tests as regressions" with "report findings and concrete fix recommendations; do not edit application code."

## Prior-work and second-pass review

> Cross-check the listed earlier PRs and their security claims against current code, callers and tests. Look for new code paths that skip established controls, stale documentation and incomplete error handling. Confirm a suspected regression with a test before reporting it as a finding. Review the proposed fixes for new bugs, test sensitivity, concurrency and migration behavior. State the exact history or diff inspected and any claims you couldn't verify.

If a separate reviewer is authorized, give it the scope, code/diff and raw evidence without asking it to agree with the original conclusions. Otherwise do a distinct second pass and label it self-review.

## Android review

> Review this Android client for security and correctness from network layer through UI and offline storage. Check that tokens go only to the exact approved origin, redirect handling, bounded reads and image decoding, session cancellation, late responses from a previous account, unreadable auth-error bodies, account/server binding, revocation, and source deletion during sync conflicts. Also test draft retention and atomic inventory edits. Verify with unit, emulator and backend tests as appropriate, and list device/runtime gaps. Fix confirmed problems within the requested scope.

## AI pipeline review

> Trace every AI workflow, including independent readers, web research, summaries, conversations, exports, cached artifacts, retries and fallbacks. Add test fixtures whose content contains embedded instructions, and assert that they cannot change endpoints, tools, secrets, authorization, persisted fields, source authority or paid work. Check that consent, grants and configuration are re-read at every dispatch boundary, that cache keys cover the complete input, and that evidence retention, output allowlists and unknown-cost handling are correct. Keep user confirmation for durable edits. Prompt wording, citation membership and schema validation don't make model output trustworthy.

## User safety and release readiness

> Review the user-safety checklist and separate implemented controls from production verification. Cover account recovery/MFA, privacy and AI consent, public sharing, metadata, export/deletion, durable cleanup, email delivery, encrypted and restorable backups, retention, alerting and native offline/session behavior. For each open item give its risk, evidence, owner or next action, and completion criterion. Use existing authorization for tests and changes; list live operations separately.

## Authorized release follow-up

Use only when the current task explicitly authorizes shipping.

> Ship the already-reviewed changes to the authorized target. Isolate the intended patch, verify integration with the current base and the exact final CI revision, and follow the requested deployment or artifact path. Leave unrelated work and signing identities untouched. Report the deployed or built commit, observed health/job or artifact results, and any remaining operational checks.
