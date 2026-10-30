# Source, licence and acquisition scope

Retrieved 30 October 2026 for Skill Data Atlas. This is an AI-assisted project provenance note.

## Attribution and source

Much, S., Mutak, A., Pohl, S., and Ranger, J. (2025). Data From a Validation Study of Two Psychometric Models on Test-taking Behavior. Journal of Open Psychology Data, 13, 1. https://doi.org/10.5334/jopd.124

Dataset: Modeling speed-ability trade-off and test-taking persistence - Parameter validation for two psychometric models. https://doi.org/10.17605/OSF.IO/9J6HM (https://osf.io/9j6hm/).

## Licence

**CC BY 4.0.** The OSF project's formal licence relationship resolves to https://api.osf.io/v2/licenses/563c1cf88c5e4a3877f9e96a/ and the data paper explicitly states this data licence in section 3.6. The original OSF node, file metadata, licence metadata and full licence text are saved here. Retain attribution, source links and the licence when sharing. This grant does not transfer rights in separate third-party tests or survey wording. The article identifies copyrighted motivational-disposition material that was not republished in its source repository; no such stimulus material has been added here. The repository AGPL does not replace the dataset licence.

## Exact selection

The unmodified original `tte_data.csv` and `mr_itemsolutions.csv` are mirrored. The original CSV and PDF main codebooks and PDF supplemental codebook accompany them. Provider SHA-256 hashes match all five copied files. The main CSV includes the source's questionnaire covariates; retaining its original bytes does not make those variables skill tests. Exclude action orientation, motivation, effort and other self-report measures from the skill-test shortlist.

Omitted source files: the alternative `tte_data.Rds` encoding; optional `mr_logdata.csv`, `ct_pagetimes.csv` and `tte_disruptions.csv`; stimulus/instruction overviews `mr_ItemOverview.pdf`, `ct_ItemOverview.pdf` and `efcm_ItemOverview.pdf`; and `Preregistration_Psychometric-Model-Validation.pdf`. These remain available from OSF. No participant values were changed, no columns were removed, and no test-item figures were copied. This is a selected file mirror, not a complete OSF deposit.

## Verified structure and study design

The downloaded CSV contains 1,244 rows and 164 columns, with 1,244 unique participant IDs. Observed Group counts are 992 in group 1 and 252 in group 2. The author codebook defines group 1 as accuracy/non-speeded instruction first and group 2 as speeded instruction first.

The original study used two distinct 10-item reasoning blocks, with each participant receiving both instruction conditions and randomized instruction order. It did not administer the same 20 items twice. Distinct block items, fixed item order and changing instructions must be accounted for when comparing scores. There is no claim here that this is an equating dataset for two established IQ instruments.

See `manifest.json` for source URLs, byte sizes, provider checksums and local SHA-256 hashes; see `CODEBOOK.project.md` for a guide to the original author documentation.
