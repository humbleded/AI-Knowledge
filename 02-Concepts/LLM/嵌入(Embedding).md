---
aliases:
  - embedding
type: concept
topic: LLM
status: usable
created: 2026-05-28
updated: 2026-05-29
source:
  - Karpathy Zero to Hero
tags:
  - LLM
  - representation
---

# Embedding

## 一句话解释

Embedding 是把离散 token ID 映射成连续向量，让模型能用向量运算学习 token 的语义、位置和关系。

## 它为什么存在

Token ID 本身只是编号。比如 `42` 并不天然比 `41` 更接近某个意思。神经网络需要连续向量作为输入，因此会维护一张可训练的表：

```text
token_id -> embedding_vector
```

训练过程中，相似上下文里反复出现的 token，其向量可能被调整到更有用的位置。

## 两类常见 embedding

- token embedding：表示“这个 token 是什么”。
- positional embedding：表示“这个 token 在序列的哪个位置”。

在 GPT 类模型里，常见输入是：

```text
token_embedding + positional_embedding
```

这让模型同时知道内容和顺序。

## 和后续模块的关系

Embedding 是模型进入深层网络前的第一步。它之后通常接：

- [[注意力机制(Attention)]]：让每个位置读取上下文信息。
- [[Transformer]] block：反复混合 token 间的信息。
- 线性层：输出下一个 token 的 logits。

## 易错点

- embedding 不是固定词典释义，而是训练出来的参数。
- embedding 维度越大表达能力越强，但参数量和计算量也增加。
- token embedding 和 positional embedding 解决的问题不同。
- 字符级模型也可以有 embedding，不只有单词或子词模型才有。

## 在 Karpathy 路线中的位置

[[../../03-Courses/LLM/Karpathy-Zero-to-Hero/02-makemore]] 会从简单字符表示逐步走向可训练 embedding；[[../../03-Courses/LLM/Karpathy-Zero-to-Hero/05-gpt-from-scratch]] 中 embedding 是 GPT 输入层的关键。

## 可实践任务

- 建一个小词表，用 PyTorch `nn.Embedding` 查看输出 shape。
- 改变 embedding 维度，观察参数量变化。
- 在 tiny 模型中打印 token embedding 和 positional embedding 的 shape。

## 相关笔记

- [[分词(Tokenization)]]
- [[注意力机制(Attention)]]
- [[Transformer]]
