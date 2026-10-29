# Complete research report

The [PDF report](../output/pdf/open-test-data-complete-research-report.pdf) combines executive findings, all 37 source profiles, the redistribution audit, acquisition provenance, codebook references, methodological guidance and a numbered bibliography. The [generated Markdown source](complete-report-source.md) is also available.

## Rebuild

Use Python 3 with `reportlab`, `mistune` and `pypdf`, plus DejaVu Sans/Mono fonts installed under `/usr/share/fonts/truetype/dejavu/`.

```bash
python3 reports/build_report.py
```

The build reads committed original research notes and the acquisition review. It does not parse participant files or embed their responses. Numbered citations are generated from source links. The resulting PDF has contents, bookmarks and clickable references; `output/pdf/report-quality-check.json` records structural checks. Poppler rendering was additionally reviewed before delivery.

To regenerate the acquisition review from the committed decision audit and locally present payloads:

```bash
python3 reports/update_acquisition_sources.py --final
```

Large release assets must be downloaded to their original manifest paths before regenerating their SHA-256 hashes. The committed [download manifest](../data/download-manifest.json) specifies exact paths, sizes and URLs.

## Release integrity helper

`publish_release_assets.py` reads the manifest and checks the existing release using the authenticated GitHub CLI. Its default is read-only:

```bash
python3 reports/publish_release_assets.py
```

The explicit `--upload` flag uploads missing manifest-designated large files. It rejects an existing asset with different bytes and does not overwrite files. It records GitHub's SHA-256 digests in [release verification](../data/release-verification.json). Dataset-specific reuse conditions remain applicable to every file.
