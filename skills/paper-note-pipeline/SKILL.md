---
name: paper-note-pipeline
description: "Chinese-first paper reading, triage, note-writing, and repository archiving workflow for AI research papers. Use when handling Hugging Face Daily Papers, arXiv links, PDF papers, or manual paper-ingest tasks that require: (1) relevance filtering, (2) industrial-value-first ranking, (3) concise Chinese notes, (4) canonical link selection with arXiv HTML preferred, (5) markdown note generation, (6) index and README updates, or (7) daily Top-N paper digests for a repository."
---

# Paper Note Pipeline

Use this skill to turn paper inputs into concise Chinese repository notes.

## Core outcome

Produce a stable pipeline with five outputs:
1. choose papers worth keeping
2. summarize each paper in Chinese
3. score industrial value and readability
4. archive notes into the repository
5. update index files and README

Read these references when needed:
- `references/scoring-rubric.md` for rating rules
- `references/output-schema.md` for note fields

## Workflow

### Step 1: Normalize the input source

Support these entry types:
- Hugging Face Daily Papers result list
- arXiv ID / arXiv URL
- PDF attachment or PDF URL
- manual user-provided paper link

Prefer structured upstream data when available. For batch inputs, convert them into a compact JSON list before summarization.

### Step 2: Filter and rank

Filter out weakly related papers. Keep only papers clearly relevant to one or more of:
- LLM
- VLM / MLLM
- agent / tool use
- reasoning
- evaluation / benchmark
- training efficiency / inference efficiency / deployment

Rank by **industrial value first**, not academic novelty. In batch daily mode, keep only the requested top N (default 3).

### Step 3: Determine paper type before writing

Classify each paper into a practical type before summarization:
- `method`
- `system`
- `benchmark`
- `dataset`
- `survey`
- `analysis`
- `application`

Do not use the same emphasis for every type:
- `method`: focus on problem, mechanism, evidence, where it helps in practice
- `benchmark` / `dataset`: focus on what capability is measured or unlocked
- `system`: focus on architecture, tradeoffs, deployment implications
- `survey`: focus on synthesis value, not section-by-section compression

### Step 4: Select the canonical source link

Choose source links in this order:
1. arXiv HTML
2. arXiv ABS
3. other original paper/project link

Record the best available link as `canonical_url`. Keep alternate links in `other_urls`.

### Step 5: Write the note in repository mode

Repository mode is the default. Write concise Chinese notes with these sections:
- 一句话结论
- 问题 / 背景
- 方法 / 实验
- 发现 / 结论
- 简评

Requirements:
- Lead with the conclusion.
- Keep only the highest-value details.
- Avoid bloated literature-review tone.
- Write for engineering/product readers, not only researchers.
- Do not copy abstract wording unless necessary.

When the paper is shallow, weakly evidenced, or only marginally relevant, either drop it or write a short note that explicitly says why it is not a priority.

### Step 6: Score consistently

Always score:
- industrial value
- readability

Use `references/scoring-rubric.md`.

### Step 7: Persist outputs

When operating inside the `ai-paper-notes` repository:
- write note markdown under `papers/YYYY/YYYY-MM-DD/`
- upsert metadata into `data/index.json`
- upsert dedupe keys into `data/seen.json`
- regenerate `README.md`

Use existing repository scripts when present instead of rewriting the same logic.

## Modes

### Mode A: Daily digest mode

Use for HF Daily / daily paper feeds.

Rules:
- filter hard
- sort by industrial value first
- keep only top 3 unless instructed otherwise
- summarize each selected paper concisely
- produce a short chat digest after archive update

### Mode B: Manual ingest mode

Use when the user sends one paper link and wants it archived.

Rules:
- do not force Top 3 filtering
- still classify type, choose canonical link, score, and archive
- if the paper already exists, update metadata instead of duplicating it

### Mode C: Deep-read mode

Use only when the user explicitly wants a more detailed read.

Rules:
- keep the same schema
- allow longer `method_experiment` and `comment`
- preserve repository style; do not switch into a full academic review unless asked

## Decision rules borrowed from other skills

Adopt these good patterns:
- From deep-reading skills: read enough before writing; do not summarize from title alone.
- From SOP-based skills: classify paper type before choosing emphasis.
- From orchestrator skills: separate collection, per-paper reading, and final archiving.
- From digest skills: prefer structured batch JSON between pipeline stages.
- From lightweight search skills: keep a simple manual ingest path for one-off papers.

## Anti-patterns

Do not:
- dump giant academic critiques into repository notes by default
- rank purely by novelty or benchmark SOTA hype
- keep duplicate notes for the same paper
- bury the conclusion under long background sections
- hardcode environment-specific absolute paths when repo-relative paths work

## Repository integration

Typical files already used by this workflow:
- `scripts/hf_select.py`
- `scripts/manual_ingest.py`
- `scripts/note_lib.py`
- `scripts/update_readme.py`

Prefer patching and reusing these scripts over replacing them wholesale.
