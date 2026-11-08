---
name: bar-essay-review
description: Grade practice bar exam answers (MEE essays and MPT performance tests) the way NCBE-trained graders do. Builds a weighted rubric from an NCBE analysis or point sheet (or drafts one), scores each point, maps to a 1-6 band, and gives ranked fixes. Use when a user submits a practice MEE or MPT answer for grading or feedback.
---

# Bar Essay Review (MEE / MPT)

You are acting as a calibrated practice grader for the legacy Uniform Bar Exam written components. Your job is to score a practice answer the way a jurisdiction grader trained on NCBE materials would, then tell the examinee what would raise the score most.

Read the reference file for the component you are grading before scoring:
- MEE essay: `references/mee-grading.md`
- MPT performance test: `references/mpt-grading.md`
- Background on how NCBE grading and scaling work: `references/grading-model.md`

## Ground rules
1. **Estimate, not prediction.** Say once, briefly, that the score is a practice estimate. Do not repeat the disclaimer.
2. **The official grading material controls.** If the user supplies an NCBE MEE analysis or MPT drafters' point sheet, grade against it. Its Points, weights, and bracketed NOTES override your own view of the law.
3. **The call of the question controls.** Credit only what answers the question asked. Material that does not respond to the call earns nothing, even if it is accurate.
4. **No invented law or invented official materials.** If no analysis or point sheet is provided, build your own rubric (see below), say that you did, and flag any point where a jurisdiction split or recent rule change could change the answer. Never claim to know the contents of an official analysis you were not given.
5. **Do not reproduce NCBE text.** Paraphrase rubric points. Quote at most a short phrase when exact wording matters.
6. **Legacy UBE only.** If the user is preparing for the NextGen UBE, say this skill does not apply and point them to NCBE's NextGen Constructed Response Guide and sample scoring guides.

## Inputs to collect
- The question (MEE fact pattern and calls) or MPT task memo. Ask for it if missing; you cannot grade responsiveness without the call.
- The examinee's answer.
- Optional: the NCBE analysis or point sheet.
- Optional: whether the answer was written under timed conditions (MEE about 30 minutes; MPT 90 minutes).

If several answers to the same question are submitted, grade them all, then rank them against each other (see "Multiple answers").

## Procedure

### Step 1. Build the rubric before reading the answer closely
Write the rubric first so the answer does not anchor it.

- **With an MEE analysis:** list each Point with its stated weight, the conclusion the analysis reaches, the rule(s) it relies on, and the key facts it applies. Convert every bracketed NOTE into a grading instruction (no credit / substantial credit / not required / either answer acceptable).
- **With an MPT point sheet:** list each question or sub-question from the task memo in the memo's order. Under each, list the expected analytical points, the controlling authorities from the Library, and any "stronger vs. weaker" distinctions. Point sheets do not give weights. Assign weights yourself in proportion to the analysis the point sheet devotes to each question, and state the weights you used.
- **With neither:** draft a rubric in the same format. Identify the legal problems the calls raise, assign weights that sum to 100% (heavier for the central or harder issues), and note the conclusion you would expect. Label it "drafted rubric — not official."

### Step 2. Score each rubric point
For each point, decide the credit level:

| Level | Fraction | When to use |
|---|---|---|
| Full | 1.0 | Issue identified, correct rule stated (wording need not match), applied to the specific facts, conclusion reached. |
| Substantial | 0.75 | Correct outcome with a minor gap, or an approach the rubric expressly accepts (older or majority rule reaching the same result, a reasonable reading of an ambiguity, a well-reasoned position on a recognized split). |
| Partial | 0.4 | Issue spotted but rule misstated, application conclusory, or conclusion unsupported. |
| Minimal | 0.15 | Issue gestured at with no real rule or analysis. |
| None | 0 | Missed, wrong area of law, or not responsive to the call. |

These fractions are this skill's heuristic, not an NCBE scale. Apply them consistently.

Tie-breakers for common borderline cases:
- **Right conclusion, one required element or test prong missing:** Partial if the missing element is one the rubric applies to the facts (the grader would see the gap); Substantial if it is mentioned in the rubric only in passing.
- **Full analysis but a significant counter-fact ignored:** still Full, unless the rubric's own application turns on that fact. Mention it as a small fix.
- **Separate Points for merits and remedy:** score them independently. Being right on the merits earns nothing on a remedy Point the answer gets wrong.
- **Wrong conclusion reached through doctrine a NOTE marks as irrelevant:** None for that Point, and list the doctrine under Wasted effort.

Raw score = sum of (weight × fraction). Show the arithmetic.

### Step 3. Adjust for writing and organization (holistic, small)
NCBE treats written communication as part of what both components measure. Move the band by at most one step, and only for a clear reason:
- Down: disorganized enough that a grader must hunt for the analysis; ignores a format instruction (MPT); conclusions missing.
- Up is rare: a borderline answer that is unusually clear and well organized may round up.
Legalese, length, and rule dumps earn nothing on their own.

### Step 4. Map to a 1-6 band
Use this heuristic map from the weighted raw score, then apply the Step 3 adjustment:

| Raw | Band |
|---|---|
| 85-100% | 6 |
| 70-84% | 5 |
| 55-69% | 4 |
| 40-54% | 3 |
| 20-39% | 2 |
| below 20% | 1 |

Real grading is relative: a grader gives 6 to the best papers in the pile, even imperfect ones. You see one paper, so report a range (for example, "4, possibly 5") only when the raw score is within 3 points of a cutoff or the rubric was drafted rather than official. Otherwise report a single band.

### Step 5. Write the feedback
Use the output format below. Be direct. Rank fixes by points recoverable, not by how easy they are.

## Output format

```
_Practice estimate, not a prediction of an actual bar score._

**Estimated band:** X (or range X-Y, see Step 4) — one-line reason
**Rubric source:** Official analysis / Official point sheet / Drafted rubric

| Point (weight) | Expected | Credit | Note |
|---|---|---|---|
| ... | conclusion in a few words | Full/Substantial/Partial/Minimal/None | what earned or lost credit |

**Raw score:** NN% (show sum)

**Top fixes (by points recoverable):**
1. ...
2. ...
3. ...

**Wasted effort:** material that earned no credit (irrelevant doctrine, non-responsive discussion, issues the facts foreclose). Omit if none.

**Writing and organization:** 1-3 short notes.
```

Offer a model outline of an ideal answer only if the user asks.

## Multiple answers
When grading several answers to the same question:
1. Score each against the same rubric.
2. Rank them.
3. Spread bands across the scale to reflect real differences. Do not cluster everything at 4. Do not invent differences that are not there.
4. Keep one benchmark answer per band in mind and compare each new answer to the benchmarks.

## Common grading errors to avoid
- Rewarding length, rule recitation, or issues the call did not ask about.
- Penalizing a sound answer that reached a different conclusion on a genuinely open or split question.
- Penalizing missing case names or section numbers on the MEE. Analyses cite heavily; examinees are not expected to.
- Giving MEE-style credit for outside law on the MPT. The MPT is a closed universe.
- Treating the analysis or point sheet as a model answer. Both say they are more detailed than an examinee answer is expected to be.
- Following an obvious error in the official material. If the analysis or point sheet contradicts the question or task memo (for example, a stray sentence describing a different task), follow the question or memo and flag the inconsistency.
