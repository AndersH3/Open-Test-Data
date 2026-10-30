# AI disclosure

Disclosure revision: **30 October 2026**. The initial research and acquisition snapshot is **29 October 2026**; integration of the earlier report, supplementary checks and three small additional mirrors are dated **30 October 2026**. The project is **Skill Data Atlas**, hosted at https://github.com/AndersH3/skill-data-atlas.

## Nature and extent of AI involvement

This report and the repository's curation material were prepared with **OpenAI Codex**, using a primary assistant and delegated AI agents. They performed substantive research, interpretation, selection, writing and coding. Newly written project prose is AI-assisted unless a file identifies another source or author.

Exact model builds, settings and contexts were not fully retained for every agent and turn. No particular checkpoint or deterministic configuration is asserted for the entire workflow.

| Work area | AI contribution | What the record supports |
|---|---|---|
| Discovery and scope | Searched for human skill, knowledge and cognitive-performance response sources; screened out personality and self-report tests from the skill shortlist | A curated search and inclusion judgment, not an exhaustive census |
| Catalogue and synthesis | Drafted the catalogue profiles, descriptions, comparisons, recommendations, citations and machine-readable catalogue, including seven earlier-report additions | AI-authored summaries that can contain interpretation or transcription errors |
| Access and licensing | Read provider terms, distinguished data from item-content rights, assessed redistribution, and revised decisions when evidence changed | A documented AI research interpretation, not independent legal clearance |
| Acquisition and packaging | Downloaded source files, selected named objective-task subsets and packaged eligible files | The selected scope is documented; some mirrors are subsets or omit duplicate encodings |
| Documentation | Wrote provenance notes and project field guides; retained author documentation where available | Project guides are labelled separately from original author codebooks |
| Code and technical checks | Produced and ran Python/R and command-line tooling for parsing, dimensions, counts, hashes, archive CRCs and release verification | Specific structural and byte-integrity checks, with limits described below |
| Report production | Drafted the narrative, generated the PDF with ReportLab, and used rendered page images for AI-assisted visual review | Layout review by AI assistants; it is not a human publication sign-off |
| Repository operations | Proposed branding and prepared GitHub metadata, links, commits, release uploads and verification records | Actions performed through tools under the project owner's task authorization |

## Human direction and review status

The project owner specified the research objective, excluded personality-oriented tests, requested redistribution-permitted downloads and a complete report, authorized GitHub publication, selected the project name and metadata, and requested this disclosure. Those directions and authorizations are distinct from a source-by-source factual or legal review.

**Independent human fact-checking, legal review and scientific peer review are not documented in the available project record.** Checks by additional AI agents remain AI checks; agreement between agents is not independent human validation. At least one delegated review attempt during the rename was interrupted by a usage limit. An interrupted attempt is not treated as a completed review. Completed checks for the delivered edition are recorded in the quality and verification files.

The maintainer remains responsible for decisions about publication and subsequent use. A later human review should be identified as a separate review with its scope, date and evidence, rather than inferred from the repository's existence or from this disclosure.

## Integration of the earlier report

AI assistants extracted the supplied `older_reports/Candidate Datasets.docx`, compared every candidate with the catalogue, checked primary sources and inspected selected files. The original was preserved unchanged with a checksum and candidate crosswalk. Its authorship, prompts and complete AI-generation history are undocumented; embedded citation tokens had no recoverable source map and were not primary evidence.

Corrections cover Music Ensemble's timed Raven block, Much–Mutak's distinct item blocks, the TüEyeQ repository and HCP's identifier-stripped export. Music Ensemble remains linked pending a field-minimization decision. The older equating recommendation became qualified guidance. Three small collections were added with original bytes, licences and codebooks; no linking model was fitted. These are AI checks, without a newly documented human review.

## Relationship to the original data

The mirrored observations were acquired from the cited external providers. This workflow **did not generate or add synthetic participant answers** to the mirrored datasets. That statement concerns this project's actions; it does not independently authenticate every upstream participant or response.

