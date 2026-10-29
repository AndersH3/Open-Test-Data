# Junyi 2020 field guide

This is a project-written codebook from the provider's dataset description and the exact original CSV headers. It is not an original-author codebook. The source ZIP supplies three CSVs and no standalone codebook. `schema-headers.json` records the header inspection; no participant example rows are copied here.

Primary description and terms: https://www.kaggle.com/datasets/junyiacademy/learning-activity-public-dataset-by-junyi-academy . Original file index: https://www.kaggle.com/api/v1/datasets/list/junyiacademy/learning-activity-public-dataset-by-junyi-academy .

## Log_Problem.csv - one problem-attempt summary

| Field | Interpretation and analysis caution |
|---|---|
| timestamp_TW | Source timestamp field. Preserve the original string; timezone/rounding should be checked against the provider before sub-minute timing analyses. |
| uuid | Anonymized learner ID; joins to Info_UserData. |
| ucid | Exercise/content ID; joins to Info_Content. An exercise contains multiple problems. |
| upid | Problem ID; distinguish from content ID. |
| problem_number | Source problem sequence/count field within practice; not a globally stable item ID. |
| exercise_problem_repeat_session | Source repeated-problem/session counter; retain without reinterpreting as an independent examinee. |
| is_correct | Platform-provided correctness indicator. Preserve source scoring; do not infer an original selected option or answer key. |
| total_sec_taken | Total seconds recorded for the problem attempt summary. It may cover more than one answer action. |
| total_attempt_cnt | Number of answer attempts recorded in the summary. |
| used_hint_cnt | Hint count. |
| is_hint_used | Indicator that hints were used. |
| is_downgrade | Platform level-change indicator, downward. |
| is_upgrade | Platform level-change indicator, upward. |
| level | Platform mastery/progression level code; not an error-free latent skill label. |

## Info_Content.csv - exercise/content metadata

| Fields | Meaning |
|---|---|
| ucid | Content key. |
| content_pretty_name | Human-readable content name. |
| content_kind | Source content type. |
| difficulty | Source difficulty metadata; not a calibrated item parameter inferred in this project. |
| subject, learning_stage | Subject and school-stage categories. |
| level1_id, level2_id, level3_id, level4_id | Content hierarchy identifiers; do not assume they form a prerequisite graph. |

## Info_UserData.csv - anonymized learner metadata

`uuid` is the join key. The remaining original fields are `gender`, `points`, `badges_cnt`, `first_login_date_TW`, `user_grade`, `user_city`, `has_teacher_cnt`, `is_self_coach`, `has_student_cnt`, `belongs_to_class_cnt`, and `has_class_cnt`. These are demographic/account/relationship metadata, not directly tested skills. The complete original headers are preserved in schema-headers.json. Provider-specific semantics for the relationship counts are not independently established; retain names/codes rather than inventing derived meanings. Do not attempt reidentification.

## Use notes

This 2020 release covers logs from August2018-July2019 and differs from the older Junyi knowledge-tracing corpus. Repeated attempts, feedback and adaptive progression require a learning-aware evaluation design. Split by learner and time as appropriate; do not use later upgrades or future history to predict earlier performance. No full problem wording, selected answers or answer-key bank is established by these CSVs.
