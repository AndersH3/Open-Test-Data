# MERLIN Written Learner Corpus v1.2

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
