# Language assessment and constructed responses

Research date: **2026-10-29**. These sources contain demonstrated performance or human grading of that performance. Access and reuse conditions differ substantially. No restricted corpus was downloaded or republished for this review.

## MERLIN: German, Italian and Czech writing

**Best fit:** openly licensed, human-rated written performance. The current provider describes **2,286 examination texts**, with CEFR ratings, tasks, learner metadata, error annotations and target hypotheses. TXT, XML-oriented annotation formats and metadata are offered. These are scored writing samples, not a dense multiple-choice response matrix. No per-item response-time data were verified. Use task and language controls when comparing scores; CEFR categories are ordinal.

The platform explicitly states **CC BY-SA 4.0** for data and resources. Its linked CLARIN download endpoint showed an anti-bot page during this review, so availability is **official-page verified; archive not inspected**. Older descriptions sometimes report 2,290; use the current 2,286 release description. [Provider and downloads](https://www.merlin-platform.eu/), [Eurac corpus description](https://www.porta.eurac.edu/lci/merlin/), [CLARIN release](https://clarin.eurac.edu/repository/xmlui/handle/20.500.12124/59).

## Cambridge CLC FCE v1.1: English examination writing

**Best fit:** essay scoring and rater/score comparisons, subject to permission. The release describes **1,244 exam scripts** from 2000–2001. It retains candidate writing and error annotations; v1.1 corrects scores, supplies historical rubric documentation, adds JSONL, and reports answer-level multiple marks for **97 evaluation scripts**. It maps task marks to 0–20 and script totals to 0–40. Do not mix scales or silently pool v1.0 and v1.1. No response-time field was verified.

This is a registered **non-commercial research/education** resource. The page prohibits corpus redistribution, including GitHub, and requires prior approval to release derived artifacts such as models or statistics. Neither response text nor exam prompts inherit this repository's license. **Official description and terms verified; registration not submitted.** [FCE v1.1 release, dated 4 May 2026](https://researchdatasets.cambridge.org/datasets/clc-fce-dataset), [original research paper](https://aclanthology.org/P11-1019/).

## Cambridge Speak & Improve Corpus 2025

**Best fit:** oral proficiency scoring. The provider describes approximately **315 hours**, over **45,000 utterances**, and over **7,000 test submissions**. Four open-speaking test parts have indicative holistic CEFR judgments by non-operational examiners; roughly 55 hours have manual transcripts and language-error annotation. Audio duration is not cognitive response latency. Published splits support evaluation, but submissions and utterances must not be counted as unique speakers.

Registration and a **non-commercial research/education** agreement apply. The provider prohibits redistribution and asks approval for derived-artifact releases. Follow the release's stated processing conditions, including its restrictions on LLM training retention. **Page and terms verified; corpus not downloaded.** [Official release, terms and application](https://researchdatasets.cambridge.org/datasets/speak-and-improve-corpus-2025), [release report](https://doi.org/10.17863/CAM.114333).

## Cambridge Write & Improve Corpus 2024

**Best fit:** revision-aware writing assessment. The current second-version description reports **5,050 learner–prompt sets from 766 users**, with about **23,000 essay versions**. Final versions have indicative CEFR labels; first/final versions carry grammatical-error annotation. Earlier and intermediate versions permit analysis of feedback and revision. This is writing practice with feedback, rather than an independent-attempt examination. No response-time field was verified. Split by learner and learner–prompt set to avoid revision leakage.

The access agreement is **non-commercial research/education**, with no corpus redistribution and approval required for derived-artifact releases. **Page and terms verified; registration not submitted.** [Official release and terms](https://researchdatasets.cambridge.org/datasets/write-and-improve-corpus-2024), [report and version description](https://www.repository.cam.ac.uk/items/ba155087-0754-4c6b-ade8-68858e1df2f0).

## English C-Test user study: constrained generation

**Best fit:** a small human gap-completion study with known solutions. The authors describe **40 participants**, **32 English C-Tests**, and **20 gaps per test**. Their data documentation identifies `ctest_user_mapping.csv` as individual responses and distinguishes these from aggregated error rates, generated GPT-4 outputs and questionnaire responses. Only the actual human gap responses belong in a skill-scoring analysis. Text gaps share passages, creating testlet dependence; the sample is small. Response-time fields were not verified.

The repository's **code is Apache-2.0**; the university data record states **CC BY 4.0**, subject to any component-specific notices. These are separate licenses. The university endpoint returned 403 in this review, so **author documentation and indexed university metadata verified; raw data not inspected**. [Author repository and data schema](https://github.com/UKPLab/arxiv2024-constrained-ctest-generation), [university data record](https://tudatalib.ulb.tu-darmstadt.de/items/1e2ff254-6bba-454f-bd9f-e4aa1ecb7658).

## SemEval 2013 Task 7: BEETLE and SciEntsBank

**Best fit:** short-answer grading. The original task contains human science answers paired with reference answers and five accuracy labels: correct, partially correct/incomplete, contradictory, irrelevant, and non-domain. BEETLE comes from an electricity tutoring system; SciEntsBank covers school science. Keep them as separate datasets. These labels are **nominal diagnostic judgments**, not five equally spaced levels. A binary correct/other transformation is possible but discards information. Both corpora have unseen-answer and unseen-question splits; unseen-domain evaluation applies only to SciEntsBank. No response-time field was verified.

The original organizer supplies three-way and five-way ZIP files, with an explicit **CC BY-SA 3.0** license. The five-way archive was parsed for this review: it contains overlapping Core/Extra views, plus reliability material. Select one documented view and normalize label variants; do not simply concatenate every XML file. Prefer the organizer release over mirrors that duplicate answers once per reference answer. Answer IDs require study-specific interpretation before reconstructing examinees; answer rows are not people. [Organizer release and archives](https://github.com/myrosia/semeval-2013-task7), [license](https://github.com/myrosia/semeval-2013-task7/blob/main/LICENSE), [original task paper](https://aclanthology.org/S13-2045/).

## Useful but outside the individual-response shortlist

**Cambridge Multiple-Choice Questions Reading Dataset** provides reading passages, questions, keys, and task/item/option statistics. Its technical report describes JSONL at the task level, rather than an examinee-by-item matrix. The report lists 120 tasks and option statistics for 78 tasks. **Do not treat aggregate facility/discrimination as individual response records or use them to reconstruct a unique joint response distribution.** Access is registered non-commercial research with no redistribution. Suitable for item/distractor design studies; insufficient by itself for rescorings of individual examinees. [Official description and terms](https://researchdatasets.cambridge.org/datasets/cambridge-multiple-choice-questions-reading-dataset), [technical report with schema](https://www.repository.cam.ac.uk/bitstreams/90fc31ea-bd4c-4b33-8474-1e127635a6d3/download).

**EFCAMDAT** is a substantial learner-writing resource, but course levels arise from placement and progression and are not independent human grades of each essay. Access requires an approved application with academic affiliation; it is not an anonymous unrestricted download. It remains useful for learning trajectories, with care about level labels and outside assistance. [University of Cambridge access page](https://ef-lab.mmll.cam.ac.uk/EFCAMDAT.html).
