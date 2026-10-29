# Duolingo SLAM - version 4 (2019-02-13)

Provider: Duolingo, Inc.; deposited by Burr Settles. Acquisition date: 2026-10-29.

## Primary sources and acquisition route

- Dataset DOI: https://doi.org/10.7910/DVN/8SWHNO
- Author task description and original schema: https://sharedtask.duolingo.com/2018.html
- Author-deposited DataCite record: https://api.datacite.org/dois/10.7910/DVN/8SWHNO
- Harvard Dataverse version4 schema.org metadata, preserved by DataONE: https://cn.dataone.org/cn/v2/object/sha256%3Ac99e7d3e18a8ee138442180c31cedf54546f51fe4b02555e0894e11cdfebc7e8
- File DOIs: https://doi.org/10.7910/DVN/8SWHNO/C1LOKO (English), https://doi.org/10.7910/DVN/8SWHNO/Z29WIF (Spanish), https://doi.org/10.7910/DVN/8SWHNO/5YWVBV (French)
- Acquisition mirror: https://github.com/xinhez/11785-project/tree/master/data

The Harvard website and payload/custom-license API returned HTTP403 from this environment. The three original-named tarballs were acquired from the public mirror above. Their exact byte sizes match the author-deposited v4 metadata; embedded CHANGELOG.md identifies v4 and embedded LICENSE.md provides the original rights notice. SHA-256 hashes identify the acquired mirror bytes. The preserved metadata object itself passes its DataONE content-addressed SHA-256 check. It did not expose original archive MD5/SHA checksums, so equality of the three data archives to the original deposit is not independently checksum-proven.

## Rights

Original notice preserved in LICENSE.md: Copyright(c)2016 Duolingo, Inc. The original archive explicitly applies **CC BY-NC 4.0**, with the complete legal code. The author-deposited metadata independently states the same licence. Canonical licence: https://creativecommons.org/licenses/by-nc/4.0/ . Noncommercial and attribution conditions remain attached. This project's software licence does not replace the dataset licence.

## Files and changes

The three tarballs are copied byte-for-byte from the identified mirror. No learner records, labels or archive contents were transformed. Original licence, citation and changelog files are also extracted unchanged for convenience. Each archive covers one course: en_es, es_en, fr_en. The archive-specific upstream documents remain beside the source manifest. CODEBOOK.md is a project-written field guide with links to the official schema; it is labelled separately from original author documentation.

Version4 adds source translation prompts and corrects dependency parsing; do not silently mix it with the original 2018 files. Original learner answer strings are not supplied; the corpus provides correct-answer tokens and error labels. This is predominantly practice rather than a common fixed proficiency examination.

## Citation

Settles, B., Brust, C., Gustafson, E., Hagiwara, M., and Madnani, N. (2018). Second Language Acquisition Modeling. Proceedings of the NAACL-HLT Workshop on Innovative Use of NLP for Building Educational Applications. ACL. Dataset: Settles, Burr, 2018, Data for the 2018 Duolingo Shared Task on Second Language Acquisition Modeling (SLAM), Harvard Dataverse, V4, doi:10.7910/DVN/8SWHNO. Preserve the exact original CITING.md files supplied with each archive.
