# Legacy candidate verification for Much and Mutak

Checked 30 October 2026 using the original data paper, formal OSF metadata and downloaded original data/codebooks. AI-assisted research note for integration; not a new analysis or human review.

## Primary evidence and important correction

The correct citation is **Much, S., Mutak, A., Pohl, S., and Ranger, J. (2025)**, *Data From a Validation Study of Two Psychometric Models on Test-taking Behavior*, DOI [10.5334/jopd.124](https://doi.org/10.5334/jopd.124). Much and Mutak share first authorship.

The older report's repeated-test claim is inaccurate. The study used **two distinct 10-item blocks**, selected as matched OMIB item pairs, for 20 main items total. Every participant completed one block under each instruction; the order of speed versus accuracy emphasis was randomized between groups. The final sample was **1,244**, with groups **992 and 252**. This is a common-person experimental block design. Block content, fixed item order and instruction effects complicate linking; it is not the same 20 items administered twice, nor two established IQ instruments. Speed emphasis did not impose a hard reasoning-test deadline. Six training items, a later masking item and two unsolvable persistence items are separate from the 20 main reasoning items. See paper sections 2.1, 2.4 and 2.5.

## Native data verification

The formal OSF node is [9j6hm](https://api.osf.io/v2/nodes/9j6hm/); dataset DOI [10.17605/OSF.IO/9J6HM](https://doi.org/10.17605/OSF.IO/9J6HM). The OSF API was accessible through Python even when browser fetch returned HTTP 403. Original files were downloaded through provider-issued links, not reconstructed from an aggregator.

The unchanged `tte_data.csv` has **1,244 rows, 164 columns and 1,244 unique ID strings**. Observed group counts match 992/252. The original author CSV codebook defines `Group=1` as non-speeded first and `Group=2` as speeded first; `X_MR*` are raw figural-element selection vectors, `Y_MR*` are binary scores and `T_MR*` are **milliseconds**. These are selected-element response arrays, not conventional single distractor codes. Main block suffixes are `MR01_01`–`MR10_01` and `MR11_02`–`MR20_02`. The original solution table has `item` and `solutionCode` columns. Additional training, masking, unsolvable persistence, concentration, confidence, self-report and demographic variables must be distinguished.

## Licence and prepared mirror

The OSF node's formal licence relationship resolves to [CC BY 4.0 metadata](https://api.osf.io/v2/licenses/563c1cf88c5e4a3877f9e96a/). The data paper independently identifies the same **data licence** in section 3.6. Provider SHA-256 values match all five retained original files.

Prepared `datasets/much-mutak-matrices-2025/` contains unchanged original main CSV and `mr_itemsolutions.csv`, original main CSV/PDF codebooks and supplemental PDF codebook, formal OSF node/file/licence metadata snapshots, full licence text, `SOURCE.md`, a labelled AI-assisted `CODEBOOK.project.md`, and a member-hash manifest. The two response/solution payloads total **1,635,153 bytes**. No stimulus PDFs or proprietary questionnaire wording were copied.

The original main CSV's questionnaire columns are preserved to retain original file bytes. AO/CM/EF measures are self-report covariates and stay outside the skill-test shortlist. Optional action logs, concentration page times and disruption free text, alternative Rds encoding, stimulus/instruction overviews and preregistration are explicitly omitted from the mirror. This is a selected file mirror, not the complete deposit.

The final catalogue, redistribution audit and download manifest consolidate the record and both payload hashes. Optional logs downloaded for inspection are not part of the published collection.

## Recommended report treatment

Add one cognitive-performance source profile, with `file_inspected` evidence and `mirrored` redistribution status, and use the corrected design in the linking discussion. Preserve the historic DOCX as an older, fallible secondary report. Prefer this dataset for speed-accuracy and common-person block-model diagnostics; it does not by itself supply a validated equating relation between two established IQ batteries.
