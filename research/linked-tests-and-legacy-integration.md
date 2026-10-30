# Linking tests and integration of earlier research

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
