# OpenNeuro ds004636: objective behavioral events

Redistribution decision: **CC0**, explicitly declared by the dataset's `dataset_description.json`, preserved under `codebooks/`. This public-domain dedication is separate from the parent repository's AGPL license. Please still credit the data authors and follow scientific attribution practice.

Dataset: https://openneuro.org/datasets/ds004636/versions/1.0.4
Dataset DOI: https://doi.org/10.18112/openneuro.ds004636.v1.0.4
Pinned source commit: `769186fe1b185fae16437f380bfebd56edf7acd7`
Source: https://github.com/OpenNeuroDatasets/ds004636/tree/769186fe1b185fae16437f380bfebd56edf7acd7
Data descriptor and author list: https://pmc.ncbi.nlm.nih.gov/articles/PMC11271451/
Retrieved: 2026-10-29.

## Scope and codebooks

This is an explicit **behavioral performance subset**, not the entire MRI study. It contains 734 original `events.tsv` files for ANT (attention), DPX (context processing), WATT3 (planning), motorSelectiveStop, stopSignal, stroop and twoByTwo (task switching), in their original BIDS paths. Files are byte-identical source members repackaged in one ZIP. MRI images, physiology, surveyMedley, discounting and preference/risk tasks were excluded. No event values were changed. All original event-sidecar JSON codebooks for the selected tasks, participant metadata/definitions and suggested exclusions are provided under `codebooks/`.

The source descriptor reports 103 study completers, with recommended task/participant exclusions and only 68 participants free of all recommended behavioral exclusions. The unfiltered selected event files actually contain 110 distinct source subject IDs, including people with incomplete/partial administrations; 110 must not be interpreted as 110 complete usable participants. Availability and usable N vary by task. Interpret event timing using the supplied sidecars; scanner onsets are not automatically reaction times. Original MRI images and test-stimulus artwork are not redistributed here.

`observed-column-schemas.json` is a project-generated convenience field inventory. Original author definitions in `task-*_events.json` take precedence. See `manifest.json` for source URLs and hashes for every original event-file member.
