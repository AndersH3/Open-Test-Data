# Front-report AI disclosure

This report was prepared with OpenAI Codex and delegated AI agents, which performed substantive research, interpretation, writing, coding and technical checks. The mirrored observations came from cited external sources; this workflow did not generate participant answers. Independent human fact-checking, legal review and peer review are not documented. See Appendix A for the full scope, evidence and limitations of AI involvement.

# 1. Executive findings


## What this research establishes

There is a substantial supply of human skill-response data online, but no single source supplies every response format, construct and reuse permission. The 44 catalogue entries cover reasoning, vocabulary, general knowledge, spatial ability, memory, attention, mathematics, science, adult literacy and numeracy, digital competence, language production and short-answer explanation. Personality, beliefs, preferences and self-reported ability are excluded from the skill-response scope.

The most important practical choice is the observation needed by the proposed scoring rule. Binary correctness supports one class of models; selected distractors, partial work, timing, repeated attempts and human rubric judgments support others. These are not interchangeable. A public sample test or aggregate item statistic does not supply the joint response patterns required to compare individual scores.

This report combines the full source review with a separate redistribution audit and downloaded collection. Every source has a decision, including sources not mirrored because their terms are restrictive, permission remains unresolved or an official download could not be obtained. Source-specific licences, original codebooks where available, project field guides and checksum manifests accompany the mirrored collection. The project licence does not override third-party conditions.

The [earlier Candidate Datasets report](../older_reports/Candidate%20Datasets.docx) is now integrated through a primary-source recheck dated 30 October 2026. Seven distinct source versions were added; IQ1 was retained without duplication. The new linking chapter corrects two-form and retest claims, distinguishes historical SAPA from other releases, and records all earlier candidates in a reconciliation table. Music Ensemble and the Much–Mutak study support common-person analyses with specific design qualifications, rather than an already established equating relation between two complete IQ instruments.

## Most useful starting points

