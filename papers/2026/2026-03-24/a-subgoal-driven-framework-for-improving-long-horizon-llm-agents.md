# A Subgoal-driven Framework for Improving Long-Horizon LLM Agents

- 日期：2026-03-24
- 来源：hf-daily
- 工业价值：★★★★★
- 易读性：★★★★

## 原始链接

- 规范链接：https://arxiv.org/html/2603.19685
- Hugging Face：https://huggingface.co/papers/2603.19685
- 其他链接：- https://arxiv.org/abs/2603.19685

## 一句话结论

这篇最值得关注的点是：作者把“子目标”同时用于推理时规划和 RL 训练时奖励塑形，显著提升了长链网页 Agent 的稳定性，开放模型 Gemma3-12B 在 WebArena-Lite 上可从 6.4% 拉到 43.0%。

## 问题 / 背景

长链网页操作的核心难点不是单步点击，而是过程中持续保持目标感。现有 LLM Agent 常在中途卡住、绕圈，RL 微调又因为奖励稀疏，很难学到哪些中间步骤真正推动任务完成。

## 方法 / 实验

论文先分析失败轨迹，发现“mid-task stuck”是主要瓶颈。方法上分两层：一是在推理阶段先把任务拆成可执行子目标，并结合回顾式反思动态修正；二是在训练阶段提出 MiRA，用里程碑式子目标完成度做 dense reward shaping，并配合 goal-conditioned value critic 做策略优化。实验主要在 WebArena-Lite 上评测，既看闭源模型接入在线规划后的收益，也看 Gemma3-12B 经 MiRA 后的提升。

## 发现 / 结论

结果很硬：在线子目标规划可让 Gemini 类模型拿到约 10 个点的绝对成功率提升；MiRA 则把 Gemma3-12B 从 6.4% 提升到 43.0%，超过文中列出的 GPT-4-Turbo、GPT-4o 和此前 open SOTA WebRL。论文传达的信息很明确：长链 Agent 的关键不只是更强底座，而是把“阶段性可验证进展”显式建进推理与训练闭环里。

## 简评

对做 Browser Agent、Computer Use、GUI 自动化和 agent RL 的团队很有现实价值。它给出的不是单点技巧，而是一套可落地的工程方向：把任务拆解、进度判断和奖励塑形统一起来，优先解决中途失焦的问题。
