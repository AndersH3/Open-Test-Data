# Project field guide: English C-Test study

This is a project-written codebook/navigation guide based on the actual archived CSV headers and author README. It is **not an original author codebook**. Source documentation: https://github.com/UKPLab/arxiv2024-constrained-ctest-generation and https://tudatalib.ulb.tu-darmstadt.de/handle/tudatalib/4205.

## Original archive tables

All CSVs reside in `User Study Data/csv/` inside the original ZIP.

| File | Verified rows | Fields and intended unit |
|---|---:|---|
| `ctest.csv` | 32 | `ctest_idx`, `ctest ` (trailing space in original header), `solution`, `plaintext`, `tokenized text`, `strategy, input text, and difficulty`: one administered C-Test form with content and keyed completions. |
| `ctest_user_mapping.csv` | 160 | `ctest_idx`, `user_idx`, `user_response`, `individual scores (1 correct, 0 incorrect)`, `total score`, `total time`, `perceived difficulty`, `score assessment`: one learner-form attempt. |
| `strategy.csv` | 8 | `strategy_idx`, `ctest_id1` through `ctest_id4`: form assignment/order. |
| `user.csv` | 40 | `user_idx`, `username (obfuscated)`, `consent`, `questionnaire`, `finished`, `strategy_idx`: anonymized study administration/assignment. |
| `questionnaire.csv` | 40 | `user_idx`, `cefr`, `years`, `frequency`, `Mother Tongue`, `Other Languages`, `Other Languages (detail)`: ancillary self-report/context, not tested ability. |

The archive also contains `aggregated_ctests/` versions with aggregate human error rates for each generated form. Do not substitute those aggregate rates for individual response patterns.

## Scoring and time

The individual-score field explicitly codes `1 correct, 0 incorrect` for gap-level judgments. Preserve observed response strings alongside their supplied gap scores. Twenty gaps share one passage/form, so they are dependent testlet observations. Total score and perceived difficulty are separate variables; the latter is self-report.

`total time` is a **whole-form duration**, not an item-response latency. The original web application's code calculates finish time minus start time using Python `datetime` and stores a duration; its display uses minutes/seconds. Source: https://github.com/UKPLab/arxiv2024-constrained-ctest-generation/blob/master/User%20Study/Interface/c_test/__init__.py. The stored CSV format is a duration string; preserve it and parse its units explicitly before analysis. No per-gap latency was established in the released CSV.

The 160 attempts by 40 users supply 3,200 gap observations. Preserve user and form IDs, assignment sequence and generation strategy when splitting or modeling. Do not interpret the 32 forms or 640 form-gap positions as independent populations, and do not combine repeated observations as if they came from unrelated people.
