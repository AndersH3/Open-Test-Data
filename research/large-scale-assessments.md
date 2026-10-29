# Large-scale skill assessments with online human response data

Research cutoff and verification date: **2026-10-29**. Scope: observed achievement/competence responses, excluding personality, beliefs, attitudes and self-reported skill use even when those variables share the same archive. Files were researched and linked; participant-level datasets were not republished. Except for the explicitly described archive-header/codebook checks, the full data were not imported or row-counted.

## Most useful choices

| Dataset | Objective construct and data | Why choose it | Main constraint |
|---|---|---|---|
| PISA 2025 | Reading, mathematics, science; individual raw/coded and scored cognitive responses, separate cognitive process archive | Newest verified PISA release; modern process and adaptive-test research | Specific PUF terms; final technical report pending 2027 |
| PISA 2022 | Mathematics, reading, science, separate creative-thinking and financial-literacy files | Mature documentation and a very large sample | Sparse/adaptive forms; COVID-era sampling cautions |
| PISA 2018 + corrected total-time files | Cognitive responses plus total time and visits | Strong option for speed–accuracy and revisit analyses | Original RT variable reflects last visit, requiring corrected supplement |
| PIAAC 2023 / cycle 2 | Adult literacy, numeracy and adaptive problem solving | Closest large-scale source to workplace-relevant adult competencies | Registration/terms; country suppressions; raw logs outside this PUF |
| PIAAC 2012 log files | Timestamped assessment interactions linked to cognitive PUF responses | Fine-grained adult task-solving processes | GESIS access terms and confidential full item documentation |
| TIMSS 2023 | Grade 4 and 8 mathematics/science item achievement responses | Curriculum-linked, multilevel, partial-credit research | Booklet design and school clustering; detailed events restricted |
| PIRLS 2021 | Reading comprehension item responses, digital process data | Reading and online reading behaviour | Passage dependence, mode changes and pandemic timing |
| ICILS 2023 | Computer/information literacy and optional computational thinking | Direct digital-skills and authoring task performance | Rubric criteria share tasks; partial item-content release |
| ICCS 2022 cognitive test only | Civic knowledge and reasoning; item options/scores, item timing | Knowledge/reasoning, distractor and timing analyses | Exclude the extensive attitude/belief scales |

The recommendations in this table are methodological judgments, not claims that the datasets validate any particular scoring algorithm.

## Dataset details and primary evidence

### 1. PISA 2025 — verified release, not a future placeholder

