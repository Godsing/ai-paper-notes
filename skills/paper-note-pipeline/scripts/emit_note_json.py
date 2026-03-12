#!/usr/bin/env python3
"""Normalize a paper-note object from stdin and print compact JSON.
Use as a lightweight final formatting helper in batch workflows.
"""
import json, sys

obj = json.load(sys.stdin)
keys = [
    'paper_id','title','date','source_name','canonical_url','hf_url','other_urls',
    'one_sentence_takeaway','problem_background','method_experiment','findings_conclusion',
    'industrial_value','readability','comment','paper_type','relevant'
]
out = {k: obj.get(k) for k in keys if k in obj}
json.dump(out, sys.stdout, ensure_ascii=False, indent=2)
print()
