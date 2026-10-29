# Catalogue fields

`catalogue.json` is an array with one object per **dataset version or source family**. `catalogue.csv` has the same records, with arrays flattened using ` | `. They describe sources, not examinees. Research date: **2026-10-29**.

| Field | Meaning |
|---|---|
| `id`, `name` | Stable project identifier and release/test name |
| `domain`, `dataset_kind` | Research grouping and actual assessment/practice/performance format |
| `constructs`, `unit`, `granularity` | Measured competencies, observation unit and response structure |
| `sample_size`, `item_count` | Counts with units, scope and caveats; text preserves uncertain/version-specific counts |
| `selected_options_retained` | Actual choices/free responses versus scored-only or unverified records |
| `response_times` | Verified timing availability and definition; unknown is distinct from absent |
| `scoring`, `priority` | Original coding/scoring and this review's suggested research use |
| `access` | Actual download, registration, application or unresolved access route |
| `license_data`, `license_items` | Response-data conditions separately from test-content rights; summaries are not replacement licenses |
| `landing_url`, `download_url` | Primary description and acquisition route; null means no direct unrestricted route established |
| `source_urls` | Primary evidence URLs, including documentation and licensing sources |
| `verification_level`, `verification_detail` | Strength and scope of evidence, independent of access restrictions |
| `verified_date` | Date checked, not the data-collection or publication date |
| `limitations`, `notes_file` | Material constraints and detailed profile path |
| `archive_url`, `documentation_url`, `sha256` | Optional version/file references and hashes where verified |

Evidence levels are defined in [methodology](../research/methodology.md): `file_inspected`, `archive_verified`, `documentation_verified`, and `metadata_only_or_unresolved`. A response-file sample qualifies as file inspection only for the inspected structure, not the entire dataset. A codebook, contents table or ZIP signature alone does not prove that participant records were parsed.

`verification-evidence.json` retains the actual checks and their limits: parsed dimensions/checksums, archive headers/listings, and source-specific structural observations. No response rows are stored. A missing checksum means that a full downloaded file hash was not recorded, not that the file failed integrity checks.

Counts across entries must not be summed: samples can overlap; multiple PISA cycles concern the same programme; SAPA's binary and option forms share observations; harmonized copies are not additional independent studies. Provider participation totals are not automatically imported-file row counts.
