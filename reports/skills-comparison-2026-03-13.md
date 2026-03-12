# 论文相关 Skills 对比报告（2026-03-13）

本报告对 6 个已安装 skill 做快速对比，目标不是评测“最学术”，而是判断谁最适合当前仓库需求：
- 每天抓 HF Daily / 未来可扩展到手动补录
- 中文总结
- 重点清楚、少废话
- 优先工业价值排序
- 能稳定写入仓库并维护 README 索引

## 对比结论

结论先说：**没有一个现成 skill 能直接完整满足需求**。最合适的做法是：
- 吸收 `paper-parse` 的深读能力
- 吸收 `paper-summarize-academic` 的“按论文类型切 SOP”思路
- 吸收 `arxiv-summarizer-orchestrator` 的流水线编排思路
- 吸收 `agentic-paper-digest-skill` 的多源抓取与 JSON 化输出思路
- 吸收 `daily-paper-digest` 的定时抓取视角
- 保留 `arxiv` 作为轻量检索/补链路入口

然后在仓库内做一个新的、面向 **AI paper notes** 场景的定制 skill。

## 简表

| Skill | 强项 | 弱项 | 适配度 |
|---|---|---|---|
| `paper-parse` | 深读强、中文友好、适合逐篇拆解 | 输出太重，默认双报告，不适合日报/仓库速记 | 高 |
| `paper-summarize-academic` | 论文类型分类 + SOP 思路好 | 过于学术评审化，篇幅重，前置字段要求多 | 中高 |
| `arxiv-summarizer-orchestrator` | 批处理/编排强，适合多阶段流水线 | 依赖子技能多，体系重，落地成本高 | 中高 |
| `arxiv` | 轻量检索、获取 arXiv 信息方便 | 更像研究助手，不像仓库写手 | 中 |
| `agentic-paper-digest-skill` | 多源抓取、JSON、适合下游处理 | 强依赖外部 repo / API key / 环境配置 | 中 |
| `daily-paper-digest` | 每日速递思路直接，HF+arXiv 聚合明确 | 更像爬虫播报，缺少高质量总结与归档规范 | 中 |

## 逐个点评

### 1. paper-parse
**优点**
- 明确围绕“读论文”设计，不是泛文档总结。
- 中文表达友好。
- 强调通读全文、关注图表、整理 temp_analysis，再输出正式报告。
- 对“先吃透再写”这件事要求最严格。

**缺点**
- 默认要求一次输出 Part A / Part B 两套报告，过重。
- 更适合单篇深读，不适合每天 Top 3 的仓库场景。
- 模板路径硬编码痕迹较重，可迁移性一般。

**可提取精华**
- 先完整读，再写，不要直接拿摘要改写。
- 单独保留分析中间态。
- 摘要不能只是翻译，要揭示论文内部逻辑。

### 2. paper-summarize-academic
**优点**
- 最大亮点是 **topic classification -> SOP selection**。
- 区分 method / dataset / benchmark / multimodal / survey 等类型，这对提升总结质量很有帮助。
- 结构化程度高，利于后续统一处理。

**缺点**
- 明显更偏 reviewer / academic critique。
- 输出要求很长，和“中文、精炼、仓库笔记”不一致。
- YAML frontmatter 不够规范，工程质量一般。

**可提取精华**
- 先判论文类型，再决定怎么总结。
- benchmark / dataset / method / system report 不应套同一模板。

### 3. arxiv-summarizer-orchestrator
**优点**
- 编排最强，明确拆成 collection / processing / reporting 三阶段。
- 适合批量处理、多篇论文、定时运行。
- 对并行上限、语言参数、输出布局都写得较清楚。

**缺点**
- 体系太重，依赖 3 个子 skill。
- 适合“研究报告工厂”，不适合现在这种轻量、稳定、可持续归档的仓库。
- 过度围绕 arXiv 目录结构，不够通用。

**可提取精华**
- 采集、逐篇处理、最终汇总三段式拆分。
- 批处理时不要让单个 worker 跨文件乱写，避免冲突。
- 用统一语言参数约束最终输出。

### 4. arxiv
**优点**
- 最轻量，适合查 paper、补 PDF、拿基本信息。
- 没有复杂环境前置。
- 可以作为 manual ingest 的补入口。

**缺点**
- 更像检索助手，不是总结流水线。
- 没有仓库归档、评分、索引更新这些能力。

**可提取精华**
- 把检索/补链接能力单独看作一个轻量入口，而不是让重型技能接管全部流程。

### 5. agentic-paper-digest-skill
**优点**
- 明确支持 arXiv + Hugging Face。
- 有 JSON 输出，适合下游 agent/脚本消费。
- 配置项详细，适合做长期系统。

**缺点**
- 明显依赖外部 repo、API key、配置文件和运行环境。
- 更偏“搭一个 digest 系统”，不是“仓库内写中文重点笔记”。
- 与你当前要的低摩擦仓库流不完全匹配。

**可提取精华**
- 上游抓取结果尽量 JSON 化，给下游总结和归档解耦。
- 多源聚合要保留配置层。

### 6. daily-paper-digest
**优点**
- 最接近“每日论文速递”产品心智。
- HF + arXiv 聚合明确。
- cron 场景天然契合。

**缺点**
- 更像“抓取 + 播报”，不是“筛选 + 深读 + 归档”。
- 缺少工业价值排序、中文速记模板、去重与仓库索引机制。
- 工程成熟度一般。

**可提取精华**
- 每日任务要有很清晰的入口和固定输出。
- 定时拉取与消息触发都应该能工作。

## 最终决策

新 skill 的设计决策如下：

1. **保留三段式流程**：采集 / 逐篇研读 / 归档发布。
2. **逐篇研读采用轻重分层**：
   - 默认是“仓库速记模式”
   - 需要时可升级为“深读模式”
3. **先做论文类型判断**：至少区分 method / benchmark / dataset / system / survey。
4. **输出统一为中文、结论优先、工程/产品导向**。
5. **固定评估两项分数**：工业价值、易读性。
6. **优先记录原始最佳链接**：arXiv HTML > arXiv ABS > 其他原始链接。
7. **上游抓取结果尽量 JSON 化**，避免后面流程和页面结构绑定太死。
8. **归档逻辑内置**：写 markdown、更新 index、更新 README、做去重。

## 结论摘要

- **最像“读论文”的**：`paper-parse`
- **最值得借鉴结构化思路的**：`paper-summarize-academic`
- **最值得借鉴流水线设计的**：`arxiv-summarizer-orchestrator`
- **最适合作为轻量补入口的**：`arxiv`
- **最值得借鉴多源/JSON 思路的**：`agentic-paper-digest-skill`
- **最贴近日报心智的**：`daily-paper-digest`

因此，新 skill 不做“谁的翻版”，而是做一个**面向仓库归档与每日速记的定制编排 skill**。
