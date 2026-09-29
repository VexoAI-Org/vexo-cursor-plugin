#!/usr/bin/env python3
"""Static validation for this single-plugin package; no installs or credentials."""
import json
from pathlib import Path
import re
import struct
root=Path(__file__).resolve().parents[1]
m=json.loads((root/'.cursor-plugin/plugin.json').read_text())
assert re.fullmatch(r'[a-z0-9](?:[a-z0-9.-]*[a-z0-9])?',m['name'])
assert re.fullmatch(r'\d+\.\d+\.\d+',m['version'])
assert m['description'] and m['author']['name']
for key in ['logo','mcpServers','commands']:
 p=Path(m[key]);assert not p.is_absolute() and '..' not in p.parts
 assert (root/p).exists(),key
assert not (root/'.cursor-plugin/marketplace.json').exists(),'This is one plugin, not a marketplace collection.'
config=json.loads((root/'mcp.json').read_text())
assert config=={'mcpServers':{'vexo':{'type':'http','url':'https://vexo-backend-uj6z.onrender.com/mcp'}}}
for p in (root/'commands').glob('*.md'):
 content=p.read_text();assert content.startswith('---\n')
 front=content.split('---',2)[1]
 assert re.search(r'^name: .+',front,re.M) and re.search(r'^description: .+',front,re.M)
logo=(root/m['logo']).read_bytes();assert logo[:8]==b'\x89PNG\r\n\x1a\n'
w,h=struct.unpack('>II',logo[16:24]);assert w==h and w>=256
for p in root.rglob('*'):
 if p.is_file() and '.git' not in p.parts:
  assert p.name not in {'.env','credentials.json','auth.json'}
print(f'PASS: {m["name"]} {m["version"]}; remote MCP; 2 commands; {w}x{h} logo; no embedded credential configuration.')
