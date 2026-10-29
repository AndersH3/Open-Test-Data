# SAPA ability and selected-option response objects

Source package: **psychTools 2.6.4**, as distributed by `cran/psychTools` at commit `7dc591f8ac11c0ef1764cf853f3065aa60653d09`. Retrieved 2026-10-29.

Declared license: **GPL (>=2)**, represented here as SPDX **GPL-2.0-or-later**. `upstream-DESCRIPTION` is the unmodified formal package license declaration. `LICENSE.GPL-2.0-or-later.txt` supplies the full GPLv2 license text with the later-version option retained. These external files keep their upstream GPL license; the parent repository's AGPL license does not replace it.

## Redistribution basis

The R developers' package specification treats DESCRIPTION License as the package's license. No separate copyright/license carveout for these response objects was found in the inspected source tree, data documentation or package metadata. CRAN policy requires clarity of rights for all package components and maintainer authorization; it expressly recognizes `.rda` files as source or readily convertible to source. Accordingly this mirror relies on the affirmative package-wide GPL grant, rather than requiring redundant per-file license headers. This is a source-object mirror, not a claim that raw data values or every original test stimulus necessarily carry copyright.

Primary package declaration: https://github.com/cran/psychTools/blob/7dc591f8ac11c0ef1764cf853f3065aa60653d09/DESCRIPTION
Package source: https://github.com/cran/psychTools/tree/7dc591f8ac11c0ef1764cf853f3065aa60653d09
R package license specification: https://cran.r-project.org/doc/manuals/r-release/R-exts.html#Licensing
CRAN all-component rights/source policy: https://cran.r-project.org/web/packages/policies.html
Canonical GPLv2: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html
License text transcription source: https://raw.githubusercontent.com/spdx/license-list-data/main/text/GPL-2.0-or-later.txt

## Attribution and data provenance

Package author/maintainer: William Revelle. Data documentation explicitly attributes collection to Revelle with David Condon, 8-31 August 2012, within the SAPA project. Cite Condon & Revelle (2014), The International Cognitive Ability Resource: Development and initial validation of a public-domain measure, Intelligence 43, 52-64, together with the versioned psychTools package and its original documentation. Original dataset information: https://www.sapa-project.org/.

## Exact mirrored scope and test-content boundary

Only `ability.rda` and `iqitems.rda`: two representations of the same 1,525 people × 16 cognitive items, plus their codebooks. The current full ICAR archive and its separate access terms are outside this mirror.

The original `.rda` files are unchanged source-distribution data objects, editable after loading in R; no executable package code or compiled binary is included. The original author `.Rd` documentation is included unchanged as the codebook. No new observations or scores were generated. No unrelated personality datasets, secure question bank, test artwork, commercial test handbook or publisher article PDF is mirrored. Permission to redistribute these packaged response objects is not a grant to administer or republish a separate current test bank.

## Source availability and GPL notices

GPLv2 section 1 permits verbatim source copies with the applicable notices, warranty disclaimer and license copy retained. The original data objects, relevant Rd source documentation and DESCRIPTION provided here are the material being redistributed; R can load them directly using `load()`. The `.rda` files are the preferred form supplied in the upstream **source** distribution, not compiled executable versions needing a separate opaque binary/source offer. The upstream full package source remains linked above for context; unrelated package datasets are not required to inspect or modify these numeric response objects.

Redistributors should retain the upstream license/attribution, source links and no-warranty notices. Any covered modifications must be identified with dates and distributed under the applicable GPL terms; retain the original >=2 option. See the full license for its conditions rather than treating this summary as the license. The project-generated `read-data.R` is a convenience example for reading the preserved source objects, not a replacement for them.
