# EdNet field guide

This project-written guide supplements the original author codebook in UPSTREAM_README.md. It is not a replacement for the original release definitions. Source: https://github.com/riiid/ednet .

| Release | Unit and key fields |
|---|---|
| KT1 | Per-user question-solving records: timestamp, solving_id, question_id, user_answer, elapsed_time. Actual headers are checked in the acquisition manifest. |
| KT2 | Per-user events: timestamp, action_type, item_id, source, user_answer, platform. Actions include enter/respond/submit. |
| KT3 | KT2-type events plus explanation and lecture entry/exit records. |
| KT4 | Broader events including audio/video operations, option elimination, payment/refund/coupon events. |
| Contents/questions.csv | question_id, bundle_id, correct_answer, part, tags and deployed_at metadata. |

In KT1 and `respond` events, `user_answer` records the selected option a-d. In KT4 `erase_choice`/`undo_erase_choice` events, it instead identifies the option being erased/restored; interpret it together with action_type. Join question IDs to `correct_answer` in Contents; do not treat absence of an answer on a navigation record as a wrong answer. The user identifier comes from the learner filename. `item_id` can identify a question, bundle, explanation, lecture or other item depending on action/release. Bundle membership represents a shared stimulus. Do not join different item types solely on a numeric suffix.

KT1 elapsed_time is in milliseconds; the source's example assigns shared duration to questions within one bundle. The shifted timestamps are not real calendar dates. KT2 can retain multiple intermediate selections. For each question, take the last respond selection before the enclosing bundle submit event; do not read user_answer from submit rows, which are bundle-level. Different KT levels overlap and must not be concatenated as independent observations.

Source archives are kept intact; any derived long table or scored matrix is the analyst's transformation and should preserve its provenance and choices.

The original Contents archive has four actual tables (lectures, payments, coupons, questions), plus macOS resource forks and filesystem metadata. contents-schema.json records their exact headers; auxiliary ._ files are not extra data tables.

KT4 adds `cursor_time`, defined by the author as the media playhead position where audio/video is played or paused. It is not an item-response latency; the inspected definition does not establish a conversion unit. The exact actual release headers are recorded in archive-schemas.json.
