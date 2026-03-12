#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / 'data' / 'index.json'
README = ROOT / 'README.md'

HEADER = '''# Applied AI Paper Notes

面向工程与产品视角的中文论文速记仓库。重点记录：
- LLM / VLM / MLLM / Agent
- 推理、工具调用、评测、训练/部署效率
- 更偏工业应用价值，而不是纯学术新颖度

## 规则

- 每日自动从 Hugging Face Daily Papers 中筛选候选
- 默认最多保留 3 篇
- 按工业应用价值优先排序
- 优先记录 arXiv HTML 链接；没有则记录 arXiv ABS 或其他原始链接
- 支持手动补录（manual ingest）
- README 长期全量保留索引

## HF Daily / 手动收录索引

| 日期 | 标题 | 来源 | 工业价值 | 易读性 |
|---|---|---|---:|---:|
'''

def stars(n:int)->str:
    n=max(1,min(5,int(n)))
    return '★'*n

with INDEX.open('r', encoding='utf-8') as f:
    data = json.load(f)
rows = []
for item in sorted(data.get('papers', []), key=lambda x: (x.get('date',''), x.get('industrial_value',0), x.get('title','')), reverse=True):
    title = (item.get('title') or '').replace('|','\\|')
    path = item.get('note_path','')
    source = item.get('source_name','')
    rows.append(f"| {item.get('date','')} | [{title}]({path}) | {source} | {stars(item.get('industrial_value',3))} | {stars(item.get('readability',3))} |")
README.write_text(HEADER + ('\n'.join(rows) + '\n' if rows else ''), encoding='utf-8')
