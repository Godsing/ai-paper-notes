# XSkill: Continual Learning from Experience and Skills in Multimodal Agents

- 日期：2026-03-14
- 来源：hf-daily
- 工业价值：★★★★★
- 易读性：★★★★

## 原始链接

- 规范链接：https://arxiv.org/html/2603.12056
- Hugging Face：https://huggingface.co/papers/2603.12056
- 其他链接：- https://arxiv.org/abs/2603.12056

## 一句话结论

XSkill 把“经验”和“技能”拆成两条可检索知识流，让多模态 agent 在不改参数的前提下持续提升工具使用效率与任务规划能力。

## 问题 / 背景

现有多模态 agent 常见两个痛点：一是工具调用低效，简单任务走太多步、复杂任务又探索不够；二是工具编排不灵活，面对新任务时很难把已有操作模式迁移过去。作者要解决的是：能否让冻结模型像人一样，从过去轨迹中持续积累可复用知识。

## 方法 / 实验

论文将知识拆为任务级 skill 和动作级 experience：前者描述可复用工作流，后者记录具体情境下的决策经验。训练阶段从多路径 rollout 中做视觉条件下的总结、跨轨迹互评和层级去重；推理阶段先做任务分解，再按当前视觉上下文检索并改写相关 skill/experience，注入 prompt 使用。实验覆盖 5 个多模态 benchmark、4 个 backbone，与 tool-only 和 learning-based baseline 对比。

## 发现 / 结论

XSkill 在不同模型和任务上都稳定优于基线，相比纯工具调用方案的 Average@4 提升约 2.58 到 6.71 分，在更难设置下相对最强基线最高提升 11.13 分。作者还发现 skill 更偏高层规划，experience 更偏局部决策与纠错，两者确实互补。

## 简评

这篇最值得工程团队看，因为它不是再训一个更大模型，而是讨论如何给 agent 建“外部可积累经验库”。对做 GUI agent、视觉工具链、复杂 workflow 编排的团队都很有现实参考价值。
