# Music Ensemble verification notes

Checked 30 October 2026. No shared catalogue or report was modified. Proposed record, concise profile and machine-readable inspection evidence are in `tmp/legacy-music/`. Original selected members are temporary inspection copies only, not proposed redistribution payloads.

## Correction decisions

- Add a genuine common-person objective battery candidate, not a two-form equating exemplar. The study's own Raven administration combined the scored items in one timed block.
- Correct authorship to Talamini et al. (2026), DOI 10.1038/s41597-026-06654-0. Kasneci et al. is the separate TüEyeQ study; eye tracking is not established for Music Ensemble.
- Correct total N to 1,438 and distinguish 1,274 matched complete records (637 pairs) from all records. The abstract and current OSF description say 678 pairs; actual clean file and body/table support 637 pairs. Do not silently choose 678.
- Primary API licence is CC BY-NC 4.0, not an unrestricted CC0 or article licence. The DOI paper's licence must not substitute for the data licence.
- Raven selected file contains 47 correctness columns: 46 scored plus retained practice S1M02correct. Excluding practice yields an exact match to clean Raven totals for all 1,438 records. No per-item timing verified in this file. Start and submit timestamps should not be called item latencies.
- Clean file contains WAIS III/IV vocabulary summary columns. This is not evidence of publicly released item-level responses linking a full WAIS instrument to Raven.
- Real IP-like fields and experimenter identifiers are present in the selected Raven file. They may represent in-lab collection devices, rather than private home addresses; no identification claim made. Recommend source-link only for this integration and assess field minimization before mirroring. Do not publish mixed questionnaire archive as a skill-only deposit.

## Primary URLs

- https://doi.org/10.1038/s41597-026-06654-0
- https://eprints.whiterose.ac.uk/id/eprint/238638/1/s41597-026-06654-0.pdf
- https://osf.io/y97t3/
- https://api.osf.io/v2/nodes/y97t3/
- https://api.osf.io/v2/files/67dd57509a9368c91e053a9c/
- https://api.osf.io/v2/licenses/60bf992258510b0009a5a9a6/
- https://osf.io/download/dk4eb/

OSF API and download URLs were actually retrieved with Python requests. Web extraction of Nature article failed its login redirect; published publisher PDF via author institution was read. Range requests returned HTTP206; Python zipfile verified each extracted member CRC. This does not verify the full archive's provider SHA256.
