---
type: concept
topic: LLM
status: usable
created: 2026-05-28
updated: 2026-05-29
source:
  - Karpathy Zero to Hero
tags:
  - LLM
  - generation
  - language-modeling
---

# Autoregressive Generation

## 一句话解释

自回归生成是让模型根据已有 token 预测下一个 token，再把预测结果接回上下文继续生成。

## 基本循环

```text
context -> model -> next_token_distribution
sample next_token
context = context + next_token
repeat
```

训练时模型学习“下一个 token 是什么”；生成时模型反复使用这个能力。

## 和训练目标的关系

GPT 类模型通常训练为：

```text
input:  [t0, t1, t2, t3]
target: [t1, t2, t3, t4]
```

模型在每个位置都预测下一个 token。这个目标让模型学会从历史上下文中估计下一个 token 的概率分布。

## 采样方式

模型输出通常是 logits，需要转换成概率分布后选择下一个 token。

- greedy：每次选概率最高的 token，稳定但容易重复。
- sampling：按概率随机采样，更有变化。
- temperature：控制分布尖锐程度。
- top-k/top-p：限制候选 token，提高生成质量。

## causal mask 的意义

自回归模型不能在预测当前位置时偷看未来 token。[[attention]] 中的 causal mask 保证第 `t` 个位置只能使用过去和当前位置的信息。

## 易错点

- 训练时可以并行预测很多位置；生成时通常要一步步追加 token。
- 低 loss 不一定意味着生成文本好，还要看采样策略和数据质量。
- 上下文窗口有限，太早的信息可能无法直接进入模型。
- 字符级生成和现代子词级生成原理相同，但粒度不同。

## 在 Karpathy 路线中的位置

[[../../03-Courses/LLM/Karpathy-Zero-to-Hero/02-makemore]] 用字符级模型展示“根据前文预测下一个字符”；[[../../03-Courses/LLM/Karpathy-Zero-to-Hero/05-gpt-from-scratch]] 把同一思想扩展到 Transformer。

## 可实践任务

- 写一个 bigram 字符生成器。
- 比较 greedy 和随机采样的输出差异。
- 在 tiny GPT 里改变 temperature，记录样本质量变化。

## 相关笔记

- [[tokenization]]
- [[attention]]
- [[transformer]]
- [[sampling-params-and-cost]]：本节「采样方式」的展开——temperature/top-k/top-p 的直觉、DeepSeek 温度表与 token 成本。
