# Verification notes for remaining older candidates

AI-assisted primary-source check on 30 October 2026. These notes support integration; the original Word report remains an unverified historical source. The final records are consolidated in `data/catalogue.json`, `data/redistribution-audit.json` and the linking chapter. This note records source-specific checks. Two small exact source-object collections were subsequently prepared at the parent agent’s request, under the project’s existing affirmative package-grant policy. Their final licence/provenance records are in `datasets/edmdata-revised-psvtr/` and `datasets/edmdata-spm-ls/`; the SPM-LS collection additionally retains the original CC BY 4.0 data terms and attribution. Proposed JSON records reflect mirrored status.

## TüEyeQ

The older report's Figshare DOI is **a metadata record**, not the participant dataset. The live Figshare API reports only `data.json` (3,312 bytes) and `metadata summary.csv` (223 bytes). The actual data deposit is [Harvard Dataverse, DOI 10.7910/DVN/JGOCKI](https://doi.org/10.7910/DVN/JGOCKI). Its [registered DOI metadata](https://api.datacite.org/dois/10.7910/DVN/JGOCKI) specifies version 2.0 and CC0; the [data paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC8208979/) also explicitly states CC0 for the dataset.

The paper describes 315 participants and four CFT 20-R blocks. It presents 56 tasks, while current Dataverse metadata describes 41. This conflict is unresolved because live Dataverse download/API access returned a robot challenge/403. Do not present either number as a file-verified column count. Correctness is dichotomized; omissions and six problematic tasks are missing. The paper describes smaller gaze subsets. Additional executive-control task data are available upon request, rather than demonstrated in the public deposit. This qualifies the older report's blanket claim that it contains only one test per person: the public CFT battery and the broader study's other tasks are distinct scopes. Add a qualified catalogue profile, with file acquisition pending provider access.

## HCP Penn Matrices

