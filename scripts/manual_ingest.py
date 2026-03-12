#!/usr/bin/env python3
import argparse, json
from note_lib import upsert_entry

ap = argparse.ArgumentParser()
ap.add_argument('--json-file', required=True)
args = ap.parse_args()
with open(args.json_file, 'r', encoding='utf-8') as f:
    entry = json.load(f)
upsert_entry(entry)
print(json.dumps({'ok': True, 'note_path': entry.get('note_path')}, ensure_ascii=False))
