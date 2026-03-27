# CarePilot: A Multi-Agent Framework for Long-Horizon Computer Task Automation in Healthcare

- 日期：2026-03-27
- 来源：hf-daily
- 工业价值：★★★★
- 易读性：★★★

## 原始链接

- 规范链接：https://arxiv.org/html/2603.24157
- Hugging Face：https://huggingface.co/papers/2603.24157
- 其他链接：- https://arxiv.org/abs/2603.24157

## 一句话结论

CarePilot 的价值在于把长链 GUI agent 真正推进到医疗软件场景：不仅提出多 agent + 双记忆框架，还补上了一个更贴近真实临床流程的长时程 benchmark。

## 问题 / 背景

现有 computer-use 和 GUI agent 评测大多集中在网页、桌面或手机等通用环境，缺少医疗软件这类高约束、强流程依赖、错误代价高的场景。医疗工作流常常要跨 DICOM viewer、标注工具、EHR/LIS 等系统连续执行十几步，传统视觉 agent 很容易在状态跟踪、面板切换和长程规划上失效。

## 方法 / 实验

论文先构建 CareFlow 基准，覆盖医学影像查看、标注、EHR 与实验室信息系统等四类临床软件任务，每个任务通常有 8 到 24 步。随后提出 CarePilot：Actor 负责结合截图、指令、工具 grounding 和长短期记忆预测下一步语义动作；Critic 负责评估动作、更新记忆并给纠错反馈，形成 actor-critic 式迭代。实验比较多种开源和闭源 VLM baseline，并做失误模式与消融分析。

## 发现 / 结论

结果显示，现有强基线在医疗长流程软件上明显掉队，而 CarePilot 在自建 benchmark 和 OOD 数据上都取得领先，文中给出的提升幅度约为相对强闭源基线 +15.26%、相对强开源基线 +3.38%。更关键的结论是：在高风险行业里，agent 要想可用，记忆、状态校验和领域 benchmark 缺一不可。

## 简评

对做医疗 AI、垂直行业 computer use、企业工作流自动化的人有现实参考价值。它未必能立刻直接落地到生产，但很清楚地指出了通用 GUI agent 进入专业软件后的真实短板。
