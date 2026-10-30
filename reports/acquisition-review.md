# Redistribution decisions and downloaded collection

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

