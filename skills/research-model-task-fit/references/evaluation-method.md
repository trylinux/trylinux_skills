# Evaluation method

## Define tasks before models

| Role | What to measure | Common false success |
|---|---|---|
| Vision/OCR extraction | Exact visible fields, units, omissions, uncertainty, conflicting photos | Plausible brand/product guessed from appearance |
| Grounded research | Correct product/version, source quality, claim-to-citation support | Model-written URL or current product page used as proof of an old label |
| Structured assembly | Valid schema, retained known fields/evidence, honest unknowns | Cleaner prose silently drops evidence or overwrites a known value |
| Summary | Factual consistency, brevity, unsupported claims and omissions | Pleasant writing introduces facts absent from supplied records |
| Pattern/document Q&A | Size-specific facts, faithful instructions, source location, context reuse | Invented rows, chart directions or an answer for the wrong size |
| Reviewer/escalation | Hard-case gain over baseline and frequency needed | Premium model used on every easy case without measured benefit |

Choose hard gates before optimizing cost. Identity corruption, privacy-route failure or fabricated instructions may disqualify a candidate even when its average score is high. Express preference tradeoffs explicitly rather than hiding them in one arbitrary weighted score.

## Candidate research

Use official model cards, provider APIs/catalogs, SDK/API documentation, pricing and retention pages. Search current primary sources; date each claim and link the exact source. Community benchmarks can generate hypotheses but do not replace task evaluation.

Distinguish model capability from hosting route capability: tools, multimodal input, accepted parameters, schema enforcement, provider fallback and data retention can vary. Verify aliases and returned model IDs. Consumer subscriptions, API allowances and pay-as-you-go credits are separate until official terms establish otherwise.

For local inference record hardware, quantization, memory, throughput and operating costs. For hosted inference include image preprocessing/tokenization, output/reasoning, search/tool fees, retries and cache effects. Do not estimate photo invoices solely from text token prices.

## Dataset and controls

Use representative easy and hard inputs: clear/damaged/multilingual labels, vintage packaging, conflicting photos, sparse records, long patterns, multiple sizes and missing facts. Protect private data; synthetic fixtures help test plumbing but cannot establish real-photo quality.

Record sample IDs, input hashes, preprocessing, prompt version, requested/returned model, endpoint route, generation IDs, parameters, timestamps, durations, usage and errors. Keep secrets out of artifacts; use private directories/files.

Establish expected answers by human inspection and reliable source evidence. Document who/what established them and unresolved ambiguity. Split development cases from held-out evaluation where sample size permits. Do not tune prompts against every final test case.

Supply identical analysis images to independent readers. A second reader receiving the first reader's answer is not an independent reading. Compare independent readers, a single-reader baseline and complete pipelines. Give the assembler both complete readings and source evidence, not only a compressed consensus.

Alternate execution order or randomize it; repeat a meaningful subset to assess variability. Fix concurrency for latency comparisons. Cache reuse must be explicit and never presented as fresh-model performance.

## Scoring and judgment

Predeclare field comparison rules, numeric tolerances and accepted synonyms. Score accuracy, omission, unsupported assertion, schema compliance and error rate separately. Keep failed calls in reliability/expense denominators. Report sample counts and checks per sample; many checks from a few documents are not many independent samples.

For source research, open cited evidence and assess whether it supports the exact claim and product/version. A returned citation establishes provenance, not truth. Preserve uncertainty when sources disagree.

Compare inputs and outputs at each boundary: known values overwritten, evidence/uncertainties dropped, citations lost, and inventory/purchase facts fabricated. A pipeline that improves label accuracy but damages evidence can still fail the quality gate.

Require exact transcription when wording matters. Label facts do not prove chemical fiber identity; current packaging specifications do not supersede the photographed item. Distinguish printed unit weight from remaining measured weight.

Measure actual elapsed end-to-end time plus stage times and, if relevant, queue time. Parallel stage duration sums are not end-to-end latency. Give median and tail latency only when sample count supports a useful interpretation; preserve raw timing.

## Cost accounting

Maintain one ledger per unique provider request including preflights, failures, retries and shared/cached stages. Separate:
- aggregate response-reported provider charge;
- tool/search costs already included or separately billed;
- BYOK upstream charges;
- estimates and unknowns;
- new charges versus reused evidence.

Avoid adding non-BYOK upstream figures already included in an aggregator's price. A zero-cost root generation can have billed nested tool calls; use aggregate response usage where available. Reconcile with generation/account metadata without counting the same request twice. Missing, invalid or non-finite cost is unknown, not zero.

A post-response continuation budget only stops subsequent calls. It cannot cap in-flight requests or parallel overshoot; provider account limits serve a different purpose. Report assumptions and maximum planned requests before a live run.

## Recommendation and handoff

Use a table with role, candidate, sample/check counts, quality failures, latency, known cost, unknown cost and recommendation. Show the simplest passing baseline alongside more complex pipelines. Explain which hard cases justify escalation and when to fall back to manual review/local operation.

Keep a dated decision log: chosen model/route, evidence, rejected alternatives actually tested, uncertainty, price/capability recheck triggers and rollback condition. Changing a model, prompt, preprocessing or provider policy should invalidate relevant caches and trigger targeted reevaluation.

Research does not automatically authorize deployment. If integration is requested, preserve per-user grants, disabled/revoked access, source privacy and confirmation boundaries; verify with deterministic fixtures separately from live-model quality.
