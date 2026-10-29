# Sources, permission and snapshot scope

Retrieved: 2026-10-29

License: **CC0-1.0**. The external dataset license remains separate from the parent repository AGPL license.

## Exact objective task selection

ANT, DPX, WATT3, motorSelectiveStop, stopSignal, stroop and twoByTwo. All734 original event files for these tasks are retained in their original BIDS paths. MRI, physiology, surveyMedley and preference/risk/discount tasks are omitted. BIDS event files are unchanged; only ZIP packaging and task selection changed.

## Primary source and license evidence

- https://raw.githubusercontent.com/OpenNeuroDatasets/ds004636/769186fe1b185fae16437f380bfebd56edf7acd7/dataset_description.json
- https://codeload.github.com/OpenNeuroDatasets/ds004636/tar.gz/769186fe1b185fae16437f380bfebd56edf7acd7
- https://raw.githubusercontent.com/OpenNeuroDatasets/ds004636/769186fe1b185fae16437f380bfebd56edf7acd7/CHANGES
- https://raw.githubusercontent.com/OpenNeuroDatasets/ds004636/769186fe1b185fae16437f380bfebd56edf7acd7/README.md
- https://raw.githubusercontent.com/OpenNeuroDatasets/ds004636/769186fe1b185fae16437f380bfebd56edf7acd7/participants.json
- https://raw.githubusercontent.com/OpenNeuroDatasets/ds004636/769186fe1b185fae16437f380bfebd56edf7acd7/participants.tsv
- https://raw.githubusercontent.com/OpenNeuroDatasets/ds004636/769186fe1b185fae16437f380bfebd56edf7acd7/task-ANT_events.json
- https://raw.githubusercontent.com/OpenNeuroDatasets/ds004636/769186fe1b185fae16437f380bfebd56edf7acd7/task-DPX_events.json
- https://raw.githubusercontent.com/OpenNeuroDatasets/ds004636/769186fe1b185fae16437f380bfebd56edf7acd7/task-WATT3_events.json
- https://raw.githubusercontent.com/OpenNeuroDatasets/ds004636/769186fe1b185fae16437f380bfebd56edf7acd7/task-motorSelectiveStop_events.json
- https://raw.githubusercontent.com/OpenNeuroDatasets/ds004636/769186fe1b185fae16437f380bfebd56edf7acd7/task-stopSignal_events.json
- https://raw.githubusercontent.com/OpenNeuroDatasets/ds004636/769186fe1b185fae16437f380bfebd56edf7acd7/task-stroop_events.json
- https://raw.githubusercontent.com/OpenNeuroDatasets/ds004636/769186fe1b185fae16437f380bfebd56edf7acd7/task-twoByTwo_events.json
- https://raw.githubusercontent.com/spdx/license-list-data/main/text/CC0-1.0.txt

## Integrity

See manifest.json for original source URLs, byte sizes and SHA-256 checksums. For repackaged subsets, every original member has its own source path and hash. Provider checksums or Git blob hashes were compared where available. No publisher article PDF was copied.

## Observed source-file coverage

734 event files from110 distinct source subject IDs. Per-task file counts: WATT3 107, stopSignal106, twoByTwo107, DPX103, motorSelectiveStop104, stroop103 and ANT104. These include incomplete/partial administrations and are not usable sample-size counts. The descriptor reports103 study completers; apply supplied exclusions and missingness checks.
