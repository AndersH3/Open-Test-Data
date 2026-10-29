#!/usr/bin/env python3
"""Combine reviewed acquisition decisions and refresh report/collection indexes.

The acquisition agents' JSON ledgers are supplied as inputs; the committed
redistribution-audit.json is the portable record, so the PDF itself has no /tmp
dependency. Use --final only when all 37 decisions are complete.
"""
from pathlib import Path
import argparse
import collections
import hashlib
import json
import urllib.parse

ROOT=Path(__file__).resolve().parents[1]
TAG='datasets-2026-10-29'
REPO='https://github.com/AndersH3/Open-Test-Data'

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--ledger',action='append',default=[])
    ap.add_argument('--override-ledger',action='append',default=[],help='Explicit reviewed replacement decisions')
    ap.add_argument('--final',action='store_true')
    args=ap.parse_args()
    cat=json.loads((ROOT/'data/catalogue.json').read_text())
    byid={r['id']:r for r in cat};decisions={}
    if not args.ledger and (ROOT/'data/redistribution-audit.json').exists():
        decisions={r['catalogue_id']:r for r in json.loads((ROOT/'data/redistribution-audit.json').read_text())['decisions']}
    for file in args.ledger:
        raw=json.loads(Path(file).read_text())
        batch=raw if isinstance(raw,list) else raw.get('decisions',[raw])
        for d in batch:
            assert d['catalogue_id'] in byid,d['catalogue_id']
            assert d['catalogue_id'] not in decisions,'Duplicate '+d['catalogue_id']
            decisions[d['catalogue_id']]=d
    for file in args.override_ledger:
        raw=json.loads(Path(file).read_text())
        for d in raw if isinstance(raw,list) else raw.get('decisions',[raw]):
            assert d['catalogue_id'] in byid
            decisions[d['catalogue_id']]=d
    for r in cat:
        decisions.setdefault(r['id'],{'catalogue_id':r['id'],'status':'pending','reason':'Acquisition or access verification still in progress.','dataset_dir':None,'license':r['license_data'],'source_urls':r['source_urls'],'payload_files':[]})
    ordered=[decisions[r['id']] for r in cat]
    if args.final:assert all(d['status']!='pending' for d in ordered),'Unfinished decisions'
    counts=collections.Counter(d['status'] for d in ordered)
    dirs=sorted(set(d['dataset_dir'] for d in ordered if d['status']=='mirrored'))
    payloads=sorted(set(f for d in ordered if d['status']=='mirrored' for f in d['payload_files']))
    inventory=[];assets={}
    for rel in payloads:
        p=ROOT/rel
        assert p.is_file(),rel
        digest=hashlib.file_digest(p.open('rb'),'sha256').hexdigest()
        large=p.stat().st_size>15_000_000
        if large:
            assert p.name not in assets,'Duplicate release asset name: '+p.name
            assets[p.name]=rel
        inventory.append({'path':rel,'bytes':p.stat().st_size,'sha256':digest,
            'storage':'github_release' if large else 'git',
            'release_asset':p.name if large else None,
            'url':f'{REPO}/releases/download/{TAG}/{urllib.parse.quote(p.name)}' if large else f'{REPO}/blob/main/{urllib.parse.quote(rel)}'})
    audit={'research_date':'2026-10-29','final':args.final,'scope':'37 previously researched catalogue entries; source-specific performance subsets explicitly identified',
      'summary':dict(counts),'unique_collection_directories':len(dirs),'decisions':ordered,
      'redistribution_policy':'Accept explicit source grants, including formal package-wide licences covering packaged response objects with no contrary data notices. A public download or paper licence alone is not a data grant; packaged data rights do not authorize separate proprietary test stimuli. Third-party licences remain separate from repository AGPL.',
      'release_tag':TAG}
    (ROOT/'data/redistribution-audit.json').write_text(json.dumps(audit,indent=2,ensure_ascii=False)+'\n')
    (ROOT/'data/download-manifest.json').write_text(json.dumps({'retrieved_date':'2026-10-29','release_tag':TAG,'files':inventory,'total_payload_bytes':sum(x['bytes'] for x in inventory)},indent=2,ensure_ascii=False)+'\n')
    lines=['# Redistribution decisions and downloaded collection','',
      f"All **37 catalogue entries** were screened separately from scientific suitability. Current result: **{counts.get('mirrored',0)} mirrored entries**, **{counts.get('excluded',0)} excluded**, **{counts.get('inaccessible',0)} licensed but inaccessible**, and **{counts.get('pending',0)} pending**. Mirrored entries map to **{len(dirs)} distinct collection folders** because BEETLE and SciEntsBank share one original release.",'',
      f"The acquired response/stimulus payloads total **{sum(x['bytes'] for x in inventory):,} bytes** across **{len(inventory)} files**. Files larger than 15 MB are GitHub release assets; smaller payloads, licences, codebooks, source records and manifests are stored in Git. The release is part of the same repository. File size and SHA-256 provide an integrity record, not proof of psychometric validity.",'',
      '## Decision standard','',
      'Redistribution was accepted where an explicit source grant covers the files. This includes formal package-wide GPL grants for packaged response objects when no contrary data notice applies; a separate file header is not required. It does not authorize separate proprietary test banks or stimuli. Standard Creative Commons licences can permit sharing with attribution, non-commercial, ShareAlike or NoDerivatives conditions. Those conditions are preserved rather than replaced by the project licence. Unresolved grants are excluded; clear licences with unavailable files are separately recorded. No restricted-use applications or custom access agreements were submitted.','',
      'Eedi is a special case: unchanged response and metadata CSV members are losslessly repackaged; every question image is excluded. No cleaned, filtered or merged derivative response table is distributed. For mixed cognitive batteries, the selected objective tasks and original member hashes are documented; surveys, preference tasks and MRI images are not part of the skill-response mirror.','',
      '## Decisions for every source','',
      '| Source | Decision | Basis |','|---|---|---|']
    for d in ordered:
        r=byid[d['catalogue_id']];link=d['source_urls'][0] if d['source_urls'] else r['landing_url']
        lines.append(f"| {r['name']} (`{r['id']}`) | {d['status']} | {d['reason']} [Primary evidence]({link}) |")
    lines += ['','## Mirrored collection documentation','']
    idx=['# Downloaded datasets','',f"Acquisition snapshot: **29 October 2026**. **{counts.get('mirrored',0)} catalogue entries** map to **{len(dirs)} unique collections**. Each collection retains its own licence. Large files are attached to the [dataset release]({REPO}/releases/tag/{TAG}); smaller files are committed here.",'',
      'See the [complete audit](../data/redistribution-audit.json), [payload manifest](../data/download-manifest.json) and [complete research PDF](../output/pdf/open-test-data-complete-research-report.pdf). Download a release asset with an authenticated GitHub account if this repository is private.','',
      '| Collection | Licence | Sources and codebooks |','|---|---|---|']
    for dr in dirs:
        ds=[d for d in ordered if d['dataset_dir']==dr and d['status']=='mirrored'];label=' / '.join(byid[d['catalogue_id']]['name'] for d in ds);d=ds[0]
        idx.append(f"| [{label}]({Path(dr).name}/) | {d['license']} | [Source record]({Path(dr).name}/SOURCE.md); original documentation and project guides in the folder |")
        lines += ['### '+label,'',f"**Licence:** {d['license']}. **Selected scope:** {d['reason']}",'',f"[Source record and documentation]({REPO}/tree/main/{dr})",'']
        source=ROOT/dr/'SOURCE.md'
        if source.exists():
            original=source.read_text()
            # Include original project-authored provenance, not protected source data.
            original='\n'.join(line for line in original.splitlines() if not line.startswith('# '))
            lines.append(original);lines.append('')
        lines+=['| Payload | Bytes | SHA-256 prefix |','|---|---:|---|']
        for f in inventory:
            if f['path'].startswith(dr+'/'):
                lines.append(f"| [{Path(f['path']).name}]({f['url']}) | {f['bytes']:,} | `{f['sha256'][:16]}` |")
        lines.append('')
    idx+=['','## Reuse and integrity','',
      'Keep each source licence and attribution with redistributed files. Never apply the repository AGPL to third-party datasets. Preserve original file bytes and distinguish an author codebook from a project field guide. SHA-256 hashes cover the payload files; dataset-level manifests additionally record member provenance and source checks where available.','',
      'For a large file, follow its manifest URL or use `gh release download datasets-2026-10-29 --repo AndersH3/Open-Test-Data --pattern FILENAME`. Verify the downloaded SHA-256 against `data/download-manifest.json`.','']
    (ROOT/'reports/acquisition-review.md').write_text('\n'.join(lines)+'\n')
    (ROOT/'datasets/README.md').write_text('\n'.join(idx)+'\n')
    verification='''# Verification, limitations and reproducibility

## What was checked

The research catalogue distinguishes response-file inspection, archive verification, primary documentation and unresolved metadata-only evidence. The acquisition phase adds byte counts, SHA-256 hashes, provider hashes where supplied, archive integrity checks, source snapshots and explicit subset rules. The downloaded payload manifest is the authoritative list of mirrored files; the 37-source audit records exclusions as well as acquisitions.

Selected source archives were parsed to verify response schemas and counts. A full parse does not establish that every response is valid or every participant is unique. Provider participation totals, file rows and distinct respondent identifiers remain separate. Some mirrors contain all deposited files; mixed batteries are limited to named objective tasks, and duplicate format encodings may be omitted. Every such selection is documented in the collection source record.

## Corrections from acquisition

MERLIN's mirrored version 1.2 has 2,287 metadata records; the earlier website description gives 2,286. The versioned deposit and actual metadata govern this mirror. The English C-Test study contains 40 users, 32 forms and 160 user-form attempts, or 3,200 observed gap scores; whole-form duration is present, while per-gap latency was not established. The working-memory deposit has two original CSV files and distinguishes raw task records from participant-collapsed scores. The OpenNeuro archive contains source subject identifiers beyond the reported study-completer cohort; recommended exclusions must be applied explicitly rather than silently deleting source rows.

## Rebuild and locate the evidence

The complete source review is in the research directory. Catalogue metadata is supplied as JSON and CSV. Source-specific licences, citations, codebooks and file manifests accompany each mirrored collection. The root download manifest identifies files stored in Git and large release assets. Files from inaccessible or non-redistributable sources are linked, not included.

The PDF is generated by `reports/build_report.py` from original project-authored Markdown. It uses ReportLab and Mistune, supplies clickable numbered citations, a contents page and PDF bookmarks, and checks the written PDF with pypdf. The committed Markdown remains readable independently of PDF-generation software. Visual rendering was reviewed before delivery; the report does not embed participant responses or protected test images.

## Limits of the findings

This is a deep, curated review with a dated acquisition snapshot, not a census of all tests. It emphasizes documented sources with useful human response data. Licences and links can change; rights are version-specific and component-specific. Original codebooks can contain ambiguities, and some files have limited documentation. A project field guide explains observed structure without claiming to be an author-approved replacement.

The review does not establish population norms, cross-cultural equivalence, causal effects, algorithmic superiority or suitability for an individual decision. No scoring experiment was run. Reuse should preserve the difference between observed answers, assigned marks, expert annotations and estimated latent traits. Independent held-out validation remains necessary for a new scoring method.
'''
    (ROOT/'reports/verification-summary.md').write_text(verification)
    print(json.dumps({'decisions':len(ordered),'summary':dict(counts),'collections':len(dirs),'payload_files':len(inventory),'payload_bytes':sum(x['bytes'] for x in inventory)},indent=2))

if __name__=='__main__':main()
