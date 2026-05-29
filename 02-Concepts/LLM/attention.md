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
  - transformer
  - attention
---

# Attention

## 一句话解释

Attention 让模型在处理当前位置时，动态选择应该从上下文中的哪些位置读取信息。

## 直觉

序列里的每个 token 不能只看自己。理解一句话、代码或故事时，当前位置常常需要参考前面的词。Attention 提供了一种可学习的读取机制：

- 当前 token 发出 query：我在找什么信息？
- 其他 token 提供 key：我有什么特征可被匹配？
- 其他 token 提供 value：如果被关注，我能贡献什么内容？

query 和 key 的匹配程度决定关注权重，权重再加权 value。

## 基本流程

```text
Q = XWq
K = XWk
V = XWv
scores = QK^T
weights = softmax(scores)
output = weights V
```

在 GPT 里还会加 causal mask，避免当前位置看到未来 token。

## causal mask 为什么重要

自回归模型训练目标是“根据过去预测未来”。如果训练时看到未来 token，loss 会虚假变低，但生成时无法使用这些信息。causal mask 保证第 `t` 个位置只能看 `<= t` 的位置。

## 多头注意力

Multi-head attention 可以理解为并行使用多套 Q/K/V，让不同 head 学不同关系，例如局部邻近、长距离依赖、语法角色或复制模式。

## 易错点

- attention 权重不是天然解释模型“真实原因”，只能作为一种观察信号。
- self-attention 的输入和被读取对象来自同一个序列。
- causal self-attention 是 GPT 的关键，和能看完整输入的 encoder attention 不同。
- attention 计算量通常随序列长度平方增长。

## 在 Karpathy 路线中的位置

[[../../03-Courses/LLM/Karpathy-Zero-to-Hero/05-gpt-from-scratch]] 中，attention 是从 bigram/MLP 语言模型走向 GPT 的核心跃迁。

## 可实践任务

- 手写一个小矩阵例子，计算 softmax attention。
- 打印 attention score、mask 后 score、softmax 权重的 shape。
- 去掉 causal mask，观察训练和生成会发生什么变化。

## 相关笔记

- [[transformer]]
- [[autoregressive-generation]]
- [[embedding]]
