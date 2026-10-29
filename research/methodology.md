# Scope, evidence and selection method

Research cutoff: **29 October 2026**. This is a curated research review, not an exhaustive registry or a certification of each test's validity.

## What counts as a skill-based test here?

Included: tasks where a person demonstrates knowledge, reasoning, memory, attention, perception, reading, numeracy, language production or another competence, and an answer or performance is observed. A broad interpretation includes cognitive ability and educational attainment. The catalogue separates fixed assessments, adaptive/sampled assessments, repeated-trial tasks, human-rated performances and learning/practice logs.

Excluded from the core shortlist: personality inventories, interests, attitudes, self-reported ability, clinical symptom questionnaires, synthetic examinees, question banks without human responses and datasets consisting only of AI responses. A mixed study can qualify through its performance-based subset; its questionnaires do not become skill tests.

## What “online available” means

Availability, openness and evidence strength are separate dimensions. Each profile records its actual route: anonymous download, software-package data, registration/agreement, application/approval, or restricted research access. An online catalogue or sample test does not establish access to individual responses. “Not verified” means the review did not establish the fact; it does not mean the feature is absent.

Evidence levels used in the catalogue:

| Level | Evidence obtained | What it does not establish |
|---|---|---|
| `file_inspected` | Actual response-file bytes were parsed or their schema inspected; full-file versus sample checks are specified | Full cleaning, psychometric validity, representativeness or legal clearance |
| `archive_verified` | Actual archive bytes/listing or range headers were checked | Response values and complete schema |
| `documentation_verified` | Primary provider/researcher description, codebook or package documentation checked | Successful end-to-end download today |
| `metadata_only_or_unresolved` | Only indexed/deposited metadata were available, or response-file evidence remains unresolved | Successful file acquisition or complete schema verification |

Evidence strength does not imply unrestricted access: even an inspected public file may carry restrictive terms. Full details and exceptions appear in the domain notes and [verification evidence](../data/verification-evidence.json). A successful HTTP response alone is not a parsed dataset. Login forms, anti-bot pages and archive errors are recorded as limitations. No restricted access agreements were accepted on the user's behalf.

## How sources were selected and checked

AI assistants conducted research in parallel across cognitive tasks, large educational assessments, learning datasets, and language/constructed-response assessment. Primary sources were preferred: provider databases and terms, university/laboratory releases, original articles and author-maintained software documentation. Search snippets were used for discovery; claims supported only by indexed metadata are explicitly marked. Selected public archives and small response files were checked directly. Counts retain their units: people, submissions, answers, items, passages and events are not interchangeable.

The priority labels express **practical suitability for a stated research use**, based on response granularity, documentation, access burden and methodological complexity. They are this review's judgments, not empirical rankings of test quality or recommendations for high-stakes individual decisions.

## Minimum fields to preserve on acquisition

For every version, save its source URL, retrieval date, checksum, original citation, applicable terms and codebook. Record participant and item IDs, response categories, answer key/version, missing codes, administration form, and timing units. Preserve original files outside the public repository until redistribution rights are clear. Maintain a separate derived table and a transformation log.

Suggested analysis representation:

| Field | Meaning |
|---|---|
| `dataset_version`, `person_id`, `item_id` | Provenance and stable within-dataset identifiers |
| `attempt_id`, `session_id`, `position` | Repeated attempts and administration order, when available |
| `raw_response`, `score`, `max_score` | Selected option/free response and explicitly derived scoring |
| `response_time_ms` | Latency only when its definition and units are known |
| `missing_reason` | Not administered, omitted, not reached, invalid and missing remain distinguishable |
| `form_id`, `testlet_id`, `skill_id` | Booklet/adaptive routing, shared stimulus and content domain |
| `weight`, `replicate_weights`, `cluster_id` | Complex sample design, if supplied |

Do not force all datasets into binary accuracy. Distractor selections, partial-credit marks and nominal error labels can support different models. A timestamp, total duration or average of previous attempts is not automatically the response time for the current item.

## Comparing scoring methods responsibly

1. Start with a transparent baseline on the same responses and comparable item exposure/forms: number correct or proportion of available marks. Account for form difficulty before comparing different adaptive/booklet sets. Add appropriate Rasch/IRT, ordinal, multidimensional or diagnostic models only where their assumptions fit the data.
2. Fit transformations, item weights and model parameters on training data; evaluate on held-out examinees. If testing generalization to new items or institutions, hold out those units too. Keep repeated attempts and revisions together, or use a time-respecting learning evaluation.
3. Examine reliability/precision, calibration, rank stability and predictive/criterion validity where suitable outcomes exist. Better agreement with a score already derived from the same answers is not independent validity evidence.
4. Model booklet missingness, adaptive routing, clustering and repeated measures. Never automatically score non-administered items as wrong. Use the official survey design for population claims.
5. Treat plausible values as multiple population-analysis draws, not observed item responses or precise labels for individual ability. Do not average plausible values into a supposedly true personal score.
6. Treat rare patterns cautiously: inspect sample size, guessing, item dependence, rapid responses and data quality before assigning unusual answers high weight. Validate any novelty-based score on independent data.

These steps are proposed analysis guidance; no scoring experiment or psychometric comparison was run in this research task.

## Licensing and publication boundary

This project stores AI-assisted research summaries, metadata and links, plus a separately licensed mirror of sources with explicit redistribution permission. Its existing repository license does **not** relicense external response data, item wording, photographs, speech recordings, keys or rubrics. A software package's license is not automatically proof of permission to administer or republish the original test. Some sources allow analysis but prohibit redistributing files; some also restrict derived outputs. The redistribution audit records each decision; consult the version-specific primary terms before publication.

## Coverage limitations

The search emphasizes openly documented datasets with useful human responses and English-language source documentation. It covers multiple domains and languages, but is not a census of occupational, vocational, physical or professional certification tests. Many commercial tests have public practice questions but no reusable person-level data. Size, access and licenses can change; recheck the recorded source before a new download. A file inspection is only a structural check, and the samples have not been validated for any particular deployment population.
