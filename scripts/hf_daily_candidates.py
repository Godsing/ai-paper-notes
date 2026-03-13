#!/usr/bin/env python3
from __future__ import annotations
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKSPACE = ROOT.parent
FETCH = WORKSPACE / 'scripts' / 'hf_daily_papers.py'
SELECT = ROOT / 'scripts' / 'hf_select.py'

raw = subprocess.check_output(['python3', str(FETCH)], text=True)
selected = subprocess.check_output(['python3', str(SELECT)], input=raw, text=True)
print(selected, end='')
