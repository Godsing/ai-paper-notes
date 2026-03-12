# Thinking to Recall: How Reasoning Unlocks Parametric Knowledge in LLMs

- 日期：2026-03-11
- 来源：hf-daily
- 工业价值：★★★★
- 易读性：★★★★

## 原始链接

- 规范链接：https://arxiv.org/html/2603.09906
- Hugging Face：https://huggingface.co/papers/2603.09906
- 其他链接：- https://arxiv.org/abs/2603.09906

## 一句话结论

论文说明：即便是单跳事实问答，显式 reasoning 也可能帮助 LLM 更好地从参数知识中把正确答案‘想出来’，但同时会放大中间幻觉带来的风险。

## 问题 / 背景

作者关注一个反直觉问题：简单事实问答明明不需要复杂推理，为什么开启 reasoning 后模型反而更容易答对？这关系到我们怎么理解 LLM 的知识召回机制。

## 方法 / 实验

论文围绕受控实验拆解了 reasoning 的作用，重点分析两类机制：一类是 reasoning token 作为额外计算缓冲区；另一类是先生成相关事实，再把答案‘引出来’。同时作者比较了不同 reasoning 轨迹与最终正确率/幻觉率之间的关系。

## 发现 / 结论

核心发现是 reasoning 不只是解释答案，还会真实改变知识召回边界；但如果中间事实是错的，也会提高最终答错的概率。对实际系统来说，更好的做法不是盲目放大长推理，而是偏向选择中间事实更干净的 reasoning 轨迹。

## 简评

对做检索增强、长推理和 self-reflection 的团队有参考价值。它提醒我们：reasoning 既可能增益知识召回，也可能成为幻觉放大器。