The [official programme page](https://www.oecd.org/en/about/programmes/pisa.html) dates the initial results to 8 September 2026. The [2025 database page](https://www.oecd.org/en/data/datasets/pisa-2025-database.html) offers cognitive responses and codebooks, while warning that only draft technical chapters are available and the final technical report is expected in 2027. The [official file index](https://webfs.oecd.org/pisa2022/index.html) separately lists cognitive and cognitive-process archives; foreign-language data are marked April 2027 and must not be counted as available at this cutoff.

Additional byte-level verification on 2026-10-29: the cognitive archive returned HTTP 206, ZIP signature and a 224,749,839-byte total, containing `CY09_MS_COG_20260806.sav`; the process archive returned the same checks, 424,600,524 bytes, containing `CY09_MS_COG_PROCESS_20260806.sav`. Only header/trailer byte ranges were read. The linked `PISA2025_Codebook.xlsx` was inspected: it includes `COG`, `COG_PROCESS` and `LDW` sheets, raw/scored response labels and action/time-to-first-action fields. This confirms archive existence and documented variables, not data quality or complete population coverage.

[NCES methodology](https://nces.ed.gov/surveys/pisa/pisa2025/technical-notes/) explains that test forms differ and ten plausible values support population inference. Simple percent-correct comparisons across different forms are invalid without design adjustment. Start with a defined country/domain/form subset and preserve routing and missingness. The survey-specific terms below apply.

### 2. PISA 2022 — mature general educational-skills benchmark

The [database landing page](https://www.oecd.org/en/data/datasets/pisa-2022-database.html) explicitly identifies a cognitive-item file alongside questionnaire files; optional domains have separate files. It also explains that the release includes systems with issues such as low response rates. The [official results](https://www.oecd.org/en/publications/2023/12/pisa-2022-results-volume-i_76772a36/full-report.html) describe nearly 700,000 tested students across 81 participating economies; this is survey participation, not a verified row count for any selected analysis.

Use scored responses for rescoring comparisons; retain raw options where codebook-supported for distractor models. Do not label questionnaire timing as cognitive response time. Mathematics/reading/science, creative thinking and financial literacy are distinct domains and optional participation differs. Released example questions are not the complete secure item bank. Prefer the technical report and codebook over assumptions about two-digit or missing response codes.

### 3. PISA 2018 — strongest documented timing correction case

The [official file index](https://webfs.oecd.org/pisa2022/index.html) offers cognitive responses and a separate cognitive-items total-time/visits archive. [Technical report Annex K](https://www.oecd.org/content/dam/oecd/en/data/datasets/pisa/pisa-2018-datasets/ssas-sps-data-files/PISA2018%20Aneex%20K%20TechReport.pdf) explains that original 2015/2018 RT values measure the last visit rather than total time. The supplementary total-time (`TT`) variables account for revisits. Its illustrated 2018 process analysis contains 551,930 students, a process-analysis subset rather than an unconditional sample size for every domain.

This makes a useful stress test for whether a speed-sensitive scoring scheme changes materially under different time definitions. Merge by documented student identifiers and verify the country component of IDs. Do not treat summary process variables as a full timestamped clickstream. Preserve item/page relationships when multiple items share a screen. Prefer TT for total-time analyses and state explicitly whether overhead/loading time is included.

### 4. PIAAC 2023 / cycle 2 — direct adult competencies

The [OECD database](https://www.oecd.org/en/data/datasets/PIAAC-2nd-Cycle-Database.html) provides country PUFs in SAS/SPSS/CSV and an international codebook. It lists national suppressions and pending files; check country availability at download time. [GESIS](https://www.gesis.org/en/data-on-adult-education/daten/piaac-daten-zyklus-1/piaac-international/international-public-use-files) confirms that international PUFs contain cognitive assessment responses, not only background questionnaires. The [technical report chapter 12](https://www.oecd.org/content/dam/oecd/en/about/programmes/edu/piaac/technical-reports/cycle-2/piaac-technical-report-2023/chapter-12-piaac-technical-report-draft-1.pdf) distinguishes the main flat PUF from cognitive log files, which are outside the public-use release described there.

Include directly assessed literacy, numeracy and adaptive problem solving; exclude occupational skill-use frequency questions. Adults are aged 16–65; adaptive routes mean individuals see different items. Maintain country IDs, sample/replicate weights and the difference between observed item scores and plausible values. Do not merge cycle-1 technology-rich problem solving with cycle-2 adaptive problem solving as though they were the same test.

### 5. PIAAC 2012 log files — process research supplement

[GESIS's official record](https://www.gesis.org/en/data-on-adult-education/daten/piaac-daten-zyklus-1/piaac-international/international-piaac-log-files) identifies **81,744** adults aged 16–65, 17 countries and timestamped interactions from literacy, numeracy and technology-rich problem solving. Sensitive text entries are masked with X characters, retaining entry length. The [catalogue entry is ZA6712](https://search.gesis.org/research_data/ZA6712), DOI `10.4232/1.12955`. Access conditions for the precise archive version must be checked there; no blanket CC licence was established.

The [OECD first-cycle page](https://www.oecd.org/en/data/datasets/piaac-1st-cycle-database.html) says logs can be linked to cognitive/background PUF data using SEQID and that complete item documentation requires a signed confidentiality application. Combine SEQID with country to avoid collisions. Event data alone are not automatically a scored person-by-item matrix. Public documentation for released items permits initial exploration; content-aware strategy interpretation across secure items has an additional access step.

### 6. TIMSS 2023 — mathematics and science

The [official release announcement](https://www.iea.nl/node/4611) confirms international achievement responses and R/SPSS/SAS downloads. The [database user guide](https://www.iea.nl/sites/default/files/2025-02/T23_UG-International-Database.pdf) describes scored achievement responses and public screen-level time/visits. [Boston College](https://timss.bc.edu/latest-news/t23-international-results-release.html) reports over 650,000 participating grade-4/grade-8 students. Use separate [grade archives](https://www.iea.nl/data-tools/repository/timss), not one pooled undifferentiated population.

Public timing is not the full event log: [IEA restricted-use documentation](https://www.iea.nl/node/4604) places timestamped responses, answer changes and navigation events behind a formal request. The large public files support partial-credit comparisons, cross-country calibration and cluster-sensitive analysis. Count actual administered items per student rather than treating the entire item pool as one common test. Test format, booklet, mode and curriculum exposure matter for comparisons. Codebook-specific missing categories must survive preprocessing.

### 7. PIRLS 2021 — reading comprehension and digital reading

The [IEA repository](https://www.iea.nl/data-tools/repository/pirls) links the second edition including log-file data. The [process-data release announcement](https://www.iea.nl/news-events/news/pirls-2021-process-data-available) confirms digital process, achievement and contextual data in R/SPSS/SAS. The [official international report description](https://www.iea.nl/publications/study-reports/international-reports-iea-studies/pirls-2021-international-results) reports about 400,000 participating students.

Use objective comprehension responses, not reading enjoyment/self-concept scales. Reading questions share passages, creating local dependence; split validation by passage if assessing transfer to unseen content. Paper and digital assessments, group-adaptive assignment and different collection schedules require separate treatment. Detailed identifying and administration variables are governed by the [restricted-use route](https://www.iea.nl/node/4053), distinct from the public achievement responses. Reproducing copyrighted passages/items requires separate rights checking.

### 8. ICILS 2023 — digital skills and computational thinking

The [user guide](https://www.iea.nl/sites/default/files/2025-02/ICILS_2023_User_Guide.pdf) distinguishes actual multiple-choice choices from assigned scores for constructed responses, computer-skills tasks and analytic criteria on authoring tasks. It documents five plausible values for each assessed competence and public/restricted variants. The [official release](https://www.iea.nl/news-events/news/icils-2023-international-report-results-and-resources-now-available-online) reports over 130,000 students across 35 education systems; CT is optional and its sample is smaller than CIL's. [Downloads and version DOI](https://www.iea.nl/data-tools/repository/icils) identify `10.58150/ICILS_2023_data_2`.

This is a strong alternative to self-reported digital competence. Multiple rubric criteria from a single authoring task are not independent questions. Account for task/module assignment, country participation and missingness. Item-level response time was not established as part of the standard public package during this review; do not advertise full clickstream access. The [technical report was revised in July 2026](https://www.iea.nl/publications/icils-2023-technical-report); use the revised version.

### 9. ICCS 2022 — retain only the civic-knowledge test

The [official repository](https://www.iea.nl/data-tools/repository/iccs) provides the second edition including process data. [IEA's process release](https://www.iea.nl/node/4452) confirms item and booklet total times in seconds. The [user guide](https://www.iea.nl/sites/default/files/2024-05/ICCS%20User%20Guide_0.pdf) describes raw multiple-choice options with correct options marked in codebooks, constructed-response scores, and supplied R/SAS/SPSS recoding programs. It explicitly separates not-administered, omitted, not-reached and invalid responses; defaults differ between calibration and proficiency scoring. Most item text/scoring guides remain secure.

Use knowledge/reasoning test files, excluding political beliefs, civic attitudes and participation questionnaires. This is narrower and more educationally situated than general reasoning. Raw options are valuable for distractor-sensitive scoring, but do not assume every incorrect option carries equal information. [The study centre's release](https://ausawards.acer.edu.au/ae/news/article/citizenship-education-in-times-of-global-challenge) reports approximately 82,000 grade-8 students in 24 education systems.

## Access and reuse: keep metadata separate from raw records

The current [PISA PUF download terms](https://survey.oecd.org/index.php?lang=en&r=survey/index&sid=197663) require institution/contact/project information and prohibit third-party distribution of PISA data, participant/school re-identification and disclosure of identifiable responses. The [PIAAC PUF terms](https://survey.oecd.org/index.php?lang=en&r=survey/index&sid=424913) impose parallel restrictions. **Do not commit PUFs to this GitHub repository.** Store catalogue metadata, links and original research notes; have each analyst obtain the files under the applicable terms. Directly reachable archive URLs are not a blanket redistribution licence.

[OECD's general data terms](https://www.oecd.org/en/about/terms-conditions.html) permit broad use with attribution except where additional conditions apply. The PUF-specific terms are why these datasets should not be labelled simply CC BY/open-redistributable. Data rights and copyrighted test-content rights remain separate.

The [IEA repository agreement](https://www.iea.nl/sites/default/files/2019-05/Disclaimer%20and%20License%20Agreement.pdf) addresses study materials and separately imposes explicit non-commercial conditions on IDB Analyzer software. Do not automatically apply the software restriction to response data. A standard open-data redistribution grant for every response archive was not established. [IEA's materials page](https://www.iea.nl/data) requires formal permission for study instruments. Catalogue response files as publicly downloadable under provider terms; keep data, software and item-content permissions separate.

## NAEP: valuable, but not a public raw-response shortlist entry

[NCES](https://nces.ed.gov/nationsreportcard/researchcenter/datatools.aspx) states that respondent-level raw data/weights from 1990 onward require a restricted-use licence. Public web tools and variable lists are not a public person-by-item dataset. [The 2017 mathematics process-data release](https://www.nationsreportcard.gov/process_data/) likewise requires a restricted-use application. Earlier historical data have different ICPSR routes and conditions; those were not validated here. Do not claim modern NAEP microdata are freely downloadable merely because released items and aggregate results are visible online.

## Recommended analysis protocol (research recommendations)

1. Pilot with one country, domain, grade and documented test form; do not silently combine grades or optional domains.
2. Retain person, item, country, school, form/module/routing, scoring version and missing-reason variables. Keep observed response, assigned item score, time and plausible values in distinct fields.
3. Never replace not-administered items with incorrect responses. Decide and document omitted/not-reached treatment separately. Evaluate sensitivity to those choices.
4. Treat plausible values as population-inference draws, not individual ground-truth ability labels. Follow provider rules for sampling and imputation variance; preserve clustering and replication weights for population claims.
5. Fit item parameters only on training participants. For transfer claims hold out whole items/passages/tasks, and for cross-national claims hold out countries or languages. Keep shared passage/task criteria together where dependence would leak information.
6. Compare scoring systems within comparable exposure designs, with uncertainty, subgroup error, reliability and prediction of held-out observed performance. Correlation with the provider's model-derived score alone is not independent validation.

