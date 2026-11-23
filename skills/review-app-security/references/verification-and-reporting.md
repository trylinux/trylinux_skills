# Verification and reporting

## Establish evidence

Record the starting SHA and dirty-tree status; capture baseline failures before changing code. Keep reviewer work separate from pre-existing changes. Inspect source, callers and actual tests rather than treating a PR description as proof.

For each hypothesis, identify the untrusted input, prerequisites, trust boundary, reachable operation, consequence and existing controls. Write a bounded local test with synthetic data and fake services. If the test can't demonstrate the problem, keep it as a question or unconfirmed risk, not a confirmed high-severity finding.

Write regression tests that assert the desired security invariant: another account gets no data, a revoked grant sends no later request, an old worker changes no newer state. These tests fail on the unfixed code and pass after the fix. Don't write tests that assert the defect exists; they have the opposite meaning and make "tests fail" ambiguous in reports.

For important fixes, show test sensitivity by running the invariant against the pre-fix code or temporarily reverting the narrow fix in isolation. Assert that the test actually reaches the boundary being fixed. A consent test that fails during setup has not proved inter-stage revocation.

## Database and concurrency

Do not substitute metadata-created tables for full migration execution. Use fresh upgrades, schema comparison, supported downgrade/re-upgrade, uniqueness/check constraints and preservation of existing data. Exercise both SQLite and real PostgreSQL when both are supported; generated PostgreSQL SQL is not live migration execution.

Data backfills may require online reflection and rows. If full-history offline SQL generation fails, report that fact and use a protected staging rehearsal; do not omit data migrations to make the command appear successful.

Threaded fixtures need independent database connections/sessions. Model configuration changed through a second session must become visible before a later outbound call. Test both ordering directions for unique-default changes. Use deterministic synchronization to reproduce stale workers and concurrent inventory consumption; avoid treating repeated timing luck as proof.

## Tooling and test scope

Adapt commands to the current repo/CI. The FAIRF example uses:
- focused Python security/ownership/account/pipeline tests, plus `tests/test_review_hardening.py` and `tests/test_review_round2.py` through `test_review_round4.py`;
- `pytest`, `node --test tests/js/*.test.cjs`;
- `bandit -q -r app config.py run.py`, `pip-audit -r requirements.txt`, `pip check`;
- fresh migration execution and real PostgreSQL concurrency;
- Android `testDebugUnitTest`, `testReleaseUnitTest`, lint, relevant assemblies and `connectedDebugAndroidTest`;
- focused secret scanning, workflow/config review and `git diff --check`.

Use current installed/CI tool versions. Run meaningful targeted checks, then required broader checks. Repeat after changes, new failures or unresolved concurrency concerns; do not repeat unchanged suites solely to accumulate pass counts.

Secret scans should report redacted locations and confidence, never credential values. Distinguish current tracked files from full history. Scanner-clean means no findings under that scanner/scope/date, not an exhaustive guarantee.

When shipping is requested, preserve the exact reviewed commit through CI and verify the merged/rebased revision. A previous branch pass does not prove the final integration. An APK build does not prove signing, distribution or device behavior; HTTP health does not prove background processing.

## Finding record

For each actionable finding, include:

| Field | Required meaning |
|---|---|
| ID and title | Stable short identifier; concrete defect |
| Severity/confidence | Preconditions, exposure and impact justify priority |
| Location | Current file/line and affected entry points |
| Trigger → impact | Behavior across the trust boundary, as shown by the test |
| Framework mapping | Category name and exact edition/ID |
| Evidence | Regression test and its result on the unfixed code |
| Resolution | Minimal fix and shared callers addressed |
| Verification | Final-revision test result and regression sensitivity |
| Status | Fixed, confirmed open, needs operator action, unconfirmed, or not applicable |

Record no-new-finding coverage too. Do not manufacture a finding for every category.

## Prior-work ledger

For each relevant earlier claim/PR: claimed behavior → current implementation/callers → validating test → discrepancy/status. Sample high-risk regressions deliberately and state the inspected range; never say “all prior work verified” unless the scope supports it.

Key FAIRF lessons: a new global-photo feature reopened catalog privacy, a new PDF path omitted parser isolation, failure handlers lacked success-path leases, old artifact reuse ignored additional inputs, and new fallbacks reused stale grants. Recheck extensions of old controls.

## Final report and operational gates

Lead with important confirmed findings, changes and tests. Separate:
1. fixed and locally verified;
2. confirmed but deferred, with consequence and concrete next step;
3. deployment/operator checks not executed;
4. known limits and untested surfaces.

Each readiness item needs evidence and a completion criterion, not just a checkbox. Email configured is different from delivered; deletion queued from erased; backup created from restored; secure defaults from live proxy/firewall verification.

Do not rerun destructive cleanup or contact live providers just to close a report item. Deliver the concrete command/change plan when the task requires additional authorization; continue unrelated authorized work. A source review is not a guarantee that no vulnerabilities remain.