| Research question | Practical sources | Interpretation |
|---|---|---|
| Can a scoring pipeline reproduce a familiar small item matrix? | SAPA ability/iqitems, fraction subtraction, ECPE grammar | Useful compact structural benchmarks. SAPA's two objects are the same sample; binary-only exports cannot recover distractor choices. Exact packaged response objects are mirrored under their formal GPL grants; separate test-stimulus rights remain distinct. |
| Does a score capture spatial performance and latency? | Ganis-Kievit mental rotation | Direct behaviour, stimulus conditions and response-time documentation; a small, task-specific validation sample. [Original deposit](https://doi.org/10.6084/m9.figshare.1045385). |
| Can responses connect tasks or instruction conditions? | Music Ensemble; Much–Mutak matrices; historical SAPA/ICAR | Common IDs, experimental blocks and planned item overlap support different designs. Check construct alignment, condition/order effects, connectedness and missingness. [Integrated linking review](../research/linked-tests-and-legacy-integration.md). |
| Does a task score remain stable on retesting? | Self-Regulation Ontology objective task subset | Raw trials and retest data permit task-specific stability checks. Exclude surveys and preference tasks. [Author data and licence](https://github.com/IanEisenberg/Self_Regulation_Ontology). |
| How should span performance receive partial credit? | Mathy-Friedman working-memory data | Original trial and participant-level files document different span-scoring rules. Preserve repeated-trial structure. [Versioned deposit](https://data.mendeley.com/datasets/kfc3jyggs7/1). |
| What do distractor choices add to educational scoring? | Eedi NeurIPS 2020; EdNet | Actual answers and keys support option-based analysis. Eedi retains only the latest student-question answer and uses separate ID spaces across task pairs; its images have additional restrictions. EdNet is longitudinal test preparation. [Eedi source](https://www.eedischool.com/projects/neurips-education-challenge), [EdNet source](https://github.com/riiid/ednet). |
| How does a score behave during learning? | Junyi 2020, EdNet, ASSISTments 2009 | Define initial knowledge, current knowledge or learning gain before evaluation. Hints, feedback, stopping rules and future attempts must not leak into predictions. [Junyi release](https://www.kaggle.com/datasets/junyiacademy/learning-activity-public-dataset-by-junyi-academy). |
| Can a score generalize across populations or countries? | PISA, PIAAC, TIMSS, PIRLS, ICILS | Large samples are useful, but exposure design, weights and latent-score estimation require their technical manuals. These sources are linked rather than mirrored where sharing permission is absent. |
| How should written performance be evaluated? | MERLIN; Cambridge FCE and Write & Improve | Use ordinal/human-rating methods and account for task and rater effects. MERLIN is redistributable; Cambridge release terms prohibit corpus sharing. [MERLIN source](https://www.merlin-platform.eu/), [Cambridge terms](https://researchdatasets.cambridge.org/datasets/clc-fce-dataset). |
| Can a short-answer score distinguish error types? | BEETLE and SciEntsBank | Nominal accuracy judgments and reference answers support grading studies. They do not form an equally spaced five-level scale. [Organizer release](https://github.com/myrosia/semeval-2013-task7). |

## Six findings that materially affect analysis

1. **Response codes carry scientific meaning.** Omitted, not-reached, not-administered and incorrect are different states. Preserve the original representation and document every transformation.
2. **Units must remain explicit.** A student, test submission, token, step, attempt, action, passage and question are different units. Dataset-size claims should state which one is counted.
3. **Timing is a measurement definition.** Last-visit time, total time, bundle/screen time, exercise duration and event timestamps require different analyses. PISA 2018's corrected supplement is a particularly clear example.
4. **A sample is not a norm.** Volunteer online samples, scanner-based cohorts, narrow historical tests and selected practice users do not automatically represent a deployment population.
5. **Observed performance is not error-free ability.** Plausible values, estimated diagnostic classes, expert Q-matrices and CEFR judgments are useful annotations or model outputs, not known personal ground truth.
6. **Reuse permission must be checked at the file and component level.** Data, code, stimuli, photographs, question images, rubrics and papers can carry different conditions. Non-commercial and ShareAlike licences permit some redistribution while retaining those obligations; an unresolved licence is not an open grant.

## Recommended progression for scoring research

First validate the scoring pipeline on a small documented response source. Then use an independently acquired dataset with the required response information and a held-out evaluation design. Estimate all weights and transformations on training observations. Compare uncertainty, calibration, ranking stability and prediction of held-out performance, rather than only correlation with a score derived from the same answers.

For practice data, use time-respecting splits and keep a learner's related records together where appropriate. For transfer to new content, hold out whole items, passages or tasks. For population claims, preserve survey design and imputation rules. A novel score that gives rare responses extra weight requires particular care about guessing, small cells, local dependence and outliers.

These recommendations are a methodological synthesis of the reviewed sources. No scoring algorithm was fitted, no causal claim was tested, and no source has been certified for high-stakes individual decisions in this task. Detailed evidence and limitations follow in the source profiles and acquisition ledger.


# 2. Research method and analysis guidance


Initial research cutoff: **29 October 2026**; earlier-report candidates and integration checked **30 October 2026**. This is a curated research review, not an exhaustive registry or a certification of each test's validity.

## What counts as a skill-based test here?

Included: tasks where a person demonstrates knowledge, reasoning, memory, attention, perception, reading, numeracy, language production or another competence, and an answer or performance is observed. A broad interpretation includes cognitive ability and educational attainment. The catalogue separates fixed assessments, adaptive/sampled assessments, repeated-trial tasks, human-rated performances and learning/practice logs.

Excluded from the core shortlist: personality inventories, interests, attitudes, self-reported ability, clinical symptom questionnaires, synthetic examinees, question banks without human responses and datasets consisting only of AI responses. A mixed study can qualify through its performance-based subset; its questionnaires do not become skill tests.

## What “online available” means

Availability, openness and evidence strength are separate dimensions. Each profile records its actual route: anonymous download, software-package data, registration/agreement, application/approval, or restricted research access. An online catalogue or sample test does not establish access to individual responses. “Not verified” means the review did not establish the fact; it does not mean the feature is absent.

Evidence levels used in the catalogue:

| Level | Evidence obtained | What it does not establish |
|---|---|---|
| `file_inspected` | Actual response-file bytes were parsed or their schema inspected; full-file versus sample checks are specified | Full cleaning, psychometric validity, representativeness or legal clearance |
| `archive_verified` | Actual archive bytes/listing or range headers were checked | Response values and complete schema |
| `documentation_verified` | Primary provider/researcher description, codebook or package documentation checked | Successful end-to-end download today |
| `metadata_only_or_unresolved` | Only indexed/deposited metadata were available, or response-file evidence remains unresolved | Successful file acquisition or complete schema verification |

Evidence strength does not imply unrestricted access: even an inspected public file may carry restrictive terms. Full details and exceptions appear in the domain notes and [verification evidence](../data/verification-evidence.json). A successful HTTP response alone is not a parsed dataset. Login forms, anti-bot pages and archive errors are recorded as limitations. No restricted access agreements were accepted on the user's behalf.

## How sources were selected and checked

AI assistants conducted research in parallel across cognitive tasks, large educational assessments, learning datasets, and language/constructed-response assessment. Primary sources were preferred: provider databases and terms, university/laboratory releases, original articles and author-maintained software documentation. Search snippets were used for discovery; claims supported only by indexed metadata are explicitly marked. Selected public archives and small response files were checked directly. Counts retain their units: people, submissions, answers, items, passages and events are not interchangeable.

The priority labels express **practical suitability for a stated research use**, based on response granularity, documentation, access burden and methodological complexity. They are this review's judgments, not empirical rankings of test quality or recommendations for high-stakes individual decisions.

## Integration of earlier research

The earlier Word report was retained byte for byte and treated as a secondary discovery document. Each named candidate was reconciled with the existing catalogue and rechecked against primary sources where obtainable. New source versions receive separate records; alternate exports of the same sample do not become independent studies. The linking chapter records corrected administration designs, source/version conflicts, missing identifiers and rights, and distinguishes file checks from documentation-only evidence. An ambiguous earlier citation is not reconstructed as a certain source. The integration did not fit a scoring or linking model.

## Minimum fields to preserve on acquisition

For every version, save its source URL, retrieval date, checksum, original citation, applicable terms and codebook. Record participant and item IDs, response categories, answer key/version, missing codes, administration form, and timing units. Preserve original files outside the public repository until redistribution rights are clear. Maintain a separate derived table and a transformation log.

Suggested analysis representation:

| Field | Meaning |
|---|---|
| `dataset_version`, `person_id`, `item_id` | Provenance and stable within-dataset identifiers |
| `attempt_id`, `session_id`, `position` | Repeated attempts and administration order, when available |
| `raw_response`, `score`, `max_score` | Selected option/free response and explicitly derived scoring |
| `response_time_ms` | Latency only when its definition and units are known |
| `missing_reason` | Not administered, omitted, not reached, invalid and missing remain distinguishable |
| `form_id`, `testlet_id`, `skill_id` | Booklet/adaptive routing, shared stimulus and content domain |
| `weight`, `replicate_weights`, `cluster_id` | Complex sample design, if supplied |

Do not force all datasets into binary accuracy. Distractor selections, partial-credit marks and nominal error labels can support different models. A timestamp, total duration or average of previous attempts is not automatically the response time for the current item.

## Comparing scoring methods responsibly

1. Start with a transparent baseline on the same responses and comparable item exposure/forms: number correct or proportion of available marks. Account for form difficulty before comparing different adaptive/booklet sets. Add appropriate Rasch/IRT, ordinal, multidimensional or diagnostic models only where their assumptions fit the data.
2. Fit transformations, item weights and model parameters on training data; evaluate on held-out examinees. If testing generalization to new items or institutions, hold out those units too. Keep repeated attempts and revisions together, or use a time-respecting learning evaluation.
3. Examine reliability/precision, calibration, rank stability and predictive/criterion validity where suitable outcomes exist. Better agreement with a score already derived from the same answers is not independent validity evidence.
4. Model booklet missingness, adaptive routing, clustering and repeated measures. Never automatically score non-administered items as wrong. Use the official survey design for population claims.
5. Treat plausible values as multiple population-analysis draws, not observed item responses or precise labels for individual ability. Do not average plausible values into a supposedly true personal score.
6. Treat rare patterns cautiously: inspect sample size, guessing, item dependence, rapid responses and data quality before assigning unusual answers high weight. Validate any novelty-based score on independent data.

These steps are proposed analysis guidance; no scoring experiment or psychometric comparison was run in this research task.

## Licensing and publication boundary

This project stores AI-assisted research summaries, metadata and links, plus a separately licensed mirror of sources with explicit redistribution permission. Its existing repository license does **not** relicense external response data, item wording, photographs, speech recordings, keys or rubrics. A software package's license is not automatically proof of permission to administer or republish the original test. Some sources allow analysis but prohibit redistributing files; some also restrict derived outputs. The redistribution audit records each decision; consult the version-specific primary terms before publication.

## Coverage limitations

The search emphasizes openly documented datasets with useful human responses and English-language source documentation. It covers multiple domains and languages, but is not a census of occupational, vocational, physical or professional certification tests. Many commercial tests have public practice questions but no reusable person-level data. Size, access and licenses can change; recheck the recorded source before a new download. A file inspection is only a structural check, and the samples have not been validated for any particular deployment population.


# 3. Redistribution decisions and downloaded collection


All **44 catalogue entries** were screened separately from scientific suitability. Current result: **18 mirrored entries**, **23 excluded**, **1 licensed but inaccessible**, **2 linked without a mirror**, and **0 pending**. Mirrored entries map to **17 distinct collection folders** because BEETLE and SciEntsBank share one original release.

The acquired response/stimulus payloads total **6,192,443,865 bytes** across **34 files**. Files larger than 15 MB are GitHub release assets; smaller payloads, licences, codebooks, source records and manifests are stored in Git. The release is part of the same repository. File size and SHA-256 provide an integrity record, not proof of psychometric validity.

## Decision standard

Redistribution was accepted where an explicit source grant covers the files. This includes formal package-wide GPL grants for packaged response objects when no contrary data notice applies; a separate file header is not required. It does not authorize separate proprietary test banks or stimuli. Standard Creative Commons licences can permit sharing with attribution, non-commercial, ShareAlike or NoDerivatives conditions. Those conditions are preserved rather than replaced by the project licence. Unresolved grants are excluded; clear licences with unavailable files are separately recorded. Linked sources are kept at the provider for documented scope or acquisition reasons; their status is separate from exclusions and inaccessible files. No restricted-use applications or custom access agreements were submitted.

Eedi is a special case: unchanged response and metadata CSV members are losslessly repackaged; every question image is excluded. No cleaned, filtered or merged derivative response table is distributed. For mixed cognitive batteries, the selected objective tasks and original member hashes are documented; surveys, preference tasks and MRI images are not part of the skill-response mirror.

## Decisions for every source

| Source | Decision | Basis |
|---|---|---|
| SAPA cognitive ability: psychTools ability / iqitems (`sapa-ability-iqitems`) | mirrored | Affirmative package-wide GPL (>=2) grant, with no contrary data-specific restriction found; exact unmodified source objects and documentation preserved. Only `ability.rda` and `iqitems.rda`: two representations of the same 1,525 people×16 cognitive items, plus their codebooks. The current full ICAR archive and its separate access terms are outside this mirror. [Primary evidence](https://github.com/cran/psychTools/blob/7dc591f8ac11c0ef1764cf853f3065aa60653d09/DESCRIPTION) |
| OpenPsychometrics Vocabulary IQ Test (`ospp-viqt`) | excluded | A distinct response-data redistribution grant was not established; public downloading does not establish permission. [Primary evidence](https://openpsychometrics.org/tests/VIQT/) |
| OpenPsychometrics Multifactor General Knowledge Test 2017-2018 (`ospp-mgkt`) | excluded | A distinct response-data redistribution grant was not established; public downloading does not establish permission. [Primary evidence](https://openpsychometrics.org/_rawdata/MGKT_data.zip) |
| OpenPsychometrics experimental matrix IQ test (`ospp-iq1`) | excluded | A distinct response-data redistribution grant was not established; public downloading does not establish permission. [Primary evidence](https://openpsychometrics.org/_rawdata/IQ1.zip) |
| OpenPsychometrics Full Scale IQ alpha v0.1 (`ospp-fsiq-alpha`) | excluded | A distinct response-data redistribution grant was not established; public downloading does not establish permission. [Primary evidence](https://openpsychometrics.org/_rawdata/FSIQ_0.1_data.zip) |
| Exposure Based Face Memory Test (`ospp-ebfmt`) | excluded | Response-data redistribution license unresolved; copyrighted face photos described as research-use, not general redistribution. [Primary evidence](https://openpsychometrics.org/_rawdata/EBFMT.zip) |
| Ganis-Kievit mental rotation validation data (`ganis-kievit-mental-rotation`) | mirrored | Original behavioral ZIP file3702010, full JPG stimulus bank and original codebooks; redundant encodings/older archive omitted explicitly [Primary evidence](https://doi.org/10.6084/m9.figshare.1045385.v13) |
| Self-Regulation Ontology objective performance-task subset (`sro-performance-tasks`) | mirrored | 23 objective tasks, complete and retest phases; original per-task gzip members untouched [Primary evidence](https://pmc.ncbi.nlm.nih.gov/articles/PMC6534563/) |
| OpenNeuro ds004636 objective task subset (`openneuro-ds004636-objective-tasks`) | mirrored | 734 BIDS events.tsv files from seven objective tasks; no MRI, surveys or preference tasks [Primary evidence](https://pmc.ncbi.nlm.nih.gov/articles/PMC11271451/) |
| Working Memory Develops at a Similar Rate Across Diverse Stimuli (`mathy-friedman-working-memory`) | mirrored | All two deposited version-1 data files, unchanged; author description and project field guide [Primary evidence](https://doi.org/10.17632/kfc3jyggs7.1) |
| ICAR current full materials and psychometric data (`icar-current-restricted`) | excluded | Current full archive uses Scientific Use License/academic access conditions and no public redistribution permission was established. [Primary evidence](https://doi.org/10.23668/psycharchives.22167) |
| Music Ensemble: objective cognitive and music-perception tasks (`music-ensemble-cognitive-tasks`) | linked | CC BY-NC 4.0 is explicit, but full 92.8 MB mixed archive is linked rather than mirrored. Selected inspected Raven data retain IP-like collection fields and experimenter identifiers; a field-minimization decision is required before a mirror. [Primary evidence](https://doi.org/10.1038/s41597-026-06654-0) |
| Much, Mutak, Pohl and Ranger: matrix reasoning under speed and accuracy instructions (`much-mutak-matrices-2025`) | mirrored | Unmodified original main CSV and machine-readable reasoning solutions, with original main and supplemental codebooks; alternative encoding, optional logs and stimulus overviews omitted explicitly. [Primary evidence](https://doi.org/10.5334/jopd.124) |
| TüEyeQ: CFT 20-R performance and eye tracking (`tueyeq-cft20r`) | inaccessible | Data CC0 grant documented; actual Harvard Dataverse deposit returned a robot challenge/403. The cited figshare DOI is metadata only; paper and version-2 task counts conflict. [Primary evidence](https://doi.org/10.7910/DVN/JGOCKI) |
| HCP Penn Progressive Matrices: edmdata response matrices (`hcp-penn-matrices-edmdata`) | excluded | Upstream HCP terms require every recipient to register and agree. Package MIT does not override those source-specific conditions; original joining IDs were removed from packaged matrices. [Primary evidence](https://tmsalab.github.io/edmdata/reference/items-hcp-penn.html) |
| Revised PSVT:R response matrix (`revised-psvtr-edmdata`) | mirrored | Affirmative package-wide MIT grant with no contrary response-object notice found; exact source object and original documentation preserved. Separate proprietary test-stimulus rights are not inferred. [Primary evidence](https://tmsalab.github.io/edmdata/reference/items_revised_psvtr.html) |
| SPM-LS: final 12 Standard Progressive Matrices items (`spm-ls-edmdata`) | mirrored | Affirmative package-wide MIT grant with no contrary response-object notice found; exact source object and original documentation preserved. Separate proprietary test-stimulus rights are not inferred. Underlying original SPM-LS data are CC BY 4.0; full terms, original-author attribution, DOI rights metadata and upstream transformation script retained alongside package MIT notices. This is the upstream binary-scored object, not the original nominal CSV; no further transformation by this project. [Primary evidence](https://tmsalab.github.io/edmdata/reference/items_spm_ls.html) |
| Historical SAPA/ICAR 2010–2013 validation response data (`sapa-icar-2010-2013-96958`) | linked | Historical deposit CC0 grant documented. Source remains linked without a new large acquisition; response-file structure and overlap not re-counted. Current full ICAR terms remain separate. [Primary evidence](https://openpsychologydata.metajnl.com/articles/10.5334/jopd.25) |
| PISA 2025 cognitive responses and process data (`pisa-2025`) | excluded | PISA public-use terms explicitly prohibit third-party redistribution; an anonymously reachable archive is not an overriding grant. [Primary evidence](https://www.oecd.org/en/data/datasets/pisa-2025-database.html) |
| PISA 2022 (`pisa-2022`) | excluded | PISA public-use terms explicitly prohibit third-party redistribution; an anonymously reachable archive is not an overriding grant. [Primary evidence](https://www.oecd.org/en/data/datasets/pisa-2022-database.html) |
| PISA 2018 cognitive responses plus corrected total-time/visits supplement (`pisa-2018-timing`) | excluded | PISA public-use terms explicitly prohibit third-party redistribution; an anonymously reachable archive is not an overriding grant. [Primary evidence](https://www.oecd.org/en/data/datasets/pisa-2018-database.html) |
| Survey of Adult Skills 2023 / PIAAC cycle 2 (`piaac-2023`) | excluded | PIAAC public-use terms explicitly prohibit distribution or disclosure to third parties. [Primary evidence](https://www.oecd.org/en/data/datasets/PIAAC-2nd-Cycle-Database.html) |
| PIAAC 2012 international log files, ZA6712 (`piaac-2012-logs`) | excluded | GESIS/OECD source-specific access conditions do not establish a transferable redistribution licence for the precise log archive. [Primary evidence](https://www.gesis.org/en/data-on-adult-education/daten/piaac-daten-zyklus-1/piaac-international/international-piaac-log-files) |
| TIMSS 2023 grades 4 and 8 (`timss-2023`) | excluded | Public download is available, but a blanket response-data redistribution grant was not established. IEA separately controls study instruments and restricted items; software restrictions are not used as a substitute for data-licence evidence. [Primary evidence](https://www.iea.nl/data-tools/repository/timss) |
| PIRLS 2021, second edition including log files (`pirls-2021`) | excluded | Public download is available, but a blanket response-data redistribution grant was not established. IEA separately controls study instruments and restricted items; software restrictions are not used as a substitute for data-licence evidence. [Primary evidence](https://www.iea.nl/data-tools/repository/pirls) |
| ICILS 2023 (`icils-2023`) | excluded | Public download is available, but a blanket response-data redistribution grant was not established. IEA separately controls study instruments and restricted items; software restrictions are not used as a substitute for data-licence evidence. [Primary evidence](https://www.iea.nl/data-tools/repository/icils) |
| ICCS 2022 civic-knowledge test and process data (`iccs-2022-cognitive`) | excluded | Public download is available, but a blanket response-data redistribution grant was not established. IEA separately controls study instruments and restricted items; software restrictions are not used as a substitute for data-licence evidence. [Primary evidence](https://www.iea.nl/data-tools/repository/iccs) |
| Tatsuoka fraction subtraction (CDM) (`fraction-subtraction`) | mirrored | Affirmative package-wide GPL (>=2) grant, with no contrary data-specific restriction found; exact unmodified source objects and documentation preserved. Only the 536 × 20 binary response matrix and 20 × 8 Q-matrix source objects; no original test-question facsimiles or item artwork. [Primary evidence](https://github.com/alexanderrobitzsch/CDM/blob/9a731f28426367d9c56576035930c7246a902894/DESCRIPTION) |
| ECPE English grammar section (CDM) (`ecpe-grammar`) | mirrored | Affirmative package-wide GPL (>=2) grant, with no contrary data-specific restriction found; exact unmodified source objects and documentation preserved. Only `data.ecpe.rda`, containing 2,922 people×28 binary grammar-item scores, participant ID and 28 × 3 Q-matrix; no ECPE test questions, forms or handbook. [Primary evidence](https://github.com/alexanderrobitzsch/CDM/blob/9a731f28426367d9c56576035930c7246a902894/DESCRIPTION) |
| ASSISTments 2009–2010 corrected collapsed Skill Builder (`assistments-2009`) | excluded | Official source says free to use with citation, but an explicit right to redistribute the release files was not established. Public download alone is not treated as permission to mirror. [Primary evidence](https://sites.google.com/site/assistmentsdata/home/2009-2010-assistment-data/skill-builder-data-2009-2010) |
| ASSISTments 2015 top-100 Skill Builders (`assistments-2015`) | excluded | No release-specific explicit redistribution licence was established from the checked primary source. Kept link-only. [Primary evidence](https://sites.google.com/site/assistmentsdata/datasets/2015-assistments-skill-builder-data) |
| Junyi Academy Online Learning Activity Dataset (2020 release; 2018–2019 logs) (`junyi-2020`) | mirrored | Full original Kaggle bundle acquired unchanged; all three source CSVs included; full ZIP CRC audit passed. Provider licence/terms and source-header field guide preserved. [Primary evidence](https://www.kaggle.com/datasets/junyiacademy/learning-activity-public-dataset-by-junyi-academy) |
| EdNet KT1–KT4 (Santa English test preparation) (`ednet`) | mirrored | Full original KT1-KT4 and Contents archives copied without byte changes; every ZIP member CRC verified. Author README/codebook and CC BY-NC4 licence preserved. KT1 final SHA-256 matches the pinned mirror LFS; fixed byte windows match the official source. Canonical Riiid CC BY-NC4 retained. [Primary evidence](https://github.com/riiid/ednet) |
| Eedi / NeurIPS 2020 Education Challenge (`eedi-neurips-2020`) | mirrored | All18originalresponse/metadata/challenge CSVtables acquired with exact original bytes and source CRC32 verified. Lossless collection packaging only; all images and macOS resource forks omitted under provider conditions. [Primary evidence](https://www.eedischool.com/projects/neurips-education-challenge) |
| Duolingo SLAM 2018 shared-task learner responses (`duolingo-slam-2018`) | mirrored | All three version4 course archives acquired unchanged from named mirror, with original Duolingo LICENSE.md/CITING.md/CHANGELOG.md. Exact source-deposited sizes match; original-deposit hashes not exposed. Complete gzip CRC audit passed. [Primary evidence](https://doi.org/10.7910/DVN/8SWHNO) |
| KDD Cup 2010 Algebra I / Bridge to Algebra (`kdd-cup-2010-algebra`) | excluded | Public competition download and rules did not establish an explicit reusable-data redistribution grant. No mirrored payload without clearer permission. [Primary evidence](https://kdd.org/kdd-cup/view/kdd-cup-2010-student-performance-evaluation/Data) |
| Database Exercises for Knowledge Tracing (DBE-KT22) (`dbe-kt22`) | excluded | Custom dataset terms could not be fully inspected; paper CC BY4 does not establish dataset rights. Source payload access also returns anti-bot403. Kept link-only because redistribution permission remains unresolved. [Primary evidence](https://arxiv.org/html/2208.12651v3) |
| MERLIN multilingual examination writing (`merlin`) | mirrored | Explicit primary redistribution license verified; unmodified source payload, full license, attribution/source links, checksums and codebooks retained. [Primary evidence](https://www.merlin-platform.eu/) |
| Cambridge CLC FCE v1.1 (`clc_fce_1_1`) | excluded | Provider-specific noncommercial research/education license expressly prohibits redistributing corpus files, including via GitHub. No registration/agreement was submitted. [Primary evidence](https://researchdatasets.cambridge.org/datasets/clc-fce-dataset) |
| Cambridge Speak & Improve Corpus 2025 (`speak_improve_2025`) | excluded | Provider-specific noncommercial research/education license expressly prohibits redistributing corpus files, including via GitHub. No registration/agreement was submitted. [Primary evidence](https://researchdatasets.cambridge.org/datasets/speak-and-improve-corpus-2025) |
| Cambridge Write & Improve Corpus 2024 (second version) (`write_improve_2024`) | excluded | Provider-specific noncommercial research/education license expressly prohibits redistributing corpus files, including via GitHub. No registration/agreement was submitted. [Primary evidence](https://researchdatasets.cambridge.org/datasets/write-and-improve-corpus-2024) |
| Constrained English C-Test user study (`ctest_mip_2024`) | mirrored | Explicit primary redistribution license verified; unmodified source payload, full license, attribution/source links, checksums and codebooks retained. [Primary evidence](https://tudatalib.ulb.tu-darmstadt.de/handle/tudatalib/4205) |
| SemEval 2013 Task 7 BEETLE (`semeval2013_beetle`) | mirrored | Explicit primary redistribution license verified; unmodified source payload, full license, attribution/source links, checksums and codebooks retained. [Primary evidence](https://github.com/myrosia/semeval-2013-task7) |
| SemEval 2013 Task 7 SciEntsBank (`semeval2013_scientsbank`) | mirrored | Explicit primary redistribution license verified; unmodified source payload, full license, attribution/source links, checksums and codebooks retained. [Primary evidence](https://github.com/myrosia/semeval-2013-task7) |

## Mirrored collection documentation

### Constrained English C-Test user study

**Licence:** CC-BY-4.0. **Selected scope:** Explicit primary redistribution license verified; unmodified source payload, full license, attribution/source links, checksums and codebooks retained.

[Source record and documentation](https://github.com/AndersH3/skill-data-atlas/tree/main/datasets/ctest_mip_2024)


This directory mirrors **User Study Data.zip**, the original, unmodified human user-study archive accompanying *Constrained C-Test Generation via Mixed-Integer Programming*. Retrieved 29 October 2026.

- Authors: Ji-Ung Lee, Marc Pfetsch and Iryna Gurevych.
- University release: https://tudatalib.ulb.tu-darmstadt.de/handle/tudatalib/4205
- Release API: https://tudatalib.ulb.tu-darmstadt.de/server/api/core/items/1e2ff254-6bba-454f-bd9f-e4aa1ecb7658
- Direct original data: https://tudatalib.ulb.tu-darmstadt.de/server/api/core/bitstreams/088d335e-b696-48f3-8f08-bc4dc2cc8dad/content
- Author documentation: https://github.com/UKPLab/arxiv2024-constrained-ctest-generation
- Paper: https://arxiv.org/abs/2404.08821

## License and attribution

The university's actual API record states `dc.rights.license = CC-BY-4.0`; it is copied unmodified in `upstream-repository-record.json`. **CC BY 4.0** permits sharing and adaptation with the required credit, license link and change notice. Full standard legal text is provided in `LICENSE.cc-by-4.0.txt`, sourced from the SPDX license-list transcription of the Creative Commons legal code: https://raw.githubusercontent.com/spdx/license-list-data/main/text/CC-BY-4.0.txt. Canonical license: https://creativecommons.org/licenses/by/4.0/.

Please cite Lee, J.-U., Pfetsch, M., and Gurevych, I. (2024), *Constrained C-Test Generation via Mixed-Integer Programming*, together with the university data release above. Retain source attribution and any component notices when redistributing. Source archives are unchanged.

The author repository's README is provided as `upstream-README.md` to document the data. Its software/documentation license is separately preserved in `upstream-code-LICENSE.Apache-2.0.txt`; Apache-2.0 must not be confused with the response-data CC BY 4.0 license. The root project license does not replace either.

## Data scope

The human study has **40 participants**, **32 C-Test forms**, and **160 participant-form attempts** (four forms per participant), each with 20 gaps: 3,200 observed gap responses. The 640 distinct form-gap positions are not 3,200 independent items. The archive includes original test forms/solutions, individual responses/scores and total form time, plus ancillary questionnaires, ratings and participant assignment tables. Ancillary self-report fields are not skill outcomes.

Only the human **User Study Data.zip** is mirrored. Separate GPT-4 prompt/output archives, variability-only generated data, model weights and executable feature-extraction software are outside this response-data acquisition. Test forms generated by a GPT-4 strategy are present as administered stimuli within the human archive; their human responses are observed human data.

`CODEBOOK.project.md` is a project-written schema guide, based on actual CSV headers and author documentation. It is not a newly discovered original-author codebook. Original files are available unchanged within the ZIP. `structural-verification.json` and `manifest.json` record structure, provenance and checksums. No learner text, responses or identifying details are reproduced in the PDF report.

| Payload | Bytes | SHA-256 prefix |
|---|---:|---|
| [User Study Data.zip](https://github.com/AndersH3/skill-data-atlas/blob/main/datasets/ctest_mip_2024/User%20Study%20Data.zip) | 47,462 | `9027d1cfa96e00be` |

### Duolingo SLAM 2018 shared-task learner responses

**Licence:** CC-BY-NC-4.0. **Selected scope:** All three version4 course archives acquired unchanged from named mirror, with original Duolingo LICENSE.md/CITING.md/CHANGELOG.md. Exact source-deposited sizes match; original-deposit hashes not exposed. Complete gzip CRC audit passed.

[Source record and documentation](https://github.com/AndersH3/skill-data-atlas/tree/main/datasets/duolingo-slam-2018)


Provider: Duolingo, Inc.; deposited by Burr Settles. Acquisition date: 2026-10-29.

## Primary sources and acquisition route

- Dataset DOI: https://doi.org/10.7910/DVN/8SWHNO
- Author task description and original schema: https://sharedtask.duolingo.com/2018.html
- Author-deposited DataCite record: https://api.datacite.org/dois/10.7910/DVN/8SWHNO
- Harvard Dataverse version4 schema.org metadata, preserved by DataONE: https://cn.dataone.org/cn/v2/object/sha256%3Ac99e7d3e18a8ee138442180c31cedf54546f51fe4b02555e0894e11cdfebc7e8
- File DOIs: https://doi.org/10.7910/DVN/8SWHNO/C1LOKO (English), https://doi.org/10.7910/DVN/8SWHNO/Z29WIF (Spanish), https://doi.org/10.7910/DVN/8SWHNO/5YWVBV (French)
- Acquisition mirror: https://github.com/xinhez/11785-project/tree/master/data

The Harvard website and payload/custom-license API returned HTTP403 from this environment. The three original-named tarballs were acquired from the public mirror above. Their exact byte sizes match the author-deposited v4 metadata; embedded CHANGELOG.md identifies v4 and embedded LICENSE.md provides the original rights notice. SHA-256 hashes identify the acquired mirror bytes. The preserved metadata object itself passes its DataONE content-addressed SHA-256 check. It did not expose original archive MD5/SHA checksums, so equality of the three data archives to the original deposit is not independently checksum-proven.

## Rights

Original notice preserved in LICENSE.md: Copyright(c)2016 Duolingo, Inc. The original archive explicitly applies **CC BY-NC 4.0**, with the complete legal code. The author-deposited metadata independently states the same licence. Canonical licence: https://creativecommons.org/licenses/by-nc/4.0/ . Noncommercial and attribution conditions remain attached. This project's software licence does not replace the dataset licence.

## Files and changes

The three tarballs are copied byte-for-byte from the identified mirror. No learner records, labels or archive contents were transformed. Original licence, citation and changelog files are also extracted unchanged for convenience. Each archive covers one course: en_es, es_en, fr_en. The archive-specific upstream documents remain beside the source manifest. CODEBOOK.md is a project-written field guide with links to the official schema; it is labelled separately from original author documentation.

Version4 adds source translation prompts and corrects dependency parsing; do not silently mix it with the original 2018 files. Original learner answer strings are not supplied; the corpus provides correct-answer tokens and error labels. This is predominantly practice rather than a common fixed proficiency examination.

## Citation

Settles, B., Brust, C., Gustafson, E., Hagiwara, M., and Madnani, N. (2018). Second Language Acquisition Modeling. Proceedings of the NAACL-HLT Workshop on Innovative Use of NLP for Building Educational Applications. ACL. Dataset: Settles, Burr, 2018, Data for the 2018 Duolingo Shared Task on Second Language Acquisition Modeling (SLAM), Harvard Dataverse, V4, doi:10.7910/DVN/8SWHNO. Preserve the exact original CITING.md files supplied with each archive.

| Payload | Bytes | SHA-256 prefix |
|---|---:|---|
| [data_en_es.tar.gz](https://github.com/AndersH3/skill-data-atlas/releases/download/datasets-2026-10-29/data_en_es.tar.gz) | 46,889,834 | `dac4e97a03e0d35d` |
| [data_es_en.tar.gz](https://github.com/AndersH3/skill-data-atlas/releases/download/datasets-2026-10-29/data_es_en.tar.gz) | 35,067,817 | `c53079ed8053f523` |
| [data_fr_en.tar.gz](https://github.com/AndersH3/skill-data-atlas/releases/download/datasets-2026-10-29/data_fr_en.tar.gz) | 16,134,930 | `f34bb1518d2fbc69` |

### ECPE English grammar section (CDM)

**Licence:** GPL-2.0-or-later. **Selected scope:** Affirmative package-wide GPL (>=2) grant, with no contrary data-specific restriction found; exact unmodified source objects and documentation preserved. Only `data.ecpe.rda`, containing 2,922 people×28 binary grammar-item scores, participant ID and 28 × 3 Q-matrix; no ECPE test questions, forms or handbook.

[Source record and documentation](https://github.com/AndersH3/skill-data-atlas/tree/main/datasets/ecpe-grammar)


Source package: **CDM 8.4-9**, as distributed by `alexanderrobitzsch/CDM` at commit `9a731f28426367d9c56576035930c7246a902894`. Retrieved 2026-10-29.

Declared license: **GPL (>=2)**, represented here as SPDX **GPL-2.0-or-later**. `upstream-DESCRIPTION` is the unmodified formal package license declaration. `LICENSE.GPL-2.0-or-later.txt` supplies the full GPLv2 license text with the later-version option retained. These external files keep their upstream GPL license; the parent repository's AGPL license does not replace it.

## Redistribution basis

The R developers' package specification treats DESCRIPTION License as the package's license. No separate copyright/license carveout for these response objects was found in the inspected source tree, data documentation or package metadata. CRAN policy requires clarity of rights for all package components and maintainer authorization; it expressly recognizes `.rda` files as source or readily convertible to source. Accordingly this mirror relies on the affirmative package-wide GPL grant, rather than requiring redundant per-file license headers. This is a source-object mirror, not a claim that raw data values or every original test stimulus necessarily carry copyright.

Primary package declaration: https://github.com/alexanderrobitzsch/CDM/blob/9a731f28426367d9c56576035930c7246a902894/DESCRIPTION
Package source: https://github.com/alexanderrobitzsch/CDM/tree/9a731f28426367d9c56576035930c7246a902894
R package license specification: https://cran.r-project.org/doc/manuals/r-release/R-exts.html#Licensing
CRAN all-component rights/source policy: https://cran.r-project.org/web/packages/policies.html
Canonical GPLv2: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html
License text transcription source: https://raw.githubusercontent.com/spdx/license-list-data/main/text/GPL-2.0-or-later.txt

## Attribution and data provenance

Package authors: Alexander Robitzsch, Thomas Kiefer, Ann Cathrice George and Ali Uenlue. Original response data source identified in the author Rd guide: Templin and Hoffman (2013) tutorial, formerly http://psych.unl.edu/jtemplin/teaching/dcm/dcm12ncme/. Cite Templin & Hoffman (2013), Obtaining diagnostic classification model estimates using Mplus, Educational Measurement: Issues and Practice 32, 37-50; Templin & Bradshaw (2014), Hierarchical diagnostic classification models, Psychometrika 79, 317-339, as well as CDM. The commercial examination content is separate.

## Exact mirrored scope and test-content boundary

Only `data.ecpe.rda`, containing 2,922 people × 28 binary grammar-item scores, participant ID and 28 × 3 Q-matrix; no ECPE test questions, forms or handbook.

The original `.rda` files are unchanged source-distribution data objects, editable after loading in R; no executable package code or compiled binary is included. The original author `.Rd` documentation is included unchanged as the codebook. No new observations or scores were generated. No unrelated personality datasets, secure question bank, test artwork, commercial test handbook or publisher article PDF is mirrored. Permission to redistribute these packaged response objects is not a grant to administer or republish a separate current test bank.

## Source availability and GPL notices

GPLv2 section 1 permits verbatim source copies with the applicable notices, warranty disclaimer and license copy retained. The original data objects, relevant Rd source documentation and DESCRIPTION provided here are the material being redistributed; R can load them directly using `load()`. The `.rda` files are the preferred form supplied in the upstream **source** distribution, not compiled executable versions needing a separate opaque binary/source offer. The upstream full package source remains linked above for context; unrelated package datasets are not required to inspect or modify these numeric response objects.

Redistributors should retain the upstream license/attribution, source links and no-warranty notices. Any covered modifications must be identified with dates and distributed under the applicable GPL terms; retain the original >=2 option. See the full license for its conditions rather than treating this summary as the license. The project-generated `read-data.R` is a convenience example for reading the preserved source objects, not a replacement for them.

| Payload | Bytes | SHA-256 prefix |
|---|---:|---|
| [data.ecpe.rda](https://github.com/AndersH3/skill-data-atlas/blob/main/datasets/ecpe-grammar/original/data.ecpe.rda) | 13,659 | `2eeeffcab7985b10` |

### Revised PSVT:R response matrix

**Licence:** MIT. **Selected scope:** Affirmative package-wide MIT grant with no contrary response-object notice found; exact source object and original documentation preserved. Separate proprietary test-stimulus rights are not inferred.

[Source record and documentation](https://github.com/AndersH3/skill-data-atlas/tree/main/datasets/edmdata-revised-psvtr)


Source: **edmdata 1.3.0**, pinned GitHub commit `3c0036e4a665b61adde011aac2215b62bd5da33d`. Retrieved **30 October 2026**. Formal package licence: **MIT + file LICENSE**. Full upstream MIT terms, both upstream copyright declarations and the original DESCRIPTION are preserved alongside this file.

## Redistribution basis

This mirror follows the same policy as the project's other R source-object mirrors: an affirmative formal package-wide grant applies to included source data absent a contrary component notice. The inspected data documentation, package metadata and source tree did not identify a contrary notice for this response object. This is a documented curation judgment, not independent legal clearance. The parent's AGPL does not replace external terms.

Package declaration: https://raw.githubusercontent.com/tmsalab/edmdata/3c0036e4a665b61adde011aac2215b62bd5da33d/DESCRIPTION
Package source: https://github.com/tmsalab/edmdata/tree/3c0036e4a665b61adde011aac2215b62bd5da33d
Full upstream MIT notice: https://raw.githubusercontent.com/tmsalab/edmdata/3c0036e4a665b61adde011aac2215b62bd5da33d/LICENSE.md

## Scope and original attribution

Exact packaged `items_revised_psvtr.rda` numeric source object (516 records × 30 items), unchanged. No questionnaire, personality measures, proprietary item artwork or test handbook.

The codebooks are unmodified author `.Rd` and R documentation. The project field guide is separate. Loading the R data object does not execute a package installer or reconstruct a secure test bank. This workflow added no observations and fitted no scoring model.

The author documentation attributes the response data to Culpepper and Balamuta (2017), “A Hierarchical Model for Accuracy and Choice on Standardized Tests,” Psychometrika 82, 820–845, https://doi.org/10.1007/s11336-015-9484-7. The instrument design is credited to Yoon (2011), “Psychometric properties of the Revised Purdue Spatial Visualization Tests: Visualization of Rotations.” Package authors are James Joseph Balamuta, Steven Andrew Culpepper and Jeffrey Alan Douglas; see the exact upstream DESCRIPTION and notices for roles and copyright holders.

The MIT grant is relied on for this packaged response source object and associated documentation. Permission to administer or republish a separate PSVT:R test form or stimulus bank is not established by this mirror. Only keyed correctness, not distractor selections or timing, is present in the inspected object.

## Technical inspection and limitations

Native R loaded the exact source object. Its dimensions and value set are recorded in `manifest.json`; all cells were binary and none were missing. The object alone does not establish a paired second test, population representativeness or scientific validity. Hashes establish byte identity, not the correctness of every interpretation or upstream rights claim. Retain original licences, notices, provenance and the distinction between author codebooks and project guidance.

| Payload | Bytes | SHA-256 prefix |
|---|---:|---|
| [items_revised_psvtr.rda](https://github.com/AndersH3/skill-data-atlas/blob/main/datasets/edmdata-revised-psvtr/original/items_revised_psvtr.rda) | 3,182 | `e2d7c69fc21d0574` |

### SPM-LS: final 12 Standard Progressive Matrices items

**Licence:** MIT AND CC-BY-4.0. **Selected scope:** Affirmative package-wide MIT grant with no contrary response-object notice found; exact source object and original documentation preserved. Separate proprietary test-stimulus rights are not inferred. Underlying original SPM-LS data are CC BY 4.0; full terms, original-author attribution, DOI rights metadata and upstream transformation script retained alongside package MIT notices. This is the upstream binary-scored object, not the original nominal CSV; no further transformation by this project.

[Source record and documentation](https://github.com/AndersH3/skill-data-atlas/tree/main/datasets/edmdata-spm-ls)


Source: **edmdata 1.3.0**, pinned GitHub commit `3c0036e4a665b61adde011aac2215b62bd5da33d`. Retrieved **30 October 2026**. Formal package licence: **MIT + file LICENSE**. Full upstream MIT terms, both upstream copyright declarations and the original DESCRIPTION are preserved alongside this file.

## Redistribution basis

This mirror follows the same policy as the project's other R source-object mirrors: an affirmative formal package-wide grant applies to included source data absent a contrary component notice. The inspected data documentation, package metadata and source tree did not identify a contrary notice for this response object. This is a documented curation judgment, not independent legal clearance. The parent's AGPL does not replace external terms.

Package declaration: https://raw.githubusercontent.com/tmsalab/edmdata/3c0036e4a665b61adde011aac2215b62bd5da33d/DESCRIPTION
Package source: https://github.com/tmsalab/edmdata/tree/3c0036e4a665b61adde011aac2215b62bd5da33d
Full upstream MIT notice: https://raw.githubusercontent.com/tmsalab/edmdata/3c0036e4a665b61adde011aac2215b62bd5da33d/LICENSE.md

## Scope and original attribution

Exact packaged `items_spm_ls.rda` numeric source object (499 records × 12 items), unchanged. No questionnaire, personality measures, proprietary item artwork or test handbook.

The codebooks are unmodified author `.Rd` and R documentation. The project field guide is separate. Loading the R data object does not execute a package installer or reconstruct a secure test bank. This workflow added no observations and fitted no scoring model.

Original study and deposit: Nils Myszkowski and Martin Storme (2018), “A snapshot of g? Binary and polytomous item-response theory investigations of the last series of the Standard Progressive Matrices (SPM-LS),” Intelligence 68, 109–116, https://doi.org/10.1016/j.intell.2018.03.010. Deposit: https://doi.org/10.17632/h3yhs5gy3w.1.

The original data deposit's registered rights metadata explicitly declares **CC BY 4.0**. The metadata snapshot and complete CC BY 4.0 text are retained. Preserve original-author attribution and the deposit DOI when redistributing the derived binary object, as well as the package MIT notices. **The package maintainers converted selected option codes to keyed binary scores and applied listwise deletion**; their original builder is retained. This project made no additional changes to the packaged data object. These two representations are not independent samples. The original nominal CSV is linked, rather than mirrored, because the provider blocked this session's download attempt.

Robitzsch (2020), https://doi.org/10.20944/preprints202007.0269.v1, is a subsequent reanalysis; it is not the original dataset collection. No right to republish Raven test stimuli is inferred.

## Technical inspection and limitations

Native R loaded the exact source object. Its dimensions and value set are recorded in `manifest.json`; all cells were binary and none were missing. The object alone does not establish a paired second test, population representativeness or scientific validity. Hashes establish byte identity, not the correctness of every interpretation or upstream rights claim. Retain original licences, notices, provenance and the distinction between author codebooks and project guidance.

| Payload | Bytes | SHA-256 prefix |
|---|---:|---|
| [items_spm_ls.rda](https://github.com/AndersH3/skill-data-atlas/blob/main/datasets/edmdata-spm-ls/original/items_spm_ls.rda) | 1,098 | `0d90692decc86da6` |

### EdNet KT1–KT4 (Santa English test preparation)

**Licence:** CC-BY-NC-4.0. **Selected scope:** Full original KT1-KT4 and Contents archives copied without byte changes; every ZIP member CRC verified. Author README/codebook and CC BY-NC4 licence preserved. KT1 final SHA-256 matches the pinned mirror LFS; fixed byte windows match the official source. Canonical Riiid CC BY-NC4 retained.

[Source record and documentation](https://github.com/AndersH3/skill-data-atlas/tree/main/datasets/ednet)


Provider: Riiid / Santa. Source checked and files retrieved on 2026-10-29.

- Author repository, licence declaration and original field descriptions: https://github.com/riiid/ednet
- Author repository README: https://raw.githubusercontent.com/riiid/ednet/master/README.md
- Original archive links: [KT1](https://bit.ly/ednet_kt1), [KT2](https://bit.ly/ednet-kt2), [KT3](https://bit.ly/ednet-kt3), [KT4](https://bit.ly/ednet-kt4), [Contents](https://bit.ly/ednet-content)
- Paper: https://arxiv.org/abs/1912.03072

## Rights

The authors explicitly release the dataset under **CC BY-NC 4.0** for research. The full legal text is in LICENSE.txt, obtained from the SPDX licence corpus: https://raw.githubusercontent.com/spdx/license-list-data/main/text/CC-BY-NC-4.0.txt . Canonical licence: https://creativecommons.org/licenses/by-nc/4.0/ . Attribution and noncommercial conditions remain attached to these files. The project's software licence does not replace them.

## Contents and changes

The full KT1, KT2, KT3, KT4 and Contents ZIP files are acquired without modifying their bytes. KT1 acquisition combines validated official-source prefix/ranges with an immutable matching mirror for remaining ranges: https://huggingface.co/datasets/Lucy9999/EdNet-KT1/resolve/790cff06b7c112c4ec072217257de5dd4ec1e77a/EdNet-KT1.zip . Fixed byte windows and size match the official file; the final archive must match the mirror LFS SHA-256 recorded in mirror-verification.json. The mirror card's MIT label does not replace Riiid's canonical CC BY-NC4 dataset licence. The release inventory records exact sizes and SHA-256 hashes. Each learner's events are stored in a separate CSV inside the source ZIP. KT1 covers question-solving responses; KT2 adds answer selection/submission events; KT3 adds explanations/lectures; KT4 adds broader activity. These are overlapping representations, not four independent samples. No unreleased question text, pictures, audio or TOEIC score file is implied.

UPSTREAM_README.md is the author's original repository README/codebook, preserved unchanged. CODEBOOK.md is a concise project field guide. Large originals are distributed as release assets to keep the Git repository usable.

## Citation

Choi, Y. et al. (2020). EdNet: A Large-Scale Hierarchical Dataset in Education. In Artificial Intelligence in Education. Also available as arXiv:1912.03072. Credit Riiid and the named authors of the linked paper.

## Limitations

Timestamps were shifted for privacy. Questions share bundles and can share elapsed times. Practice, feedback, recommendations and answer revisions affect responses. Higher-level actions must not be counted as all being scored answers. See the author README for exact action/source semantics.

| Payload | Bytes | SHA-256 prefix |
|---|---:|---|
| [ednet-Contents.zip](https://github.com/AndersH3/skill-data-atlas/blob/main/datasets/ednet/raw/ednet-Contents.zip) | 173,976 | `aa910a0436d9dbac` |
| [ednet-KT1.zip](https://github.com/AndersH3/skill-data-atlas/releases/download/datasets-2026-10-29/ednet-KT1.zip) | 1,201,163,816 | `0d13933f90201c51` |
| [ednet-KT2.zip](https://github.com/AndersH3/skill-data-atlas/releases/download/datasets-2026-10-29/ednet-KT2.zip) | 555,757,666 | `bb5dec5708b6af91` |
| [ednet-KT3.zip](https://github.com/AndersH3/skill-data-atlas/releases/download/datasets-2026-10-29/ednet-KT3.zip) | 762,774,456 | `cc7823d9a5a0570c` |
| [ednet-KT4.zip](https://github.com/AndersH3/skill-data-atlas/releases/download/datasets-2026-10-29/ednet-KT4.zip) | 1,169,540,359 | `ae7b699f64980a2e` |

### Eedi / NeurIPS 2020 Education Challenge

**Licence:** CC-BY-NC-ND-4.0. **Selected scope:** All18originalresponse/metadata/challenge CSVtables acquired with exact original bytes and source CRC32 verified. Lossless collection packaging only; all images and macOS resource forks omitted under provider conditions.

[Source record and documentation](https://github.com/AndersH3/skill-data-atlas/tree/main/datasets/eedi-neurips-2020)


Provider: Eedi and the NeurIPS 2020 Education Challenge organizers. Retrieval date: 2026-10-29.

- Primary project and licence declaration: https://www.eedischool.com/projects/neurips-education-challenge
- Original ZIP: https://dqanonymousdata.blob.core.windows.net/neurips-public/data.zip
- Author guide and citation: https://arxiv.org/abs/2007.12061
- Detailed version of guide: https://arxiv.org/html/2007.12061v3

## Rights

The provider explicitly applies **CC BY-NC-ND 4.0**: attribution and noncommercial use, with no distribution of modified material. LICENSE.txt contains the full standard licence, obtained from https://raw.githubusercontent.com/spdx/license-list-data/main/text/CC-BY-NC-ND-4.0.txt . Canonical licence: https://creativecommons.org/licenses/by-nc-nd/4.0/ .

The provider adds a separate condition for question images: they are only for model training, and must not be printed or shared. **Every image is excluded from this mirror.** The original full ZIP must not be republished as a release asset because it contains those images.

## Packaging and changes

The 18 original response, metadata and challenge CSV tables are extracted; auxiliary macOS resource forks are excluded. Their bytes are unchanged; lossless recompression and collecting files into a new ZIP are technical packaging changes. No observations, columns, IDs or values are changed. extraction-manifest.json records original archive member paths, sizes, CRC32 and SHA-256 hashes. The source archive inventory records all original filenames; image files are not downloaded into this collection. Auxiliary macOS resource forks are not treated as data tables.

This is a collection of unchanged files under their original licence, not a relicense under this repository's software licence. Do not distribute transformed versions of these data under the no-derivatives condition. CODEBOOK.md is a project-written factual guide, with links to the original author descriptions.

## Citation

Wang, Z., Lamb, A., Saveliev, E., Cameron, P., Zaykov, Y., Hernandez-Lobato, J. M., Turner, R. E., Baraniuk, R. G., Barton, C., Jones, S. P., Woodhead, S., and Zhang, C. (2020). Diagnostic Questions: The NeurIPS 2020 Education Challenge. arXiv:2007.12061.

## Scope caveats

The release retains only the latest answer for each student-question pair. Task1/2 and task3/4 IDs are independently anonymized: identical-looking IDs cannot be joined across task pairs. Timestamps are not response durations. Preserve the official train/test partitions and withheld-label conventions.

| Payload | Bytes | SHA-256 prefix |
|---|---:|---|
| [eedi-2020-response-and-metadata-csvs.zip](https://github.com/AndersH3/skill-data-atlas/releases/download/datasets-2026-10-29/eedi-2020-response-and-metadata-csvs.zip) | 615,045,122 | `2a956a053c21ce57` |

### Tatsuoka fraction subtraction (CDM)

**Licence:** GPL-2.0-or-later. **Selected scope:** Affirmative package-wide GPL (>=2) grant, with no contrary data-specific restriction found; exact unmodified source objects and documentation preserved. Only the 536 × 20 binary response matrix and 20 × 8 Q-matrix source objects; no original test-question facsimiles or item artwork.

[Source record and documentation](https://github.com/AndersH3/skill-data-atlas/tree/main/datasets/fraction-subtraction)


Source package: **CDM 8.4-9**, as distributed by `alexanderrobitzsch/CDM` at commit `9a731f28426367d9c56576035930c7246a902894`. Retrieved 2026-10-29.

Declared license: **GPL (>=2)**, represented here as SPDX **GPL-2.0-or-later**. `upstream-DESCRIPTION` is the unmodified formal package license declaration. `LICENSE.GPL-2.0-or-later.txt` supplies the full GPLv2 license text with the later-version option retained. These external files keep their upstream GPL license; the parent repository's AGPL license does not replace it.

## Redistribution basis

The R developers' package specification treats DESCRIPTION License as the package's license. No separate copyright/license carveout for these response objects was found in the inspected source tree, data documentation or package metadata. CRAN policy requires clarity of rights for all package components and maintainer authorization; it expressly recognizes `.rda` files as source or readily convertible to source. Accordingly this mirror relies on the affirmative package-wide GPL grant, rather than requiring redundant per-file license headers. This is a source-object mirror, not a claim that raw data values or every original test stimulus necessarily carry copyright.

Primary package declaration: https://github.com/alexanderrobitzsch/CDM/blob/9a731f28426367d9c56576035930c7246a902894/DESCRIPTION
Package source: https://github.com/alexanderrobitzsch/CDM/tree/9a731f28426367d9c56576035930c7246a902894
R package license specification: https://cran.r-project.org/doc/manuals/r-release/R-exts.html#Licensing
CRAN all-component rights/source policy: https://cran.r-project.org/web/packages/policies.html
Canonical GPLv2: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html
License text transcription source: https://raw.githubusercontent.com/spdx/license-list-data/main/text/GPL-2.0-or-later.txt

## Attribution and data provenance

Package authors: Alexander Robitzsch, Thomas Kiefer, Ann Cathrice George and Ali Uenlue. Original data: Tatsuoka, K. (1984), Analysis of errors in fraction addition and subtraction problems; Tatsuoka, C. (2002), Data analytic methods for latent partially ordered classification models, JRSS Series C 51, 337-350. The original Rd guide cites the Royal Statistical Society datasets website as the response-data source. Preserve these original-data citations alongside the CDM package citation.

## Exact mirrored scope and test-content boundary

Only the 536 × 20 binary response matrix and 20 × 8 Q-matrix source objects; no original test-question facsimiles or item artwork.

The original `.rda` files are unchanged source-distribution data objects, editable after loading in R; no executable package code or compiled binary is included. The original author `.Rd` documentation is included unchanged as the codebook. No new observations or scores were generated. No unrelated personality datasets, secure question bank, test artwork, commercial test handbook or publisher article PDF is mirrored. Permission to redistribute these packaged response objects is not a grant to administer or republish a separate current test bank.

## Source availability and GPL notices

GPLv2 section 1 permits verbatim source copies with the applicable notices, warranty disclaimer and license copy retained. The original data objects, relevant Rd source documentation and DESCRIPTION provided here are the material being redistributed; R can load them directly using `load()`. The `.rda` files are the preferred form supplied in the upstream **source** distribution, not compiled executable versions needing a separate opaque binary/source offer. The upstream full package source remains linked above for context; unrelated package datasets are not required to inspect or modify these numeric response objects.

Redistributors should retain the upstream license/attribution, source links and no-warranty notices. Any covered modifications must be identified with dates and distributed under the applicable GPL terms; retain the original >=2 option. See the full license for its conditions rather than treating this summary as the license. The project-generated `read-data.R` is a convenience example for reading the preserved source objects, not a replacement for them.

| Payload | Bytes | SHA-256 prefix |
|---|---:|---|
| [fraction.subtraction.data.rda](https://github.com/AndersH3/skill-data-atlas/blob/main/datasets/fraction-subtraction/original/fraction.subtraction.data.rda) | 1,953 | `b6be3376c173d5be` |
| [fraction.subtraction.qmatrix.rda](https://github.com/AndersH3/skill-data-atlas/blob/main/datasets/fraction-subtraction/original/fraction.subtraction.qmatrix.rda) | 408 | `5b2faf01cd753d78` |

### Ganis-Kievit mental rotation validation data

**Licence:** CC-BY-4.0. **Selected scope:** Original behavioral ZIP file3702010, full JPG stimulus bank and original codebooks; redundant encodings/older archive omitted explicitly

[Source record and documentation](https://github.com/AndersH3/skill-data-atlas/tree/main/datasets/ganis-kievit-mental-rotation)


Retrieved: 2026-10-29

License: **CC-BY-4.0**. The external dataset license remains separate from the parent repository AGPL license.

## Exact file selection

Behavioral ZIP3702010, full JPG stimulus bank3191717, README_stimuli1571341, Datadescription_behaviour1878074 and deposit metadata. Source version13. Alternate PCT/image-name encodings and older behavioral ZIP are redundant representations and remain linked in metadata; they are not copied. All downloaded original files are unchanged.

## Primary source and license evidence

- https://doi.org/10.6084/m9.figshare.1045385.v13
- https://api.figshare.com/v2/articles/1045385
- https://ndownloader.figshare.com/files/3191717
- https://ndownloader.figshare.com/files/1571341
- https://ndownloader.figshare.com/files/1878074
- https://ndownloader.figshare.com/files/3702010
- https://raw.githubusercontent.com/spdx/license-list-data/main/text/CC-BY-4.0.txt

## Integrity

See manifest.json for original source URLs, byte sizes and SHA-256 checksums. For repackaged subsets, every original member has its own source path and hash. Provider checksums or Git blob hashes were compared where available. No publisher article PDF was copied.

| Payload | Bytes | SHA-256 prefix |
|---|---:|---|
| [All-stimuli-JPG-file3191717.zip](https://github.com/AndersH3/skill-data-atlas/releases/download/datasets-2026-10-29/All-stimuli-JPG-file3191717.zip) | 30,364,670 | `bd64561ec9c9cc57` |
| [Behavioural_data-file3702010.zip](https://github.com/AndersH3/skill-data-atlas/blob/main/datasets/ganis-kievit-mental-rotation/original/Behavioural_data-file3702010.zip) | 1,747,699 | `3b56dde3defc36d5` |

### Junyi Academy Online Learning Activity Dataset (2020 release; 2018–2019 logs)

**Licence:** CC-BY-NC-SA-4.0. **Selected scope:** Full original Kaggle bundle acquired unchanged; all three source CSVs included; full ZIP CRC audit passed. Provider licence/terms and source-header field guide preserved.

[Source record and documentation](https://github.com/AndersH3/skill-data-atlas/tree/main/datasets/junyi-2020)


Provider: Junyi Academy Foundation. Kaggle owner: junyiacademy. Retrieval date: 2026-10-29. Dataset version reported by the provider API: 9 (last updated 2020-05-13).

- Source and provider terms: https://www.kaggle.com/datasets/junyiacademy/learning-activity-public-dataset-by-junyi-academy
- Provider metadata: https://www.kaggle.com/api/v1/datasets/view/junyiacademy/learning-activity-public-dataset-by-junyi-academy
- Original full ZIP: https://www.kaggle.com/api/v1/datasets/download/junyiacademy/learning-activity-public-dataset-by-junyi-academy
- Original file index: https://www.kaggle.com/api/v1/datasets/list/junyiacademy/learning-activity-public-dataset-by-junyi-academy
- Referenced provider policy: https://www.junyiacademy.org/about/policy

## Rights and attribution

The provider explicitly applies **CC BY-NC-SA 4.0**. The full standard licence is LICENSE.txt, obtained from https://raw.githubusercontent.com/spdx/license-list-data/main/text/CC-BY-NC-SA-4.0.txt . Canonical licence: https://creativecommons.org/licenses/by-nc-sa/4.0/ . Additional provider notices are preserved in UPSTREAM_TERMS.md, including exclusions for trademarks/logos, non-distortion, disclaimers and requests to share research feedback. No logo or unreleased problem content is included.

Citation requested by provider: P. J. Chen, M. E. Hsieh, T. Y. Tsai (2020). Junyi Academy Online Learning Activity Dataset: A large-scale public online learning activity dataset from elementary to senior high school students. Dataset available from the source above.

## Files and changes

The original ZIP is copied without changing its bytes. It contains Info_Content.csv, Info_UserData.csv and Log_Problem.csv. The source describes 16,217,311 problem attempts by 72,630 selected learners from August 2018 through July 2019. Source file sizes and acquired hashes are in the manifest. Large payload is a release asset rather than a Git blob. CODEBOOK.md is a project-written field guide; no standalone original author codebook file was supplied in the full ZIP.

This is distinct from the legacy 2015 Junyi dataset. Do not transplant its schema or prerequisite graph to this release. The anonymized learner metadata are licensed by the provider; do not attempt to identify individuals.

| Payload | Bytes | SHA-256 prefix |
|---|---:|---|
| [junyi-2020-original.zip](https://github.com/AndersH3/skill-data-atlas/releases/download/datasets-2026-10-29/junyi-2020-original.zip) | 1,615,467,938 | `d3272a56b3657d19` |

### Working Memory Develops at a Similar Rate Across Diverse Stimuli

**Licence:** CC-BY-4.0. **Selected scope:** All two deposited version-1 data files, unchanged; author description and project field guide

[Source record and documentation](https://github.com/AndersH3/skill-data-atlas/tree/main/datasets/mathy-friedman-working-memory)


Retrieved: 2026-10-29

License: **CC-BY-4.0**. The external dataset license remains separate from the parent repository AGPL license.

## Exact file selection

All two files in the official version1 file list, unchanged: dat_all.csv and dat_partialcreditunitAGG_Unstacked.csv. Raw file parsed as3,564 rows ×16 columns; collapsed file99 rows ×23 columns. The name field contains99 unique numeric participant codes, rather than personal names. Delimiter is semicolon; original line endings preserved. No separately deposited author codebook exists, so a clearly labeled project field guide and author description accompany the original files.

## Primary source and license evidence

- https://doi.org/10.17632/kfc3jyggs7.1
- https://data.mendeley.com/public-api/datasets/kfc3jyggs7?version=1
- https://data.mendeley.com/public-api/datasets/kfc3jyggs7/files?folder_id=root&version=1
- https://data.mendeley.com/public-files/datasets/kfc3jyggs7/files/d0c5b8d5-169c-473f-b2dd-5c61a88b89c4/file_downloaded
- https://data.mendeley.com/public-files/datasets/kfc3jyggs7/files/af641063-4d8e-4329-975e-17daa875cec5/file_downloaded
- https://raw.githubusercontent.com/spdx/license-list-data/main/text/CC-BY-4.0.txt

## Integrity

See manifest.json for original source URLs, byte sizes and SHA-256 checksums. For repackaged subsets, every original member has its own source path and hash. Provider checksums or Git blob hashes were compared where available. No publisher article PDF was copied.

| Payload | Bytes | SHA-256 prefix |
|---|---:|---|
| [dat_all.csv](https://github.com/AndersH3/skill-data-atlas/blob/main/datasets/mathy-friedman-working-memory/original/dat_all.csv) | 238,445 | `0d0b9195af8ee4e8` |
| [dat_partialcreditunitAGG_Unstacked.csv](https://github.com/AndersH3/skill-data-atlas/blob/main/datasets/mathy-friedman-working-memory/original/dat_partialcreditunitAGG_Unstacked.csv) | 31,012 | `e2cd767d5d4a956d` |

### MERLIN multilingual examination writing

**Licence:** CC-BY-SA-4.0. **Selected scope:** Explicit primary redistribution license verified; unmodified source payload, full license, attribution/source links, checksums and codebooks retained.

[Source record and documentation](https://github.com/AndersH3/skill-data-atlas/tree/main/datasets/merlin)


This directory mirrors the unmodified official v1.2 corpus bundles from the Eurac Research CLARIN Centre. Retrieved 29 October 2026. Data/resources are **CC BY-SA 4.0**, as stated in both the repository metadata and source archive license. The project root license does not replace this license.

- Landing page: https://clarin.eurac.edu/repository/xmlui/handle/20.500.12124/59
- Stable handle: https://hdl.handle.net/20.500.12124/59
- Primary API record: https://clarin.eurac.edu/repository/rest/items/44?expand=all
- Project: https://www.merlin-platform.eu/
- Versioned author GitLab: https://gitlab.inf.unibz.it/commul/merlin-platform/data-bundle/-/tags/v1.2
- License legal text: `LICENSE.cc-by-sa-4.0.txt`; original archive license: `upstream-metadata-LICENSE`.
- Provider record: `upstream-repository-record.json`, original unmodified API response; provider MD5 values and newly computed SHA-256 values appear in `manifest.json`.

## Attribution

Credit the MERLIN corpus authors listed in the original `upstream-metadata-README.md`, the MERLIN project partners, and Eurac Research (Institute for Applied Linguistics). The deposit lists Katrin Wisniewski, Andrea Abel, Kateřina Vodičková, Sybille Plassmann, Detmar Meurers, Claudia Woldt, Karin Schöne, Verena Blaschitz, Verena Lyding, Lionel Nicolas, Chiara Vettori, Pavel Pečený, Jirka Hana, Veronika Čurdová, Barbora Štindlová, Gudrun Klein, Louise Lauppe, Adriane Boyd, Serhiy Bykh, and Julia Krivanek.

Reference: Boyd, A., Hana, J., Nicolas, L., Meurers, D., Wisniewski, K., Abel, A., Schöne, K., Štindlová, B., and Vettori, C. (2014). *The MERLIN corpus: learner language and the CEFR*. Proceedings of LREC2014, pp. 1281-1288. https://aclanthology.org/L14-1488/

The EU Lifelong Learning Programme supported the corpus, project 518989-LLP-1-2011-1-DE-KA2-KA2MP. Preserve the original disclaimer, acknowledgements and attribution in source files.

## Contents and codebooks

The mirrored bundles preserve the complete observed learner performances, ratings and manual annotations in several representations. These are copies of the same learner performances, **not independent samples**:

- `merlin-text-v1.2.zip`: human-readable learner texts, metadata and target hypotheses.
- `merlin-metadata-v1.2.zip`: learner/task metadata, CEFR ratings, derived indicators and German complexity measures.
- `merlin-tasks-v1.2.zip`: examination task information.
- `merlin-docs-v1.2.zip`: original annotation, transcription and rating documentation.
- `merlin-exmaralda-v1.2.zip` and `merlin-solr-v1.2.zip`: additional smaller annotation/search representations already retrieved.
- The optional PAULA and relANNIS all-in-one encodings were deliberately not mirrored: the retained plain texts, metadata/ratings, tasks and EXMARaLDA representation already preserve observed skill performance and manual annotation. Those optional encodings add alternative packaging and automatic dependency/NLP annotations; they are not additional human responses. Slow transfers were cancelled, and no partial archives are retained. Both original formats remain available from the source repository.
- `README.html`, `CHANGELOG.html`: provider bundle descriptions and release changes.

For convenient reading, `codebooks/` also contains byte-identical PDFs extracted from the documentation ZIP. `CODEBOOK.project.md` is this project's brief navigation/field guide; it is not an author-supplied replacement codebook.

## Verified version-specific size

The v1.2 metadata CSV has **2,287 rows, 362 columns and 2,287 distinct author IDs**: Czech 441, German 1,033, Italian 813. The v1.2 README and deposit agree on 2,287. The project website's older 2,286 description should not override the actual versioned snapshot. No participant names, answer text or corpus excerpts are reproduced in the research report.

Original bundles remain unmodified. Extraction of documentation PDFs and metadata documentation does not alter their bytes. No scoring or dataset cleaning was performed.

| Payload | Bytes | SHA-256 prefix |
|---|---:|---|
| [merlin-docs-v1.2.zip](https://github.com/AndersH3/skill-data-atlas/blob/main/datasets/merlin/merlin-docs-v1.2.zip) | 5,300,101 | `81d97dc4a090fe30` |
| [merlin-exmaralda-v1.2.zip](https://github.com/AndersH3/skill-data-atlas/releases/download/datasets-2026-10-29/merlin-exmaralda-v1.2.zip) | 18,030,739 | `9113f045f28c0742` |
| [merlin-metadata-v1.2.zip](https://github.com/AndersH3/skill-data-atlas/blob/main/datasets/merlin/merlin-metadata-v1.2.zip) | 602,475 | `1e990c82803a3557` |
| [merlin-solr-v1.2.zip](https://github.com/AndersH3/skill-data-atlas/blob/main/datasets/merlin/merlin-solr-v1.2.zip) | 6,563,942 | `56dd28d9d913a4a8` |
| [merlin-tasks-v1.2.zip](https://github.com/AndersH3/skill-data-atlas/blob/main/datasets/merlin/merlin-tasks-v1.2.zip) | 8,766,318 | `82073cfd03b0f94e` |
| [merlin-text-v1.2.zip](https://github.com/AndersH3/skill-data-atlas/blob/main/datasets/merlin/merlin-text-v1.2.zip) | 12,697,116 | `949f1ef6c22e6602` |

### Much, Mutak, Pohl and Ranger: matrix reasoning under speed and accuracy instructions

**Licence:** CC-BY-4.0. **Selected scope:** Unmodified original main CSV and machine-readable reasoning solutions, with original main and supplemental codebooks; alternative encoding, optional logs and stimulus overviews omitted explicitly.

[Source record and documentation](https://github.com/AndersH3/skill-data-atlas/tree/main/datasets/much-mutak-matrices-2025)


Retrieved 30 October 2026 for Skill Data Atlas. This is an AI-assisted project provenance note.

## Attribution and source

Much, S., Mutak, A., Pohl, S., and Ranger, J. (2025). Data From a Validation Study of Two Psychometric Models on Test-taking Behavior. Journal of Open Psychology Data, 13, 1. https://doi.org/10.5334/jopd.124

Dataset: Modeling speed-ability trade-off and test-taking persistence - Parameter validation for two psychometric models. https://doi.org/10.17605/OSF.IO/9J6HM (https://osf.io/9j6hm/).

## Licence

**CC BY 4.0.** The OSF project's formal licence relationship resolves to https://api.osf.io/v2/licenses/563c1cf88c5e4a3877f9e96a/ and the data paper explicitly states this data licence in section 3.6. The original OSF node, file metadata, licence metadata and full licence text are saved here. Retain attribution, source links and the licence when sharing. This grant does not transfer rights in separate third-party tests or survey wording. The article identifies copyrighted motivational-disposition material that was not republished in its source repository; no such stimulus material has been added here. The repository AGPL does not replace the dataset licence.

## Exact selection

The unmodified original `tte_data.csv` and `mr_itemsolutions.csv` are mirrored. The original CSV and PDF main codebooks and PDF supplemental codebook accompany them. Provider SHA-256 hashes match all five copied files. The main CSV includes the source's questionnaire covariates; retaining its original bytes does not make those variables skill tests. Exclude action orientation, motivation, effort and other self-report measures from the skill-test shortlist.

Omitted source files: the alternative `tte_data.Rds` encoding; optional `mr_logdata.csv`, `ct_pagetimes.csv` and `tte_disruptions.csv`; stimulus/instruction overviews `mr_ItemOverview.pdf`, `ct_ItemOverview.pdf` and `efcm_ItemOverview.pdf`; and `Preregistration_Psychometric-Model-Validation.pdf`. These remain available from OSF. No participant values were changed, no columns were removed, and no test-item figures were copied. This is a selected file mirror, not a complete OSF deposit.

## Verified structure and study design

The downloaded CSV contains 1,244 rows and 164 columns, with 1,244 unique participant IDs. Observed Group counts are 992 in group 1 and 252 in group 2. The author codebook defines group 1 as accuracy/non-speeded instruction first and group 2 as speeded instruction first.

The original study used two distinct 10-item reasoning blocks, with each participant receiving both instruction conditions and randomized instruction order. It did not administer the same 20 items twice. Distinct block items, fixed item order and changing instructions must be accounted for when comparing scores. There is no claim here that this is an equating dataset for two established IQ instruments.

See `manifest.json` for source URLs, byte sizes, provider checksums and local SHA-256 hashes; see `CODEBOOK.project.md` for a guide to the original author documentation.

| Payload | Bytes | SHA-256 prefix |
|---|---:|---|
| [mr_itemsolutions.csv](https://github.com/AndersH3/skill-data-atlas/blob/main/datasets/much-mutak-matrices-2025/original/mr_itemsolutions.csv) | 829 | `e5fb1b59fcafd1cd` |
| [tte_data.csv](https://github.com/AndersH3/skill-data-atlas/blob/main/datasets/much-mutak-matrices-2025/original/tte_data.csv) | 1,634,324 | `288515597704dc92` |

### OpenNeuro ds004636 objective task subset

**Licence:** CC0-1.0. **Selected scope:** 734 BIDS events.tsv files from seven objective tasks; no MRI, surveys or preference tasks

[Source record and documentation](https://github.com/AndersH3/skill-data-atlas/tree/main/datasets/openneuro-ds004636-objective-tasks)


Retrieved: 2026-10-29

License: **CC0-1.0**. The external dataset license remains separate from the parent repository AGPL license.

## Exact objective task selection

ANT, DPX, WATT3, motorSelectiveStop, stopSignal, stroop and twoByTwo. All734 original event files for these tasks are retained in their original BIDS paths. MRI, physiology, surveyMedley and preference/risk/discount tasks are omitted. BIDS event files are unchanged; only ZIP packaging and task selection changed.

## Primary source and license evidence

- https://raw.githubusercontent.com/OpenNeuroDatasets/ds004636/769186fe1b185fae16437f380bfebd56edf7acd7/dataset_description.json
- https://codeload.github.com/OpenNeuroDatasets/ds004636/tar.gz/769186fe1b185fae16437f380bfebd56edf7acd7
- https://raw.githubusercontent.com/OpenNeuroDatasets/ds004636/769186fe1b185fae16437f380bfebd56edf7acd7/CHANGES
- https://raw.githubusercontent.com/OpenNeuroDatasets/ds004636/769186fe1b185fae16437f380bfebd56edf7acd7/README.md
- https://raw.githubusercontent.com/OpenNeuroDatasets/ds004636/769186fe1b185fae16437f380bfebd56edf7acd7/participants.json
- https://raw.githubusercontent.com/OpenNeuroDatasets/ds004636/769186fe1b185fae16437f380bfebd56edf7acd7/participants.tsv
- https://raw.githubusercontent.com/OpenNeuroDatasets/ds004636/769186fe1b185fae16437f380bfebd56edf7acd7/task-ANT_events.json
- https://raw.githubusercontent.com/OpenNeuroDatasets/ds004636/769186fe1b185fae16437f380bfebd56edf7acd7/task-DPX_events.json
- https://raw.githubusercontent.com/OpenNeuroDatasets/ds004636/769186fe1b185fae16437f380bfebd56edf7acd7/task-WATT3_events.json
- https://raw.githubusercontent.com/OpenNeuroDatasets/ds004636/769186fe1b185fae16437f380bfebd56edf7acd7/task-motorSelectiveStop_events.json
- https://raw.githubusercontent.com/OpenNeuroDatasets/ds004636/769186fe1b185fae16437f380bfebd56edf7acd7/task-stopSignal_events.json
- https://raw.githubusercontent.com/OpenNeuroDatasets/ds004636/769186fe1b185fae16437f380bfebd56edf7acd7/task-stroop_events.json
- https://raw.githubusercontent.com/OpenNeuroDatasets/ds004636/769186fe1b185fae16437f380bfebd56edf7acd7/task-twoByTwo_events.json
- https://raw.githubusercontent.com/spdx/license-list-data/main/text/CC0-1.0.txt

## Integrity

See manifest.json for original source URLs, byte sizes and SHA-256 checksums. For repackaged subsets, every original member has its own source path and hash. Provider checksums or Git blob hashes were compared where available. No publisher article PDF was copied.

## Observed source-file coverage

734 event files from110 distinct source subject IDs. Per-task file counts: WATT3 107, stopSignal106, twoByTwo107, DPX103, motorSelectiveStop104, stroop103 and ANT104. These include incomplete/partial administrations and are not usable sample-size counts. The descriptor reports103 study completers; apply supplied exclusions and missingness checks.

| Payload | Bytes | SHA-256 prefix |
|---|---:|---|
| [objective-task-events.zip](https://github.com/AndersH3/skill-data-atlas/blob/main/datasets/openneuro-ds004636-objective-tasks/original/objective-task-events.zip) | 2,331,899 | `b3970a91f6c02a80` |

### SAPA cognitive ability: psychTools ability / iqitems

**Licence:** GPL-2.0-or-later. **Selected scope:** Affirmative package-wide GPL (>=2) grant, with no contrary data-specific restriction found; exact unmodified source objects and documentation preserved. Only `ability.rda` and `iqitems.rda`: two representations of the same 1,525 people×16 cognitive items, plus their codebooks. The current full ICAR archive and its separate access terms are outside this mirror.

[Source record and documentation](https://github.com/AndersH3/skill-data-atlas/tree/main/datasets/sapa-ability-iqitems)


Source package: **psychTools 2.6.4**, as distributed by `cran/psychTools` at commit `7dc591f8ac11c0ef1764cf853f3065aa60653d09`. Retrieved 2026-10-29.

Declared license: **GPL (>=2)**, represented here as SPDX **GPL-2.0-or-later**. `upstream-DESCRIPTION` is the unmodified formal package license declaration. `LICENSE.GPL-2.0-or-later.txt` supplies the full GPLv2 license text with the later-version option retained. These external files keep their upstream GPL license; the parent repository's AGPL license does not replace it.

## Redistribution basis

The R developers' package specification treats DESCRIPTION License as the package's license. No separate copyright/license carveout for these response objects was found in the inspected source tree, data documentation or package metadata. CRAN policy requires clarity of rights for all package components and maintainer authorization; it expressly recognizes `.rda` files as source or readily convertible to source. Accordingly this mirror relies on the affirmative package-wide GPL grant, rather than requiring redundant per-file license headers. This is a source-object mirror, not a claim that raw data values or every original test stimulus necessarily carry copyright.

Primary package declaration: https://github.com/cran/psychTools/blob/7dc591f8ac11c0ef1764cf853f3065aa60653d09/DESCRIPTION
Package source: https://github.com/cran/psychTools/tree/7dc591f8ac11c0ef1764cf853f3065aa60653d09
R package license specification: https://cran.r-project.org/doc/manuals/r-release/R-exts.html#Licensing
CRAN all-component rights/source policy: https://cran.r-project.org/web/packages/policies.html
Canonical GPLv2: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html
License text transcription source: https://raw.githubusercontent.com/spdx/license-list-data/main/text/GPL-2.0-or-later.txt

## Attribution and data provenance

Package author/maintainer: William Revelle. Data documentation explicitly attributes collection to Revelle with David Condon, 8-31 August 2012, within the SAPA project. Cite Condon & Revelle (2014), The International Cognitive Ability Resource: Development and initial validation of a public-domain measure, Intelligence 43, 52-64, together with the versioned psychTools package and its original documentation. Original dataset information: https://www.sapa-project.org/.

## Exact mirrored scope and test-content boundary

Only `ability.rda` and `iqitems.rda`: two representations of the same 1,525 people × 16 cognitive items, plus their codebooks. The current full ICAR archive and its separate access terms are outside this mirror.

The original `.rda` files are unchanged source-distribution data objects, editable after loading in R; no executable package code or compiled binary is included. The original author `.Rd` documentation is included unchanged as the codebook. No new observations or scores were generated. No unrelated personality datasets, secure question bank, test artwork, commercial test handbook or publisher article PDF is mirrored. Permission to redistribute these packaged response objects is not a grant to administer or republish a separate current test bank.

## Source availability and GPL notices

GPLv2 section 1 permits verbatim source copies with the applicable notices, warranty disclaimer and license copy retained. The original data objects, relevant Rd source documentation and DESCRIPTION provided here are the material being redistributed; R can load them directly using `load()`. The `.rda` files are the preferred form supplied in the upstream **source** distribution, not compiled executable versions needing a separate opaque binary/source offer. The upstream full package source remains linked above for context; unrelated package datasets are not required to inspect or modify these numeric response objects.

Redistributors should retain the upstream license/attribution, source links and no-warranty notices. Any covered modifications must be identified with dates and distributed under the applicable GPL terms; retain the original >=2 option. See the full license for its conditions rather than treating this summary as the license. The project-generated `read-data.R` is a convenience example for reading the preserved source objects, not a replacement for them.

| Payload | Bytes | SHA-256 prefix |
|---|---:|---|
| [ability.rda](https://github.com/AndersH3/skill-data-atlas/blob/main/datasets/sapa-ability-iqitems/original/ability.rda) | 13,019 | `64e1c8c8a70662b5` |
| [iqitems.rda](https://github.com/AndersH3/skill-data-atlas/blob/main/datasets/sapa-ability-iqitems/original/iqitems.rda) | 9,972 | `97e70070d17ff140` |

### SemEval 2013 Task 7 BEETLE / SemEval 2013 Task 7 SciEntsBank

**Licence:** CC-BY-SA-3.0. **Selected scope:** Explicit primary redistribution license verified; unmodified source payload, full license, attribution/source links, checksums and codebooks retained.

[Source record and documentation](https://github.com/AndersH3/skill-data-atlas/tree/main/datasets/semeval2013-task7)


This directory mirrors the **unmodified original five-way release**, covering both catalogue entries `semeval2013_beetle` and `semeval2013_scientsbank`. Retrieved 29 October 2026.

- Provider/organizer: Myroslava Dzikovska and collaborators; original corpora collected by Myroslava Dzikovska (University of Edinburgh) and Rodney Nielsen (University of North Texas).
- Source repository: https://github.com/myrosia/semeval-2013-task7
- Direct archive: https://raw.githubusercontent.com/myrosia/semeval-2013-task7/main/semeval-5way.zip
- License evidence and full legal text: `LICENSE.cc-by-sa-3.0.txt`, copied verbatim from the organizer repository. The license is **Creative Commons Attribution-ShareAlike 3.0 Unported**. The project root license does not replace it.
- Original author README: `upstream-README.md`.
- Codebook: `CODEBOOK.project.md` is a project-written structural field guide, not an original-author codebook; it links the original task specification. XML data and original supplied metadata remain inside the archive.
- Checksums and provenance: `manifest.json`.

## Required attribution

Dzikovska, M. O., Nielsen, R., Brew, C., Leacock, C., Giampiccolo, D., Bentivogli, L., Clark, P., Dagan, I., and Dang, H. T. (2013). *SemEval-2013 Task 7: The Joint Student Response Analysis and 8th Recognizing Textual Entailment Challenge*. Proceedings of the 7th International Workshop on Semantic Evaluation, pp. 263-274. https://aclanthology.org/S13-2045/

Dzikovska, M., Nielsen, R., and Leacock, C. (2015/2016). *The joint student response analysis and recognizing textual entailment challenge: making sense of student responses in educational applications*. Language Resources and Evaluation. https://doi.org/10.1007/s10579-015-9313-8

## Integrity and use notes

The ZIP includes overlapping **Core** and **Extra** representations plus separate reliability material. Do not concatenate all XML files as independent observations. Preserve the official unseen-answer and unseen-question evaluation partitions; unseen-domain evaluation is SciEntsBank-only. Selected answer rows are not distinct examinees. No response-time variable was established. No transformed dataset is included.

| Payload | Bytes | SHA-256 prefix |
|---|---:|---|
| [semeval-5way.zip](https://github.com/AndersH3/skill-data-atlas/blob/main/datasets/semeval2013-task7/semeval-5way.zip) | 12,983,203 | `57c14e5c260d8cfd` |

### Self-Regulation Ontology objective performance-task subset

**Licence:** CC-BY-4.0. **Selected scope:** 23 objective tasks, complete and retest phases; original per-task gzip members untouched

[Source record and documentation](https://github.com/AndersH3/skill-data-atlas/tree/main/datasets/sro-performance-tasks)


Retrieved: 2026-10-29

License: **CC-BY-4.0**. The external dataset license remains separate from the parent repository AGPL license.

## Exact objective task selection

- adaptive_n_back
- attention_network_task
- choice_reaction_time
- digit_span
- directed_forgetting
- dot_pattern_expectancy
- go_nogo
- hierarchical_rule
- keep_track
- local_global_letter
- motor_selective_stop_signal
- psychological_refractory_period_two_choices
- recent_probes
- shape_matching
- shift_task
- simon
- simple_reaction_time
- spatial_span
- stim_selective_stop_signal
- stop_signal
- stroop
- threebytwo
- tower_of_london

Both complete and retest phase files are retained. Selection and ZIP packaging are the only changes; every original gzip member is unmodified. Excluded are surveys, preferences, risky choice, discounting and ancillary demographic tables. Raven/CRT files are omitted to keep stimulus-content rights narrow.

## Primary source and license evidence

- https://github.com/IanEisenberg/Self_Regulation_Ontology/blob/4e6e837fb5aaca87ed5914fd9be251156f43eec9/README.md#license
- https://github.com/IanEisenberg/Self_Regulation_Ontology/tree/4e6e837fb5aaca87ed5914fd9be251156f43eec9/Data/Complete_02-16-2019
- https://github.com/IanEisenberg/Self_Regulation_Ontology/tree/4e6e837fb5aaca87ed5914fd9be251156f43eec9/Data/Retest_02-16-2019
- https://raw.githubusercontent.com/IanEisenberg/Self_Regulation_Ontology/4e6e837fb5aaca87ed5914fd9be251156f43eec9/Data/README.md
- https://raw.githubusercontent.com/IanEisenberg/Self_Regulation_Ontology/4e6e837fb5aaca87ed5914fd9be251156f43eec9/Data/Complete_02-16-2019/README.txt
- https://raw.githubusercontent.com/IanEisenberg/Self_Regulation_Ontology/4e6e837fb5aaca87ed5914fd9be251156f43eec9/Data/Retest_02-16-2019/README.txt
- https://raw.githubusercontent.com/spdx/license-list-data/main/text/CC-BY-4.0.txt

## Integrity

See manifest.json for original source URLs, byte sizes and SHA-256 checksums. For repackaged subsets, every original member has its own source path and hash. Provider checksums or Git blob hashes were compared where available. No publisher article PDF was copied.

| Payload | Bytes | SHA-256 prefix |
|---|---:|---|
| [Complete_02-16-2019-objective-tasks.zip](https://github.com/AndersH3/skill-data-atlas/releases/download/datasets-2026-10-29/Complete_02-16-2019-objective-tasks.zip) | 56,562,944 | `63bea957f44bb7c7` |
| [Retest_02-16-2019-objective-tasks.zip](https://github.com/AndersH3/skill-data-atlas/releases/download/datasets-2026-10-29/Retest_02-16-2019-objective-tasks.zip) | 16,481,482 | `bf8c60ad0c28024b` |



# 4. Cognitive ability and performance


Initial 11 profiles verified 29 October 2026. Seven additional profiles and the older report's IQ1 comparison were checked on 30 October in the [linking and integration chapter](linked-tests-and-legacy-integration.md). Scope: observed human responses to tasks with objectively assessable performance. Personality, preference, symptom, and other self-report columns in mixed datasets are outside scope. This is a source catalogue; raw participant data and test items should remain with their providers unless reuse rights have been established.

## Best starting points

- **SAPA `ability`/`iqitems`**: compact, documented binary and selected-option matrices; especially convenient for checking alternative scoring and item models.
- **OpenPsychometrics VIQT and MGKT**: larger samples with raw selected answers and explicit scoring; useful for penalties, omissions, partial credit, and answer-option analyses. Public download is established; a blanket data redistribution licence was not established from the inspected pages/codebooks.
- **Ganis–Kievit mental rotation**: particularly clear CC BY 4.0 coverage of both data and stimuli, with actual behavioural validation data.
- **Self-Regulation Ontology task subset**: trial-level accuracy/latency and a retest cohort; useful for testing score stability. Exclude its surveys and preference-based decisions from a strict skill-test analysis.
- **OpenNeuro ds004636 performance tasks**: CC0 event data with documented quality exclusions; select attention, interference, inhibition, and planning tasks, and exclude survey and preference tasks.

These priorities are research judgments about usefulness for scoring work, not claims that the instruments are interchangeable or suitable for individual decisions.

## 1. SAPA cognitive ability: `psychTools::ability` and `iqitems`

**Data:** 1,525 people, 16 items spanning verbal/basic reasoning, letter series, matrix reasoning, and spatial rotation. `iqitems` preserves chosen options; `ability` supplies correct/incorrect coding. These are two representations of the **same observations**, not independent replications. `iqitems` documentation includes a 16-element answer key and demonstrates converting zero responses to missing before scoring. Timing is not documented in these objects. Useful for nominal response models, classical scoring, IRT, missingness, and multidimensionality. The maintainer flags nonmonotonic traces for two matrix items. **Verification:** exact upstream source objects acquired and loaded in native R; both response representations are 1,525 ×16. **Access:** public R package, no registration. **Rights:** the original packaged response objects and author documentation are covered by the formal package-wide GPL (>=2) grant; no contrary data notice was found. Exact source objects are mirrored with the full licence and pinned metadata. Separate proprietary stimuli and the current ICAR bank are not covered by that conclusion. [Current ability documentation](https://raw.githubusercontent.com/cran/psychTools/master/man/ability.Rd), [iqitems documentation and key](https://raw.githubusercontent.com/cran/psychTools/master/man/iqitems.Rd), [package licence](https://raw.githubusercontent.com/cran/psychTools/master/DESCRIPTION).

## 2. OpenPsychometrics Vocabulary IQ Test (VIQT)

**Data/file verified:** 12,173 records, 131 columns; 45 objective synonym questions, selected-answer codes, 45 `E` fields, and published total scores. The codebook defines `-1` as “don't know” and `0` as unanswered; ten positive bitmask codes identify the selected word pair. The historical formula is `score_right - 0.35 * score_wrong`. Item wording and keys are in the ZIP. `E1`–`E45` are present, but their units were not defined in the inspected codebook; do not silently assume milliseconds. Good for omission-versus-error rules, guessing penalties, distractor models, and subgroup robustness. **Limitations:** voluntary online sample, includes only supplemental-survey completers, English vocabulary depends on language exposure. Exclude supplemental personality columns. **Rights:** data and item redistribution licence not specified in inspected source/codebook. [Official test and caveats](https://openpsychometrics.org/tests/VIQT/), [download and codebook](https://openpsychometrics.org/_rawdata/VIQT_data.zip).

## 3. OpenPsychometrics Multifactor General Knowledge Test (MGKT, 2017–2018 data)

**Data/file verified:** 19,218 records; 32 multi-select questions, each with ten options and five keyed correct options. `QxA` stores selected answers, `QxS` the historical question score, `QxE` milliseconds, and `QxI` presentation position. Keys and wording are supplied. This is a **32-question test with dependent option judgments**, not 320 independent questions. The ZIP defines `QxS = selected correct - selected incorrect`. The current MGKT2 webpage instead describes a 1.25-point wrong-answer penalty; preserve version-specific rules. Good for partial credit, penalties, speed, order effects, and local dependence. **Limitations:** cultural/US knowledge dependence and minimally cleaned volunteer data; ages below 13 excluded at source. **Rights:** no clear data/item redistribution licence established. [Historical data and codebook](https://openpsychometrics.org/_rawdata/MGKT_data.zip), [current form, with different scoring](https://openpsychometrics.org/tests/MGKT2/).

## 4. OpenPsychometrics experimental matrix IQ test (IQ1)

**Data/file verified:** 400 records × 28 columns: `Q1`–`Q25`, `score`, `gender`, `age`. ZIP includes matrix and answer images. `10` marks the keyed image; `1`–`7` identify distractor images, independent of randomly assigned screen position. Zero values occur but are not explained in the inspected original codebook; retain them distinctly pending resolution. No latency fields. Good small selected-option matrix for scoring and distractor diagnostics. **Limitations:** developer explicitly describes mediocre data-collection quality; small, self-selected sample; not a commercial Raven test and not population norms. **Rights:** no explicit licence established for data/images in the inspected ZIP or index. [Official ZIP and original codebook](https://openpsychometrics.org/_rawdata/IQ1.zip), [printable instrument](https://openpsychometrics.org/printable/intelligence-quotient-test.pdf).

## 5. OpenPsychometrics Full Scale IQ alpha v0.1

**Data/file verified:** 3,194 records × 61 columns. Historical alpha contains **19 composite questions**: seven vocabulary, six rotation, six short-term memory. Each records a score (`s`), selected answers (`a`), and elapsed milliseconds (`e`); CSV uses commas and quoted answer lists. Correct selections gain one point and incorrect selections lose one. Demo HTML/JavaScript and stimulus JSON are included. This is different from the current six-section online test. Useful for multi-select partial credit and speed–accuracy methods across three task types. **Limitations:** alpha instrument and self-selected unsupervised participants; source filters donors who reported research-suitable data and apparent repeat attempts. **Rights:** no clear data/item redistribution licence established from inspected archive. [Versioned alpha data, codebook and demo](https://openpsychometrics.org/_rawdata/FSIQ_0.1_data.zip), [current test](https://openpsychometrics.org/tests/FSIQ/).

## 6. Exposure Based Face Memory Test (EBFMT)

**Data/file verified:** parsed **1,768 records × 275 columns**; the index advertises 1,769, so record this discrepancy rather than silently choosing one. `Q1`–`Q75`: new/seen responses, coded 1/2; `LAPSE1`–`LAPSE75`: milliseconds. The inspected codebook does not supply the correct old/new sequence, so establish the key before accuracy rescoring. Useful as a latency/recognition pipeline example, with mixed personality columns excluded. **Major limitation:** developer reports statistical/conceptual problems and recommends the Cambridge Face Memory Test over this instrument. **Rights:** developer specifies copyrighted photographs free for research use, with other instrument parts CC BY 4.0; a distinct response-data licence was not established. Avoid copying the photos into a general open repository. [Data/codebook](https://openpsychometrics.org/_rawdata/EBFMT.zip), [development and licence](https://openpsychometrics.org/tests/EBFMT/development/).

## 7. Ganis–Kievit mental rotation validation dataset

**Data:** real behavioural validation sample of 54 participants, with 384 available 3D stimuli. This is a response dataset **plus** stimuli, not merely an item bank. Trial-level behaviour supports angular-disparity, accuracy and latency analyses; demographics are included. **Access:** public Figshare downloads; record has two files both named `Behavioural_data.zip`, so pin file ID/checksum rather than filename alone. API metadata, archive structure and embedded original file description verified. Per-participant XLSX files retain trial/stimulus, desired and actual responses, latency, angle and correctness. Timeouts are N/A and scored incorrect; filtered latency summaries are separate from raw trials. Workbook values were not parsed. **Rights:** Figshare record explicitly CC BY 4.0 for the deposited data/stimuli; cite Ganis & Kievit (2015). Strong source for studying spatial performance and condition-dependent difficulty, although the sample is small and task-specific. [Dataset DOI and licence](https://doi.org/10.6084/m9.figshare.1045385), [behaviour description](https://ndownloader.figshare.com/files/1878074), [behaviour archive file 3702010](https://ndownloader.figshare.com/files/3702010), [paper](https://doi.org/10.5334/jopd.ai).

## 8. Self-Regulation Ontology (performance-task subset only)

**Data:** 522 participants completed a battery of 37 behavioural tasks and 22 surveys; 150 completed retesting. Authors explicitly provide raw trial-by-trial and processed data. **Included scope:** objectively scored cognitive tasks such as choice reaction time and stop signal; use task-specific accuracy, response times, and scoring code. Exclude self-report surveys, discounting preferences, and risk-taking choices from a strict skills catalogue. **Access:** public GitHub data, with dated releases. **Rights:** repository states data CC BY 4.0; individual experimental-code/stimulus licences not fully audited. **Verification:** article/repository documentation, no full raw archive parsed. **Use:** compare score stability and speed–accuracy scoring with participant-level train/test splits. **Limitations:** browser/MTurk measurement, varied task reliability, missingness and differing cleaning/imputation stages. Use raw trials for rescoring; do not confuse the imputed derived-variable matrix with independent item responses. [Paper and data availability](https://pmc.ncbi.nlm.nih.gov/articles/PMC6534563/), [data release](https://github.com/IanEisenberg/Self_Regulation_Ontology/tree/master/Data/Complete_02-16-2019), [repository licence statement](https://github.com/IanEisenberg/Self_Regulation_Ontology), [retest paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC6431228/).

## 9. OpenNeuro ds004636: objective task subset

**Data:** 103 study completers; behavioural event files accompany an fMRI dataset. Select ANT, cued task switching, DPX, Stroop, stop-signal variants and tower planning. Exclude survey medley and preference-based card/discounting tasks. Raw/cleaned behavioural files are separately hosted on OSF. **Access:** public OpenNeuro BIDS `events.tsv` plus task JSON, and OSF project. **Rights:** dataset's own `dataset_description.json` states **CC0**, independently of the paper's CC BY licence. Stimulus/code rights require separate review. **Verification:** descriptor and dataset metadata; event payloads not parsed. **Use:** task-specific latency/accuracy models and cleaning robustness. **Limitations:** in-scanner procedures differ from ordinary testing; 103 is not the usable N for every task. Authors recommend 12 full exclusions and 23 partial exclusions; 68 have no recommended behavioural exclusion. [Descriptor](https://pmc.ncbi.nlm.nih.gov/articles/PMC11271451/), [versioned data](https://openneuro.org/datasets/ds004636/versions/1.0.4), [CC0 metadata](https://raw.githubusercontent.com/OpenNeuroDatasets/ds004636/master/dataset_description.json), [raw behaviour OSF](https://osf.io/sjvnw/).

## 10. Working Memory Develops at a Similar Rate Across Diverse Stimuli

**Data/file verified:** both original version-1 CSVs were acquired and parsed: `dat_all` has 3,564 rows and 16 columns; the participant-collapsed file has 99 rows and 23 columns. The `name` field contains 99 numeric participant codes. Semicolon delimiters and original line endings are retained. Author metadata describes all-or-nothing and partial-credit unit scoring. **Access:** Mendeley Data v1, DOI 10.17632/kfc3jyggs7.1, through its public API. **Rights:** dataset CC BY 4.0; separate stimulus rights not audited. No separate author codebook was deposited, so author metadata and a labelled project field guide accompany the originals. **Use:** compare span-scoring representations with care about aggregation and repeated observations. Exact item-count and timing semantics remain unresolved; “raw” does not establish response-time availability. [Official dataset and licence](https://data.mendeley.com/datasets/kfc3jyggs7/1).

## 11. Current ICAR full materials: academically restricted candidate

The current archive (published 2 June 2026) contains tests, psychometric data and automatic generators. Its **1.05 GB main ZIP is Sharing Level 1 / Scientific Use License v1**; only the public README is CC BY 4.0. The official FAQ restricts use to academic research/teaching, requires project registration, and prohibits broad public distribution of materials. It reports psychometric data from an online sample but no population norms. Archive response dimensions and exact fields were not independently inspected. Treat this as **conditional access**, not a freely redistributable dataset; historical “public-domain” paper titles do not establish the current archive's terms. The separately distributed SAPA package example above remains a distinct source. [Current archive](https://doi.org/10.23668/psycharchives.22167), [official ICAR FAQ](https://icar-project.com/), [Scientific Use License record](https://www.psycharchives.org/en/item/7466aa16-69bd-49ea-baef-7f828f5b223f).

## File verification manifest

Downloads were inspected in memory on 29 October 2026, with Python standard-library `zipfile` and `csv`; no participant rows are reproduced here. Values below describe downloaded snapshots, not guaranteed permanent upstream content. No formal validity analysis, participant deduplication, or licence clearance was performed.

| Archive | Parsed rows | Columns | SHA-256 |
| --- | ---: | ---: | --- |
| IQ1.zip | 400 | 28 | `99e3a918c0f3452ea25c38788bfa713b34a49f4370529dc0591cc4fc12ec2743` |
| VIQT_data.zip | 12,173 | 131 | `dfeda357d8e5eba931d7cfe7b2a3e3cca3364ee782f7f9f480e392f3b2e6ed2c` |
| MGKT_data.zip | 19,218 | 137 header fields | `bcf5b135ed1116c08da7470875f7f30d5d37118785a66c271c89198e12ceef24` |
| EBFMT.zip | 1,768 | 275 | `adfaa0cd2eadfcb053d53c75109c01175df90fe688c62a28d20f33b66c8d60e1` |
| FSIQ_0.1_data.zip | 3,194 | 61 | `6ac2deb7aa6913dc7f5c8141a48d6cc3035403eb07d5db411827505c46696135` |
| Ganis behavioural file 3702010 | Workbook values not parsed | Original schema inspected | `3b56dde3defc36d54c85b671f83ade2f7ded685b326be973583ad115bb994e03` |

IQ1 uses comma-separated data; VIQT and EBFMT use tabs despite `.csv` names. MGKT and FSIQ use commas with quoted selected-answer lists. Preserve response codes and separate original scoring from newly derived scoring.


# 5. Linking tests and integration of earlier research


Supplementary review: **30 October 2026**. The earlier [Candidate Datasets report](../older_reports/Candidate%20Datasets.docx) is preserved unchanged, with its [file identity and provenance](../older_reports/README.md). Its recoverable DOI links were treated as discovery leads. Embedded line-number citation tokens have no source map in the Word file and were replaced by new primary references in this chapter. The earlier document's authorship and complete AI-generation history are not documented.

## What the earlier report contributes

The earlier report asks a more specific question than the broad skill-data search: can responses from the same people connect different instruments, subtests or test conditions? It adds useful reasoning, spatial and eye-tracking candidates and motivates an explicit linking design. Its strongest two-form recommendation does not survive the primary-source check. Music Ensemble's Raven sets form one timed administration; Much and colleagues' matrices form two differently instructed blocks of different matched items. Both can support useful measurement research, but neither establishes interchangeable scores on two independently administered established IQ tests.

The current catalogue retains the already inspected OpenPsychometrics IQ1 entry, adds distinct earlier-report source versions, and keeps IRW as a discovery resource. Historical SAPA/ICAR response data are separated from the compact psychTools objects and the conditional current ICAR archive. Shared people, matched musician/nonmusician pairs, alternate item blocks and repeat administrations are different structures; the word "paired" must identify which structure is meant.

## Which designs support which analyses

| Design | What it permits | What still needs checking |
|---|---|---|
| Common people completing multiple tasks | Joint calibration, associations, dimensionality and prediction across tasks | Stable IDs, overlapping observations, construct alignment, missingness and order effects |
| Different forms sharing anchor items | Placement on a common metric under an anchor design | Identical content/scoring, sufficient overlap and anchor invariance across groups |
| Different blocks under different instructions | Study of instruction, block and item effects | Counterbalancing, position/fatigue, matched-item assumptions and condition-specific parameters |
| Repeated administrations | Retest stability and change | Practice, memory, interval, attrition and time-varying ability |
| Matched people from different groups | Covariate-controlled group comparison | A matched pair is two different people; it is not a within-person retest |

These are analysis recommendations, not fitted results. A relevant Crane et al. (2008) paper illustrates common-item co-calibration of four cognitive screening instruments, with checks for differential item functioning. Its methods do not require every person to take every instrument. The older document's abbreviated Crane citation does not uniquely identify a paper or establish a public NACC response file. Treat it as a [methodological reference](https://pmc.ncbi.nlm.nih.gov/articles/PMC2762121/), rather than a new downloadable response collection.

A correlation, a shared participant ID or a common IRT scale does not alone justify equating. Before interpreting scores as interchangeable, establish the intended construct, population, administration, precision and invariance. Use stable source IDs and item/condition/order metadata; estimate linking transformations on training observations and check held-out people and subgroups. The earlier search did not establish a public item-level WAIS-to-Raven crosswalk. That is a dated search result, not proof that no such dataset exists.

## Reconciliation of the older claims

| Earlier candidate or claim | Integrated treatment |
|---|---|
| Music Ensemble as two parallel Raven/CFT20-R forms | Corrected to one timed Raven block; retained as a common-person task battery. CFT20-R belongs to TüEyeQ. |
| Mutak and Much as the same test repeated twice | Corrected to two matched ten-item blocks with changed instructions; 20 main items in total. |
| TüEyeQ figshare DOI as participant-data download | Corrected to a metadata record; Harvard Dataverse is the participant-data repository. Version conflicts remain explicit. |
| HCP as only one test per person | Corrected: the full HCP battery has multiple tasks. Its EDMdata Penn export drops the joining identifier. |
| OpenPsychometrics IQ1 as public domain | Existing inspected 400 by 25 response entry retained; an explicit redistribution licence remains unestablished. |
| Revised PSVT:R and SPM-LS as CC BY 4.0 | Counts are checked against package documentation; data and separate stimulus rights are assessed individually below. |
| SAPA/ICAR as roughly 97,000 complete paired tests | Historical release identified separately; planned item missingness prevents treating it as two complete tests per person. |
| Only two sources can support links | Withdrawn as a blanket conclusion: existing SRO/OpenNeuro batteries and historical SAPA also require source-specific overlap checks. |
| IRW's dataset count and Crane citation | IRW retained as a changing discovery resource; Crane retained as methods, without inventing a public data grant. |

## Additional source profiles

### Music Ensemble cognitive battery

The [Music Ensemble project](https://osf.io/y97t3/) provides objective tasks sharing participant IDs, including Raven matrices, span tasks, updating and music perception. The original OSF archive is [analysis.zip](https://osf.io/download/dk4eb/); the project API specifies [CC BY-NC 4.0](https://api.osf.io/v2/licenses/60bf992258510b0009a5a9a6/). Stimulus rights remain separate. Personality and self-report outcomes are outside this review's skill scope.

Selected original ZIP members were inspected by byte ranges, without downloading the full 92.8 MB archive. `raven.csv` has 1,438 records, 59 columns and 47 binary correctness fields. One field, `S1M02correct`, is a retained practice item: excluding it reproduces the clean Raven score for every record. The clean file has 1,274 matched records, or 637 pairs; the current abstract/OSF description instead claims 678 pairs. Preserve this discrepancy.

The [2026 data descriptor](https://doi.org/10.1038/s41597-026-06654-0) describes one ten-minute Raven block combining ten Set I items with 36 Set II items. This corrects the older report's parallel-test interpretation. Common people support joint calibration and dimensionality research; they do not by themselves establish score interchangeability. The Raven CSV retains IP-like collection fields and experimenter identifiers. Keep the source linked pending an explicit field-minimization decision; do not mirror the mixed archive wholesale.

### Much, Mutak, Pohl and Ranger matrices study

The [2025 data descriptor](https://doi.org/10.5334/jopd.124) and [OSF deposit](https://doi.org/10.17605/OSF.IO/9J6HM) describe 1,244 people completing two distinct ten-item reasoning blocks, each under a different speed/accuracy instruction. Instruction order was randomized between groups; the inspected CSV has group counts 992/252. These are different matched items, not the same 20-item test repeated. Speed emphasis did not impose a hard reasoning-test deadline.

The original `tte_data.csv` was parsed as **1,244 rows by 164 columns**, with unique IDs. `X_MR` fields retain figural-element selection vectors, `Y_MR` fields binary scores, and `T_MR` fields milliseconds. Training, masking, unsolvable persistence and concentration tasks have separate meanings. The original author codebooks define these fields.

Selected unchanged [response and solution files](../datasets/much-mutak-matrices-2025/SOURCE.md) are mirrored under the formal **CC BY 4.0** data grant, with original codebooks, licence text and matching provider SHA-256 values. Alternative formats, optional logs and stimulus overviews are omitted explicitly. Self-report covariates remain in the unchanged source CSV but stay outside the skill shortlist. This is useful for condition-sensitive scoring and common-person block models; fixed item order, block content, instruction effects, floor effects and unsupervised timing qualify naive score comparisons.

### TüEyeQ CFT performance and eye tracking

The [data paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC8208979/) describes 315 participants completing a CFT 20-R battery with four subtests. It reports 56 presented tasks, binary correctness, omitted responses and six technically problematic items marked missing. Gaze coverage is smaller: 229 participants in raw gaze files and 186 in task-split gaze files. This is a multidomain battery; full-test equating is not demonstrated.

The older [figshare record](https://api.figshare.com/v2/articles/14173244) contains metadata files, rather than participant responses. The actual participant repository is [Harvard Dataverse, DOI 10.7910/DVN/JGOCKI](https://doi.org/10.7910/DVN/JGOCKI). Its [registered version-2 metadata](https://api.datacite.org/dois/10.7910/DVN/JGOCKI) describes 41 tasks, conflicting with the paper. **The discrepancy is unresolved:** live Dataverse access returned a robot challenge/403, so response files were not parsed. Neither count is presented as a current file-verified width.

The paper and deposit metadata specify **CC0** for data; rights to separate CFT stimuli are not inferred. The source remains linked with acquisition pending access. Additional executive-control data are described as available on request, rather than established in the public deposit. Timing and eye-tracking analyses must preserve the source's clock, cleaning and task definitions.

### HCP Penn Matrices in edmdata

The [edmdata documentation](https://tmsalab.github.io/edmdata/reference/items-hcp-penn.html) describes two alternative **1,201 by 24** correctness matrices. One preserves structural missingness after a five-consecutive-error stopping rule; they are representations of the same people. Five entirely nonresponding subjects were removed. The [pinned builder](https://raw.githubusercontent.com/tmsalab/edmdata/3c0036e4a665b61adde011aac2215b62bd5da33d/data-raw/hcp-penn-matrix/hcp_penn_matrix_build.R) drops the original HCP subject identifier. The export alone therefore cannot reliably join other HCP outcomes.

The [broader HCP battery](https://www.humanconnectome.org/study/hcp-young-adult/document/quick-reference-open-access-vs-restricted-data) contains multiple cognitive tasks, correcting the older report's single-test claim. Obtaining a source-authorized identifier mapping and the relevant item-level outcomes is separate from downloading one matrix.

The [upstream data-use terms](https://www.vps.humanconnectome.org/study/hcp-young-adult/data-use-terms) require every Open Access data user, including recipients of shared copies, to register and agree. The package's MIT declaration does not remove these conditions. Keep this source linked without an unrestricted mirror; no agreement was accepted on the user's behalf. Package documentation and build code were inspected; the response objects were not loaded in this check. Discontinuation and family-related sampling require analysis-specific treatment.

### Revised PSVT R response matrix

The [source documentation](https://tmsalab.github.io/edmdata/reference/items_revised_psvtr.html) identifies a revised Purdue spatial-rotation test response matrix. Native R inspection of the [pinned package object](https://raw.githubusercontent.com/tmsalab/edmdata/3c0036e4a665b61adde011aac2215b62bd5da33d/data/items_revised_psvtr.rda) confirmed **516 rows by 30 columns**, only 0/1 values and no missing cells. It contains scored correctness, rather than selected distractors; no timing or second-instrument linkage was established.

The [package metadata](https://raw.githubusercontent.com/tmsalab/edmdata/3c0036e4a665b61adde011aac2215b62bd5da33d/DESCRIPTION) and [full licence](https://raw.githubusercontent.com/tmsalab/edmdata/3c0036e4a665b61adde011aac2215b62bd5da33d/LICENSE.md) declare MIT. The earlier report's CC BY 4.0 attribution was not established for this packaged object. Rights to the separate PSVT:R test instrument and stimulus figures are distinct. The [exact source object and author documentation](../datasets/edmdata-revised-psvtr/SOURCE.md) are mirrored with MIT notices; no instrument figures are copied. This small binary matrix supports IRT and factor-model prototypes; it supplies no demonstrated common-person bridge to another instrument.

### SPM LS final series response data

The [edmdata object](https://tmsalab.github.io/edmdata/reference/items_spm_ls.html) contains **499 rows by 12 columns**, verified in native R as binary with no missing cells. It covers the final SPM series. The [builder](https://raw.githubusercontent.com/tmsalab/edmdata/3c0036e4a665b61adde011aac2215b62bd5da33d/data-raw/spm-ls/spm-ls-build.R) converts original nominal responses to keyed correctness and performs listwise deletion. These are consequential transformations, not new participants.

The original [Myszkowski–Storme deposit](https://data.mendeley.com/datasets/h3yhs5gy3w/1) is dated 2018; the older report's Robitzsch 2020 attribution refers to reanalysis. The [original deposit's registered rights](https://api.datacite.org/dois/10.17632/h3yhs5gy3w.1) specify **CC BY 4.0**, while the packaged binary object has the package MIT grant. Preserve the original source attribution and transformation provenance. The [exact packaged object](../datasets/edmdata-spm-ls/SOURCE.md) is mirrored with both MIT notices and underlying CC BY 4.0 attribution and terms. The original nominal CSV could not be retrieved in this check. Separate Raven stimulus rights are not inferred. There is no verified paired second-test file. Choose the original nominal data for distractor research and the documented binary representation for correctness-level models; do not count them as independent samples.

### Historical SAPA ICAR validation data

The [2016 descriptor](https://openpsychologydata.metajnl.com/articles/10.5334/jopd.25) reports **96,958 people** receiving random subsets from a **60-item pool**: nine letter/number series, eleven matrices, sixteen verbal-reasoning and twenty-four rotation items. Responses are already scored 0/1; selected distractors and item times were not verified. The actual repository is [Harvard Dataverse](https://doi.org/10.7910/DVN/AD9RVY), with [version-3 rights metadata](https://api.datacite.org/dois/10.7910/DVN/AD9RVY) specifying **CC0**. Participant files were not parsed or mirrored in this integration.

This historical release is distinct from the 1,525 by 16 psychTools sample and from the current full ICAR archive with separate scientific-use conditions. Avoid assuming those samples are independent without an overlap check. Random subsets do not supply two complete tests to every person, but connected item overlap can support joint calibration under suitable missingness and measurement assumptions. The old report's complete-test criterion should therefore be separated from the broader question of whether linking is possible. Web-volunteer sampling, missingness, source version and connectivity remain material limitations.

## Evidence and acquisition record

The [catalogue](../data/catalogue.json), [verification evidence](../data/verification-evidence.json), [integration crosswalk](../data/legacy-report-integration.json) and [redistribution audit](../data/redistribution-audit.json) retain distinct checks for each source. File inspection is structural evidence, not independent scientific validation or human review. No linking model, scoring comparison or equating function was fitted as part of this integration.


# 6. Large educational and adult assessments


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



# 7. Subject tests and learning-response data


Research date: **29 October 2026**. Scope: observed human skill/knowledge performance. These ten entries include fixed tests and learning platforms, which need different evaluation designs. Redistributable response files are separately mirrored in the dataset collection and release, with original licences, provenance and codebooks; sources without a clear sharing grant remain linked only. See the redistribution audit for current acquisition status.

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

**Data terms:** original packaged response and Q-matrix source objects are distributed under the CDM package-wide GPL (>=2) grant, with no contrary data notice found. Exact source objects and author documentation are mirrored; separate test-content rights remain distinct. **Item terms:** Published historical items; separate permission for reproducing item text not verified.

**Limits:** Historical, narrow curriculum sample; not population norms. Q-matrix is a modelling specification, not directly observed mastery. No option-level distractor responses or timing.

**Primary sources:** [source 1](https://raw.githubusercontent.com/alexanderrobitzsch/cdm/master/man/fraction.subtraction.data.Rd), [source 2](https://alexanderrobitzsch.r-universe.dev/CDM/data/fraction.subtraction.qmatrix/csv), [source 3](https://alexanderrobitzsch.r-universe.dev/CDM).

**Data route:** [download/landing](https://alexanderrobitzsch.r-universe.dev/CDM/data/fraction.subtraction.data/csv).

## 2. ECPE English grammar section (CDM)

**Best use:** high: fixed-test multidimensional scoring comparison. **Verification:** raw-file-verified: full JSON contains data (2,922 records, id plus E1–E28) and q.matrix (28 records).

Dense scored binary response matrix and 28×3 Q-matrix. Population/scale: 2,922 examinees (raw-file verified). Content: 28 grammar items; not the complete ECPE exam. Timing: No

**Scoring:** Binary correctness; remove the id column before scoring.

**Access:** Anonymous JSON export or data.ecpe in CDM.

**Data terms:** the exact packaged ECPE response/Q-matrix source object is distributed under CDM's formal package-wide GPL (>=2), with no contrary data notice found. Source object, licence and author codebook are mirrored; no ECPE question forms or proprietary handbook are supplied. **Item terms:** Full ECPE test content is not supplied by this response export; no item republication grant verified.

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

**Access:** The complete original 2020 Kaggle archive is mirrored, with all source CSVs and a full ZIP CRC audit. Official API/source-policy provenance and hashes are retained.

**Data terms:** CC BY-NC-SA 4.0 in uploader data card and Kaggle API metadata, with additional source policy text. **Item terms:** Content metadata supplied; separate rights to full online problems should not be inferred.

**Limits:** Distinct from the legacy 2015 Junyi dataset with about 25.9 million logs; schemas and counts must not be combined. An exercise is a group of problems, not a single item. Adaptive practice and repeated attempts require longitudinal evaluation.

**Primary sources:** [source 1](https://www.kaggle.com/datasets/junyiacademy/learning-activity-public-dataset-by-junyi-academy), [source 2](https://www.kaggle.com/api/v1/datasets/view/junyiacademy/learning-activity-public-dataset-by-junyi-academy), [source 3](https://www.kaggle.com/api/v1/datasets/download/junyiacademy/learning-activity-public-dataset-by-junyi-academy/Info_Content.csv), [source 4](https://www.kaggle.com/api/v1/datasets/download/junyiacademy/learning-activity-public-dataset-by-junyi-academy/Log_Problem.csv).

**Data route:** [download/landing](https://www.kaggle.com/api/v1/datasets/download/junyiacademy/learning-activity-public-dataset-by-junyi-academy).

## 6. EdNet KT1–KT4 (Santa English test preparation)

**Best use:** high for option-based longitudinal scoring and speed/accuracy studies. **Verification:** all original KT1-KT4 and Contents archives acquired, source hashes recorded and every ZIP member CRC verified. Actual CSV headers and sample records inspected.

KT1 question-solving logs; KT2 answer-selection actions; KT3 explanations/lectures; KT4 wider actions. Population/scale: KT1: 784,309 per-student files; approximately 131 million actions refers to the broad dataset, not KT1 answer rows. Content: 13,169 keyed question metadata rows (raw-file verified). Timing: KT1 elapsed_time in milliseconds; bundle timing can be shared across associated questions; shifted timestamps.

**Scoring:** Join user_answer (a–d) to Contents correct_answer; bundles identify shared stimuli.

**Access:** All five original archives are mirrored. KT1 remaining ranges used a pinned, region-verified mirror and matched its full published SHA-256; canonical author CC BY-NC4 terms apply. Other archives came from author-linked public endpoints.

**Data terms:** CC BY-NC 4.0, stated by authors for research purposes. **Item terms:** Released Contents includes keys/tags/IDs, not question text, passages or audio; no right to reproduce unreleased materials inferred.

**Limits:** High-level actions are not all test responses. Learning, recommendation policy, review and response revisions affect scores. No released external TOEIC score criterion: README still labels scores as to be released.

**Primary sources:** [source 1](https://github.com/riiid/ednet), [source 2](https://bit.ly/ednet-content), [source 3](https://arxiv.org/abs/1912.03072).

**Data route:** [download/landing](https://bit.ly/ednet_kt1).

## 7. Eedi / NeurIPS 2020 Education Challenge

**Best use:** high for noncommercial distractor-aware scoring within source terms; do not redistribute modified data or question images. **Verification:** raw-sample-verified: ZIP directory, tasks 1/2 and 3/4 training headers and answer metadata; question metadata and official counts also checked. Official licence and additional image restrictions directly verified (page lines 52–56).

QuestionId/UserId/AnswerId with IsCorrect, CorrectAnswer, AnswerValue; subject and answer metadata. Population/scale: Official training counts: tasks 1/2 118,971 students and 15,867,850 answers; tasks 3/4 4,918 students and 1,382,727 answers. Content: 27,613 questions (tasks 1/2); 948 (tasks 3/4), with images supplied for the smaller set. Timing: Inspected answer metadata has DateAnswered and Confidence but no duration field; DateAnswered is a timestamp, not response time.

**Scoring:** CorrectAnswer and selected AnswerValue support rescoring and distractor models; IsCorrect is provided.

**Access:** All original response/metadata/challenge CSVs are mirrored from public Azure byte ranges; every image and macOS resource fork is excluded. The canonical original archive is about 626 MB.

**Data terms:** CC BY-NC-ND 4.0 is explicitly stated on the official Eedi challenge page: noncommercial use, attribution with a licence link, and no distribution of modified material. **Item terms:** The official source restricts question images to model training and prohibits all other uses, printing and sharing with anyone.

**Limits:** Sparse, selected educational sample, not a common complete test. Task splits differ in people/items/metadata; preserve their identities. Training counts differ from totals that include challenge answers. Only the latest student-question answer is retained. Tasks 1/2 and tasks 3/4 have separately anonymised question/user/answer IDs; do not cross-join matching numeric IDs across the task pairs. See the [official guide](https://arxiv.org/html/2007.12061v3).

**Primary sources:** [source 1](https://www.eedischool.com/projects/neurips-education-challenge), [source 2](https://www.eedischool.com/research), [source 3](https://arxiv.org/abs/2007.12061), [source 4](https://dqanonymousdata.blob.core.windows.net/neurips-public/data.zip).

**Data route:** [download/landing](https://dqanonymousdata.blob.core.windows.net/neurips-public/data.zip).

## 8. Duolingo SLAM 2018 shared-task learner responses

**Best use:** medium: language learning/error prediction rather than a fixed proficiency test. **Verification:** acquired version-4 archives inspected; original licence and citation files retained; full gzip CRC audits and SHA-256 checks passed. The Harvard endpoint was unavailable, so the named unchanged mirror and the verification limits are recorded.

Token correctness/error labels, correct-answer tokens, user/session and exercise metadata across three language tracks. Population/scale: initial release described >2 million tokens and >6,000 learners. The acquired version-4 files contain 7,141,267 token rows across nine split files and 2,387,567 exercise metadata records; these are not unique learners. Content: No fixed common item count; tracks en_es, es_en and fr_en. Timing: Whole-exercise seconds; some null/negative logging values need cleaning.

**Scoring:** 0=OK and 1=mistake; this is reversed from ordinary correct=1 coding.

**Access:** Original version-4 course archives obtained from a named public mirror. Archive sizes match author-deposited metadata; the original deposit exposed no hash for independent upstream equality checking. Mirror hashes, original licences and provenance are preserved.

**Data terms:** CC BY-NC 4.0 is confirmed by original Duolingo LICENSE.md within all three archives and author-deposited metadata. No additional prohibition on sharing was found in those original files. **Item terms:** Do not infer a licence for the entire Duolingo curriculum beyond the released corpus.

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


# 8. Language assessment and constructed responses


Research date: **2026-10-29**. These sources contain demonstrated performance or human grading of that performance. Access and reuse conditions differ substantially. No restricted corpus was downloaded or republished for this review.

## MERLIN: German, Italian and Czech writing

**Best fit:** openly licensed, human-rated written performance. The mirrored version 1.2 contains **2,287 examination texts**, with CEFR ratings, tasks, learner metadata, error annotations and target hypotheses. TXT, XML-oriented annotation formats and metadata are offered. These are scored writing samples, not a dense multiple-choice response matrix. No per-item response-time data were verified. Use task and language controls when comparing scores; CEFR categories are ordinal.

The platform and versioned deposit explicitly state **CC BY-SA 4.0** for data and resources. Normal public CLARIN API routes supplied the original text, metadata, tasks, manual annotations and codebooks. The actual metadata has 2,287 rows and 362 columns; the earlier website count of 2,286 and older 2,290 descriptions refer to other descriptions/versions. Optional PAULA/relANNIS NLP encodings were not mirrored. **Original files, provider MD5 and archive integrity verified.** [Provider and downloads](https://www.merlin-platform.eu/), [Eurac corpus description](https://www.porta.eurac.edu/lci/merlin/), [CLARIN release](https://clarin.eurac.edu/repository/xmlui/handle/20.500.12124/59).

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

**Best fit:** a small human gap-completion study with known solutions. The authors describe **40 participants**, **32 English C-Tests**, and **20 gaps per test**. Their data documentation identifies `ctest_user_mapping.csv` as individual responses and distinguishes these from aggregated error rates, generated GPT-4 outputs and questionnaire responses. Only the actual human gap responses belong in a skill-scoring analysis. Text gaps share passages, creating testlet dependence; the sample is small. Whole-form duration is retained for all 160 user-form attempts; no per-gap latency was established.

The repository's **code is Apache-2.0**; the university data record states **CC BY 4.0**, subject to any component-specific notices. These are separate licenses. A normal public university API route supplied the original human-study archive. It contains 40 users, 32 forms, 160 attempts and 3,200 observed gap scores; auxiliary questionnaire records are distinct from skill responses. **Source files, provider MD5 and schema verified.** [Author repository and data schema](https://github.com/UKPLab/arxiv2024-constrained-ctest-generation), [university data record](https://tudatalib.ulb.tu-darmstadt.de/items/1e2ff254-6bba-454f-bd9f-e4aa1ecb7658).

## SemEval 2013 Task 7: BEETLE and SciEntsBank

**Best fit:** short-answer grading. The original task contains human science answers paired with reference answers and five accuracy labels: correct, partially correct/incomplete, contradictory, irrelevant, and non-domain. BEETLE comes from an electricity tutoring system; SciEntsBank covers school science. Keep them as separate datasets. These labels are **nominal diagnostic judgments**, not five equally spaced levels. A binary correct/other transformation is possible but discards information. Both corpora have unseen-answer and unseen-question splits; unseen-domain evaluation applies only to SciEntsBank. No response-time field was verified.

The original organizer supplies three-way and five-way ZIP files, with an explicit **CC BY-SA 3.0** license. The five-way archive was parsed for this review: it contains overlapping Core/Extra views, plus reliability material. Select one documented view and normalize label variants; do not simply concatenate every XML file. Prefer the organizer release over mirrors that duplicate answers once per reference answer. Answer IDs require study-specific interpretation before reconstructing examinees; answer rows are not people. [Organizer release and archives](https://github.com/myrosia/semeval-2013-task7), [license](https://github.com/myrosia/semeval-2013-task7/blob/main/LICENSE), [original task paper](https://aclanthology.org/S13-2045/).

## Useful but outside the individual-response shortlist

**Cambridge Multiple-Choice Questions Reading Dataset** provides reading passages, questions, keys, and task/item/option statistics. Its technical report describes JSONL at the task level, rather than an examinee-by-item matrix. The report lists 120 tasks and option statistics for 78 tasks. **Do not treat aggregate facility/discrimination as individual response records or use them to reconstruct a unique joint response distribution.** Access is registered non-commercial research with no redistribution. Suitable for item/distractor design studies; insufficient by itself for rescorings of individual examinees. [Official description and terms](https://researchdatasets.cambridge.org/datasets/cambridge-multiple-choice-questions-reading-dataset), [technical report with schema](https://www.repository.cam.ac.uk/bitstreams/90fc31ea-bd4c-4b33-8474-1e127635a6d3/download).



# 9. Discovery resources and exclusions


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


# 10. Verification, limitations and reproducibility


## What was checked

The research catalogue distinguishes response-file inspection, archive verification, primary documentation and unresolved metadata-only evidence. The acquisition phase adds byte counts, SHA-256 hashes, provider hashes where supplied, archive integrity checks, source snapshots and explicit subset rules. The downloaded payload manifest is the authoritative list of mirrored files; the complete source audit records exclusions as well as acquisitions.

Selected source archives were parsed to verify response schemas and counts. A full parse does not establish that every response is valid or every participant is unique. Provider participation totals, file rows and distinct respondent identifiers remain separate. Some mirrors contain all deposited files; mixed batteries are limited to named objective tasks, and some alternative formats or additional annotations may be omitted. Every such selection is documented in the collection source record.

## Corrections from acquisition

MERLIN's mirrored version 1.2 has 2,287 metadata records; the earlier website description gives 2,286. The versioned deposit and actual metadata govern this mirror. The English C-Test study contains 40 users, 32 forms and 160 user-form attempts, or 3,200 observed gap scores; whole-form duration is present, while per-gap latency was not established. The working-memory deposit has two original CSV files and distinguishes raw task records from participant-collapsed scores. The OpenNeuro archive contains source subject identifiers beyond the reported study-completer cohort; recommended exclusions must be applied explicitly rather than silently deleting source rows.

## Earlier report integration

The earlier Candidate Datasets document is preserved unchanged in older_reports. Its candidates and recommendations were reconciled against primary papers, data dictionaries and inspected response files on 30 October 2026. The linking chapter records corrected designs, version conflicts, evidence levels and unresolved access. The original citation tokens cannot substitute for recoverable primary references.

## Rebuild and locate the evidence

The complete source review is in the research directory. Catalogue metadata is supplied as JSON and CSV. Source-specific licences, citations, codebooks and file manifests accompany each mirrored collection. The root download manifest identifies files stored in Git and large release assets. Files from inaccessible or non-redistributable sources are linked, not included.

The PDF is generated by `reports/build_report.py` from AI-assisted project Markdown. It uses ReportLab and Mistune, supplies clickable numbered citations, a contents page and PDF bookmarks, and checks the written PDF with pypdf. The committed Markdown remains readable independently of PDF-generation software. Visual rendering was inspected by AI assistants before delivery; the report does not embed participant responses or protected test images.

## Limits of the findings

This is a deep, curated review with a dated acquisition snapshot, not a census of all tests. It emphasizes documented sources with useful human response data. Licences and links can change; rights are version-specific and component-specific. Original codebooks can contain ambiguities, and some files have limited documentation. A project field guide explains observed structure without claiming to be an author-approved replacement.

The review does not establish population norms, cross-cultural equivalence, causal effects, algorithmic superiority or suitability for an individual decision. No scoring experiment was run. Reuse should preserve the difference between observed answers, assigned marks, expert annotations and estimated latent traits. Independent held-out validation remains necessary for a new scoring method.


# Sources

[1] earlier Candidate Datasets report - https://github.com/AndersH3/skill-data-atlas/blob/main/older_reports/Candidate%20Datasets.docx
[2] Original deposit - https://doi.org/10.6084/m9.figshare.1045385
[3] Integrated linking review - https://github.com/AndersH3/skill-data-atlas/blob/main/research/linked-tests-and-legacy-integration.md
[4] Author data and licence - https://github.com/IanEisenberg/Self_Regulation_Ontology
[5] Versioned deposit - https://data.mendeley.com/datasets/kfc3jyggs7/1
[6] Eedi source - https://www.eedischool.com/projects/neurips-education-challenge
[7] EdNet source - https://github.com/riiid/ednet
[8] Junyi release - https://www.kaggle.com/datasets/junyiacademy/learning-activity-public-dataset-by-junyi-academy
[9] MERLIN source - https://www.merlin-platform.eu/
[10] Cambridge terms - https://researchdatasets.cambridge.org/datasets/clc-fce-dataset
[11] Organizer release - https://github.com/myrosia/semeval-2013-task7
[12] verification evidence - https://github.com/AndersH3/skill-data-atlas/blob/main/data/verification-evidence.json
[13] SAPA cognitive ability: psychTools ability / iqitems - source documentation - https://github.com/cran/psychTools/blob/7dc591f8ac11c0ef1764cf853f3065aa60653d09/DESCRIPTION
[14] OpenPsychometrics Vocabulary IQ Test - source documentation - https://openpsychometrics.org/tests/VIQT/
[15] OpenPsychometrics Multifactor General Knowledge Test 2017-2018 - source documentation - https://openpsychometrics.org/_rawdata/MGKT_data.zip
[16] OpenPsychometrics experimental matrix IQ test - source documentation - https://openpsychometrics.org/_rawdata/IQ1.zip
[17] OpenPsychometrics Full Scale IQ alpha v0.1 - source documentation - https://openpsychometrics.org/_rawdata/FSIQ_0.1_data.zip
[18] Exposure Based Face Memory Test - source documentation - https://openpsychometrics.org/_rawdata/EBFMT.zip
[19] Ganis-Kievit mental rotation validation data - source documentation - https://doi.org/10.6084/m9.figshare.1045385.v13
[20] Self-Regulation Ontology objective performance-task subset - source documentation - https://pmc.ncbi.nlm.nih.gov/articles/PMC6534563/
[21] OpenNeuro ds004636 objective task subset - source documentation - https://pmc.ncbi.nlm.nih.gov/articles/PMC11271451/
[22] Working Memory Develops at a Similar Rate Across Diverse Stimuli - source documentation - https://doi.org/10.17632/kfc3jyggs7.1
[23] ICAR current full materials and psychometric data - source documentation - https://doi.org/10.23668/psycharchives.22167
[24] Music Ensemble: objective cognitive and music-perception tasks - source documentation - https://doi.org/10.1038/s41597-026-06654-0
[25] Much, Mutak, Pohl and Ranger: matrix reasoning under speed and accuracy instructions - source documentation - https://doi.org/10.5334/jopd.124
[26] TüEyeQ: CFT 20-R performance and eye tracking - source documentation - https://doi.org/10.7910/DVN/JGOCKI
[27] HCP Penn Progressive Matrices: edmdata response matrices - source documentation - https://tmsalab.github.io/edmdata/reference/items-hcp-penn.html
[28] Revised PSVT:R response matrix - source documentation - https://tmsalab.github.io/edmdata/reference/items_revised_psvtr.html
[29] SPM-LS: final 12 Standard Progressive Matrices items - source documentation - https://tmsalab.github.io/edmdata/reference/items_spm_ls.html
[30] Historical SAPA/ICAR 2010–2013 validation response data - source documentation - https://openpsychologydata.metajnl.com/articles/10.5334/jopd.25
[31] PISA 2025 cognitive responses and process data - source documentation - https://www.oecd.org/en/data/datasets/pisa-2025-database.html
[32] PISA 2022 - source documentation - https://www.oecd.org/en/data/datasets/pisa-2022-database.html
[33] PISA 2018 cognitive responses plus corrected total-time/visits supplement - source documentation - https://www.oecd.org/en/data/datasets/pisa-2018-database.html
[34] Survey of Adult Skills 2023 / PIAAC cycle 2 - source documentation - https://www.oecd.org/en/data/datasets/PIAAC-2nd-Cycle-Database.html
[35] PIAAC 2012 international log files, ZA6712 - source documentation - https://www.gesis.org/en/data-on-adult-education/daten/piaac-daten-zyklus-1/piaac-international/international-piaac-log-files
[36] TIMSS 2023 grades 4 and 8 - source documentation - https://www.iea.nl/data-tools/repository/timss
[37] PIRLS 2021, second edition including log files - source documentation - https://www.iea.nl/data-tools/repository/pirls
[38] ICILS 2023 - source documentation - https://www.iea.nl/data-tools/repository/icils
[39] ICCS 2022 civic-knowledge test and process data - source documentation - https://www.iea.nl/data-tools/repository/iccs
[40] Tatsuoka fraction subtraction (CDM) - source documentation - https://github.com/alexanderrobitzsch/CDM/blob/9a731f28426367d9c56576035930c7246a902894/DESCRIPTION
[41] ASSISTments 2009–2010 corrected collapsed Skill Builder - source documentation - https://sites.google.com/site/assistmentsdata/home/2009-2010-assistment-data/skill-builder-data-2009-2010
[42] ASSISTments 2015 top-100 Skill Builders - source documentation - https://sites.google.com/site/assistmentsdata/datasets/2015-assistments-skill-builder-data
[43] Duolingo SLAM 2018 shared-task learner responses - source documentation - https://doi.org/10.7910/DVN/8SWHNO
[44] KDD Cup 2010 Algebra I / Bridge to Algebra - source documentation - https://kdd.org/kdd-cup/view/kdd-cup-2010-student-performance-evaluation/Data
[45] Database Exercises for Knowledge Tracing (DBE-KT22) - source documentation - https://arxiv.org/html/2208.12651v3
[46] Cambridge Speak & Improve Corpus 2025 - source documentation - https://researchdatasets.cambridge.org/datasets/speak-and-improve-corpus-2025
[47] Cambridge Write & Improve Corpus 2024 (second version) - source documentation - https://researchdatasets.cambridge.org/datasets/write-and-improve-corpus-2024
[48] Constrained English C-Test user study - source documentation - https://tudatalib.ulb.tu-darmstadt.de/handle/tudatalib/4205
[49] Source record and documentation - https://github.com/AndersH3/skill-data-atlas/tree/main/datasets/ctest_mip_2024
[50] Constrained English C-Test user study - source documentation - https://tudatalib.ulb.tu-darmstadt.de/server/api/core/items/1e2ff254-6bba-454f-bd9f-e4aa1ecb7658
[51] tudatalib.ulb.tu-darmstadt.de - content - https://tudatalib.ulb.tu-darmstadt.de/server/api/core/bitstreams/088d335e-b696-48f3-8f08-bc4dc2cc8dad/content
[52] Constrained English C-Test user study - source documentation - https://github.com/UKPLab/arxiv2024-constrained-ctest-generation
[53] arxiv.org - 2404.08821 - https://arxiv.org/abs/2404.08821
[54] raw.githubusercontent.com - CC-BY-4.0.txt - https://raw.githubusercontent.com/spdx/license-list-data/main/text/CC-BY-4.0.txt
[55] creativecommons.org - 4.0 - https://creativecommons.org/licenses/by/4.0/
[56] User Study Data.zip - https://github.com/AndersH3/skill-data-atlas/blob/main/datasets/ctest_mip_2024/User%20Study%20Data.zip
[57] Source record and documentation - https://github.com/AndersH3/skill-data-atlas/tree/main/datasets/duolingo-slam-2018
[58] Duolingo SLAM 2018 shared-task learner responses - source documentation - https://sharedtask.duolingo.com/2018.html
[59] Duolingo SLAM 2018 shared-task learner responses - source documentation - https://api.datacite.org/dois/10.7910/DVN/8SWHNO
[60] cn.dataone.org - sha256:c99e7d3e18a8ee138442180c31cedf54546f51fe4b02555e0894e11cdfebc7e8 - https://cn.dataone.org/cn/v2/object/sha256%3Ac99e7d3e18a8ee138442180c31cedf54546f51fe4b02555e0894e11cdfebc7e8
[61] doi.org - C1LOKO - https://doi.org/10.7910/DVN/8SWHNO/C1LOKO
[62] doi.org - Z29WIF - https://doi.org/10.7910/DVN/8SWHNO/Z29WIF
[63] doi.org - 5YWVBV - https://doi.org/10.7910/DVN/8SWHNO/5YWVBV
[64] Duolingo SLAM 2018 shared-task learner responses - source documentation - https://github.com/xinhez/11785-project/tree/master/data
[65] creativecommons.org - 4.0 - https://creativecommons.org/licenses/by-nc/4.0/
[66] data_en_es.tar.gz - https://github.com/AndersH3/skill-data-atlas/releases/download/datasets-2026-10-29/data_en_es.tar.gz
[67] data_es_en.tar.gz - https://github.com/AndersH3/skill-data-atlas/releases/download/datasets-2026-10-29/data_es_en.tar.gz
[68] data_fr_en.tar.gz - https://github.com/AndersH3/skill-data-atlas/releases/download/datasets-2026-10-29/data_fr_en.tar.gz
[69] Source record and documentation - https://github.com/AndersH3/skill-data-atlas/tree/main/datasets/ecpe-grammar
[70] Tatsuoka fraction subtraction (CDM) - source documentation - https://github.com/alexanderrobitzsch/CDM/tree/9a731f28426367d9c56576035930c7246a902894
[71] R Core Team - Writing R Extensions: Licensing - https://cran.r-project.org/doc/manuals/r-release/R-exts.html#Licensing
[72] CRAN Repository Policy - source formats and licensing - https://cran.r-project.org/web/packages/policies.html
[73] www.gnu.org - gpl-2.0.html - https://www.gnu.org/licenses/old-licenses/gpl-2.0.html
[74] raw.githubusercontent.com - GPL-2.0-or-later.txt - https://raw.githubusercontent.com/spdx/license-list-data/main/text/GPL-2.0-or-later.txt
[75] psych.unl.edu - dcm12ncme - http://psych.unl.edu/jtemplin/teaching/dcm/dcm12ncme/
[76] data.ecpe.rda - https://github.com/AndersH3/skill-data-atlas/blob/main/datasets/ecpe-grammar/original/data.ecpe.rda
[77] Source record and documentation - https://github.com/AndersH3/skill-data-atlas/tree/main/datasets/edmdata-revised-psvtr
[78] HCP Penn Progressive Matrices: edmdata response matrices - source documentation - https://raw.githubusercontent.com/tmsalab/edmdata/3c0036e4a665b61adde011aac2215b62bd5da33d/DESCRIPTION
[79] github.com - 3c0036e4a665b61adde011aac2215b62bd5da33d - https://github.com/tmsalab/edmdata/tree/3c0036e4a665b61adde011aac2215b62bd5da33d
[80] Revised PSVT:R response matrix - source documentation - https://raw.githubusercontent.com/tmsalab/edmdata/3c0036e4a665b61adde011aac2215b62bd5da33d/LICENSE.md
[81] doi.org - s11336-015-9484-7 - https://doi.org/10.1007/s11336-015-9484-7
[82] items_revised_psvtr.rda - https://github.com/AndersH3/skill-data-atlas/blob/main/datasets/edmdata-revised-psvtr/original/items_revised_psvtr.rda
[83] Source record and documentation - https://github.com/AndersH3/skill-data-atlas/tree/main/datasets/edmdata-spm-ls
[84] doi.org - j.intell.2018.03.010 - https://doi.org/10.1016/j.intell.2018.03.010
[85] SPM-LS: final 12 Standard Progressive Matrices items - source documentation - https://doi.org/10.17632/h3yhs5gy3w.1
[86] doi.org - preprints202007.0269.v1 - https://doi.org/10.20944/preprints202007.0269.v1
[87] items_spm_ls.rda - https://github.com/AndersH3/skill-data-atlas/blob/main/datasets/edmdata-spm-ls/original/items_spm_ls.rda
[88] Source record and documentation - https://github.com/AndersH3/skill-data-atlas/tree/main/datasets/ednet
[89] raw.githubusercontent.com - README.md - https://raw.githubusercontent.com/riiid/ednet/master/README.md
[90] KT1 - https://bit.ly/ednet_kt1
[91] KT2 - https://bit.ly/ednet-kt2
[92] KT3 - https://bit.ly/ednet-kt3
[93] KT4 - https://bit.ly/ednet-kt4
[94] Contents - https://bit.ly/ednet-content
[95] EdNet KT1–KT4 (Santa English test preparation) - source documentation - https://arxiv.org/abs/1912.03072
[96] raw.githubusercontent.com - CC-BY-NC-4.0.txt - https://raw.githubusercontent.com/spdx/license-list-data/main/text/CC-BY-NC-4.0.txt
[97] EdNet KT1–KT4 (Santa English test preparation) - source documentation - https://huggingface.co/datasets/Lucy9999/EdNet-KT1/resolve/790cff06b7c112c4ec072217257de5dd4ec1e77a/EdNet-KT1.zip
[98] ednet-Contents.zip - https://github.com/AndersH3/skill-data-atlas/blob/main/datasets/ednet/raw/ednet-Contents.zip
[99] ednet-KT1.zip - https://github.com/AndersH3/skill-data-atlas/releases/download/datasets-2026-10-29/ednet-KT1.zip
[100] ednet-KT2.zip - https://github.com/AndersH3/skill-data-atlas/releases/download/datasets-2026-10-29/ednet-KT2.zip
[101] ednet-KT3.zip - https://github.com/AndersH3/skill-data-atlas/releases/download/datasets-2026-10-29/ednet-KT3.zip
[102] ednet-KT4.zip - https://github.com/AndersH3/skill-data-atlas/releases/download/datasets-2026-10-29/ednet-KT4.zip
[103] Source record and documentation - https://github.com/AndersH3/skill-data-atlas/tree/main/datasets/eedi-neurips-2020
[104] Eedi / NeurIPS 2020 Education Challenge - source documentation - https://dqanonymousdata.blob.core.windows.net/neurips-public/data.zip
[105] Eedi / NeurIPS 2020 Education Challenge - source documentation - https://arxiv.org/abs/2007.12061
[106] Eedi / NeurIPS 2020 Education Challenge - source documentation - https://arxiv.org/html/2007.12061v3
[107] raw.githubusercontent.com - CC-BY-NC-ND-4.0.txt - https://raw.githubusercontent.com/spdx/license-list-data/main/text/CC-BY-NC-ND-4.0.txt
[108] creativecommons.org - 4.0 - https://creativecommons.org/licenses/by-nc-nd/4.0/
[109] eedi-2020-response-and-metadata-csvs.zip - https://github.com/AndersH3/skill-data-atlas/releases/download/datasets-2026-10-29/eedi-2020-response-and-metadata-csvs.zip
[110] Source record and documentation - https://github.com/AndersH3/skill-data-atlas/tree/main/datasets/fraction-subtraction
[111] fraction.subtraction.data.rda - https://github.com/AndersH3/skill-data-atlas/blob/main/datasets/fraction-subtraction/original/fraction.subtraction.data.rda
[112] fraction.subtraction.qmatrix.rda - https://github.com/AndersH3/skill-data-atlas/blob/main/datasets/fraction-subtraction/original/fraction.subtraction.qmatrix.rda
[113] Source record and documentation - https://github.com/AndersH3/skill-data-atlas/tree/main/datasets/ganis-kievit-mental-rotation
[114] Ganis-Kievit mental rotation validation data - source documentation - https://api.figshare.com/v2/articles/1045385
[115] ndownloader.figshare.com - 3191717 - https://ndownloader.figshare.com/files/3191717
[116] ndownloader.figshare.com - 1571341 - https://ndownloader.figshare.com/files/1571341
[117] Ganis-Kievit mental rotation validation data - source documentation - https://ndownloader.figshare.com/files/1878074
[118] Ganis-Kievit mental rotation validation data - source documentation - https://ndownloader.figshare.com/files/3702010
[119] All-stimuli-JPG-file3191717.zip - https://github.com/AndersH3/skill-data-atlas/releases/download/datasets-2026-10-29/All-stimuli-JPG-file3191717.zip
[120] Behavioural_data-file3702010.zip - https://github.com/AndersH3/skill-data-atlas/blob/main/datasets/ganis-kievit-mental-rotation/original/Behavioural_data-file3702010.zip
[121] Source record and documentation - https://github.com/AndersH3/skill-data-atlas/tree/main/datasets/junyi-2020
[122] Junyi Academy Online Learning Activity Dataset (2020 release; 2018–2019 logs) - source documentation - https://www.kaggle.com/api/v1/datasets/view/junyiacademy/learning-activity-public-dataset-by-junyi-academy
[123] www.kaggle.com - learning-activity-public-dataset-by-junyi-academy - https://www.kaggle.com/api/v1/datasets/download/junyiacademy/learning-activity-public-dataset-by-junyi-academy
[124] www.kaggle.com - learning-activity-public-dataset-by-junyi-academy - https://www.kaggle.com/api/v1/datasets/list/junyiacademy/learning-activity-public-dataset-by-junyi-academy
[125] www.junyiacademy.org - policy - https://www.junyiacademy.org/about/policy
[126] raw.githubusercontent.com - CC-BY-NC-SA-4.0.txt - https://raw.githubusercontent.com/spdx/license-list-data/main/text/CC-BY-NC-SA-4.0.txt
[127] creativecommons.org - 4.0 - https://creativecommons.org/licenses/by-nc-sa/4.0/
[128] junyi-2020-original.zip - https://github.com/AndersH3/skill-data-atlas/releases/download/datasets-2026-10-29/junyi-2020-original.zip
[129] Source record and documentation - https://github.com/AndersH3/skill-data-atlas/tree/main/datasets/mathy-friedman-working-memory
[130] Working Memory Develops at a Similar Rate Across Diverse Stimuli - source documentation - https://data.mendeley.com/public-api/datasets/kfc3jyggs7?version=1
[131] data.mendeley.com - files - https://data.mendeley.com/public-api/datasets/kfc3jyggs7/files?folder_id=root&version=1
[132] data.mendeley.com - file downloaded - https://data.mendeley.com/public-files/datasets/kfc3jyggs7/files/d0c5b8d5-169c-473f-b2dd-5c61a88b89c4/file_downloaded
[133] data.mendeley.com - file downloaded - https://data.mendeley.com/public-files/datasets/kfc3jyggs7/files/af641063-4d8e-4329-975e-17daa875cec5/file_downloaded
[134] dat_all.csv - https://github.com/AndersH3/skill-data-atlas/blob/main/datasets/mathy-friedman-working-memory/original/dat_all.csv
[135] dat_partialcreditunitAGG_Unstacked.csv - https://github.com/AndersH3/skill-data-atlas/blob/main/datasets/mathy-friedman-working-memory/original/dat_partialcreditunitAGG_Unstacked.csv
[136] Source record and documentation - https://github.com/AndersH3/skill-data-atlas/tree/main/datasets/merlin
[137] clarin.eurac.edu - 59 - https://clarin.eurac.edu/repository/xmlui/handle/20.500.12124/59
[138] MERLIN multilingual examination writing - source documentation - https://hdl.handle.net/20.500.12124/59
[139] MERLIN multilingual examination writing - source documentation - https://clarin.eurac.edu/repository/rest/items/44?expand=all
[140] gitlab.inf.unibz.it - v1.2 - https://gitlab.inf.unibz.it/commul/merlin-platform/data-bundle/-/tags/v1.2
[141] aclanthology.org - L14-1488 - https://aclanthology.org/L14-1488/
[142] merlin-docs-v1.2.zip - https://github.com/AndersH3/skill-data-atlas/blob/main/datasets/merlin/merlin-docs-v1.2.zip
[143] merlin-exmaralda-v1.2.zip - https://github.com/AndersH3/skill-data-atlas/releases/download/datasets-2026-10-29/merlin-exmaralda-v1.2.zip
[144] merlin-metadata-v1.2.zip - https://github.com/AndersH3/skill-data-atlas/blob/main/datasets/merlin/merlin-metadata-v1.2.zip
[145] merlin-solr-v1.2.zip - https://github.com/AndersH3/skill-data-atlas/blob/main/datasets/merlin/merlin-solr-v1.2.zip
[146] merlin-tasks-v1.2.zip - https://github.com/AndersH3/skill-data-atlas/blob/main/datasets/merlin/merlin-tasks-v1.2.zip
[147] merlin-text-v1.2.zip - https://github.com/AndersH3/skill-data-atlas/blob/main/datasets/merlin/merlin-text-v1.2.zip
[148] Source record and documentation - https://github.com/AndersH3/skill-data-atlas/tree/main/datasets/much-mutak-matrices-2025
[149] Much, Mutak, Pohl and Ranger: matrix reasoning under speed and accuracy instructions - source documentation - https://doi.org/10.17605/OSF.IO/9J6HM
[150] osf.io - 9j6hm - https://osf.io/9j6hm/
[151] api.osf.io - 563c1cf88c5e4a3877f9e96a - https://api.osf.io/v2/licenses/563c1cf88c5e4a3877f9e96a/
[152] mr_itemsolutions.csv - https://github.com/AndersH3/skill-data-atlas/blob/main/datasets/much-mutak-matrices-2025/original/mr_itemsolutions.csv
[153] tte_data.csv - https://github.com/AndersH3/skill-data-atlas/blob/main/datasets/much-mutak-matrices-2025/original/tte_data.csv
[154] Source record and documentation - https://github.com/AndersH3/skill-data-atlas/tree/main/datasets/openneuro-ds004636-objective-tasks
[155] OpenNeuro ds004636 objective task subset - source documentation - https://raw.githubusercontent.com/OpenNeuroDatasets/ds004636/769186fe1b185fae16437f380bfebd56edf7acd7/dataset_description.json
[156] codeload.github.com - 769186fe1b185fae16437f380bfebd56edf7acd7 - https://codeload.github.com/OpenNeuroDatasets/ds004636/tar.gz/769186fe1b185fae16437f380bfebd56edf7acd7
[157] raw.githubusercontent.com - CHANGES - https://raw.githubusercontent.com/OpenNeuroDatasets/ds004636/769186fe1b185fae16437f380bfebd56edf7acd7/CHANGES
[158] raw.githubusercontent.com - README.md - https://raw.githubusercontent.com/OpenNeuroDatasets/ds004636/769186fe1b185fae16437f380bfebd56edf7acd7/README.md
[159] raw.githubusercontent.com - participants.json - https://raw.githubusercontent.com/OpenNeuroDatasets/ds004636/769186fe1b185fae16437f380bfebd56edf7acd7/participants.json
[160] raw.githubusercontent.com - participants.tsv - https://raw.githubusercontent.com/OpenNeuroDatasets/ds004636/769186fe1b185fae16437f380bfebd56edf7acd7/participants.tsv
[161] raw.githubusercontent.com - task-ANT events.json - https://raw.githubusercontent.com/OpenNeuroDatasets/ds004636/769186fe1b185fae16437f380bfebd56edf7acd7/task-ANT_events.json
[162] raw.githubusercontent.com - task-DPX events.json - https://raw.githubusercontent.com/OpenNeuroDatasets/ds004636/769186fe1b185fae16437f380bfebd56edf7acd7/task-DPX_events.json
[163] raw.githubusercontent.com - task-WATT3 events.json - https://raw.githubusercontent.com/OpenNeuroDatasets/ds004636/769186fe1b185fae16437f380bfebd56edf7acd7/task-WATT3_events.json
[164] raw.githubusercontent.com - task-motorSelectiveStop events.json - https://raw.githubusercontent.com/OpenNeuroDatasets/ds004636/769186fe1b185fae16437f380bfebd56edf7acd7/task-motorSelectiveStop_events.json
[165] raw.githubusercontent.com - task-stopSignal events.json - https://raw.githubusercontent.com/OpenNeuroDatasets/ds004636/769186fe1b185fae16437f380bfebd56edf7acd7/task-stopSignal_events.json
[166] raw.githubusercontent.com - task-stroop events.json - https://raw.githubusercontent.com/OpenNeuroDatasets/ds004636/769186fe1b185fae16437f380bfebd56edf7acd7/task-stroop_events.json
[167] raw.githubusercontent.com - task-twoByTwo events.json - https://raw.githubusercontent.com/OpenNeuroDatasets/ds004636/769186fe1b185fae16437f380bfebd56edf7acd7/task-twoByTwo_events.json
[168] raw.githubusercontent.com - CC0-1.0.txt - https://raw.githubusercontent.com/spdx/license-list-data/main/text/CC0-1.0.txt
[169] objective-task-events.zip - https://github.com/AndersH3/skill-data-atlas/blob/main/datasets/openneuro-ds004636-objective-tasks/original/objective-task-events.zip
[170] Source record and documentation - https://github.com/AndersH3/skill-data-atlas/tree/main/datasets/sapa-ability-iqitems
[171] SAPA cognitive ability: psychTools ability / iqitems - source documentation - https://github.com/cran/psychTools/tree/7dc591f8ac11c0ef1764cf853f3065aa60653d09
[172] www.sapa-project.org -  - https://www.sapa-project.org/
[173] ability.rda - https://github.com/AndersH3/skill-data-atlas/blob/main/datasets/sapa-ability-iqitems/original/ability.rda
[174] iqitems.rda - https://github.com/AndersH3/skill-data-atlas/blob/main/datasets/sapa-ability-iqitems/original/iqitems.rda
[175] Source record and documentation - https://github.com/AndersH3/skill-data-atlas/tree/main/datasets/semeval2013-task7
[176] raw.githubusercontent.com - semeval-5way.zip - https://raw.githubusercontent.com/myrosia/semeval-2013-task7/main/semeval-5way.zip
[177] SemEval 2013 Task 7 BEETLE - source documentation - https://aclanthology.org/S13-2045/
[178] doi.org - s10579-015-9313-8 - https://doi.org/10.1007/s10579-015-9313-8
[179] semeval-5way.zip - https://github.com/AndersH3/skill-data-atlas/blob/main/datasets/semeval2013-task7/semeval-5way.zip
[180] Source record and documentation - https://github.com/AndersH3/skill-data-atlas/tree/main/datasets/sro-performance-tasks
[181] Self-Regulation Ontology objective performance-task subset - source documentation - https://github.com/IanEisenberg/Self_Regulation_Ontology/blob/4e6e837fb5aaca87ed5914fd9be251156f43eec9/README.md#license
[182] github.com - Complete 02-16-2019 - https://github.com/IanEisenberg/Self_Regulation_Ontology/tree/4e6e837fb5aaca87ed5914fd9be251156f43eec9/Data/Complete_02-16-2019
[183] github.com - Retest 02-16-2019 - https://github.com/IanEisenberg/Self_Regulation_Ontology/tree/4e6e837fb5aaca87ed5914fd9be251156f43eec9/Data/Retest_02-16-2019
[184] raw.githubusercontent.com - README.md - https://raw.githubusercontent.com/IanEisenberg/Self_Regulation_Ontology/4e6e837fb5aaca87ed5914fd9be251156f43eec9/Data/README.md
[185] raw.githubusercontent.com - README.txt - https://raw.githubusercontent.com/IanEisenberg/Self_Regulation_Ontology/4e6e837fb5aaca87ed5914fd9be251156f43eec9/Data/Complete_02-16-2019/README.txt
[186] raw.githubusercontent.com - README.txt - https://raw.githubusercontent.com/IanEisenberg/Self_Regulation_Ontology/4e6e837fb5aaca87ed5914fd9be251156f43eec9/Data/Retest_02-16-2019/README.txt
[187] Complete_02-16-2019-objective-tasks.zip - https://github.com/AndersH3/skill-data-atlas/releases/download/datasets-2026-10-29/Complete_02-16-2019-objective-tasks.zip
[188] Retest_02-16-2019-objective-tasks.zip - https://github.com/AndersH3/skill-data-atlas/releases/download/datasets-2026-10-29/Retest_02-16-2019-objective-tasks.zip
[189] Current ability documentation - https://raw.githubusercontent.com/cran/psychTools/master/man/ability.Rd
[190] iqitems documentation and key - https://raw.githubusercontent.com/cran/psychTools/master/man/iqitems.Rd
[191] package licence - https://raw.githubusercontent.com/cran/psychTools/master/DESCRIPTION
[192] download and codebook - https://openpsychometrics.org/_rawdata/VIQT_data.zip
[193] current form, with different scoring - https://openpsychometrics.org/tests/MGKT2/
[194] printable instrument - https://openpsychometrics.org/printable/intelligence-quotient-test.pdf
[195] current test - https://openpsychometrics.org/tests/FSIQ/
[196] development and licence - https://openpsychometrics.org/tests/EBFMT/development/
[197] paper - https://doi.org/10.5334/jopd.ai
[198] data release - https://github.com/IanEisenberg/Self_Regulation_Ontology/tree/master/Data/Complete_02-16-2019
[199] retest paper - https://pmc.ncbi.nlm.nih.gov/articles/PMC6431228/
[200] versioned data - https://openneuro.org/datasets/ds004636/versions/1.0.4
[201] CC0 metadata - https://raw.githubusercontent.com/OpenNeuroDatasets/ds004636/master/dataset_description.json
[202] raw behaviour OSF - https://osf.io/sjvnw/
[203] official ICAR FAQ - https://icar-project.com/
[204] Scientific Use License record - https://www.psycharchives.org/en/item/7466aa16-69bd-49ea-baef-7f828f5b223f
[205] file identity and provenance - https://github.com/AndersH3/skill-data-atlas/blob/main/older_reports/README.md
[206] methodological reference - https://pmc.ncbi.nlm.nih.gov/articles/PMC2762121/
[207] Music Ensemble project - https://osf.io/y97t3/
[208] analysis.zip - https://osf.io/download/dk4eb/
[209] CC BY-NC 4.0 - https://api.osf.io/v2/licenses/60bf992258510b0009a5a9a6/
[210] response and solution files - https://github.com/AndersH3/skill-data-atlas/blob/main/datasets/much-mutak-matrices-2025/SOURCE.md
[211] data paper - https://pmc.ncbi.nlm.nih.gov/articles/PMC8208979/
[212] figshare record - https://api.figshare.com/v2/articles/14173244
[213] registered version-2 metadata - https://api.datacite.org/dois/10.7910/DVN/JGOCKI
[214] pinned builder - https://raw.githubusercontent.com/tmsalab/edmdata/3c0036e4a665b61adde011aac2215b62bd5da33d/data-raw/hcp-penn-matrix/hcp_penn_matrix_build.R
[215] broader HCP battery - https://www.humanconnectome.org/study/hcp-young-adult/document/quick-reference-open-access-vs-restricted-data
[216] upstream data-use terms - https://www.vps.humanconnectome.org/study/hcp-young-adult/data-use-terms
[217] pinned package object - https://raw.githubusercontent.com/tmsalab/edmdata/3c0036e4a665b61adde011aac2215b62bd5da33d/data/items_revised_psvtr.rda
[218] exact source object and author documentation - https://github.com/AndersH3/skill-data-atlas/blob/main/datasets/edmdata-revised-psvtr/SOURCE.md
[219] builder - https://raw.githubusercontent.com/tmsalab/edmdata/3c0036e4a665b61adde011aac2215b62bd5da33d/data-raw/spm-ls/spm-ls-build.R
[220] Myszkowski-Storme deposit - https://data.mendeley.com/datasets/h3yhs5gy3w/1
[221] original deposit's registered rights - https://api.datacite.org/dois/10.17632/h3yhs5gy3w.1
[222] exact packaged object - https://github.com/AndersH3/skill-data-atlas/blob/main/datasets/edmdata-spm-ls/SOURCE.md
[223] Harvard Dataverse - https://doi.org/10.7910/DVN/AD9RVY
[224] version-3 rights metadata - https://api.datacite.org/dois/10.7910/DVN/AD9RVY
[225] catalogue - https://github.com/AndersH3/skill-data-atlas/blob/main/data/catalogue.json
[226] integration crosswalk - https://github.com/AndersH3/skill-data-atlas/blob/main/data/legacy-report-integration.json
[227] redistribution audit - https://github.com/AndersH3/skill-data-atlas/blob/main/data/redistribution-audit.json
[228] official programme page - https://www.oecd.org/en/about/programmes/pisa.html
[229] official file index - https://webfs.oecd.org/pisa2022/index.html
[230] NCES methodology - https://nces.ed.gov/surveys/pisa/pisa2025/technical-notes/
[231] official results - https://www.oecd.org/en/publications/2023/12/pisa-2022-results-volume-i_76772a36/full-report.html
[232] Technical report Annex K - https://www.oecd.org/content/dam/oecd/en/data/datasets/pisa/pisa-2018-datasets/ssas-sps-data-files/PISA2018%20Aneex%20K%20TechReport.pdf
[233] GESIS - https://www.gesis.org/en/data-on-adult-education/daten/piaac-daten-zyklus-1/piaac-international/international-public-use-files
[234] technical report chapter 12 - https://www.oecd.org/content/dam/oecd/en/about/programmes/edu/piaac/technical-reports/cycle-2/piaac-technical-report-2023/chapter-12-piaac-technical-report-draft-1.pdf
[235] catalogue entry is ZA6712 - https://search.gesis.org/research_data/ZA6712
[236] OECD first-cycle page - https://www.oecd.org/en/data/datasets/piaac-1st-cycle-database.html
[237] official release announcement - https://www.iea.nl/node/4611
[238] database user guide - https://www.iea.nl/sites/default/files/2025-02/T23_UG-International-Database.pdf
[239] Boston College - https://timss.bc.edu/latest-news/t23-international-results-release.html
[240] IEA restricted-use documentation - https://www.iea.nl/node/4604
[241] process-data release announcement - https://www.iea.nl/news-events/news/pirls-2021-process-data-available
[242] official international report description - https://www.iea.nl/publications/study-reports/international-reports-iea-studies/pirls-2021-international-results
[243] restricted-use route - https://www.iea.nl/node/4053
[244] user guide - https://www.iea.nl/sites/default/files/2025-02/ICILS_2023_User_Guide.pdf
[245] official release - https://www.iea.nl/news-events/news/icils-2023-international-report-results-and-resources-now-available-online
[246] technical report was revised in July 2026 - https://www.iea.nl/publications/icils-2023-technical-report
[247] IEA's process release - https://www.iea.nl/node/4452
[248] user guide - https://www.iea.nl/sites/default/files/2024-05/ICCS%20User%20Guide_0.pdf
[249] The study centre's release - https://ausawards.acer.edu.au/ae/news/article/citizenship-education-in-times-of-global-challenge
[250] PISA PUF download terms - https://survey.oecd.org/index.php?lang=en&r=survey/index&sid=197663
[251] PIAAC PUF terms - https://survey.oecd.org/index.php?lang=en&r=survey/index&sid=424913
[252] OECD's general data terms - https://www.oecd.org/en/about/terms-conditions.html
[253] IEA repository agreement - https://www.iea.nl/sites/default/files/2019-05/Disclaimer%20and%20License%20Agreement.pdf
[254] IEA's materials page - https://www.iea.nl/data
[255] NCES - https://nces.ed.gov/nationsreportcard/researchcenter/datatools.aspx
[256] The 2017 mathematics process-data release - https://www.nationsreportcard.gov/process_data/
[257] Tatsuoka fraction subtraction (CDM) - source documentation - https://raw.githubusercontent.com/alexanderrobitzsch/cdm/master/man/fraction.subtraction.data.Rd
[258] Tatsuoka fraction subtraction (CDM) - source documentation - https://alexanderrobitzsch.r-universe.dev/CDM/data/fraction.subtraction.qmatrix/csv
[259] Tatsuoka fraction subtraction (CDM) - source documentation - https://alexanderrobitzsch.r-universe.dev/CDM
[260] alexanderrobitzsch.r-universe.dev - csv - https://alexanderrobitzsch.r-universe.dev/CDM/data/fraction.subtraction.data/csv
[261] ECPE English grammar section (CDM) - source documentation - https://raw.githubusercontent.com/alexanderrobitzsch/cdm/master/man/data.ecpe.Rd
[262] alexanderrobitzsch.r-universe.dev - json - https://alexanderrobitzsch.r-universe.dev/CDM/data/data.ecpe/json
[263] ASSISTments 2009–2010 corrected collapsed Skill Builder - source documentation - https://sites.google.com/site/assistmentsdata/home/2009-2010-assistment-data
[264] ASSISTments 2009–2010 corrected collapsed Skill Builder - source documentation - https://sites.google.com/site/assistmentsdata/an-explanation-on-how-to-interpret-our-data-sets
[265] drive.google.com - view - https://drive.google.com/file/d/1NNXHFRxcArrU0ZJSb9BIL56vmUt5FhlE/view?usp=sharing
[266] drive.google.com - view - https://drive.google.com/file/d/0B_hO8cnpcIMgUGZzRnh3bHJrSjQ/view?usp=sharing
[267] Junyi Academy Online Learning Activity Dataset (2020 release; 2018–2019 logs) - source documentation - https://www.kaggle.com/api/v1/datasets/download/junyiacademy/learning-activity-public-dataset-by-junyi-academy/Info_Content.csv
[268] Junyi Academy Online Learning Activity Dataset (2020 release; 2018–2019 logs) - source documentation - https://www.kaggle.com/api/v1/datasets/download/junyiacademy/learning-activity-public-dataset-by-junyi-academy/Log_Problem.csv
[269] Eedi / NeurIPS 2020 Education Challenge - source documentation - https://www.eedischool.com/research
[270] Duolingo SLAM 2018 shared-task learner responses - source documentation - https://research.duolingo.com/
[271] dataverse.harvard.edu - dataset.xhtml - https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/8SWHNO
[272] KDD Cup 2010 Algebra I / Bridge to Algebra - source documentation - https://kdd.org/cupfiles/
[273] KDD Cup 2010 Algebra I / Bridge to Algebra - source documentation - https://kdd.org/kdd-cup/view/kdd-cup-2010-student-performance-evaluation/Rules
[274] kdd.org - algebra 2005 2006.zip - https://kdd.org/cupfiles/algebra_2005_2006.zip
[275] Database Exercises for Knowledge Tracing (DBE-KT22) - source documentation - https://api.datacite.org/dois/10.26193/6DZWOH
[276] Database Exercises for Knowledge Tracing (DBE-KT22) - source documentation - https://dataverse.ada.edu.au/dataset.xhtml?persistentId=doi:10.26193/6DZWOH
[277] Maintainer documentation - https://raw.githubusercontent.com/alexanderrobitzsch/cdm/master/man/data.dtmr.Rd
[278] Eurac corpus description - https://www.porta.eurac.edu/lci/merlin/
[279] original research paper - https://aclanthology.org/P11-1019/
[280] release report - https://doi.org/10.17863/CAM.114333
[281] report and version description - https://www.repository.cam.ac.uk/items/ba155087-0754-4c6b-ade8-68858e1df2f0
[282] university data record - https://tudatalib.ulb.tu-darmstadt.de/items/1e2ff254-6bba-454f-bd9f-e4aa1ecb7658
[283] license - https://github.com/myrosia/semeval-2013-task7/blob/main/LICENSE
[284] Official description and terms - https://researchdatasets.cambridge.org/datasets/cambridge-multiple-choice-questions-reading-dataset
[285] technical report with schema - https://www.repository.cam.ac.uk/bitstreams/90fc31ea-bd4c-4b33-8474-1e127635a6d3/download
[286] Item Response Warehouse - https://itemresponsewarehouse.org/
[287] collections - https://itemresponsewarehouse.org/collections.html
[288] core standard - https://itemresponsewarehouse.org/standard.html
[289] 2025 IRW introduction - https://doi.org/10.3758/s13428-025-02796-y
[290] Official access page - https://ef-lab.mmll.cam.ac.uk/EFCAMDAT.html
[291] github.com - skill-data-atlas - https://github.com/AndersH3/skill-data-atlas
[292] payload manifest - https://github.com/AndersH3/skill-data-atlas/blob/main/data/download-manifest.json
[293] release verification - https://github.com/AndersH3/skill-data-atlas/blob/main/data/release-verification.json
[294] dataset source records - https://github.com/AndersH3/skill-data-atlas/blob/main/datasets/README.md
[295] report quality record - https://github.com/AndersH3/skill-data-atlas/blob/main/output/pdf/report-quality-check.json
[296] report builder - https://github.com/AndersH3/skill-data-atlas/blob/main/reports/build_report.py

# Appendix A. AI disclosure


Disclosure revision: **30 October 2026**. The initial research and acquisition snapshot is **29 October 2026**; integration of the earlier report, supplementary checks and three small additional mirrors are dated **30 October 2026**. The project is **Skill Data Atlas**, hosted at https://github.com/AndersH3/skill-data-atlas.

## Nature and extent of AI involvement

This report and the repository's curation material were prepared with **OpenAI Codex**, using a primary assistant and delegated AI agents. They performed substantive research, interpretation, selection, writing and coding. Newly written project prose is AI-assisted unless a file identifies another source or author.

Exact model builds, settings and contexts were not fully retained for every agent and turn. No particular checkpoint or deterministic configuration is asserted for the entire workflow.

| Work area | AI contribution | What the record supports |
|---|---|---|
| Discovery and scope | Searched for human skill, knowledge and cognitive-performance response sources; screened out personality and self-report tests from the skill shortlist | A curated search and inclusion judgment, not an exhaustive census |
| Catalogue and synthesis | Drafted the catalogue profiles, descriptions, comparisons, recommendations, citations and machine-readable catalogue, including seven earlier-report additions | AI-authored summaries that can contain interpretation or transcription errors |
| Access and licensing | Read provider terms, distinguished data from item-content rights, assessed redistribution, and revised decisions when evidence changed | A documented AI research interpretation, not independent legal clearance |
| Acquisition and packaging | Downloaded source files, selected named objective-task subsets and packaged eligible files | The selected scope is documented; some mirrors are subsets or omit duplicate encodings |
| Documentation | Wrote provenance notes and project field guides; retained author documentation where available | Project guides are labelled separately from original author codebooks |
| Code and technical checks | Produced and ran Python/R and command-line tooling for parsing, dimensions, counts, hashes, archive CRCs and release verification | Specific structural and byte-integrity checks, with limits described below |
| Report production | Drafted the narrative, generated the PDF with ReportLab, and used rendered page images for AI-assisted visual review | Layout review by AI assistants; it is not a human publication sign-off |
| Repository operations | Proposed branding and prepared GitHub metadata, links, commits, release uploads and verification records | Actions performed through tools under the project owner's task authorization |

## Human direction and review status

The project owner specified the research objective, excluded personality-oriented tests, requested redistribution-permitted downloads and a complete report, authorized GitHub publication, selected the project name and metadata, and requested this disclosure. Those directions and authorizations are distinct from a source-by-source factual or legal review.

**Independent human fact-checking, legal review and scientific peer review are not documented in the available project record.** Checks by additional AI agents remain AI checks; agreement between agents is not independent human validation. At least one delegated review attempt during the rename was interrupted by a usage limit. An interrupted attempt is not treated as a completed review. Completed checks for the delivered edition are recorded in the quality and verification files.

The maintainer remains responsible for decisions about publication and subsequent use. A later human review should be identified as a separate review with its scope, date and evidence, rather than inferred from the repository's existence or from this disclosure.

## Integration of the earlier report

AI assistants extracted the supplied `older_reports/Candidate Datasets.docx`, compared every candidate with the catalogue, checked primary sources and inspected selected files. The original was preserved unchanged with a checksum and candidate crosswalk. Its authorship, prompts and complete AI-generation history are undocumented; embedded citation tokens had no recoverable source map and were not primary evidence.

Corrections cover Music Ensemble's timed Raven block, Much–Mutak's distinct item blocks, the TüEyeQ repository and HCP's identifier-stripped export. Music Ensemble remains linked pending a field-minimization decision. The older equating recommendation became qualified guidance. Three small collections were added with original bytes, licences and codebooks; no linking model was fitted. These are AI checks, without a newly documented human review.

## Relationship to the original data

The mirrored observations were acquired from the cited external providers. This workflow **did not generate or add synthetic participant answers** to the mirrored datasets. That statement concerns this project's actions; it does not independently authenticate every upstream participant or response.

AI generated project summaries, catalogue records, interpretation, field guides and tooling. It did not become the original collector or author of the underlying studies. Original data, author documentation and project-authored guides are distinguished in the source records and manifests.

Source studies may themselves contain automatically generated stimuli, annotations or model-derived scores. For example, the English C-Test study compared generation strategies including GPT-4. Such upstream use is distinct from generating respondent answers for this repository. Upstream AI involvement was not exhaustively audited across every source; the original study documentation remains authoritative for that question.

Some acquisitions preserve a selected portion of a source rather than its entire deposit. SRO and OpenNeuro contain documented objective-task subsets. Eedi preserves 18 original CSV tables without the restricted question images or macOS resource forks. MERLIN omits optional alternative encodings and automatic NLP annotations. Lossless repackaging and these scope choices are recorded; they should not be described as universal full-deposit mirrors.

## Tools, inspection and verification limits

The assistants consulted public provider pages, papers, repositories, codebooks, schemas, file inventories and selected file contents. Local tools downloaded and processed the source files. AI-readable tool outputs included structural information, counts and selected samples. The repository does not contain a complete record of every value or byte exposed through tool outputs, so it cannot establish that participant-level material was never processed by an AI system.

Published provenance records are not complete access or service-retention logs. AI service providers' retention settings and training-use status were not audited as part of this project; the repository makes no guarantee about them. No claim is made that this project independently anonymized the released data or established the adequacy of the original consent and privacy arrangements.

SHA-256 comparisons and archive CRC checks test byte integrity and archive consistency. Schema and dimension checks describe inspected file structure. Recounted rows, tokens, attempts and identifiers retain their stated units. These checks do **not** establish scientific validity, representativeness, genuine human participation, ethical approval, lawful ownership of every upstream component, or suitability for an individual assessment decision. A checksum match also does not establish that an AI's interpretation of a variable is correct.

AI-assisted visual review checks page layout and legibility. It does not verify every scientific assertion, reference, licence interpretation or code path. No new scoring model was fitted, no superiority of a scoring method was demonstrated, and no causal or population-norm claim was validated in this task.

## Material corrections and residual uncertainty

The workflow included substantive revisions, illustrating the need to revisit AI conclusions against primary evidence:

| Issue | Final treatment |
|---|---|
| Eedi licence initially treated as unconfirmed | The provider's CC BY-NC-ND 4.0 statement and additional image restrictions were found and recorded; only unchanged CSV tables were mirrored |
| Packaged response objects initially excluded because a separate data header was absent | Formal package-wide GPL grants and the absence of contrary notices were reassessed; the SAPA and two CDM source objects were included without inferring rights to separate proprietary stimuli |
| MERLIN website and deposited release counts differed | The mirrored version 1.2 metadata was checked as 2,287 records, with the earlier website count of 2,286 explicitly distinguished |

The report can still contain missed sources, inaccurate summaries, broken links, version mismatches, mistaken assumptions or code defects. Source documentation itself can be incomplete. The catalogue's evidence levels and stated unknowns should be retained rather than converted into a general claim that all information is verified. Licence interpretations should be rechecked against the precise source and intended use; this disclosure does not change upstream terms.

## Evidence and reproducibility

The [catalogue](../data/catalogue.json), [redistribution audit](../data/redistribution-audit.json), [payload manifest](../data/download-manifest.json), [release verification](../data/release-verification.json), [dataset source records](../datasets/README.md), and [report quality record](../output/pdf/report-quality-check.json) identify the available evidence. These records support specific checks, not a complete history of the research process.

The [report builder](build_report.py) and published Markdown permit regeneration of the report from its inputs, subject to the documented software and font dependencies. The complete prompts, per-agent settings, intermediate outputs, search paths and all access logs were not retained as a reproducible research package. **Rebuilding the PDF is distinct from reproducing the AI-assisted discovery and decision process.**

This disclosure describes the work recorded for this edition. It should be updated if additional AI work, human review, data transformations or licensing decisions materially change the project.
