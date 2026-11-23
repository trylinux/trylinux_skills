<!-- wording-ok: historical record, intentionally not loaded by the skill -->
> **Not part of the skill.** This provenance record was moved out of `skills/review-app-security/references/` so it isn't loaded into model context. It quotes historical prompts and security terminology verbatim, which can trip cyber-safety classifiers on refusal-prone models. Keep it here for audit only.

# Recovered prompts and provenance

## Retrieval scope

Extracted November 23, 2026 from the available Codex app history and FAIRF checkout `da3404de0a8a055a961e98fffd900e5146d677d4`.

Read all 75 available history pages (438 turns) across 53 other local FAIRF chats, including older pages; checked the archived local-chat inventory, which contained no FAIRF chat. Searched security/review history, read both repository security reports and the relevant PR descriptions, and checked the discussion timelines for PRs #71, #92, #91 and #116 (all returned no comments). This is the accessible local/history scope, not proof that every review ever performed is recoverable.

Only relevant user prompts are reproduced below. Ambient browser blocks, formatting escapes and HTML space entities were removed; spelling is otherwise preserved. Dates use America/Los_Angeles. Source chat titles are retained verbatim. Turn IDs permit locating the original without publishing full chats.

## Repeated pre-deployment prompt

Six occurrences share this wording (list punctuation/spacing varies):

> Before I deploy,
> Lets do a code review. Look for
> 1) Owasp top 10, owasp api top 10, owasp llm top 10
> 2) Code reuse opportunities and code redundancy problems
> Propose and fix any outsanding isues

| Date | Chat title | Turn ID |
|---|---|---|
| 2026-10-28 | Build yarn archive website | `01a18532-d569-7011-8639-4424a8b48d02` |
| 2026-10-28 | Build yarn archive website | `01a18512-4bcd-7051-95cb-7fece3a925a4` |
| 2026-10-29 | Review current features | `01a18969-633d-7183-a140-cd2d29d66bcb` |
| 2026-10-29 | Add skein metadata research | `01a188b9-48fc-7cf2-8b26-522eaa4d4370` |
| 2026-10-28 | Add nginx config for myfiber.arts | `01a18555-91d0-7112-92ea-4e1e4b23aca5` |
| 2026-10-28 | Add skein metadata research | `01a1860f-fbff-7b42-96f7-03f6ab937b38` |

## Other review, safety and follow-up prompts

Follow-up release instructions are historical authorizations for those tasks, not standing permissions. Pattern-integration and safety-checklist requests broaden the coverage; they are distinguished from standalone repository reviews below.

### Review and fix codebase issues — 2026-11-02 (Review request)

Source turn: `01a19ed6-5262-7b43-8fad-38e986a2bef8`.

> Lets do another major code review
>
> Lets do a big code review here. On top of a standard code review of the entire code base, lest also
> 1) Owasp top 10, owasp api top 10, owasp llm top 10
> 2) Code reuse opportunities and code redundancy problems
> 3) Cross check all of the previous done work (mostly done by codex)
> 4) Double check any prompt injection opportunities.
> Propose and fix any outsanding isues

### Improve pattern user journeys — 2026-11-21 (Release follow-up)

Source turn: `01a201df-3523-7740-9728-ed4a88f6d703`.

> Merge the latest changes into main, build a new Play Store bundle with all the security fixes, and give me the download link.

### Improve pattern user journeys — 2026-11-21 (Review request)

Source turn: `01a2019d-d5af-70e1-85d4-2f7e3abd74d2`.

> Lets do another massive code review of everything to ensure safety

### Test yarn model combinations — 2026-11-01 (Pattern/AI security requirements)

Source turn: `01a199e4-e463-7673-be11-1528fd172dee`.

> Okay lets do patterns next. Review how pattern uploads and analysis work now, then figure out the best model combo for understanding them, including prompt injection protection. But also I want users to be able to hold a conversation about the pattern and then have the ability to export that chat at a later date

### Test yarn model combinations — 2026-11-01 (Pattern/AI security requirements)

Source turn: `01a1998e-fef6-7081-ba41-506aa4bcfb1d`.

> Lets start building this in to the yarn identification.
>
>
> We will do the next with patterns and understanding how to build out various pieces of that, plus prompt injection security

### Find Android app update options — 2026-10-31 (Review request)

