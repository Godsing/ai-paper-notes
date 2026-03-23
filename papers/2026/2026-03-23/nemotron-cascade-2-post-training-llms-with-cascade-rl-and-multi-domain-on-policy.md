# Nemotron-Cascade 2: Post-Training LLMs with Cascade RL and Multi-Domain On-Policy Distillation

- 日期：2026-03-23
- 来源：hf-daily
- 工业价值：★★★★★
- 易读性：★★★

## 原始链接

- 规范链接：https://arxiv.org/abs/2603.19220
- Hugging Face：https://huggingface.co/papers/2603.19220
- 其他链接：-

## 一句话结论

Nemotron-Cascade 2 的重点不是又一个大模型发布，而是给出一套更像工程流水线的后训练 recipe：把 Cascade RL 扩到多领域，再用按领域选最强中间 teacher 的 on-policy distillation 稳住收益。

## 问题 / 背景

后训练里常见的问题是：RL 能带来推理和 agent 能力提升，但训练过程容易出现 benchmark 回退、不同能力域此消彼长，而且高性能模型往往依赖很大的参数规模，不利于实际部署。

## 方法 / 实验

作者发布一个 30B MoE、激活 3B 参数的开放模型。流程上先做精细 SFT，再把 Cascade RL 扩展到更广的推理与 agent 场景；训练过程中，对数学、代码等不同领域分别选取表现最强的中间 teacher，持续做 multi-domain on-policy distillation，用来回收退化并维持增益。论文同时公开模型 checkpoint 与训练数据。

## 发现 / 结论

按论文给出的结果，这个配方让模型以相对小得多的激活参数，逼近前沿开放模型的数学与代码推理水平，并强调其 agent 能力也较强。作者想证明的是：高密度能力不只靠更大 base model，也可以靠更系统的后训练编排拿到。

## 简评

这篇对做开源推理模型、RL 后训练和 agent 模型迭代的团队最有现实价值，因为它讨论的是可复用训练策略，不只是榜单成绩。需要注意的是，本次总结只能基于 arXiv ABS 页面，因为 HTML 原文不可用，细节可信度不如全文阅读场景。
