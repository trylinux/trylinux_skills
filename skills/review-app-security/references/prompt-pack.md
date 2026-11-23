# Reusable review prompts

These are synthesized templates, not verbatim historical prompts. Use the requested mode and adapt scope to the current project. No template grants authority beyond the user's request.

## Full review with fixes

> Use $review-app-security for a major review of this codebase. Cover ordinary correctness plus current OWASP Web, API and LLM Top 10 risks; security-relevant code reuse and redundancy; prior-work claims and regressions; and direct/indirect prompt-injection paths. Map web, workers, mobile clients, storage, providers and deployment boundaries. Reproduce credible issues with local synthetic fixtures, fix confirmed problems, and add regression tests. Preserve unrelated work. Report severity, file locations, evidence, final-revision checks, unresolved risks and operational gates. Do not infer deployment authorization from this review request.

For report-only work, replace “fix confirmed problems, and add regression tests” with “report findings and concrete fix recommendations; do not edit application code.”

## Prior-work and second-pass review

> Cross-check the specified prior PRs and security claims against current code, call sites and tests. Look for new paths that bypass established controls, stale documentation and incomplete failure handling. Reproduce suspected regressions before calling them findings. Review the proposed fixes for new bugs, test sensitivity, concurrency and migration behavior. State the exact history/diff inspected and any claims you could not verify.

If a separate reviewer is authorized, give it the scope, code/diff and raw evidence without requiring agreement with the original conclusions. Otherwise perform a distinct second pass and accurately label it self-review.

## Android review

> Review Android security and correctness from transport through UI and offline storage. Check exact-origin credential forwarding, redirects, bounded reads/decodes, session cancellation, late old-account responses, malformed authentication-error bodies, account/server binding, revocation and source deletion during sync conflicts. Also test draft retention and atomic inventory edits. Verify with unit, emulator and backend tests as appropriate, and state device/runtime gaps. Fix confirmed problems within the requested scope.

## AI and prompt-injection review

> Trace every AI workflow, including independent readers, web research, summaries, conversations, exports, cached artifacts, retries and fallbacks. Use synthetic malicious source content to test whether it can influence endpoints, tools, secrets, authorization, persisted fields, source authority or paid work. Check fresh consent/grants/configuration at every dispatch boundary, complete-input cache fingerprints, evidence retention, output allowlists and unknown-cost handling. Preserve user confirmation for durable edits. Do not equate prompt wording, citation membership or schema validation with trustworthy model output.

## User safety and release readiness

> Review the user-safety checklist and distinguish implemented controls from production verification. Cover account recovery/MFA, privacy and AI consent, public sharing, metadata, export/deletion, durable cleanup, email delivery, encrypted/restorable backups, retention, alerting and native offline/session behavior. For each open item state its risk, evidence, owner or next action and completion criterion. Use existing authorization for tests/changes; identify live operations separately.

## Authorized shipment follow-up

> Ship the already reviewed changes within the explicitly authorized target. Isolate the intended patch, verify current-base integration and the exact final CI revision, and follow the requested deployment/artifact path. Preserve unrelated work and signing identities. Report the deployed/built commit, observed health/job or artifact results, and any remaining operational validation.

Historical requests sometimes included “ship it”; use this template only when shipment is authorized in the current task.
