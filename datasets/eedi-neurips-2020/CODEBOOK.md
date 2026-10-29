# Eedi field guide

Project-written factual guide to the original CSVs. Primary schema: https://arxiv.org/html/2007.12061v3 . The original provider did not bundle a separate codebook file in data.zip; the author guide is linked rather than copying a paper under uncertain document rights.

| File group / field | Meaning |
|---|---|
| train_task_1_2.csv; train_task_3_4.csv | Observed training responses for separate task pairs. |
| QuestionId | Anonymized question identifier, meaningful within its task pair. |
| UserId | Anonymized learner identifier, meaningful within its task pair. |
| AnswerId | Identifier linking an answer to answer metadata within its task pair. |
| IsCorrect | Source binary correctness label. |
| CorrectAnswer | Correct one of the four answer choices. |
| AnswerValue | Actual learner choice, preserving distractor information. |
| answer_metadata / DateAnswered | Answer date/time, not elapsed response duration. |
| answer_metadata / Confidence | Optional learner confidence; missingness is distinct from a measured zero. |
| GroupId, QuizId, SchemeOfWorkId | Contextual assignment identifiers supplied in answer metadata. |
| question_metadata / SubjectId | List of subject identifiers; join to subject metadata. |
| student_metadata | Anonymized demographic/premium-status metadata; no attempt should be made to reidentify people. |
| subject_metadata | Subject names and hierarchy. |
| test_data | Official public/private challenge partitions and released solution tables; their naming does not imply restricted download status. |

Only the latest response per learner-question pair is retained. The two task pairs have independent anonymization, so never cross-join their numeric IDs. The 948 task3/4 question images are excluded under the provider's additional condition. Shared numeric codes have meaning only in the original task partition. `DateAnswered` does not provide time-on-item. No selected-option prediction label should be inferred from IsCorrect alone; use the supplied AnswerValue/CorrectAnswer where present.

All retained CSV bytes remain unchanged. The acquisition manifest is authoritative for actual filenames, headers, counts and checksums; some official challenge files contain intentionally withheld answer columns.

`schema-headers.json` records actual source headers. The student metadata fields are UserId, Gender, DateOfBirth and PremiumPupil; these are ancillary metadata and are not test items. The subject table fields are SubjectId, Name, ParentId and Level. Some question-quality challenge files contain pairwise/ranking output columns; their detailed metric definitions must be obtained from the original author guide, and they must not be silently interpreted as student accuracy.
