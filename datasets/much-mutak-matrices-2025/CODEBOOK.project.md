# Project field guide

This AI-assisted Skill Data Atlas guide is separate from the original author codebooks in `codebooks/`. Refer to those codebooks for authoritative variable definitions and value encodings.

## Main file and identifiers

`original/tte_data.csv` is the unchanged source CSV: 1,244 participant rows, 164 columns, 1,244 distinct `ID` strings. `Group` identifies instruction order: 1 means non-speeded/accuracy first, then speeded; 2 means speeded first, then accuracy. Counts are 992 and 252 respectively. Preserve IDs as strings when joining source files.

## Main reasoning responses

The first block's item suffixes are `MR01_01` through `MR10_01`; the second block's are `MR11_02` through `MR20_02`. Prefixes have different meanings:

- `X_` preserves the raw selected figural elements as a character-vector representation of zero/one selections. This is not a single conventional multiple-choice distractor number.
- `Y_` is the source's binary scored response (0/1).
- `T_` is item response time in **milliseconds**, according to the author codebook.

`Y_MR_01` and `Y_MR_02` are source block sum scores. The solution-code table `original/mr_itemsolutions.csv` has columns `item` and `solutionCode`; consult the supplemental codebook before implementing a new scoring rule. Never infer option meanings from a numeric code alone.

The file also includes six training items (`MRt`), a solvable masking item (`MRm`), and two unsolvable persistence items (`MRp`). Persistence items should not be counted as ordinary scored matrix items. Repeated objective concentration tasks use `X_CT` raw counts and `Y_CT` scored responses; they are a separate task, not additional reasoning items. Confidence ratings and questionnaires have different measurement status.

## Analysis boundaries

`AO`, `CM` and `EF` variables concern self-reported action orientation, current motivation and effort. Their presence in an unchanged source CSV does not place them in the skill-test shortlist. Demographic, device, attention-check and disruption fields are context or quality variables, not measured skill labels.

Each person received both 10-item reasoning blocks under different instructions. Treat this as a common-person experimental block design. Account for block content, fixed item order, instruction-order group, fatigue and speed-accuracy effects. Do not describe it as a repeated administration of the same 20-item test or as two independently validated IQ tests. Source warnings about difficult items, floor effects, unsupervised timing and limited population generalizability still apply.

## Scope and integrity

No data values or column names were altered. Only selected source files are mirrored; see `SOURCE.md` for omissions. Original author documentation remains separate from this guide. The accompanying manifest records the provider's SHA-256 and the matching local SHA-256 for all original files. Checksums establish byte identity, not validity of a new scoring method.