AI generated project summaries, catalogue records, interpretation, field guides and tooling. It did not become the original collector or author of the underlying studies. Original data, author documentation and project-authored guides are distinguished in the source records and manifests.

Source studies may themselves contain automatically generated stimuli, annotations or model-derived scores. For example, the English C-Test study compared generation strategies including GPT-4. Such upstream use is distinct from generating respondent answers for this repository. Upstream AI involvement was not exhaustively audited across every source; the original study documentation remains authoritative for that question.

Some acquisitions preserve a selected portion of a source rather than its entire deposit. SRO and OpenNeuro contain documented objective-task subsets. Eedi preserves 18 original CSV tables without the restricted question images or macOS resource forks. MERLIN omits optional alternative encodings and automatic NLP annotations. Lossless repackaging and these scope choices are recorded; they should not be described as universal full-deposit mirrors.

## Tools, inspection and verification limits

The assistants consulted public provider pages, papers, repositories, codebooks, schemas, file inventories and selected file contents. Local tools downloaded and processed the source files. AI-readable tool outputs included structural information, counts and selected samples. The repository does not contain a complete record of every value or byte exposed through tool outputs, so it cannot establish that participant-level material was never processed by an AI system.

Published provenance records are not complete access or service-retention logs. AI service providers' retention settings and training-use status were not audited as part of this project; the repository makes no guarantee about them. No claim is made that this project independently anonymized the released data or established the adequacy of the original consent and privacy arrangements.

SHA-256 comparisons and archive CRC checks test byte integrity and archive consistency. Schema and dimension checks describe inspected file structure. Recounted rows, tokens, attempts and identifiers retain their stated units. These checks do **not** establish scientific validity, representativeness, genuine human participation, ethical approval, lawful ownership of every upstream component, or suitability for an individual assessment decision. A checksum match also does not establish that an AI's interpretation of a variable is correct.

AI-assisted visual review checks page layout and legibility. It does not verify every scientific assertion, reference, licence interpretation or code path. No new scoring model was fitted, no superiority of a scoring method was demonstrated, and no causal or population-norm claim was validated in this task.

## Material corrections and residual uncertainty

The workflow included substantive revisions, illustrating the need to revisit AI conclusions against primary evidence:

| Issue | Final treatment |
|---|---|
| Eedi licence initially treated as unconfirmed | The provider's CC BY-NC-ND 4.0 statement and additional image restrictions were found and recorded; only unchanged CSV tables were mirrored |
| Packaged response objects initially excluded because a separate data header was absent | Formal package-wide GPL grants and the absence of contrary notices were reassessed; the SAPA and two CDM source objects were included without inferring rights to separate proprietary stimuli |
| MERLIN website and deposited release counts differed | The mirrored version 1.2 metadata was checked as 2,287 records, with the earlier website count of 2,286 explicitly distinguished |

The report can still contain missed sources, inaccurate summaries, broken links, version mismatches, mistaken assumptions or code defects. Source documentation itself can be incomplete. The catalogue's evidence levels and stated unknowns should be retained rather than converted into a general claim that all information is verified. Licence interpretations should be rechecked against the precise source and intended use; this disclosure does not change upstream terms.

## Evidence and reproducibility

The [catalogue](../data/catalogue.json), [redistribution audit](../data/redistribution-audit.json), [payload manifest](../data/download-manifest.json), [release verification](../data/release-verification.json), [dataset source records](../datasets/README.md), and [report quality record](../output/pdf/report-quality-check.json) identify the available evidence. These records support specific checks, not a complete history of the research process.

The [report builder](build_report.py) and published Markdown permit regeneration of the report from its inputs, subject to the documented software and font dependencies. The complete prompts, per-agent settings, intermediate outputs, search paths and all access logs were not retained as a reproducible research package. **Rebuilding the PDF is distinct from reproducing the AI-assisted discovery and decision process.**

This disclosure describes the work recorded for this edition. It should be updated if additional AI work, human review, data transformations or licensing decisions materially change the project.
