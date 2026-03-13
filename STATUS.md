# STATUS

## 已完成

- 仓库骨架
- README 全量索引模板
- 单篇笔记模板
- 去重索引：`data/seen.json`
- 全量索引：`data/index.json`
- 手动补录脚本雏形：`scripts/manual_ingest.py`
- README 生成器：`scripts/update_readme.py`
- HF Daily Top 3 选择器雏形：`scripts/hf_select.py`
- 论文阅读子 agent 规范初稿：`prompts/paper-reader.md`

## 已新增

- 6 个论文相关 skills 已安装并完成快速对比
- 对比报告：`reports/skills-comparison-2026-03-13.md`
- 新 skill：`skills/paper-note-pipeline/`
- skill 打包产物：`dist/paper-note-pipeline.skill`
- 已把“先读 arXiv HTML 原文，再写总结；ABS 仅作降级”写入 skill 并实现 `fetch_paper_source.py`

## 待完成

- 将 HF Daily cron 接到仓库写入流程
- 用独立子 agent 实际执行逐篇总结
- 更稳的工业价值排序规则
- manual ingest 正式命令入口
