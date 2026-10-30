# Project field guide for Revised PSVT:R

This AI-assisted guide supplements the unchanged author codebook in `codebooks/`; it is not an original author codebook.

Load `original/items_revised_psvtr.rda` using R `load()`. The object is named `items_revised_psvtr` and is a numeric matrix with **516 rows and 30 columns**. Each row is one packaged respondent record; each column is one test item. **1 means keyed correct and 0 means incorrect**. Inspection found no missing cells. Treat row position or stored row labels as internal indices unless an original documented identifier mapping is available.

The mirror supports binary item-response and factor models. It does not retain original selected distractors or response times, and does not establish a second instrument completed by the same people. Do not compare different archived representations as if they were separate cohorts.

External licence: **MIT**; see `SOURCE.md` and the full notices. The project AGPL does not replace those terms or establish rights to proprietary test content.