Source turn: `01a19458-3beb-7110-88af-4f488615efc1`.

> Another major problem is that the inventory isn't actual editable on the android app. Lets get this fixed. Also, lets do a code review of the android app looking for security issues and bugs. Once this is done, ship it, I won't be here.

### Find next resend security steps — 2026-10-30 (Safety checklist)

Source turn: `01a18edc-70a3-7093-9b50-6c33feaf959f`.

> What is next on the security checklist? I'm still waiting on various things for the resend work to be complete

### Create user safety to-do list — 2026-10-30 (Release follow-up)

Source turn: `01a18e8e-a061-7fd2-be58-195c43befedd`.

> Lets get the remaining Android and deployment changes reviewed, tested, pushed and merged too.

### Create user safety to-do list — 2026-10-30 (Safety checklist)

Source turn: `01a18e6a-b6e2-7762-bd4c-82c06c418a2a`.

> Open the PR and start working down the security checklist.

### Create user safety to-do list — 2026-10-30 (Safety checklist)

Source turn: `01a18e5d-1e40-70c3-85a2-b50ac0ef78f3`.

> lets put together a todo list on the security side, especially user safety.

## Review outcomes used to turn prompts into procedure

| Source | Contribution |
|---|---|
| [Initial security report](https://github.com/trylinux/FAIRF/blob/da3404de0a8a055a961e98fffd900e5146d677d4/docs/SECURITY_REVIEW.md) and early security commits | Provider secret handling, explicit origins, owner-scoped caches, production limits, staged integrity, shared services; user-safety and deployment evidence tracked separately |
| [PR #50](https://github.com/trylinux/FAIRF/pull/50) | Consent, recovery/MFA, exports/erasure, metadata cleanup and readiness gates |
| [PR #71](https://github.com/trylinux/FAIRF/pull/71) | Broad Web/API/LLM, reuse and prior-PR review; normalized identity limits, token-kind/scope separation, catalog poisoning, worker leases, parser isolation; independent fix review found additional bugs |
| [PR #92](https://github.com/trylinux/FAIRF/pull/92), commits `affcf92` / `680db29` | Second broad review; citation grounding, shared-photo privacy, inherited-model fan-out, repeated parser paths, admin takeover, APK publication races and regression-sensitive tests |
| [PR #91](https://github.com/trylinux/FAIRF/pull/91) and [Android report](https://github.com/trylinux/FAIRF/blob/da3404de0a8a055a961e98fffd900e5146d677d4/docs/ANDROID_SECURITY_REVIEW.md) | Credential origins, session lifecycle, bounded media, drafts, partial writes and atomic inventory changes |
| [PR #116](https://github.com/trylinux/FAIRF/pull/116), tests/test_review_round3.py | DNS validation/connection gap, failure leases, durable cleanup, complete-input caches, inter-stage consent, output/accounting allowlists, full migrations and signing-secret scope |
| [Fourth review commit](https://github.com/trylinux/FAIRF/commit/f0d55b4), tests/test_review_round4.py | Fresh authorization/configuration through retries/fallbacks, malformed-401 revocation, immediate offline-source pruning before conflict handling |
| docs/PATTERN_MODEL_PIPELINE.md and docs/YARN_IDENTIFICATION_PIPELINE.md at the same source SHA | Private-document/tool separation, evidence/consent/cache boundaries and bounded injection-test claims |

The security report calls its passes October 29, November 2 and November 21; source chat dates are recorded independently and may differ. Do not infer a one-to-one commit mapping for every repeated early prompt.

## Missing originals and synthesis limits

PRs #71 and #92 link to a Claude Code session. Their original user prompts were not available in the retrieved PR descriptions or empty discussion timelines, and that external session transcript was not retrieved. Their stated scope and outcomes informed the checklist; no reconstructed wording is presented as an original prompt.

The prompts in prompt-pack.md and operational details in the other references are synthesized guidance, not quotations from an unseen agent conversation. No new application audit, production test or live provider experiment was performed while creating this skill. Historical scanner/test results are not current security guarantees.

Earlier report sections contain time-specific claims such as “no model-controlled tools”; later workflows introduced provider-hosted search. Re-read actual current capabilities, not only the oldest coverage note. Likewise, a formerly fixed issue can recur through a new path.
