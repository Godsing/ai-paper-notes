# ToolRosetta: Bridging Open-Source Repositories and Large Language Model Agents through Automated Tool Standardization

- 日期：2026-03-25
- 来源：hf-daily
- 工业价值：★★★★★
- 易读性：★★★★

## 原始链接

- 规范链接：https://arxiv.org/html/2603.09290
- Hugging Face：https://huggingface.co/papers/2603.09290
- 其他链接：- https://arxiv.org/abs/2603.09290

## 一句话结论

ToolRosetta 最值得看的点是：它试图把“仓库代码 → 可被 Agent 直接调用的 MCP 工具”自动化，若工程质量成立，会显著降低工具接入和复现实验的人力成本。

## 问题 / 背景

现在很多高价值工具都埋在异构开源仓库里，接口、依赖和运行方式都不统一，导致 LLM agent 虽然会调工具框架，却很难大规模稳定复用真实世界代码。作者要解决的是：能否把代码仓库自动标准化成可执行、可编排的 MCP 工具，而不是继续靠人工逐个封装。

## 方法 / 实验

ToolRosetta 采用分层多 agent 流程：Planning agent 负责整体编排，Tool-search agent 找候选仓库，MCP-construction agent 做仓库克隆、语义分析、环境配置和 MCP 服务生成，另加 Security agent 做隐私泄露与安全风险检查。论文称其可自动把 1580 个开源工具转成标准化可执行接口，并在多个科学领域任务上比较任务完成效果。

## 发现 / 结论

论文报告 ToolRosetta 相比商业 LLM 和既有 scientific agent baseline 有明显任务完成率提升，六个科学领域的宏平均准确率相对最强基线提升超过 31%。更重要的结论是：如果工具标准化本身能被自动化，Agent 的能力上限就不再只受限于人工维护的小型工具库。

## 简评

对做 MCP、Agent 平台、企业内部工具封装和代码资产复用的团队很值得看。它击中的不是单个 benchmark，而是一个真实工程瓶颈：工具很多，但可调用的工具太少。需要保留一点审慎：这类系统真正落地时，环境隔离、依赖治理和安全审计往往比论文结果更难。
