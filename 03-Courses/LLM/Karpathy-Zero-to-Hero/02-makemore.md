---
type: course-note
topic: Karpathy Zero to Hero
status: usable
created: 2026-05-28
updated: 2026-05-29
source:
  - Karpathy Neural Networks Zero to Hero
tags:
  - Course/Karpathy
  - LLM
  - language-modeling
---

# 02 Makemore

## 定位

Makemore 用字符级名字生成任务解释语言模型的核心问题：给定已有上下文，预测下一个 token。

这节把“训练神经网络”从抽象的计算图推进到真实序列数据，让 [[../../../02-Concepts/LLM/tokenization]]、[[../../../02-Concepts/LLM/embedding]] 和 [[../../../02-Concepts/LLM/autoregressive-generation]] 变得具体。

## 学习目标

- 理解字符级语言模型。
- 理解 bigram 模型如何从计数出发。
- 理解训练数据如何变成监督学习样本。
- 理解上下文长度如何影响模型可用信息。
- 理解 embedding 如何把字符 ID 变成可训练向量。

## 核心流程

```text
名字文本
-> 字符表
-> token ID
-> input/target 样本
-> 模型预测下一个字符
-> loss
-> backprop + update
-> 采样生成新名字
```

## 应该能回答的问题

- 字符级 tokenization 和现代 LLM 的子词 tokenization 有什么差别？
- 为什么 bigram 模型只能看一个历史字符？
- context length 变大后，训练样本如何变化？
- embedding 表的 shape 是什么？
- 生成时为什么要把预测 token 接回上下文？

## 实践记录

- [ ] 构建字符表、`stoi`、`itos`。
- [ ] 训练 bigram 名字生成器。
- [ ] 改变 context length 并比较生成质量。
- [ ] 打印 embedding、hidden layer、logits 的 shape。
- [ ] 记录 loss 曲线和样本输出。

## 输出笔记

完成本节后应产生或更新：

- [[../../../02-Concepts/LLM/tokenization]]
- [[../../../02-Concepts/LLM/embedding]]
- [[../../../02-Concepts/LLM/autoregressive-generation]]
- [[../../../04-Projects/LLM/README|LLM 项目记录]]
- [[../../../log|维护日志]]

## 相关概念

- [[../../../02-Concepts/LLM/tokenization]]
- [[../../../02-Concepts/LLM/embedding]]
- [[../../../02-Concepts/LLM/autoregressive-generation]]
- [[../../../01-Maps/Karpathy AI 学习路线]]
