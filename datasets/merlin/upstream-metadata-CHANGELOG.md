# Changelog

## 1.2 - 2025-04-04

merlin-metadata:

- fix `_task_id`, `_author_L1`, `_rating_fair_cefr_rough` columns of a few entries
- add `task_id-topic-short_mapping.txt`

merlin-text:

- add `_metafn` directories, which encode metadata fields in filenames as:  
  `_test_language / _rating_fair_cefr_rough _-_ _task-topic-short _-_ _author_L1 _-_ _author_id .txt`
- fix "Notice: Undefined index:..." lines

merlin-docs, merlin-exmaralda, merlin-paula, merlin-relannis, merlin-solr, merlin-tasks:

- version bump without changes

## 1.1.1 - 2025-04-04

merlin-relannis:

- merge changes from v1.0.1
- bump version to 1.1.1
- no other changes to the data, in particular the corrections (garbled TH1s for
  German texts 1061_0120358 and 1061_0120440) are NOT included

## 1.0.1 - 2025-04-04

merlin-annis:

- deprecated, use merlin-relannis instead:
  this format is missing annotation layers.

merlin-relannis:

- UN(!)-deprecate relANNIS:
  THIS format contains the full set of annotations (whereas the annis format is missing layers).
- fix example queries
- add corpus metadata (corpus_annotation.tab) for the ANNIS UI
- add "-v1.0.1"-postfix to corpus names to allow for multiple versions
  in ANNIS
- no other changes to the data

## 1.1 - 2018-08-24

merlin-annis, merlin-exmaralda, merlin-paula, merlin-solr, merlin-text:

- corrected garbled TH1s for German texts 1061_0120358 and 1061_0120440

merlin-docs, merlin-metadata, merlin-tasks:

- version bump without changes

merlin-relannis:

- deprecated, use merlin-annis instead

## 1.0 - 2014-12-31

Initial release of MERLIN corpus available through the MERLIN platform:
http://merlin-platform.eu
