#!/usr/bin/env python3
"""Acquire missing main PDFs from open primary repositories; never mark them read."""
import concurrent.futures
import hashlib
import json
from pathlib import Path
import subprocess
import tempfile
from urllib.parse import urlencode

ROOT = Path(__file__).resolve().parents[1]


def fetch(url):
    with tempfile.NamedTemporaryFile() as f:
        result = subprocess.run(
            ['curl', '-fsSL', '--max-time', '25', '--max-filesize', '157286400', url, '-o', f.name],
            capture_output=True,
        )
        return Path(f.name).read_bytes() if result.returncode == 0 else b''


def run(entry):
    folder = ROOT / 'papers' / entry['folder']
    dest = folder / 'main.pdf'
    if dest.exists() and dest.read_bytes()[:5] == b'%PDF-':
        return entry['folder'], 'already present'
    doi = entry['doi']
    candidates = []
    if doi.startswith(('10.1101/', '10.64898/')):
        candidates.append('https://www.biorxiv.org/content/' + doi + '.full.pdf')
    if doi.startswith('10.7554/eLife.'):
        candidates.append('https://elifesciences.org/articles/' + doi.split('.')[-1] + '.pdf')
    # Europe PMC includes author manuscripts and NIH-hosted preprints.
    query = 'https://www.ebi.ac.uk/europepmc/webservices/rest/search?' + urlencode(
        {'query': 'DOI:"' + doi + '"', 'format': 'json', 'pageSize': 5}
    )
    payload = fetch(query)
    try:
        results = json.loads(payload).get('resultList', {}).get('result', [])
    except (ValueError, TypeError):
        results = []
    for result in results:
        pmcid = result.get('pmcid')
        if pmcid and pmcid.startswith('PMC'):
            candidates.append('https://europepmc.org/articles/' + pmcid + '?pdf=render')
    if doi.startswith('10.1371/'):
        journal = 'plosone' if '/journal.pone.' in doi else 'ploscompbiol'
        candidates.append('https://journals.plos.org/' + journal + '/article/file?id=' + doi + '&type=printable')
    attempts = []
    metadata_path = folder / 'metadata.json'
    meta = json.loads(metadata_path.read_text())
    for url in dict.fromkeys(candidates):
        data = fetch(url)
        if data.startswith(b'%PDF-'):
            dest.write_bytes(data)
            meta.setdefault('assets', []).append({
                'filename': 'main.pdf', 'url': url, 'bytes': len(data),
                'sha256': hashlib.sha256(data).hexdigest(),
            })
            meta['main_pdf_acquisition'] = 'Downloaded; verify version during full reading.'
            metadata_path.write_text(json.dumps(meta, indent=2) + '\n')
            return entry['folder'], 'downloaded'
        attempts.append({'url': url, 'error': 'No valid PDF received'})
    meta['main_pdf_fallback_attempts'] = attempts
    metadata_path.write_text(json.dumps(meta, indent=2) + '\n')
    return entry['folder'], 'still missing'


if __name__ == '__main__':
    entries = json.loads((ROOT / 'papers/catalog.json').read_text())
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        for result in pool.map(run, entries):
            print(*result, sep=': ', flush=True)
