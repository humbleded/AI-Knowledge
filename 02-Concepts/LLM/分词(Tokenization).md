---
aliases:
  - tokenization
type: concept
topic: LLM
status: usable
created: 2026-05-28
updated: 2026-05-29
source:
  - Karpathy Zero to Hero
tags:
  - LLM
  - data
  - language-modeling
---

# Tokenization

## 一句话解释

Tokenization 是把文本切分成模型可处理的 token，并把 token 映射成数字 ID 的过程。

## 为什么重要

语言模型不直接处理字符串。模型看到的是整数序列，例如：

```text
"hello" -> [68, 101, 108, 108, 111]
```

这些整数再进入 [[嵌入(Embedding)]] 层，变成向量。Tokenization 决定了：

- 文本被拆成多细。
- 模型的词表有多大。
- 同一段文本会占多少上下文长度。
- 罕见词、中文、代码、空格和标点如何表示。

## 常见粒度

- 字符级 token：简单，适合教学和 tiny 模型；Karpathy 的 makemore 和 tiny Shakespeare 常用这种方式讲清楚原理。
- 子词 token：现代 LLM 常用，兼顾词表大小和表达能力。
- 单词级 token：直观，但词表容易爆炸，遇到新词困难。

## 和语言模型训练的关系

自回归语言模型通常学习：

```text
给定前面的 token，预测下一个 token
```

例如训练样本可以是：

```text
input:  [t0, t1, t2]
target: [t1, t2, t3]
```

这直接连接到 [[自回归生成(Autoregressive)]]。

## 易错点

- token 不一定等于单词，一个中文字符、英文子词、空格都可能成为 token。
- token 数量影响上下文窗口和推理成本。
- tokenizer 是模型行为的一部分，换 tokenizer 会改变数据分布。
- 字符级模型更容易理解，但不代表现代 LLM 都是字符级。

## 在 Karpathy 路线中的位置

[[../../03-Courses/LLM/Karpathy-Zero-to-Hero/02-makemore]] 用字符级建模解释数据如何变成训练样本；[[../../03-Courses/LLM/Karpathy-Zero-to-Hero/05-gpt-from-scratch]] 则把 token 序列喂入 Transformer。

## 可实践任务

- 对一段文本建立字符表，写出 `stoi` 和 `itos`。
- 把字符串编码成 ID，再解码回来。
- 改变上下文长度，观察训练样本如何变化。

## 相关笔记

- [[嵌入(Embedding)]]
- [[自回归生成(Autoregressive)]]
- [[../../03-Courses/LLM/Karpathy-Zero-to-Hero/02-makemore]]
