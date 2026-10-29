# Duolingo SLAM field guide - v4

Project-written factual guide. Original schema: https://sharedtask.duolingo.com/2018.html . Original version/citation/licence documentation is preserved under upstream-documentation/ and inside each original tarball.

## Course and split organization

- en_es: people learning English who already speak Spanish.
- es_en: people learning Spanish who already speak English.
- fr_en: people learning French who already speak English.

Files represent TRAIN, DEV and TEST splits. TRAIN includes the label column. DEV/TEST features and answer-key files are distinct. Preserve the supplied split and join keys by token instance ID. v4 filenames use the 20190204 data stamp; the archive changelog identifies the February13,2019 v4 release.

## Exercise metadata

| Field | Meaning |
|---|---|
| prompt | Source-language translation prompt, where supplied in v4; not the learner's answer. |
| user | Anonymized learner identifier. |
| countries | Country-code metadata supplied by source. |
| days | Time since beginning of the learner's recorded course history, in days. |
| client | Access client such as web, Android or iOS. |
| session | Context such as lesson, practice or test. |
| format | reverse_translate, reverse_tap or listen exercise format. |
| time | Whole-exercise time in seconds, shared by its tokens; not a per-token response latency. |

## Token rows

Whitespace-delimited rows contain token instance ID, correct-answer token, Universal Dependencies POS, morphological features, dependency edge label, dependency head and (for labelled files) error label. `0` means OK and `1` means mistake - the reverse of correct=1 coding. The dependency analysis is machine generated, not a gold human parse. Empty lines separate exercises and lines beginning # supply metadata.

The original schema notes some negative time values due to logging bugs; treat them as missing if using timing. Tokens within an exercise are dependent and share timing. Models must not use future interactions or answer keys for held-out predictions. The labels describe alignment to a correct answer; they are not a copy of what the learner actually typed.
