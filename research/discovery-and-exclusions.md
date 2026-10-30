# Discovery resources and boundaries

Checked **2026-10-29**. These resources extend the search; they are not additional independent response datasets in the catalogue count.

## Item Response Warehouse

The [Item Response Warehouse](https://itemresponsewarehouse.org/) harmonizes responses across many source studies. Its [collections](https://itemresponsewarehouse.org/collections.html) offer useful starting points: `math`, `reading_vocab`, `trials`, `q_matrix`, and international assessments. Its [core standard](https://itemresponsewarehouse.org/standard.html) uses a common long response representation; nominal responses and item text have separate standards.

Screen each table against the original study, version, license and transformation code. The warehouse also contains personality, symptoms, preferences and simulated/synthetic responses, all outside this project's core scope. Collection membership is partly rule-derived and not exhaustive. A harmonized binary score may omit selected distractors, trial structure or original missing categories. Avoid counting an original source and its harmonized copy as independent evidence. The warehouse is especially useful for discovering more candidates after the carefully documented starter set in this repository.

The older report's “900+ datasets” statement is traceable to version 28.2 in the [2025 IRW introduction](https://doi.org/10.3758/s13428-025-02796-y); it should not be presented as a current live total. Its cognitive candidates were reconciled separately in the [linking chapter](linked-tests-and-legacy-integration.md). IRW remains a resource, not an additional paired-test cohort.

## Important exclusions and conditional candidates

| Source/type | Treatment | Reason and primary evidence |
|---|---|---|
| Personality, attitudes, symptoms, interests and self-reported skill | Excluded | These do not observe demonstrated competence; mixed-source questionnaires remain excluded even if the study also has cognitive tests. |
| Modern NAEP respondent-level microdata | Outside public-download shortlist | [NCES requires restricted-use access](https://nces.ed.gov/nationsreportcard/researchcenter/datatools.aspx); public results and questions do not establish access to raw person-by-item responses. |
| Cambridge MCQ Reading Dataset | Aggregate/item resource, not core individual-response dataset | [Technical-report schema](https://www.repository.cam.ac.uk/bitstreams/90fc31ea-bd4c-4b33-8474-1e127635a6d3/download) contains item/option statistics and keys; no examinee-by-item matrix is established. |
| EFCAMDAT | Supplementary learning corpus | [Official access page](https://ef-lab.mmll.cam.ac.uk/EFCAMDAT.html) requires approval/academic affiliation; placement or course level is not an independent rating of each essay. |
| Current full ICAR archive | Conditional candidate in catalogue | [Current release](https://doi.org/10.23668/psycharchives.22167) has separate scientific-use conditions. Do not generalize historical public-domain wording to the current full archive or confuse the README license with the ZIP license. |
| ASSISTments 2015 sequence data | Retained as practice-log candidate with limits | [Release documentation](https://sites.google.com/site/assistmentsdata/datasets/2015-assistments-skill-builder-data) and inspected CSV identify sequences/skill builders; this release does not provide a conventional item-response matrix with actual question IDs. |
| Simulated data packaged beside real test examples | Excluded from empirical evidence | Consult each data object's documentation. A simulated examinee response can test software recovery but cannot validate a scoring method against human performance. See the learning notes for the DTMR example. |
| Public practice questions or answer keys alone | Excluded from response-data shortlist | They enable administration or content analysis, but do not supply observed human response patterns, error rates, reliability or participant rankings. |

“Conditional” is not a judgment that a source is unusable. It records the extra access, licensing or structural work required before it can answer the intended research question.
