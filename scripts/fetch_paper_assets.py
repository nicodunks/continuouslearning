#!/usr/bin/env python3
"""Fetch publisher PDFs/supplements and validate files; never label HTML as a PDF."""
import concurrent.futures
import hashlib
import json
from pathlib import Path
import re
import subprocess
import tempfile
from urllib.parse import urljoin

ROOT=Path(__file__).resolve().parents[1]

def fetch(url):
    with tempfile.NamedTemporaryFile() as f:
        r=subprocess.run(['curl','-fsSL','--max-time','45','--retry','1',url,'-o',f.name],capture_output=True)
        if r.returncode: return None
        return Path(f.name).read_bytes()

def run(entry):
    folder=ROOT/'papers'/entry['folder']
    meta=json.loads((folder/'metadata.json').read_text())
    assets=meta.get('assets',[])
    doi=entry['doi']; base='https://doi.org/'+doi
    if doi.startswith('10.1038/'):
        base='https://www.nature.com/articles/'+doi.split('/')[1]
    elif doi.startswith('10.7554/eLife.'):
        base='https://elifesciences.org/articles/'+doi.split('.')[-1]
    candidates=[]
    page=fetch(base)
    if page:
        html=page.decode(errors='replace')
        for h in re.findall(r'(?:href|content)=[\"\']([^\"\']+)[\"\']',html):
            h=h.replace('&amp;','&')
            if re.search(r'\.(pdf|zip|mov|mp4)(?:\?|$)',h):
                if any(k in h for k in ['MOESM','supp','elife-','download','/pdf','/articles/']):candidates.append(urljoin(base,h))
    if doi.startswith('10.1038/'): candidates.insert(0,base+'.pdf')
    if doi.startswith('10.7554/'): candidates.insert(0,base+'.pdf')
    errors=[]
    for url in dict.fromkeys(candidates):
        if any(a['url']==url for a in assets): continue
        ext=re.search(r'\.(pdf|zip|mov|mp4)(?:\?|$)',url).group(1)
        name='main.pdf' if url==base+'.pdf' else url.split('/')[-1].split('?')[0]
        if (folder/name).exists():continue
        data=fetch(url)
        if not data or (ext=='pdf' and not data.startswith(b'%PDF-')) or (ext=='zip' and not data.startswith(b'PK')):
            errors.append({'url':url,'error':'Unavailable or unexpected format'});continue
        # Avoid storing unexpectedly huge archives in this low-space workspace.
        if len(data)>150*1024**2:
            errors.append({'url':url,'error':'Larger than 150 MiB; inspect separately'});continue
        (folder/name).write_bytes(data)
        assets.append(dict(filename=name,url=url,bytes=len(data),sha256=hashlib.sha256(data).hexdigest()))
    meta['assets']=assets;meta['download_errors']=errors
    (folder/'metadata.json').write_text(json.dumps(meta,indent=2)+'\n')
    return (entry['folder'],len(assets),len(errors))

if __name__=='__main__':
    entries=json.loads((ROOT/'papers/catalog.json').read_text())
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        for result in pool.map(run,entries):print(result,flush=True)
