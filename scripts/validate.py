#!/usr/bin/env python3
"""Static validation for this single-plugin package; no installs or credentials."""
import json
from pathlib import Path
import re
import xml.etree.ElementTree as ET
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
commands=list((root/'commands').glob('*.md'))
assert {p.stem for p in commands}=={'vexo-context','vexo-brief','vexo-execute'}
for p in commands:
 content=p.read_text();assert content.startswith('---\n')
 front=content.split('---',2)[1]
 assert re.search(r'^name: .+',front,re.M) and re.search(r'^description: .+',front,re.M)
logo=ET.parse(root/m['logo']).getroot()
assert logo.tag=='{http://www.w3.org/2000/svg}svg'
w,h=(float(logo.attrib[key]) for key in ('width','height'))
assert w==h and w>=256
viewbox=[float(value) for value in logo.attrib['viewBox'].split()]
assert len(viewbox)==4 and viewbox[2]==viewbox[3] and viewbox[2]>0
for p in root.rglob('*'):
 if p.is_file() and '.git' not in p.parts:
  assert p.name not in {'.env','credentials.json','auth.json'}
print(f'PASS: {m["name"]} {m["version"]}; remote MCP; {len(commands)} commands; {w:g}x{h:g} logo; no embedded credential configuration.')
