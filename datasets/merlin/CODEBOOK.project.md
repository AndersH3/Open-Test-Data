# Project navigation guide: MERLIN v1.2

This is a project-written guide, not an original-author codebook. Consult the original PDFs in `codebooks/` and source documentation ZIP for full definitions and procedures.

## Original codebooks retained

- `codebooks/ratings/MERLIN_Technical-report.pdf`: rating procedures, CEFR alignment and related measurement design.
- `codebooks/annotationscheme/Annotation guidelines.pdf`: annotation instructions.
- `codebooks/annotationscheme/MERLIN-annotation-scheme.pdf`: annotation category scheme.
- `codebooks/annotationscheme/MERLIN_FAQ_final.pdf`: original FAQ.
- `codebooks/transcription/Transcription-guidelines_DE.pdf`: transcription conventions.

These PDFs are byte-identical extractions from the original `merlin-docs-v1.2.zip`. The original metadata README, changelog and license are also provided directly.

## Metadata families

The source CSV in `merlin-metadata-v1.2.zip` is `merlin-metadata-v1.2/metadata_ratings_indicators.csv` (2,287 rows, 362 columns). It includes:

| Prefix/field | Structural meaning |
|---|---|
| `_author_id` | Corpus author identifier; preserve original codes rather than interpreting them as external personal identifiers. |
| `_author_L1`, `_author_age`, `_author_gender` | Original learner metadata; unnecessary for many scoring analyses and not skill scores. |
| `_test_language`, `_test_level_cefr` | Test language and target examination CEFR level. |
| `_task_*`, `_text_type` | Task assignment and genre metadata. |
| `_rating_fair_cefr`, `_rating_fair_cefr_rough` | CEFR-related ratings; follow original technical report for meaning. |
| `_rating_*` | Criterion ratings, including vocabulary, accuracy, coherence and sociolinguistic appropriateness. Do not assume equally spaced numeric scales. |
| `has_*` | Source annotation availability flags. Missing annotation is not zero errors. |
| `count_*` | Annotation/token/sentence counts. |
| `ind_*` | Derived indicators, including normalized counts/error-free ratios. |
| `lex_*`, `morph_*`, `syn_*` | Complexity measures, documented as German-only in the source metadata README. |

The published plain-text representation encodes some metadata in filenames. Different format bundles represent the **same** texts. Target hypotheses are annotations/corrections, not a second independent student performance. Reading passages/tasks create dependencies, and ratings may depend on language, task, raters and sample. Response-time availability was not established.
