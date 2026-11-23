---
name: research-model-task-fit
description: Research and benchmark which AI models fit specific tasks, including vision/OCR, sourced research, structured assembly and summarization. Compare quality, evidence retention, latency, privacy and actual cost using reproducible trials rather than general rankings.
---

# Research model fit by task

Produce a dated, task-specific recommendation backed by reproducible evidence. A model good at reading images may not be the best researcher, assembler or summarizer.

Read [evaluation-method.md](references/evaluation-method.md) for task decomposition, fair comparisons, scoring and cost accounting. Read [skeinwise-case-study.md](references/skeinwise-case-study.md) when reproducing the yarn/pattern experiments or using FAIRF's runners.

## Workflow

1. Define the input, required output, expensive failure modes and hard constraints. Establish success criteria, representative cases, privacy requirements, latency and spending limits. Use available context before asking for missing constraints.
2. Separate roles: extraction, grounded research, structured assembly, short factual summary, conversation over retained evidence, and difficult-case review. Test a simple baseline before adding a pipeline.
3. Research current official model/provider documentation. Record exact model ID, route, modalities, tools, schema support, limits, privacy eligibility, pricing units and date. Verify the actual account route with a small permitted preflight; a model-family marketing page does not prove endpoint capability.
4. Freeze samples, hidden expected answers, prompts and scoring before the main comparison. Keep reference answers out of model inputs. Change one meaningful factor at a time; record requested and returned models and all errors.
5. Run only within the user's authorized data-sharing and cost scope. Preparing a manifest or report does not require calling a paid provider. If live execution is not authorized, deliver the concrete run plan and cost/data scope for approval. Do not ask again for authorization already established.
6. Compare stage quality and end-to-end quality, actual wall time, failed/retried attempts and reconciled costs. Inspect contradictions and lost evidence manually. A report's numeric score is not itself ground truth.
7. Recommend a model or routing policy **for each role**, with fallback conditions, measured tradeoffs, uncertainties and revisit triggers. Do not change production defaults as a side effect of research.

## Deliverable

Include the dated candidate/source table, benchmark design and coverage, per-role results, pipeline regressions, cost/latency accounting, recommendation and reproduction artifacts. Distinguish documentation claims, successful preflights, measured results and hypotheses.

If a model was unavailable, record unavailable rather than poor quality. If billing is incomplete, report unknown rather than free. If trials were not run, state that the recommendation is provisional. Never preserve an old winner or rate as a timeless fact.
