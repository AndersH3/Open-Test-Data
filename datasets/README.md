# Downloaded datasets

Acquisition snapshot: **29 October 2026**. **15 catalogue entries** map to **14 unique collections**. Each collection retains its own licence. Large files are attached to the [dataset release](https://github.com/AndersH3/skill-data-atlas/releases/tag/datasets-2026-10-29); smaller files are committed here.

See the [complete audit](../data/redistribution-audit.json), [payload manifest](../data/download-manifest.json) and [complete research PDF](../output/pdf/skill-data-atlas-complete-research-report.pdf). Download a release asset with an authenticated GitHub account if this repository is private.

| Collection | Licence | Sources and codebooks |
|---|---|---|
| [Constrained English C-Test user study](ctest_mip_2024/) | CC-BY-4.0 | [Source record](ctest_mip_2024/SOURCE.md); original documentation and project guides in the folder |
| [Duolingo SLAM 2018 shared-task learner responses](duolingo-slam-2018/) | CC-BY-NC-4.0 | [Source record](duolingo-slam-2018/SOURCE.md); original documentation and project guides in the folder |
| [ECPE English grammar section (CDM)](ecpe-grammar/) | GPL-2.0-or-later | [Source record](ecpe-grammar/SOURCE.md); original documentation and project guides in the folder |
| [EdNet KT1–KT4 (Santa English test preparation)](ednet/) | CC-BY-NC-4.0 | [Source record](ednet/SOURCE.md); original documentation and project guides in the folder |
| [Eedi / NeurIPS 2020 Education Challenge](eedi-neurips-2020/) | CC-BY-NC-ND-4.0 | [Source record](eedi-neurips-2020/SOURCE.md); original documentation and project guides in the folder |
| [Tatsuoka fraction subtraction (CDM)](fraction-subtraction/) | GPL-2.0-or-later | [Source record](fraction-subtraction/SOURCE.md); original documentation and project guides in the folder |
| [Ganis-Kievit mental rotation validation data](ganis-kievit-mental-rotation/) | CC-BY-4.0 | [Source record](ganis-kievit-mental-rotation/SOURCE.md); original documentation and project guides in the folder |
| [Junyi Academy Online Learning Activity Dataset (2020 release; 2018–2019 logs)](junyi-2020/) | CC-BY-NC-SA-4.0 | [Source record](junyi-2020/SOURCE.md); original documentation and project guides in the folder |
| [Working Memory Develops at a Similar Rate Across Diverse Stimuli](mathy-friedman-working-memory/) | CC-BY-4.0 | [Source record](mathy-friedman-working-memory/SOURCE.md); original documentation and project guides in the folder |
| [MERLIN multilingual examination writing](merlin/) | CC-BY-SA-4.0 | [Source record](merlin/SOURCE.md); original documentation and project guides in the folder |
| [OpenNeuro ds004636 objective task subset](openneuro-ds004636-objective-tasks/) | CC0-1.0 | [Source record](openneuro-ds004636-objective-tasks/SOURCE.md); original documentation and project guides in the folder |
| [SAPA cognitive ability: psychTools ability / iqitems](sapa-ability-iqitems/) | GPL-2.0-or-later | [Source record](sapa-ability-iqitems/SOURCE.md); original documentation and project guides in the folder |
| [SemEval 2013 Task 7 BEETLE / SemEval 2013 Task 7 SciEntsBank](semeval2013-task7/) | CC-BY-SA-3.0 | [Source record](semeval2013-task7/SOURCE.md); original documentation and project guides in the folder |
| [Self-Regulation Ontology objective performance-task subset](sro-performance-tasks/) | CC-BY-4.0 | [Source record](sro-performance-tasks/SOURCE.md); original documentation and project guides in the folder |

## Reuse and integrity

Keep each source licence and attribution with redistributed files. Never apply the repository AGPL to third-party datasets. Preserve original file bytes and distinguish an author codebook from a project field guide. SHA-256 hashes cover the payload files; dataset-level manifests additionally record member provenance and source checks where available.

For a large file, follow its manifest URL or use `gh release download datasets-2026-10-29 --repo AndersH3/skill-data-atlas --pattern FILENAME`. Verify the downloaded SHA-256 against `data/download-manifest.json`.

