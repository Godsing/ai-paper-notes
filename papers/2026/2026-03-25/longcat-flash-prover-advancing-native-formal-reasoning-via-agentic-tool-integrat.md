# LongCat-Flash-Prover: Advancing Native Formal Reasoning via Agentic Tool-Integrated Reinforcement Learning

- 日期：2026-03-25
- 来源：hf-daily
- 工业价值：★★★★
- 易读性：★★★

## 原始链接

- 规范链接：https://arxiv.org/html/2603.21065
- Hugging Face：https://huggingface.co/papers/2603.21065
- 其他链接：- https://arxiv.org/abs/2603.21065

## 一句话结论

LongCat-Flash-Prover 的核心价值是把 Lean4 形式化推理拆成自动形式化、草图生成和证明三种原生能力，再用工具集成 RL 去做长链可验证训练，证明开源模型也能把 formal reasoning 推到更实用的水平。

## 问题 / 背景

现有 LLM 在自然语言推理上进步很快，但一进到 Lean4 这类形式化证明环境，就会遇到长链决策、编译反馈、语义一致性和 reward hacking 等一整套新问题。传统工具调用套路并不足以直接解决这类严格验证任务。

## 方法 / 实验

论文提出 Hybrid-Experts Iteration Framework，分别训练 auto-formalization、sketching 和 proving 专家，通过 Lean4 编译与验证反馈合成高质量轨迹，再做迭代优化。RL 阶段引入 HisPO，用分层 importance sampling 和梯度屏蔽缓解 MoE 长链训练中的策略陈旧与训练-推理引擎不一致问题；同时加入 theorem consistency 与 legality detection，抑制形式化场景常见的 reward hacking。实验覆盖 auto-formalization、theorem proving 和一般推理任务。

## 发现 / 结论

结果显示它在开放权重 formal reasoning 上做到很强：MiniF2F-Test 用 72 次尝试可达 97.1%，ProverBench 达 70.8%，PutnamBench 达 41.5%，并宣称明显优于现有开源基线。更值得注意的是，作者强调样本效率和工具反馈闭环，而不只是靠更大搜索预算硬堆结果。

## 简评

这篇更偏前沿研究，但对做可验证代码生成、证明助手、数学推理和高可靠 agent 的团队仍有参考价值。短期内它未必直接转成通用产品能力，但它说明：一旦任务具备可验证环境，agentic RL 加工具反馈确实能比纯语言监督更有效。
