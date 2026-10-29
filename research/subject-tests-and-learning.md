# Subject tests and learning-response datasets

Research date: **29 October 2026**. Scope: observed human skill/knowledge performance. These ten entries include fixed tests and learning platforms, which need different evaluation designs. No raw student data is intended for committing to the project; store links, provenance, schemas and conditions.

## Main findings

- **Start fixed-test scoring comparisons with fraction subtraction and ECPE**: small dense response matrices make the unit clear and let multiple scoring methods share the same observations. Neither contains ground-truth latent ability.
- **Use Eedi for distractor-aware scoring**: observed option choices and correct-answer keys make it unusually relevant. The official source specifies CC BY-NC-ND 4.0 and additional restrictions on question images; record metadata and links without republishing images or modified data.
- **Use ASSISTments 2009, Junyi and EdNet for learning-aware scoring**: account for repeated practice, feedback, selection and time before evaluating generalisation.
- **ASSISTments 2015 is often misdescribed**: the 100 identifiers are skill-builder sequences, not individual questions. This matters for any method claiming item calibration.
- **Separate access from reuse**: public downloads can have noncommercial licences or unresolved terms; package software licences do not automatically settle original test-content rights.

## Verification evidence

Raw-file verification means a complete small file was retrieved and structurally checked, not that every response was independently validated. Raw-sample verification means headers/first records or selected ZIP members were inspected. Page-verified entries were not downloaded successfully. No identifying profile data was analysed.

| Source | Direct observation in this run |
|---|---|
| Fraction subtraction | Full CSV: 536 rows, 20 columns, values only 0/1. |
| ECPE | Full JSON: 2,922 records; id plus 28 responses; Q-matrix has 28 rows. |
| ASSISTments 2009 corrected | Byte-range sample: item/template identifiers, correct, answer_text, ms_first_response, hints. |
| ASSISTments 2015 | Full 18,334,729-byte CSV: 708,631 rows; 19,917 users; 100 sequences; exactly four columns. |
| Junyi 2020 | Official Kaggle metadata and licence; full Info_Content: 1,330 rows; partial Log_Problem decompressed to inspect actual header. |
| EdNet | Full 173,976-byte Contents ZIP: 13,169 questions with correct_answer and bundle/tags. Large learner logs page-verified. |
| Eedi | HTTP-range ZIP inspection: task-3/4 training header contains selected answer and correct answer; question metadata has subject IDs; 948 question image filenames. |
| KDD Cup | First compressed master-file records decoded from official archive; correctness/timing/knowledge-component fields verified. |
| Duolingo | Official task schema and deposited DOI metadata inspected; Harvard download denied here. |
| DBE-KT22 | Authors' paper/schema and deposited DOI metadata inspected; ADA download denied by anti-bot service. |

## 1. Tatsuoka fraction subtraction (CDM)

**Best use:** high: compact fixed-test scoring benchmark. **Verification:** raw-file-verified: full CSV has 536 rows × 20 item columns and only 0/1; official package documentation checked.

Dense binary correctness matrix; separate item-by-skill Q-matrix. Population/scale: 536 students (raw-file verified). Content: 20 test items; 8 skill attributes. Timing: No

**Scoring:** 1=correct, 0=incorrect; responses already scored; no original selected-answer trace.

**Access:** Anonymous CSV export or CDM R package.

**Data terms:** CDM package GPL (>=2); separate original dataset grant was not identified. Record package distribution terms without assuming they settle all third-party data rights. **Item terms:** Published historical items; separate permission for reproducing item text not verified.

**Limits:** Historical, narrow curriculum sample; not population norms. Q-matrix is a modelling specification, not directly observed mastery. No option-level distractor responses or timing.

