# Project field guide for SPM-LS

This AI-assisted guide supplements the unchanged author codebook in `codebooks/`; it is not an original author codebook.

Load `original/items_spm_ls.rda` using R `load()`. The object is named `items_spm_ls` and is a numeric matrix with **499 rows and 12 columns**. Each row is one packaged respondent record; each column is one test item. **1 means keyed correct and 0 means incorrect**. Inspection found no missing cells. Treat row position or stored row labels as internal indices unless an original documented identifier mapping is available.

The mirror supports binary item-response and factor models. It does not retain original selected distractors or response times, and does not establish a second instrument completed by the same people. Do not compare different archived representations as if they were separate cohorts.

External licence: **MIT AND CC-BY-4.0**; see `SOURCE.md` and the full notices. The project AGPL does not replace those terms or establish rights to proprietary test content.
