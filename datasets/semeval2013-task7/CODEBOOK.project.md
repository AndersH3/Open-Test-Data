# Project field guide: original SemEval 2013 Task 7 XML

This guide was written for Skill Data Atlas after inspecting the archive structure. It is **not an original author codebook** and does not redefine the official task. Original source and task specification: https://github.com/myrosia/semeval-2013-task7 and https://aclanthology.org/S13-2045/.

## Observation structure

Each XML file has a `question` root. Files are grouped first by corpus (`beetle` or `sciEntsBank`), then by training/evaluation partition and Core/Extra representation. A file holds question/reference material and one or more `studentAnswer` records. The archive also includes SciEntsBank reliability material, which is not another independent test split.

| XML component | Meaning / caution |
|---|---|
| `question` `id` | Question identifier, interpreted within its corpus/module. |
| `testSet` | Supplied partition identifier; preserve the official split. |
| `module`, `qtype`, `stype` | Author-supplied question/module metadata; use original task documentation for study-specific interpretation. |
| `questionText` | Question wording. |
| `referenceAnswers` / `referenceAnswer` | Reference response material. Some questions have several reference answers; do not duplicate learner records once per reference answer. |
| `studentAnswers` / `studentAnswer` | Learner answer records; textual content is observed learner language. |
| `studentAnswer` `id` | Source answer identifier, not a globally unique examinee ID. |
| `studentAnswer` `accuracy` | Nominal accuracy category described below. |
| `studentAnswer` `count`, `answerMatch` | Supplied supplementary attributes; do not treat them as performance scores without the original task specification. |

## Five-way accuracy labels

- `correct`: complete/correct response relative to the reference.
- `partially_correct_incomplete`: partly correct but incomplete.
- `contradictory`: contradicts the reference.
- `irrelevant`: domain content that does not answer the question.
- `non_domain`: answer outside domain content.

These are **nominal judgments**, not five equally spaced proficiency levels. The official binary reduction treats only `correct` as correct; the other categories collapse to incorrect. Preserve the original label alongside any derived reduction. Across ancillary archive views, blank values or spelling variants such as `non-domain` may occur; choose the task view before normalizing.

## Verified Core-view dimensions

Selecting only XML paths with `/Core/`, across the original train/evaluation partitions and excluding reliability material, yields 5,199 BEETLE answer rows / 56 distinct question IDs and 10,804 SciEntsBank answer rows / 196 distinct question IDs. These are archive structural counts, not unique participants or independent observations. No cleaning, examinee reconstruction or validity analysis was performed.
