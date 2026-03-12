from __future__ import annotations
import json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX_PATH = ROOT / 'data' / 'index.json'
SEEN_PATH = ROOT / 'data' / 'seen.json'
TEMPLATE_PATH = ROOT / 'templates' / 'paper-note.md.tmpl'


def slugify(text:str)->str:
    text = text.lower().strip()
    text = re.sub(r'[^a-z0-9\u4e00-\u9fff]+', '-', text)
    text = re.sub(r'-+', '-', text).strip('-')
    return text[:80] or 'paper'


def stars(n:int)->str:
    n=max(1,min(5,int(n)))
    return '★'*n


def load_json(path:Path, default):
    if not path.exists():
        return default
    with path.open('r', encoding='utf-8') as f:
        return json.load(f)


def save_json(path:Path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write('\n')


def render_note(entry:dict)->str:
    tpl = TEMPLATE_PATH.read_text(encoding='utf-8')
    mapping = {
        'title': entry['title'],
        'date': entry['date'],
        'source_name': entry['source_name'],
        'industrial_value_stars': stars(entry['industrial_value']),
        'readability_stars': stars(entry['readability']),
        'canonical_url': entry['canonical_url'],
        'hf_url': entry.get('hf_url','-') or '-',
        'other_urls': '\n'.join(f'- {u}' for u in entry.get('other_urls',[]) if u) or '-',
        'one_sentence_takeaway': entry['one_sentence_takeaway'],
        'problem_background': entry['problem_background'],
        'method_experiment': entry['method_experiment'],
        'findings_conclusion': entry['findings_conclusion'],
        'comment': entry['comment'],
    }
    for k,v in mapping.items():
        tpl = tpl.replace('{{'+k+'}}', str(v))
    return tpl


def upsert_entry(entry:dict)->dict:
    index = load_json(INDEX_PATH, {'papers': []})
    seen = load_json(SEEN_PATH, {'papers': {}})
    key = entry.get('paper_id') or entry.get('canonical_url') or entry['title']
    slug = slugify(entry['title'])
    year = entry['date'][:4]
    note_rel = f"papers/{year}/{entry['date']}/{slug}.md"
    note_path = ROOT / note_rel
    note_path.parent.mkdir(parents=True, exist_ok=True)
    note_path.write_text(render_note(entry), encoding='utf-8')
    entry['note_path'] = note_rel
    seen['papers'][key] = {
        'title': entry['title'],
        'date': entry['date'],
        'note_path': note_rel,
        'canonical_url': entry['canonical_url'],
        'source_name': entry['source_name'],
    }
    replaced = False
    for i, old in enumerate(index['papers']):
        old_key = old.get('paper_id') or old.get('canonical_url') or old.get('title')
        if old_key == key:
            index['papers'][i] = entry
            replaced = True
            break
    if not replaced:
        index['papers'].append(entry)
    save_json(INDEX_PATH, index)
    save_json(SEEN_PATH, seen)
    return entry
