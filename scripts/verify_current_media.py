import pathlib,json,hashlib,re,sys
r=pathlib.Path(sys.argv[1] if len(sys.argv)>1 else '.')
m=json.loads((r/'CURRENT_MEDIA_MANIFEST.json').read_text('utf-8'))
assert m['number_of_public_files']==17 and len(m['files'])==17
paths=[x['path'] for x in m['files']]
assert len(set(paths))==17
sums={}
for line in (r/'CURRENT_SHA256SUMS.txt').read_text('utf-8').splitlines():
 if line and not line.startswith('#'):
  h,p=line.split('  ',1); sums[p]=h
assert set(sums)==set(paths)
for x in m['files']:
 p=pathlib.PurePosixPath(x['path'])
 assert not p.is_absolute() and '..' not in p.parts and 'FINAL' in p.name
 assert re.fullmatch('[0-9a-f]{64}',x['sha256'])
 b=(r/p).read_bytes()
 assert len(b)==x['size_bytes']>0, str(p)+' size mismatch'
 assert hashlib.sha256(b).hexdigest()==x['sha256']==sums[str(p)], str(p)+' hash mismatch'
 assert not b.startswith(b'version https://git-lfs')
for p in r.rglob('*'):
 if '.git' in p.parts: continue
 assert not re.search(r'school|grade10|защит|письменная|10класс',p.name,re.I),str(p)
for x in paths: assert x in (r/'README.md').read_text('utf-8')
print('PASS: 17/17 FINAL assets, sizes, SHA-256, manifest, catalogue and filenames')
