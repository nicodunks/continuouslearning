#!/usr/bin/env python3
"""Download the pinned full graph and annotations; verify publisher MD5 and size."""
import base64
import hashlib
import json
from pathlib import Path
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]

def digest(path, algorithm):
    h = hashlib.new(algorithm)
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(8 * 1024 * 1024), b''):
            h.update(chunk)
    return h

def main():
    manifest = json.loads((ROOT / 'data/manifest.json').read_text())
    raw = ROOT / 'data/raw'
    raw.mkdir(parents=True, exist_ok=True)
    results = []
    for item in manifest['files']:
        path = raw / item['name']
        if not path.exists():
            if shutil.disk_usage(raw).free < item['size'] + 2 * 1024**3:
                raise RuntimeError('Insufficient space with 2 GiB reserve')
            partial = path.with_suffix(path.suffix + '.part')
            print('Downloading', item['name'], flush=True)
            subprocess.run(['curl', '--fail', '--location', '--retry', '3', '--continue-at', '-', '--output', str(partial), item['url'] + '?generation=' + item['generation']], check=True)
            path_to_check = partial
        else:
            path_to_check = path
        assert path_to_check.stat().st_size == item['size'], 'Size mismatch'
        assert base64.b64encode(digest(path_to_check, 'md5').digest()).decode() == item['md5_base64'], 'Publisher checksum mismatch'
        if path_to_check != path:
            path_to_check.rename(path)
        results.append({'name':item['name'], 'size':item['size'], 'sha256':digest(path, 'sha256').hexdigest(), 'publisher_md5_verified':True})
        print('Verified', item['name'], flush=True)
    (ROOT / 'data/download_receipt.json').write_text(json.dumps(results, indent=2)+'\n')

if __name__ == '__main__':
    main()
