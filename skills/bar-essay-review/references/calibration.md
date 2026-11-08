# Calibration log

How the skill's scores compare with known outcomes. Update this when new graded essays become available. No question or answer text is recorded here.

## Benchmark set 1: Georgia February 2026 sample answers (2026-11-08)

Georgia publishes applicant answers that "received a high score" from the examiner who graded them. Georgia is not a UBE jurisdiction; its essays are state-drafted (four per three-hour session, about 45 minutes each, under Georgia law). Its MPTs are standard NCBE items. No analyses or point sheets were available, so every grade used the drafted-rubric path. Grader: Sonnet 5.5, blind to the fact that the answers were high-scoring.

Expected result for a calibrated skill: bands 5-6 for every answer.

### Before recalibration (single band map: 6 ≥ 85, 5 ≥ 70, 4 ≥ 55, 3 ≥ 40)

| Item | Raw | Band |
|---|---|---|
| MPT-1 (Otto v. Nolan), sample 1 | 72% | 4-5 |
| MPT-2 (In re Franklin Defenders of the Earth), sample 1 | 72% | 4-5 |
| Essay 1 (Contracts/UCC), sample 1 | 60% | 4 (3) |
| Essay 1, sample 3 | 43% | 3 (2-4) |
| Essay 2 (Real Property), sample 1 | 73% | 4-5 |
| Essay 2, sample 2 | 82% | 5 (6) |
| Essay 2, sample 3 | 64% | 4 |

Mean raw 67%. Mode band 4. The skill ran about one band low on NCBE MPTs and one to two bands low on state-drafted essays.

Spot-check of the worst case (Essay 1, sample 3): the grader's criticisms were accurate. The answer used cost instead of contract price for expectation damages, stacked reliance on expectation, and framed breach as promissory estoppel. The examiner still scored it high. Conclusion: real graders set the top of the scale at the best paper in the pile, which contains errors; a drafted rubric set it at a perfect answer.

### Changes made in response
1. Separate band column for drafted rubrics: 6 ≥ 75, 5 ≥ 58, 4 ≥ 42, 3 ≥ 28, 2 ≥ 14.
2. Drafted rubrics must target a strong timed answer, not a perfect one.
3. New tie-breakers: misnamed doctrine with sound reasoning = Substantial; weaker-but-legitimate theory = Substantial; correct measure with arithmetic slip = Substantial; flagged assumptions acceptable.
4. Guidance for advocacy calls, numeric calls, and state-drafted essays.
5. MPT: File-based rules count as authorities; scoping instructions are gatekeeping; close calls with no official answer accept either reasoned conclusion.
6. Multiple-answers section rewritten with a ranking template and a rule for when bands may differ.

### After recalibration (reruns, same grader model, blind)
Because of an edit error, the reruns used the new rubric-building guidance and tie-breakers but the OLD single band table. That isolates the two effects.

| Item | Raw before → after | Band on old table | Band on drafted table (now in SKILL.md) |
|---|---|---|---|
| Essay 1, sample 3 | 43% → 45% | 3 | 4 |
| MPT-1, sample 1 | 72% → 76% | 5 | 6 |
| Essay 2, sample 2 | 82% → 75% | 5 | 6 |

Observations:
- The guidance changes moved raw scores only a few points. The band-table shift does most of the correction.
- Run-to-run noise on the same answer with the same skill is about ±5 raw points (Essay 2 sample 2 fell 7 points between runs). Treat a single grade as ±1 band.
- Essay 1 sample 3 remains the outlier at band 4. Its errors are real (wrong damages measure, stacked remedies, promissory estoppel as breach theory). The skill was not bent further to rescue it; a 4 with accurate feedback is a more useful result for a learner than a 6 that hides the errors.
- Two reruns independently reported the missing drafted table as a "dangling reference," which is how the edit error was caught. Sonnet's friction reports are a reliable check on the skill's internal consistency.

## Benchmark set 2: real-score ladders + NY/CO/GA holdout (2026-11-08)

