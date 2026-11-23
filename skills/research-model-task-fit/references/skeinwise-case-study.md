# Skeinwise case study and reproducible runners

Source snapshot: `trylinux/FAIRF` at `da3404de0a8a055a961e98fffd900e5146d677d4`, inspected November 23, 2026.
[Source tree](https://github.com/trylinux/FAIRF/tree/da3404de0a8a055a961e98fffd900e5146d677d4).
Access may be required. The general evaluation method works without these scripts; do not assume they are installed with this skill.

## Recorded pipeline decisions

Yarn: independent image readers → sourced web researcher → guarded record assembler. Both readers receive identical images; research and assembly receive both readings. Only the researcher gets search/fetch tools. Known photo-specific values outrank generic current-web package facts. Dye lot requires a label lot transcription, not a color code. Inventory amount, acquisition history and replacement price are not inferred into authoritative fields.

Pattern: independent readers → private conversation/assembly over saved evidence, with no web tools. Separate original instructions, transcription, analysis, proposals and confirmed requirements. Cached readings are private and invalidated when relevant sources/settings change.

Summary: short factual prose over saved approved facts, no new search; validate against the provided facts and use a local description if appropriate.

Historical example IDs in the source configuration:
- image readers: `xiaomi/mimo-v2.6-flash`, `google/gemini-3.8-flash`;
- yarn researcher: `deepseek/deepseek-v4.1-flash-1017`;
- assembler: `google/gemini-3.5-flash-lite`;
- separate summary comparison: `mistralai/mistral-small-2603` versus DeepSeek.

These are configuration/history, not a current recommendation or independently verified live availability. The older provider assessment and later pipelines describe different stages of the project; do not flatten them into one timeless winner.

The pattern document reports nine selected cases from 125 provided PDFs, 54 selected factual checks per reader, and 27 follow-up calls with 54 checks for assembly. It reports about $0.0152 per case for both readings plus three follow-ups and 24 targeted injection cases. Those are bounded historical claims, not a fresh experiment, full-corpus accuracy estimate, general injection immunity or current price quote. No raw private benchmark dataset is included here.

## Configurable yarn benchmark

Read `docs/YARN_BENCHMARKS.md`, `scripts/benchmark_yarn_pipeline.py` and `scripts/report_yarn_benchmark.py` in the current checkout. Runners use internal app adapters; check compatibility after adapter changes.

The manifest has `photo_directory`, `samples`, `models`, `identification_models` and `pipelines`.
Each sample has unique simple `id`, `label_for_report`, and one to five relative photo paths. Each model alias declares `provider`, exact `model`, `key_env`, optional `base_url` and `search_engine`. Pipelines map `name`, `identify`, `research`, `organize` to model aliases.

A separate `label_checks.json` contains `method` and expected answers keyed by sample ID under `samples`. Optional `sources` is excluded from scoring. Fiber uses percentage/name pairs, e.g. `[[80, "wool"], [20, "nylon"]]`. Expected answers are used only after generation.

Prepare this layout outside source control:

```text
comparison/
  manifest.json
  label_checks.json
  results/
```

From the FAIRF root, in its Python environment, after authorization for the selected inputs/providers/spend:

```sh
python scripts/benchmark_yarn_pipeline.py \
  --manifest /private/path/comparison/manifest.json \
  --output /private/path/comparison/results \
  --secrets-env /private/path/provider.env --phase all --workers 1
python scripts/report_yarn_benchmark.py /private/path/comparison
```

The second command is local/report-only. New run directories/files use 0700/0600. Outputs include private paths, label facts and provider text; review before sharing.

The runner has `identify`, `pipelines` and `all` phases; `--sample` and `--model` permit exploration. The reporter requires complete identification and pipeline coverage for its supplied manifest and matching image hashes. Report partial experiments with a matching subset manifest, not a misleading full-run denominator. Successful stages can be reused; concurrent pipelines may duplicate uncached shared calls. One worker is a sensible initial spend-control choice, not a universal optimum.

## Dual-reader experiment

`scripts/benchmark_dual_vision_yarn.py` has its own fixed `MODELS` constants, using only the manifest's samples/photo directory. Editing model aliases in the manifest does not configure that runner.

```sh
python scripts/benchmark_dual_vision_yarn.py \
  --manifest /private/path/manifest.json \
  --label-checks /private/path/label_checks.json \
  --output /private/path/dual-comparison \
  --secrets-env /private/path/provider.env --workers 1
```

Inspect `--resume`, `--retry-incomplete`, and `--reconcile-only`. Reconciliation refreshes billing metadata without new model calls but may contact the provider; combine with resume for an existing run. It is not the same as an offline report.

## Summary comparison

`scripts/compare_summary_models.py` selects ten active records for a specified user, evenly spaced by supplied fact-text length. It alternates model order, records prompt hashes/usage/latency, and does not persist generated summaries to application records.

```sh
python scripts/compare_summary_models.py \
  --user-id 123 --output /private/path/summary-selection.json --dry-run
```

Use an actual authorized user ID. Dry run reads database facts but makes no external model calls. For a later authorized live run choose a new output filename: the script refuses to overwrite existing output. The two candidates are hard-coded; inspect/update an isolated copy for a new comparison. Sampling by length covers density, not every difficult semantic case.

## Reporter caveats discovered during extraction

The generic reporter's cost helper sums missing values as zero. Treat those totals as **reported known charges**, not proof of a complete/free run; inspect raw usage and mark missing billing separately.

The label scorer allows ±1 for grams/meters, checks fiber pairs for inclusion, and accepts normalized substring matches for list alternatives. It can therefore miss extra incorrect fiber claims or overly broad alternatives. Review errors manually and tighten scoring for the actual task. Do not mistake a perfect score for complete correctness.

The reporter examines dropped evidence, uncertainty and citations and known-field changes; retain those gates alongside field accuracy. Its timing sums stage durations and excludes queue time, so independently measure wall time when comparing parallel workflows.

## Source paths

- `docs/AI_PROVIDERS.md`, `docs/HUGGINGFACE.md`, `docs/INTEGRATIONS.md`: candidate research and provider routing history; refresh prices/terms.
- `docs/YARN_BENCHMARKS.md` and the four scripts above: mechanics and limitations.
- `docs/YARN_IDENTIFICATION_PIPELINE.md`, `docs/PATTERN_MODEL_PIPELINE.md`: roles, evidence, cost/cache/privacy boundaries.
- `app/services/research_summary.py`: summary fact boundary/validation.

Deterministic tests validate adapters, artifacts and scoring with fixtures; they do not demonstrate live model quality or spend accuracy.
