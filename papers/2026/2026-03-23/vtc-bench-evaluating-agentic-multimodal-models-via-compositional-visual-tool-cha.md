# VTC-Bench: Evaluating Agentic Multimodal Models via Compositional Visual Tool Chaining

- 日期：2026-03-23
- 来源：hf-daily
- 工业价值：★★★★
- 易读性：★★★★

## 原始链接

- 规范链接：https://arxiv.org/html/2603.15030
- Hugging Face：https://huggingface.co/papers/2603.15030
- 其他链接：- https://arxiv.org/abs/2603.15030

## 一句话结论

VTC-Bench 用 32 个视觉工具、680 道多步任务把多模态 agent 的真实短板暴露得很清楚：现阶段模型会调工具，但还远不会稳定地做复杂视觉工具链规划。

## 问题 / 背景

现有多模态工具调用 benchmark 的工具集偏少、轨迹偏短，难以反映真实视觉工作流里常见的多工具组合、长链路依赖和执行规划问题，所以很容易高估模型的视觉 agent 能力。

## 方法 / 实验

作者构建了 VTC-Bench：基于 32 个 OpenCV 风格视觉操作，设计 680 个任务，覆盖九类认知层级，并给出 ground-truth tool trajectory。实验评测了 19 个主流 MLLM，同时分析模型在陌生工具、组合调用和长链执行下的表现。

## 发现 / 结论

结果并不乐观：最强模型 Gemini-3.0-Pro 也只有约 51% 表现。模型普遍难以适应多样工具集，对未见操作泛化差；遇到复杂任务时，经常反复依赖少数熟悉函数，而不是为当前问题选择最优工具链。闭源模型加工具后收益更明显，开源模型有时甚至退化。

## 简评

对做视觉 agent、GUI/屏幕理解、图像处理工作流的人很值得看。它的价值不在于提出新模型，而在于告诉你：如果要把多模态 agent 真正推向生产，评测必须从“会不会调一个工具”升级到“能不能稳定编排整条工具链”。
