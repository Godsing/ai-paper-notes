# Output Schema

For each selected paper, produce a compact structured object with these fields:

- `paper_id`
- `title`
- `date`
- `source_name`
- `canonical_url`
- `hf_url`
- `other_urls`
- `one_sentence_takeaway`
- `problem_background`
- `method_experiment`
- `findings_conclusion`
- `industrial_value`
- `readability`
- `comment`
- `paper_type`
- `relevant`

Notes:
- Prefer arXiv HTML as `canonical_url` when reachable.
- Fall back to arXiv ABS, then other primary source links.
- Keep all Chinese text concise and easy to scan.
- `comment` should explain why the paper is worth attention from an engineering/product viewpoint.
