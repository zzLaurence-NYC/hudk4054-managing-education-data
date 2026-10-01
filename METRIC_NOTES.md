# Metric verification and provenance notes

Reviewed October 1, 2026. Code links are pinned to repository revision `55bc4b2fc64cc946192a6c67e384c5c4c99e8350`, whose commit date is October 14, 2025. This revision is later than the July 2025 dataset release. It describes inspected code, not a proven reconstruction of the released workbook. No author scripts were executed.

## Verified code definitions

| Metric | Inspected computation | Source |
|---|---|---|
| Reliance | 0.40 text similarity + 0.10 copy-paste + 0.20 structural similarity + 0.20 prompt-response consistency + 0.10 query-submission link | [ARR](https://github.com/lisaza88/An-Empirical-Research-Study-of-ChatGPT-4o-Use-in-Engineering-Education/blob/55bc4b2fc64cc946192a6c67e384c5c4c99e8350/ARR%20-%20compute_ai_response_reliance) |
| Query depth | 0.35 lexical structure + 0.35 multistep depth + 0.30 focus clarity | [QD](https://github.com/lisaza88/An-Empirical-Research-Study-of-ChatGPT-4o-Use-in-Engineering-Education/blob/55bc4b2fc64cc946192a6c67e384c5c4c99e8350/QD%20-%20compute_query_depth) |
| Query efficiency | QD divided by nonempty prompt-block count, capped at 100; zero when count is zero | [QE](https://github.com/lisaza88/An-Empirical-Research-Study-of-ChatGPT-4o-Use-in-Engineering-Education/blob/55bc4b2fc64cc946192a6c67e384c5c4c99e8350/QE%20-%20compute_query_efficiency) |
| Prompt refinement | Mean Flesch-Kincaid grade change for adjacent prompts passing semantic/edit-similarity filters; floored at zero | [PRD](https://github.com/lisaza88/An-Empirical-Research-Study-of-ChatGPT-4o-Use-in-Engineering-Education/blob/55bc4b2fc64cc946192a6c67e384c5c4c99e8350/PRD%20-%20compute_prompt_refinement_depth) |
| Response utility | 0.45 semantic novelty + 0.40 conceptual transformation + 0.15 contribution to final response | [RU](https://github.com/lisaza88/An-Empirical-Research-Study-of-ChatGPT-4o-Use-in-Engineering-Education/blob/55bc4b2fc64cc946192a6c67e384c5c4c99e8350/RU%20-%20compute_response_utility) |
| Problem solving | 0.40 stepwise alignment + 0.40 conceptual application + 0.20 independent expansion | [PS](https://github.com/lisaza88/An-Empirical-Research-Study-of-ChatGPT-4o-Use-in-Engineering-Education/blob/55bc4b2fc64cc946192a6c67e384c5c4c99e8350/PS%20-%20compute_problem_solving_score) |
| Structural complexity | 0.40 sentence-length score + 0.60 grammatical-complexity score; both components capped at 100 | [SC](https://github.com/lisaza88/An-Empirical-Research-Study-of-ChatGPT-4o-Use-in-Engineering-Education/blob/55bc4b2fc64cc946192a6c67e384c5c4c99e8350/SC%20-%20compute_structural_complexity) |
| Content richness | 50 times type-token ratio + 50 times lexical density | [CR](https://github.com/lisaza88/An-Empirical-Research-Study-of-ChatGPT-4o-Use-in-Engineering-Education/blob/55bc4b2fc64cc946192a6c67e384c5c4c99e8350/CR%20-%20compute_content_richness) |

Each inspected metric module rounds its final output to two decimal places. This does not mean that every component was validated or that all formulas reproduce this workbook. The AI Response Complexity calculation was not verified.

## Export discrepancies

The [published export routine](https://github.com/lisaza88/An-Empirical-Research-Study-of-ChatGPT-4o-Use-in-Engineering-Education/blob/55bc4b2fc64cc946192a6c67e384c5c4c99e8350/Final%20Dataset%20-%20final_export_to_excel) assigns zero to unavailable metrics and absent students' grades. The workbook instead contains blanks for several such fields. It also contains four positive query counts on absent rows, while the inspected exporter sets absent-row query counts to zero.

The exporter defines access as presence in the metric lookup when attendance is 1, and zero otherwise. Thus access in this code is a derived availability indicator, not an untouched randomization schedule. The QD module writes `query_depth_score`, but the exporter reads `ai_query_depth_score`. No intermediate renaming step was established in this audit. These discrepancies require a version explanation or a fuller pipeline; they do not establish which workbook values are incorrect.

## Query-efficiency diagnostic

For the 936 access records, the audit computed `round(min(exported QD / exported Query Count, 100), 2)` and compared it with exported QE. There are 107 exact matches (tolerance 1e-9), 905 within 0.5 points, and 31 more than 0.5 points apart. The largest absolute difference is 0.67. A 0.5-point threshold is a diagnostic for nearest-integer rounding, not a published validity threshold.

The actual code counts nonempty raw prompt blocks and uses its intermediate QD value. Those inputs may differ from the integer values in this spreadsheet. Therefore this check flags unresolved precision/version alignment; it is not a full replication or proof of erroneous scores.

## Construct interpretation

RU incorporates student transformation and contribution, so it should not be described as pure intrinsic answer quality. Reliance includes multiple similarities and linkages, so a score of 60 does not establish that exactly 60% of a submission was copied. SC and CR quantify limited language features; they cannot independently establish conceptual correctness or transferable knowledge. The numeric scale for PRD in the inspected code is not a normalized 0-100 scale.

The absence of raw prompts, responses, assignments and component scores prevents independent metric recomputation. The final dictionary separates source definitions, observed values and unresolved measurement questions instead of filling these gaps with assumptions.
