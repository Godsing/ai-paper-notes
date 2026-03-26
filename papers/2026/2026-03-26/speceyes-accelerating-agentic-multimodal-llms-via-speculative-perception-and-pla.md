# SpecEyes: Accelerating Agentic Multimodal LLMs via Speculative Perception and Planning

- 日期：2026-03-26
- 来源：hf-daily
- 工业价值：★★★★★
- 易读性：★★★★

## 原始链接

- 规范链接：https://arxiv.org/html/2603.23483
- Hugging Face：https://huggingface.co/papers/2603.23483
- 其他链接：- https://arxiv.org/abs/2603.23483

## 一句话结论

SpecEyes 用“小模型先猜、大模型兜底”的 speculative agent 流程，直接切掉不少不必要的视觉工具链，把 agentic MLLM 的时延和并发瓶颈一起打下来。

## 问题 / 背景

多模态 agent 为了做细粒度视觉推理，通常要反复调用裁剪、放大、OCR 等工具；问题是这些步骤天然串行，单请求时延随 agentic depth 线性增长，并发时几乎吃不到 batching 红利。

## 方法 / 实验

论文把 speculative 思路从 token 级抬到 agent 级：先用轻量、无工具的小型 MLLM 预测回答和执行轨迹，再用基于 answer separability 的认知门控判断这次猜测是否可信；低置信样本才回退到原始大模型工具链。系统层面又做了异构并行，让小模型并发跑、把大模型串行开销尽量藏到后面。实验覆盖 V* Bench、HR-Bench、POPE，并分析了门控校准与消融。

## 发现 / 结论

在三套 benchmark 上，SpecEyes 相比原始 agent baseline 实现 1.1 到 3.35 倍加速，同时精度持平甚至最高提升 6.7%。论文最有价值的点不是某个门控分数，而是说明：很多视觉 agent 查询根本不需要完整工具链，可以先做便宜的 speculative triage。

## 简评

非常值得做多模态 agent serving 的团队看。它对应的是线上真实痛点：工具调用链太深、吞吐上不去、单位请求成本太高。相比纯 token/speculative decoding，这篇更贴近 agent 系统级优化。
