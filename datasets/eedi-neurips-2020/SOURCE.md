# Eedi / NeurIPS 2020 Education Challenge - response CSV collection

Provider: Eedi and the NeurIPS 2020 Education Challenge organizers. Retrieval date: 2026-10-29.

- Primary project and licence declaration: https://www.eedischool.com/projects/neurips-education-challenge
- Original ZIP: https://dqanonymousdata.blob.core.windows.net/neurips-public/data.zip
- Author guide and citation: https://arxiv.org/abs/2007.12061
- Detailed version of guide: https://arxiv.org/html/2007.12061v3

## Rights

The provider explicitly applies **CC BY-NC-ND 4.0**: attribution and noncommercial use, with no distribution of modified material. LICENSE.txt contains the full standard licence, obtained from https://raw.githubusercontent.com/spdx/license-list-data/main/text/CC-BY-NC-ND-4.0.txt . Canonical licence: https://creativecommons.org/licenses/by-nc-nd/4.0/ .

The provider adds a separate condition for question images: they are only for model training, and must not be printed or shared. **Every image is excluded from this mirror.** The original full ZIP must not be republished as a release asset because it contains those images.

## Packaging and changes

The 18 original response, metadata and challenge CSV tables are extracted; auxiliary macOS resource forks are excluded. Their bytes are unchanged; lossless recompression and collecting files into a new ZIP are technical packaging changes. No observations, columns, IDs or values are changed. extraction-manifest.json records original archive member paths, sizes, CRC32 and SHA-256 hashes. The source archive inventory records all original filenames; image files are not downloaded into this collection. Auxiliary macOS resource forks are not treated as data tables.

This is a collection of unchanged files under their original licence, not a relicense under this repository's software licence. Do not distribute transformed versions of these data under the no-derivatives condition. CODEBOOK.md is a project-written factual guide, with links to the original author descriptions.

## Citation

Wang, Z., Lamb, A., Saveliev, E., Cameron, P., Zaykov, Y., Hernandez-Lobato, J. M., Turner, R. E., Baraniuk, R. G., Barton, C., Jones, S. P., Woodhead, S., and Zhang, C. (2020). Diagnostic Questions: The NeurIPS 2020 Education Challenge. arXiv:2007.12061.

## Scope caveats

The release retains only the latest answer for each student-question pair. Task1/2 and task3/4 IDs are independently anonymized: identical-looking IDs cannot be joined across task pairs. Timestamps are not response durations. Preserve the official train/test partitions and withheld-label conventions.
