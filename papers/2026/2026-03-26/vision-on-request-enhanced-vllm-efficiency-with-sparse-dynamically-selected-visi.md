# VISion On Request: Enhanced VLLM efficiency with sparse, dynamically selected, vision-language interactions

- 日期：2026-03-26
- 来源：hf-daily
- 工业价值：★★★★★
- 易读性：★★★★

## 原始链接

- 规范链接：https://arxiv.org/html/2603.23495
- Hugging Face：https://huggingface.co/papers/2603.23495
- 其他链接：- https://arxiv.org/abs/2603.23495

## 一句话结论

VISOR 不再靠“删视觉 token”省算力，而是改成“少数关键层再看全量视觉信息”，因此在保住高分辨率细节的同时显著降低 LVLM 推理成本。

## 问题 / 背景

现有高效 LVLM 大多通过 pruning / merging / compression 减少视觉 token，但这会形成信息瓶颈；一旦任务需要细粒度理解、文档阅读或高分辨率视觉推理，性能就容易明显掉。

## 方法 / 实验

VISOR 把开销重点从“多少 token 被保留”转到“多少层真的需要做重视觉交互”。做法是：大部分层只保留便宜的 text-image cross-attention 提供通用视觉上下文；只有少数经过策略选择的层才执行会更新视觉表征的 self-attention。作者还训练了一个覆盖多种计算预算的统一模型，并用轻量策略网络按样本动态分配需要开启的 self-attention 层数；同时验证它能与 token reduction 方法叠加。

## 发现 / 结论

实验表明，VISOR 在多项视觉语言 benchmark 上以更低 FLOPs 达到或超过现有高效方法，尤其在需要细节理解的“hard”任务上优势更明显。核心结论是：比起永久丢掉视觉信息，更有效的路线可能是按需打开高成本视觉-语言交互。

## 简评

这篇对做 VLM 推理优化、边缘部署、文档/屏幕理解的人很有参考价值。它提供了一个比 token 压缩更稳的效率方向，而且和现有压缩路线是可组合的。
