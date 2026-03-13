# Source Reading Rules

Default rule: **read arXiv HTML first, then write the note**.

## Priority order

1. arXiv HTML full text
2. arXiv ABS page
3. original project / publisher page
4. Hugging Face summary only as fallback

## Mandatory behavior

- Do not write a final note from title + abstract alone when arXiv HTML is available.
- First test whether `https://arxiv.org/html/<id>` is reachable.
- If reachable, extract enough body text to understand:
  - problem setting
  - core method or system design
  - experiment/evaluation evidence
  - limitations or caveats when obvious
- Only fall back to ABS when HTML is unavailable or clearly broken.
- If forced to fall back, state that internally in the workflow and keep `canonical_url` equal to the best available original source.

## What to read from HTML

Prefer these sections when present:
- Abstract
- Introduction
- Method / Approach / Architecture
- Experiments / Evaluation
- Conclusion

Do not try to copy the whole paper into the note. Read enough to support a faithful concise summary.
