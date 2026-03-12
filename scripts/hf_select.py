#!/usr/bin/env python3
import json, sys

KEYS = ['llm','language model','vlm','mllm','multimodal','agent','agentic','reasoning','tool','benchmark','inference','deployment']

def score(p):
    text = ((p.get('title') or '') + '\n' + (p.get('summary') or '')).lower()
    s = 0
    for k in KEYS:
        if k in text:
            s += 1
    # industrial preference bumps
    for k in ['agent','tool','inference','deployment','benchmark','reasoning']:
        if k in text:
            s += 2
    return s

payload = json.load(sys.stdin)
papers = payload.get('papers', [])
ranked = sorted(papers, key=score, reverse=True)
json.dump({'date': payload.get('date'), 'papers': ranked[:3]}, sys.stdout, ensure_ascii=False, indent=2)
print()