### Data
- **Score ladders (development set).** Two Seperac grading reports, each containing the NCBE question, the NCBE analysis or point sheet, and 10 real graded answers scored 1 through 10 on Seperac's 0-10 UBE-equivalent scale: F19 MEE 1 (Torts: negligence, proximate cause, res ipsa, joint and several liability) and F10 MPT 1 (State v. McLain: persuasive brief, suppression and lesser-included-offense motions). The low and middle scores are examinee-reported actual scores; the top three or four on each ladder are released state answers. Official-rubric path.
- **Holdout.** 7 New York BOLE answers that "received scores superior to the average" (Feb 2024, Feb 2025, July 2025; MEE and MPT); 7 Georgia Feb 2026 high-scoring answers; Colorado applicant 278's two Feb 2025 MPTs (score unknown). Drafted-rubric path.
- Conversion of 0-10 to bands uses Seperac's own 0-6 legend: 10→6, 8→5, 7→4, 5→3, 3→2, 2→1 (intermediate values interpolated).
- Every grade was blind: opaque file names, no score information in any file the grader could read, one fresh Sonnet grader per answer.

### Iterations
| Version | Change | Pooled rank corr. | MEE bias / MAE | MPT bias / MAE | Notes |
|---|---|---|---|---|---|
| baseline | (skill at commit 4ffb54d) | 0.78 | +0.2 / 0.9 | −0.5 / 0.7 | MEE compressed to the middle; strong answers scored low; "Partial" covered both real-9 and real-2 answers |
| v2 | Four-component credit; grade to strong timed answer, not official depth | 0.86 | +0.9 / 1.0 | +0.6 / 1.1 | Fixed the top; inflated weak answers (real-1 MPT went 11% → 53%) because naming the issue + stating the conclusion earned 0.35 per Point |
| v3 | Application weighted 0.50; analysis gate; MPT issue-spotting worth 0 | 0.76 | +0.5 / 0.7 | +0.1 / 0.9 | Weak answers fixed; MPT noisy because graders chose different row structures (2 rows vs 5) and gate punished rule-heavy answers |
| **v4** | Rule and Application **counted against Step 1 checklists**; fixed row rule; MPT gate 0.40 | **0.86** | **0.0 / 0.7** | **−0.1 / 0.9** | Adopted |

### Run-to-run noise (v4)
The MPT ladder was graded twice by independent graders. Mean absolute difference 3.3 raw points (max 8.2); band agreement 10/10. Under impression-based scoring (baseline through v3) the same answers swung 15-25 raw points between runs. Checklist counting is the main reason v4 is usable for a single grade.

### Holdout (v4, drafted path)
- New York above-average: 7/7 at band 5-6 (expected ≥ 4).
- Georgia high-score: 5/7 at band 5-6, 2/7 at band 4 (one of the 4s is the answer with real doctrinal errors noted in benchmark set 1). Round 1 had 1/7 at 5-6.
- Colorado 278: MPT-1 band 5 (range 4-5), MPT-2 band 5 (range 5-6). Consistent with earlier runs.

### Cutoffs
Band cutoffs were deliberately not tuned on the ladders: with near-zero bias on both item types, fitting cutoffs to 20 answers would overfit. The official and drafted tables are unchanged from benchmark set 1.

### Limits
- One MEE item and one MPT item with real scores. Rank correlation of about 0.87 is in the range reported for agreement between trained human graders on essays, but this is one subject each.
- The released-state answers at the top of each ladder carry Seperac's assigned scores, which may be less exact than the examinee-reported ones.
- No real-score data yet for weak answers on the drafted path.

## Benchmark set 0: synthetic MEE answer (2026-11-08)
One answer written by the skill's author to July 2026 MEE Question 1 (Criminal Law and Procedure), with the official analysis supplied. Author predicted 62% / band 4; grader returned 62% / band 4. This confirms the skill is applied consistently, not that the official-rubric band map matches real graders. The official column remains unvalidated.

## Open questions
- More real-score ladders in other subjects, especially an MPT objective memo and an MEE with a remedy-heavy call.
- Weak answers on the drafted path (no official material).
- Georgia's "high score" is a threshold, not a rank. Some of these answers may be 5s rather than 6s in a UBE pool.
