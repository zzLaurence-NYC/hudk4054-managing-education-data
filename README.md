# AI Prompting Behaviors and Academic Performance in Engineering Education

Metadata documentation and a reproducible data audit for HUDK 4054, Managing Education Data.

**Project author:** Zhicheng Zhao  
**ORCID:** [0009-0003-8291-0277](https://orcid.org/0009-0003-8291-0277)  
**Institution:** Teachers College, Columbia University  
**Documentation date:** October 1, 2026  
**Original dataset DOI:** [10.5281/zenodo.15871671](https://doi.org/10.5281/zenodo.15871671)

This is a secondary-use documentation project. The original dataset was produced by the researchers credited in the Zenodo record. The linked DOI identifies their dataset; this documentation project has not been assigned a separate DOI.

## Project overview

The project prepares an existing engineering-education dataset for transparent reuse in learning analytics. The proposed research question is: How are students' AI prompting behaviors and reliance on AI output associated with weekly assignment performance? A longer-term interest is whether AI-assisted learning behaviors reflect capability formation beyond successful task completion.

The completed work here is a file audit and metadata documentation. No effect estimates, predictive models or causal conclusions are reported. Measures of writing and AI-assisted problem solving are treated as capability proxies, not established measures of independent ability.

## Data and file overview

Download the original workbook from the [Zenodo record](https://zenodo.org/records/15871671). Its filename is `An Empirical Study of ChatGPT-4o Use in Engineering Education Prompting and Performance.xlsx`. The record page labels the release v2, published July 12, 2025. The audited workbook matches its published MD5 checksum: `cc90ed86843cff4eb8ab71760e049802`.

| Property | Audited result |
|---|---|
| Format | Excel `.xlsx`; 146,887 bytes |
| Sheet and occupied range | `Sheet1!A1:Q2049` |
| Header and observations | One header row; 2,048 data rows |
| Variables | 17 |
| Participants and coverage | 128 distinct student IDs; each has all 16 weeks |
| Unit of observation | Student-week record, including absent weeks |
| Candidate key | `Student ID` + `Week`; no duplicate combinations |
| Attendance | 1,866 present records; 182 absent records |
| Workbook structure | No hidden sheets/rows/columns, merged cells or formulas found |

The participant counts by file label are: Systems Engineering 22, Electronic Engineering 42, Processes Engineering 28, and Environmental Engineering 36. Each student belongs to one file-level course category. The workbook contains computed metrics and grades; it does not contain raw prompts, AI responses, timestamps or full submitted texts.

| Project file | Contents |
|---|---|
| [data_dictionary.csv](data_dictionary.csv) | All 17 variables, units, source definitions, observed ranges, missingness, derivation evidence and unresolved questions |
| [variable_profile.csv](variable_profile.csv) | Reproducible column-level descriptive checks |
| [audit_checklist.csv](audit_checklist.csv) | Executed checks and outstanding verification |
| [audit_issues.csv](audit_issues.csv) | Source row locations for issues; no copied student records |
| [METRIC_NOTES.md](METRIC_NOTES.md) | Code formulas and discrepancies requiring verification |
| [audit.py](audit.py) | Read-only audit script; new run outputs go to `audit_results/` |
| [requirements.txt](requirements.txt) | Versions used for the audit |
| [provenance.json](provenance.json) | Source hashes, metadata and code revision |
| [REFLECTIONS.md](REFLECTIONS.md) | Responses to the assignment's three reflection questions |

## Sharing, access and attribution

Zenodo provides open access. Its [machine-readable metadata](https://zenodo.org/api/records/15871671) records the dataset license as **CC BY 4.0**. This repository links to the source instead of redistributing the workbook. The original study code is separately available in the [authors' GitHub repository](https://github.com/lisaza88/An-Empirical-Research-Study-of-ChatGPT-4o-Use-in-Engineering-Education); a dataset license should not be assumed to license unrelated repository code.

The source describes the identifiers as anonymized. Reuse should retain source attribution and should not attempt to identify participants. Dataset questions should be directed through the original repository/record. Questions about this secondary documentation can be raised through the project repository after publication.

**Dataset citation:** Isaza Dominguez, L. G. (2025). *Python Code and Dataset for An Empirical Study of ChatGPT-4o Use in Engineering Education: Prompting and Performance* (v2) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.15871671

The creator is credited as listed in Zenodo; its separate contributor entries are retained in the source record. No new dataset authorship or DOI is claimed.

## Methodological information

### Original study context

The [published paper](https://doi.org/10.1016/j.iheduc.2026.101105) describes 128 fourth-year engineering students and 16 weekly sessions, with rotating task types and assigned AI access. The workbook supports the student/week counts. This audit did not independently validate recruitment, consent procedures, grading rubrics, randomization implementation or the study's inferential results. The exact calendar schedule, demographics and original assignment schedule are not recoverable from these 17 columns.

The current source-code export routine constructs `AI Access` from attendance and the presence of a student/session metric record. Consequently, the exported field cannot automatically be equated with the original randomized assignment. The inspected code revision also differs from the workbook in missing-value handling. See [metric verification notes](METRIC_NOTES.md).

### Audit and processing performed

1. Read workbook structure and physical cell values without saving changes to the source.
2. Profile types, distinct values, ranges and physical blanks; distinguish identifier repetition from duplicate observations.
3. Test student-week uniqueness, full week coverage, binary codes and the documented assignment-grade range.
4. Cross-tabulate attendance and access, then compare each metric's missingness and zero patterns with those conditions.
5. Flag cross-field inconsistencies and inspect relevant author code; retain records and unresolved version differences.
6. Export documentation and audit results to separate files; verify the source SHA-256 remained unchanged.

No rows were removed, no values were imputed, and no original column names were changed. Suggested analysis names in the dictionary are optional aliases only. Blank values are read by pandas as `NaN`; they are actual empty source cells in the columns reported below. Numeric nonmissing values happen to be integers in this release, even when pandas uses `float64` to accommodate missingness.

### Data quality findings

| Check | Result and interpretation |
|---|---|
| Exact duplicate rows / duplicate student-week keys | 0 / 0 |
| Week and binary codes | All weeks in 1-16; Attendance and AI Access in 0/1 |
| Assignment grades | Nonmissing values in 20-100, within the documented 0-100 grade scale |
| Access/query inconsistency | 20 records have `AI Access=0` and positive query counts |
| Attendance/query inconsistency | Four of those 20 records also have `Attendance=0` |
| Query-efficiency formula diagnostic | Using exported depth/count: 107/936 access records match exactly; 31 differ by more than 0.5 |
| Pipeline equivalence | Not established; raw texts, component scores and release-specific processing are missing |

These are verification flags, not a basis for silently correcting a field or removing a participant. Range validity is not evidence of real-world accuracy.

### Missing values and zero values

| Condition | Records | Observed pattern |
|---|---:|---|
| Present, AI access | 936 | All 17 fields populated |
| Present, no AI access | 930 | Reliance, refinement and AI response complexity blank |
| Absent, no AI access | 182 | Those three fields plus assignment grade, structural complexity and content richness blank |

The three access-related fields each have 1,112 blanks (54.30%). Assignment Score, Structural Complexity Score and Content Richness Score each have 182 blanks (8.89%). Query Depth, Query Efficiency, Response Utility and AI-Driven Problem-Solving are zero in all 1,112 no-access records.

These patterns suggest condition-dependent non-applicability, but the exact coding policy needs source confirmation. Do not convert all blanks to zero or delete every row with any missing value. Such deletion would retain only AI-access observations. Any later analysis must define the applicable population and document its missing-data treatment separately.

## Data-specific information

The table below is a compact dictionary. Ranges are **observed**, not theoretical scale limits. Source-based definitions, full category labels, code formulas and field-specific uncertainties are in [data_dictionary.csv](data_dictionary.csv). Missing counts refer to physical blanks. The `AI Access` and `Attendance` codes are 0=no/absent and 1=yes/present.

| Original variable | Working definition | Observed range or categories | Missing | Proposed research role |
|---|---|---|---:|---|
| Student ID | Anonymized participant identifier. | 128 distinct identifiers; 16 records per identifier | 0 | Identifier |
| Course | Engineering course/program label. | Systems Engineering; Electronic Engineering; Processes Engineering; Environmental Engineering | 0 | Controls / design context |
| Week | Teaching week. | 1-16 | 0 | Controls / design context |
| Attendance | Recorded attendance. | 0-1 | 0 | Controls / selection context |
| AI Access | Recorded ChatGPT-4o access status. | 0-1 | 0 | AI exposure |
| Activity Type | Weekly task category. | Case Study Analysis; Engineering Design Report; Multi-Step Engineering Problem-Solving; Experimental Data Analysis | 0 | Controls / design context |
| AI Query Count | Recorded number of prompts. | 0-38 | 0 | AI behavior |
| AI Response Reliance Score | Composite association of AI output with submitted work. | 0-100 | 1112 | AI reliance |
| Assignment Score | Weekly assignment grade. | 20-100 | 182 | Outcome |
| AI Query Depth & Structure Score | Composite prompt depth and structure. | 0-100 | 0 | AI behavior |
| AI Query Efficiency Score | Prompt depth relative to number of prompts. | 0-50 | 0 | AI behavior |
| Prompt Refinement Depth Score | Prompt revision metric based on selected adjacent prompts. | 11-81 | 1112 | AI behavior |
| AI Response Complexity Score | Linguistic/syntactic complexity of AI responses. | 10-94 | 1112 | AI behavior / interaction context |
| AI Response Utility Score | Composite AI-response utility/integration metric. | 0-100 | 0 | AI behavior / interaction context |
| AI-Driven Problem-Solving Score | Composite use of AI content in a solution. | 0-76 | 0 | Capability proxy |
| Structural Complexity Score | Structural features of submitted writing. | 30-90 | 182 | Capability proxy |
| Content Richness Score | Lexical diversity and density of submitted writing. | 29-90 | 182 | Capability proxy |

The definitions use the [Zenodo dataset notes](https://zenodo.org/records/15871671) and the individually linked author-code modules in the dictionary. Their correspondence to the exact workbook-generation pipeline is not assumed.

### Research framework and interpretation

The proposed framework is **AI exposure → AI behavior / reliance → capability proxies → performance outcomes**. `AI Access` measures exposure as recorded in the export. Prompt count, depth, efficiency and refinement describe behavior. Response complexity describes the AI output; utility mixes response and student-integration information. Reliance is a composite association measure, not a diagnosis of dependence or a plagiarism determination.

Problem-solving and writing scores are provisional capability proxies. `Assignment Score` is the weekly outcome. Course, Week and Activity Type describe study context; Attendance describes participation and potential selection. Student ID identifies repeated observations and should not be treated as an ordinary numeric predictor.

Tasks repeat in a fixed four-week cycle: Case Study Analysis, Engineering Design Report, Multi-Step Engineering Problem-Solving, Experimental Data Analysis. Each task occurs in 512 records. Week determines Activity Type, so including unrestricted week categories and activity categories together creates redundant information. Students also contribute repeated observations; 2,048 records are not 2,048 independent participants.

This file does not measure delayed retention, transfer to a novel task, employment, opportunities or social mobility. It contains no age or CGPA field. AI-assisted writing quality cannot by itself establish independent capability formation. Proposed associations should not be presented as causal effects of prompting strategy.

## Metadata standard

This project selects **Data Documentation Initiative (DDI), using the DDI-Codebook documentation model**. It fits a study with participant-level repeated records and derived behavioral variables because it organizes study identity, provenance, access, methods, file structure and variable descriptions. [DDI-Codebook documentation](https://ddialliance.org/ddi-codebook)

| DDI documentation level | Implementation here |
|---|---|
| Study identification and provenance | Project overview, original creator citation, source DOI and hashes |
| Methods and access | Study context, audit procedures, sharing and license information |
| Data-file description | Workbook, sheet, dimensions, observation unit and candidate key |
| Variable description and grouping | Dictionary with labels, representations, units, codes, missingness, derivation evidence and research roles |

This is a human-readable DDI-informed README and CSV dictionary. It is not a schema-validated DDI XML export.

## Reproducing the audit

Download the workbook from Zenodo and keep it outside the repository. From this project folder, use Python with the listed dependencies:

```bash
python -m pip install -r requirements.txt
python audit.py "/absolute/path/An Empirical Study of ChatGPT-4o Use in Engineering Education Prompting and Performance.xlsx"
```

The script writes to `audit_results/`, never to the input workbook. The expected MD5 is recorded above; the script also compares SHA-256 before and after reading. The packaged results correspond to the source hash in [provenance.json](provenance.json). Outputs from a different file/version should be treated as a new audit.

For an Excel check in a separate working copy, use `COUNTBLANK(H2:H2049)` (1,112), `COUNTIFS(E2:E2049,0,G2:G2049,">0")` (20), and `COUNTIFS(D2:D2049,0,G2:G2049,">0")` (4). To test the key, fill `COUNTIFS($A$2:$A$2049,A2,$C$2:$C$2049,C2)` down a helper column; every result should be 1.

## Outstanding verification

Before substantive modeling, resolve the 20 access/query flags; recover original assignment and attendance rules; establish the release-specific metric formulas, rounding and missing-value policies; verify the grading rubric; and obtain a defensible measure of independent capability if that becomes the target construct. These open items do not prevent documenting the file accurately, but they limit what can be inferred from it.
