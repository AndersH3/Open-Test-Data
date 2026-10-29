#!/usr/bin/env python3
"""Upload only manifest-designated large files to this snapshot's GitHub release.

Uses the existing authenticated gh CLI. Existing matching assets are verified
and skipped. Different bytes under an existing name cause a failure; nothing
is overwritten. The release must already exist. Default is read-only.
"""
from pathlib import Path
import argparse
import concurrent.futures
import json
import subprocess

ROOT=Path(__file__).resolve().parents[1]
REPO='AndersH3/Open-Test-Data'
TAG='datasets-2026-10-29'

def gh(args):
    r=subprocess.run(['gh',*args],text=True,capture_output=True)
    if r.returncode:raise RuntimeError(r.stderr.strip())
    return r.stdout

def snapshot():
    releases=json.loads(gh(['api',f'repos/{REPO}/releases','--paginate']))
    return next(r for r in releases if r['tag_name']==TAG)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--upload',action='store_true');ap.add_argument('--workers',type=int,default=2)
    args=ap.parse_args()
    manifest=json.loads((ROOT/'data/download-manifest.json').read_text())
    wanted=[r for r in manifest['files'] if r['storage']=='github_release']
    current=snapshot();existing={r['name']:r for r in current['assets']}
    pending=[]
    for r in wanted:
        a=existing.get(r['release_asset'])
        if a:
            assert a['size']==r['bytes'] and a['state']=='uploaded',r['path']+' size/state mismatch'
            if a.get('digest'):assert a['digest']=='sha256:'+r['sha256'],r['path']+' digest mismatch'
        else:pending.append(r)
    print(json.dumps({'already_verified':len(wanted)-len(pending),'pending':len(pending),'pending_bytes':sum(r['bytes'] for r in pending),'upload_authorized_by_flag':args.upload}),flush=True)
    if not args.upload:return
    def upload(r):
        gh(['release','upload',TAG,str(ROOT/r['path']),'--repo',REPO])
        return {'uploaded':r['release_asset'],'bytes':r['bytes']}
    with concurrent.futures.ThreadPoolExecutor(max_workers=max(1,min(args.workers,3))) as ex:
        futures=[ex.submit(upload,r) for r in pending]
        for f in concurrent.futures.as_completed(futures):print(json.dumps(f.result()),flush=True)
    final={r['name']:r for r in snapshot()['assets']}
    checks=[]
    for r in wanted:
        a=final[r['release_asset']]
        assert a['size']==r['bytes'] and a['state']=='uploaded'
        digest=a.get('digest')
        if digest:assert digest=='sha256:'+r['sha256']
        checks.append({'path':r['path'],'asset_id':a['id'],'name':a['name'],'bytes':a['size'],'github_digest':digest,'sha256_matches':bool(digest),'state':a['state']})
    (ROOT/'data/release-verification.json').write_text(json.dumps({'release_tag':TAG,'repository':REPO,'assets':checks},indent=2)+'\n')
    print(json.dumps({'verified_assets':len(checks),'all_available_digests_match':all(x['sha256_matches'] for x in checks)}),flush=True)

if __name__=='__main__':main()
