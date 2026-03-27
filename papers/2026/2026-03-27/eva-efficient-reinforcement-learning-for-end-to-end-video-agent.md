# EVA: Efficient Reinforcement Learning for End-to-End Video Agent

- 日期：2026-03-27
- 来源：hf-daily
- 工业价值：★★★★★
- 易读性：★★★★

## 原始链接

- 规范链接：https://arxiv.org/html/2603.22918
- Hugging Face：https://huggingface.co/papers/2603.22918
- 其他链接：- https://arxiv.org/abs/2603.22918
- https://github.com/wangruohui/EfficientVideoAgent

## 一句话结论

EVA 的核心价值是把长视频理解从“先喂一堆帧再让模型回答”，改成“先规划再感知”的端到端视频 agent，并用三阶段训练把效果和算力效率一起拉上去。

## 问题 / 背景

长视频理解的主要瓶颈不是模型完全看不懂，而是视频 token 太长、冗余太多，传统均匀采样或被动看完整段视频都很浪费。现有 agent 方法虽然会调工具，但通常流程写死，而且仍然是 perception-first，面对超长视频时既贵又不够准。

## 方法 / 实验

EVA 采用 summary-plan-action-reflection 的循环：先只根据问题决定看什么、什么时候看、以什么分辨率和帧率看，再逐轮缩小关键时间段。训练上用 SFT 冷启动、KTO 学习成功/失败策略偏好、GRPO 做在线强化学习；同时构建 EVA-SFT、EVA-KTO、EVA-RL 三套数据。实验覆盖 6 个视频理解 benchmark，并专门比较长视频场景下的精度与计算效率。

## 发现 / 结论

论文报告 EVA 相比通用 MLLM baseline 提升约 6% 到 12%，比已有 adaptive agent 方案再高 1% 到 3%。更重要的是，它证明视频 agent 真正有用的不是多接一个采样工具，而是让模型先做 query-driven 规划，把视觉预算集中花在关键片段上。

## 简评

对做视频搜索、监控分析、长视频 QA、多模态 agent 的团队很值得看。它给出的不是单点 trick，而是一条更贴近线上成本约束的系统路线：先规划，再按需看视频。