[Package documentation](https://tmsalab.github.io/edmdata/reference/items-hcp-penn.html) describes two 1,201 × 24 correctness matrices. They are alternative encodings of one sample, not independent datasets. Five nonresponding people were removed; the missingness-preserving variant retains nonadministered items after the five-consecutive-error stopping rule. The package builder [at pinned commit 3c0036e4a665b61adde011aac2215b62bd5da33d](https://raw.githubusercontent.com/tmsalab/edmdata/3c0036e4a665b61adde011aac2215b62bd5da33d/data-raw/hcp-penn-matrix/hcp_penn_matrix_build.R) drops the HCP subject ID. Therefore the standalone matrix is unsuitable for a reliable join to other HCP tests unless a defensible original mapping is acquired.

The [HCP cognitive battery](https://www.humanconnectome.org/study/hcp-young-adult/document/quick-reference-open-access-vs-restricted-data) contains several objective tests. The assertion that HCP participants each took only one test is wrong. Whether the required other instrument's item-level records can be joined is a separate question.

[HCP terms](https://www.vps.humanconnectome.org/study/hcp-young-adult/data-use-terms) require every user of Open Access participant data, including shared copies, to register and agree. The edmdata package's MIT declaration does not establish that these upstream conditions disappear. Recommend a linked, terms-qualified catalogue entry and no unrestricted project mirror.

## Revised PSVT:R

[Author package documentation](https://tmsalab.github.io/edmdata/reference/items_revised_psvtr.html) identifies 516 × 30 binary responses. I loaded the exact [pinned R data object](https://raw.githubusercontent.com/tmsalab/edmdata/3c0036e4a665b61adde011aac2215b62bd5da33d/data/items_revised_psvtr.rda) in native R: 516 rows, 30 columns, values only 0/1, zero missing cells. The 3,182-byte object and its computed SHA-256 are recorded in the proposed JSON profile.

The source package formally declares [MIT](https://raw.githubusercontent.com/tmsalab/edmdata/3c0036e4a665b61adde011aac2215b62bd5da33d/DESCRIPTION), with [full licence text](https://raw.githubusercontent.com/tmsalab/edmdata/3c0036e4a665b61adde011aac2215b62bd5da33d/LICENSE.md). That supports the package's declared grant, not rights to redistribute the original PSVT:R instrument. The inspected object retains correctness only and establishes no cross-test linkage. Recommend catalogue inclusion with precise rights scope and provenance.

## SPM-LS

[Author documentation](https://tmsalab.github.io/edmdata/reference/items_spm_ls.html) describes 499 × 12 binary responses from the final SPM series. Native R confirmed 499 rows, 12 columns, only 0/1 values and no missing cells in the 1,098-byte [pinned packaged object](https://raw.githubusercontent.com/tmsalab/edmdata/3c0036e4a665b61adde011aac2215b62bd5da33d/data/items_spm_ls.rda). The package's [build script](https://raw.githubusercontent.com/tmsalab/edmdata/3c0036e4a665b61adde011aac2215b62bd5da33d/data-raw/spm-ls/spm-ls-build.R) shows how original nominal answer codes are converted to keyed binary responses, followed by listwise deletion. The original [Myszkowski–Storme deposit](https://data.mendeley.com/datasets/h3yhs5gy3w/1) is dated 2018; Robitzsch 2020 is a reanalysis, not its original collection.

The original deposit's [DataCite metadata](https://api.datacite.org/dois/10.17632/h3yhs5gy3w.1) explicitly declares **CC BY 4.0**. The package binary object carries the package MIT declaration. Original stimulus rights remain separate. Add a catalogue entry distinguishing original nominal and packaged binary representations, without asserting either is an independent cohort or paired-test dataset.

## Historical SAPA and ICAR

This is a distinct historical release, not a duplicate of the current catalogue's psychTools 1,525 × 16 sample or the current restricted full ICAR bundle. The [2016 data descriptor](https://openpsychologydata.metajnl.com/articles/10.5334/jopd.25) reports **96,958 people**, random subsets from a **60-item pool**, and already-scored 0/1 responses. The data are hosted at [Harvard Dataverse DOI 10.7910/DVN/AD9RVY](https://doi.org/10.7910/DVN/AD9RVY), rather than the older report's unspecific OSF claim. Both the article and [registered current V3 metadata](https://api.datacite.org/dois/10.7910/DVN/AD9RVY) state CC0. No response file was parsed here.

The design can support connected joint item calibration if the observed overlap permits it. Random subsets do not provide two complete tests for every person, but that does not make all linking impossible. Keep the exact release and missingness qualifications. Add as a separate catalogue source; no large download is needed for this integration.

## Existing IQ1 and discovery resources

IQ1 is already catalogue entry `ospp-iq1`; its selected-option codes, small sample and unresolved redistribution rights were already inspected. Cross-reference rather than duplicate it as a new Culpepper/Balamuta dataset. The EDMdata transformation is another representation of those source observations.

The [2025 IRW introduction](https://doi.org/10.3758/s13428-025-02796-y) states over 900 datasets **for version 28.2**. It is a discovery/standardization resource, not one paired cognitive sample. The [current project site](https://itemresponsewarehouse.org/) has expanded standards including synthetic/simulated data, so human objective performance and source-specific licence screening remain necessary. Preserve the historical count with its version, rather than assert it is a current total.

The older report's abbreviated “Crane et al. 2008 NACC” reference is insufficient to identify a unique paper. A relevant primary paper, [Crane et al., DOI10.1016/j.jclinepi.2007.11.011](https://pmc.ncbi.nlm.nih.gov/articles/PMC2762121/), co-calibrates cognitive screening instruments using **common items**, not a same-person paired-test sample. It is methodological context; no new public response payload was established. Do not identify it as an NACC download without further evidence.

## General correction for integration

A common-person design is one option, not a universal requirement for linking. Common-item anchors can support linking across separate samples; dimensionality, anchor invariance, connectedness and uncertainty remain essential. A battery, a repeated condition, two halves of one instrument and two independently established interchangeable tests must not be conflated. The older report's “only two datasets meet the criterion” conclusion should become a scoped, qualified finding rather than an exhaustive census.