**Primary sources:** [source 1](https://raw.githubusercontent.com/alexanderrobitzsch/cdm/master/man/fraction.subtraction.data.Rd), [source 2](https://alexanderrobitzsch.r-universe.dev/CDM/data/fraction.subtraction.qmatrix/csv), [source 3](https://alexanderrobitzsch.r-universe.dev/CDM).

**Data route:** [download/landing](https://alexanderrobitzsch.r-universe.dev/CDM/data/fraction.subtraction.data/csv).

## 2. ECPE English grammar section (CDM)

**Best use:** high: fixed-test multidimensional scoring comparison. **Verification:** raw-file-verified: full JSON contains data (2,922 records, id plus E1–E28) and q.matrix (28 records).

Dense scored binary response matrix and 28×3 Q-matrix. Population/scale: 2,922 examinees (raw-file verified). Content: 28 grammar items; not the complete ECPE exam. Timing: No

**Scoring:** Binary correctness; remove the id column before scoring.

**Access:** Anonymous JSON export or data.ecpe in CDM.

**Data terms:** CDM package GPL (>=2); original ECPE response-data licence not separately verified. **Item terms:** Full ECPE test content is not supplied by this response export; no item republication grant verified.

**Limits:** Only one section of an English proficiency exam. No raw option choices, response times, or criterion proficiency scores in this object. Estimated diagnostic classes do not constitute ground-truth skill labels.

**Primary sources:** [source 1](https://raw.githubusercontent.com/alexanderrobitzsch/cdm/master/man/data.ecpe.Rd), [source 2](https://alexanderrobitzsch.r-universe.dev/CDM).

**Data route:** [download/landing](https://alexanderrobitzsch.r-universe.dev/CDM/data/data.ecpe/json).

## 3. ASSISTments 2009–2010 corrected collapsed Skill Builder

**Best use:** high: learning-aware scoring and timing; medium for fixed ability. **Verification:** raw-sample-verified: corrected CSV header and first records inspected, not complete row counts.

Longitudinal scored problems, skill tags, hints/attempt counts, response text and timing fields. Population/scale: Not recounted for the corrected collapsed release; published counts for other preprocessing variants should not be substituted. Content: Problem and template identifiers present; exact corrected-release unique count not recounted. Timing: ms_first_response and overlap_time present in raw header.

**Scoring:** correct plus attempt/hint indicators; tutoring or hints can make a response incorrect under Skill Builder rules.

**Access:** Official Google Sites links corrected collapsed CSV on Google Drive; anonymous byte-range sample succeeded.

**Data terms:** Official parent page states free to use and asks for precise source citation; no standard licence found. **Item terms:** No separate grant for reproducing exercise content verified.

**Limits:** Use the corrected collapsed version: original files duplicate records for multi-skill questions. Mastery stopping, feedback and repeated practice make a naive fixed-ability analysis inappropriate. response text is not itself an item bank or verified answer key.

**Primary sources:** [source 1](https://sites.google.com/site/assistmentsdata/home/2009-2010-assistment-data/skill-builder-data-2009-2010), [source 2](https://sites.google.com/site/assistmentsdata/home/2009-2010-assistment-data), [source 3](https://sites.google.com/site/assistmentsdata/an-explanation-on-how-to-interpret-our-data-sets).

**Data route:** [download/landing](https://drive.google.com/file/d/1NNXHFRxcArrU0ZJSb9BIL56vmUt5FhlE/view?usp=sharing).

## 4. ASSISTments 2015 top-100 Skill Builders

**Best use:** low for item scoring; medium for skill-level knowledge tracing. **Verification:** raw-file-verified: full CSV row count, unique user/sequence counts, and columns checked.

Four columns only: user_id, log_id, sequence_id, correct. Population/scale: 19,917 users; 708,631 rows (raw-file verified). Content: 100 sequence_id values (skill builders), not 100 distinct test questions. Timing: No timing column.

**Scoring:** Binary correct label.

**Access:** Official Google Sites → Google Drive CSV; full 18,334,729-byte CSV retrieved anonymously for structural verification.

**Data terms:** No release-specific standard licence found; do not infer an explicit redistribution grant from download availability. **Item terms:** Item text is absent.

**Limits:** No question identifier: not suitable for calibrating actual individual items. No timestamps, response options, keys, question text, or response times in this file. Treating sequence_id as item_id changes the scientific unit.

**Primary sources:** [source 1](https://sites.google.com/site/assistmentsdata/datasets/2015-assistments-skill-builder-data).

**Data route:** [download/landing](https://drive.google.com/file/d/0B_hO8cnpcIMgUGZzRnh3bHJrSjQ/view?usp=sharing).

## 5. Junyi Academy Online Learning Activity Dataset (2020 release; 2018–2019 logs)

**Best use:** high for longitudinal skill modelling. **Verification:** metadata- and raw-sample-verified: official Kaggle API licence/card; full Info_Content (1,330 rows), Log_Problem header and first decompressed records inspected.

Log_Problem.csv with uuid, ucid, upid, correctness, time, attempts, hints and level transitions; content/user tables. Population/scale: Official card: 16,217,311 attempts by 72,630 selected students; not independently recounted. Content: 1,330 exercise/content metadata rows raw-file verified; unique problem upid count not recounted. Timing: total_sec_taken; timestamp_TW also present.

**Scoring:** is_correct plus attempt/hint indicators; chosen raw answers and an answer key are absent from inspected schema.

**Access:** Official Kaggle page and API; anonymous individual-file API requests worked during verification (large Log_Problem is compressed).

**Data terms:** CC BY-NC-SA 4.0 in uploader data card and Kaggle API metadata, with additional source policy text. **Item terms:** Content metadata supplied; separate rights to full online problems should not be inferred.

**Limits:** Distinct from the legacy 2015 Junyi dataset with about 25.9 million logs; schemas and counts must not be combined. An exercise is a group of problems, not a single item. Adaptive practice and repeated attempts require longitudinal evaluation.

**Primary sources:** [source 1](https://www.kaggle.com/datasets/junyiacademy/learning-activity-public-dataset-by-junyi-academy), [source 2](https://www.kaggle.com/api/v1/datasets/view/junyiacademy/learning-activity-public-dataset-by-junyi-academy), [source 3](https://www.kaggle.com/api/v1/datasets/download/junyiacademy/learning-activity-public-dataset-by-junyi-academy/Info_Content.csv), [source 4](https://www.kaggle.com/api/v1/datasets/download/junyiacademy/learning-activity-public-dataset-by-junyi-academy/Log_Problem.csv).

**Data route:** [download/landing](https://www.kaggle.com/api/v1/datasets/download/junyiacademy/learning-activity-public-dataset-by-junyi-academy).

## 6. EdNet KT1–KT4 (Santa English test preparation)

**Best use:** high for option-based longitudinal scoring and speed/accuracy studies. **Verification:** raw-metadata-verified: full Contents ZIP and question CSV; log schema/examples and archive links page-verified.

KT1 question-solving logs; KT2 answer-selection actions; KT3 explanations/lectures; KT4 wider actions. Population/scale: KT1: 784,309 per-student files; approximately 131 million actions refers to the broad dataset, not KT1 answer rows. Content: 13,169 keyed question metadata rows (raw-file verified). Timing: KT1 elapsed_time in milliseconds; bundle timing can be shared across associated questions; shifted timestamps.

**Scoring:** Join user_answer (a–d) to Contents correct_answer; bundles identify shared stimuli.

**Access:** Public author GitHub links Google Drive ZIPs; Contents archive retrieved, full multi-GB KT archives not downloaded.

**Data terms:** CC BY-NC 4.0, stated by authors for research purposes. **Item terms:** Released Contents includes keys/tags/IDs, not question text, passages or audio; no right to reproduce unreleased materials inferred.

**Limits:** High-level actions are not all test responses. Learning, recommendation policy, review and response revisions affect scores. No released external TOEIC score criterion: README still labels scores as to be released.

**Primary sources:** [source 1](https://github.com/riiid/ednet), [source 2](https://bit.ly/ednet-content), [source 3](https://arxiv.org/abs/1912.03072).

**Data route:** [download/landing](https://bit.ly/ednet_kt1).

## 7. Eedi / NeurIPS 2020 Education Challenge

**Best use:** high for noncommercial distractor-aware scoring within source terms; do not redistribute modified data or question images. **Verification:** raw-sample-verified: ZIP directory, tasks 1/2 and 3/4 training headers and answer metadata; question metadata and official counts also checked. Official licence and additional image restrictions directly verified (page lines 52–56).

QuestionId/UserId/AnswerId with IsCorrect, CorrectAnswer, AnswerValue; subject and answer metadata. Population/scale: Official training counts: tasks 1/2 118,971 students and 15,867,850 answers; tasks 3/4 4,918 students and 1,382,727 answers. Content: 27,613 questions (tasks 1/2); 948 (tasks 3/4), with images supplied for the smaller set. Timing: Inspected answer metadata has DateAnswered and Confidence but no duration field; DateAnswered is a timestamp, not response time.

**Scoring:** CorrectAnswer and selected AnswerValue support rescoring and distractor models; IsCorrect is provided.

**Access:** Current Eedi research page links a 626 MB ZIP on Azure; anonymous HTTP byte-range access and ZIP members verified.

**Data terms:** CC BY-NC-ND 4.0 is explicitly stated on the official Eedi challenge page: noncommercial use, attribution with a licence link, and no distribution of modified material. **Item terms:** The official source restricts question images to model training and prohibits all other uses, printing and sharing with anyone.

**Limits:** Sparse, selected educational sample, not a common complete test. Task splits differ in people/items/metadata; preserve their identities. Training counts differ from totals that include challenge answers. Only the latest student-question answer is retained. Tasks 1/2 and tasks 3/4 have separately anonymised question/user/answer IDs; do not cross-join matching numeric IDs across the task pairs. See the [official guide](https://arxiv.org/html/2007.12061v3).

**Primary sources:** [source 1](https://www.eedischool.com/projects/neurips-education-challenge), [source 2](https://www.eedischool.com/research), [source 3](https://arxiv.org/abs/2007.12061), [source 4](https://dqanonymousdata.blob.core.windows.net/neurips-public/data.zip).

**Data route:** [download/landing](https://dqanonymousdata.blob.core.windows.net/neurips-public/data.zip).

## 8. Duolingo SLAM 2018 shared-task learner responses

**Best use:** medium: language learning/error prediction rather than a fixed proficiency test. **Verification:** page- and DOI-metadata-verified; full data files not inspected due Harvard access denial.

Token correctness/error labels, correct-answer tokens, user/session and exercise metadata across three language tracks. Population/scale: Initial release: >2 million annotated tokens, >6,000 learners, first 30 days (use version-specific counts). Content: No fixed common item count; tracks en_es, es_en and fr_en. Timing: Whole-exercise seconds; some null/negative logging values need cleaning.

**Scoring:** 0=OK and 1=mistake; this is reversed from ordinary correct=1 coding.

**Access:** Official shared-task page links Harvard Dataverse DOI; primary page/API were blocked in this runtime, but DataCite deposited metadata was readable.

**Data terms:** CC BY-NC 4.0 explicitly stated in author-deposited DataCite description; Dataverse also records custom terms. **Item terms:** Do not infer a licence for the entire Duolingo curriculum beyond the released corpus.

**Limits:** Original challenge version provides labels rather than actual learner strings. Most sessions are lessons/practice; only about 1% are test sessions. Tokens in one exercise are dependent and share a duration; inspect current version and label files before analysis.

**Primary sources:** [source 1](https://sharedtask.duolingo.com/2018.html), [source 2](https://api.datacite.org/dois/10.7910/DVN/8SWHNO), [source 3](https://research.duolingo.com/).

**Data route:** [download/landing](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/8SWHNO).

## 9. KDD Cup 2010 Algebra I / Bridge to Algebra

**Best use:** medium: process/learning-aware scoring. **Verification:** raw-sample-verified: official ZIP first member algebra_2005_2006_master.txt and tab-delimited header/records inspected.

Step-level correctness, attempts/hints, timing, knowledge components and opportunity counts. Population/scale: Development sets: Algebra 2005–06 575 students/813,661 steps; Algebra 2006–07 1,840/2,289,726; Bridge 2006–07 1,146/3,656,871 (official table). Content: Steps nested in problems; not a fixed common test. Unique item counts not asserted. Timing: Step duration, first transaction, correct transaction and related timestamp columns.

**Scoring:** Correct First Attempt (1/0); development master files provide labels for all steps.

**Access:** Official SIGKDD archive index serves ZIPs anonymously, despite historical competition rules mentioning registration.

**Data terms:** No explicit standard reusable-data licence found; competition availability is not an unrestricted redistribution grant. **Item terms:** No independent grant for Cognitive Tutor item content verified.

**Limits:** One opportunity summarises several attempts, not a single independent response. Mastery, curriculum ordering, hints and repeated steps complicate fixed-trait models. Several challenge test columns are withheld; use labelled master files when evaluating observed correctness.

**Primary sources:** [source 1](https://kdd.org/kdd-cup/view/kdd-cup-2010-student-performance-evaluation/Data), [source 2](https://kdd.org/cupfiles/), [source 3](https://kdd.org/kdd-cup/view/kdd-cup-2010-student-performance-evaluation/Rules).

**Data route:** [download/landing](https://kdd.org/cupfiles/algebra_2005_2006.zip).

## 10. Database Exercises for Knowledge Tracing (DBE-KT22)

**Best use:** high candidate once access and custom terms are resolved. **Verification:** paper- and DOI-metadata-verified; source data unavailable to this runtime.

Correctness, timing, hints, answer revisions, question text/choices, expert difficulty and question/concept relationships. Population/scale: Paper reports 1,361 students and 167,222 interactions; not independently recounted. Content: 212 questions, 98 knowledge components (paper). Timing: time_taken in seconds; number of answer changes also documented.

**Scoring:** Generated practice_sequences.json answers are binary (0=wrong, 1=correct). Question-choice text is documented, but retention of each learner’s selected option in the released raw records remains unverified because source files were inaccessible; do not claim option-level rescoring. Optional confidence/difficulty ratings are ancillary.

**Access:** Authors describe unrestricted ADA access, but current landing/API returned an anti-bot Access Denied page in this runtime.

**Data terms:** DataCite registers custom dataset terms, including required citation/acknowledgement; full custom licence could not be inspected. Do not apply the paper CC BY 4.0 licence to the dataset. **Item terms:** Question/choice text documented as included; exact item redistribution conditions unresolved with dataset terms.

**Limits:** Practice, hints and optional feedback rather than a fixed independent examination. Actual download and complete data-use terms remain an access-verification task. Expert difficulty is a rating, not a known true latent ability.

**Primary sources:** [source 1](https://arxiv.org/html/2208.12651v3), [source 2](https://api.datacite.org/dois/10.26193/6DZWOH), [source 3](https://dataverse.ada.edu.au/dataset.xhtml?persistentId=doi:10.26193/6DZWOH).

**Data route:** [download/landing](https://dataverse.ada.edu.au/dataset.xhtml?persistentId=doi:10.26193/6DZWOH).

## Exclusions and traps

- **CDM::data.dtmr** is explicitly **simulated**. Its name refers to a real study of teachers' rational-number understanding, but the packaged 5,000×27 matrix is not a sample of observed teachers. [Maintainer documentation](https://raw.githubusercontent.com/alexanderrobitzsch/cdm/master/man/data.dtmr.Rd).
- **Simulated-5** in knowledge-tracing literature is synthetic; keep it separate from empirical performance data.
- A platform interaction count can include opening explanations, changing answers, media playback and purchases. EdNet's total action count must not be relabelled as the number of scored questions.
- Legacy Junyi and the 2020 Kaggle release use different populations, identifiers and tables. In particular, the inspected 2020 content table has hierarchical level IDs; a legacy prerequisite graph should not silently be attached to it.
- A binary scored matrix supports rescoring only at the correctness level. A new scoring rule that needs distractors, partial work, confidence or response time requires those actual fields.

## Evaluation design for the project

For a fixed-test score, first use one response per person-item and compare with sum score, Rasch/2PL and suitable multidimensional models. For practice logs, define whether a score estimates initial knowledge, current knowledge or learning gain; hold out later events and whole learners as appropriate. Fit item statistics and all normalisation parameters using training data only. Do not use final-course outcomes, future attempts, hints or time measured after the prediction target as input features.

For all sources, retain the original data version, file checksum, response coding and missing-value conventions. Keep omission, wrong answer, not-administered and not-reached separate when the source distinguishes them. A Q-matrix is expert annotation; an estimated ability or diagnostic classification is model output. Neither is a directly observed gold-standard trait.
