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
  - transformer
---

# 05 GPT From Scratch

## 定位

GPT From Scratch 把前面学到的语言建模、embedding、attention 和训练循环组合起来，从零实现一个小型 GPT。

这节的目标不是训练大模型，而是理解现代 GPT 类模型的骨架：token 进入模型后如何变成向量，向量如何通过 causal self-attention 读取上下文，最后如何输出下一个 token 的概率分布。

## 学习目标

- 理解 Transformer block 的组成。
- 理解 [[../../../02-Concepts/LLM/注意力机制(Attention)]] 和 causal mask。
- 理解 [[../../../02-Concepts/LLM/Transformer]] 中 residual、layer norm、feed-forward 的角色。
- 理解 [[../../../02-Concepts/LLM/自回归生成(Autoregressive)]] 的训练和生成循环。
- 从零实现并训练一个小型 GPT。

## 核心结构

```text
token IDs
-> token embedding + positional embedding
-> repeated Transformer blocks
-> layer norm
-> language modeling head
-> logits for next token
```

每个 Transformer block 大致是：

```text
x = x + causal_self_attention(layer_norm(x))
x = x + feed_forward(layer_norm(x))
```

## 应该能回答的问题

- 为什么 GPT 需要 causal mask？
- token embedding 和 positional embedding 的 shape 分别是什么？
- attention head 的 Q/K/V 分别从哪里来？
- logits、probabilities、sampled token 有什么区别？
- 训练时为什么能并行预测多个位置，而生成时要逐步追加 token？

## 实践记录

- [ ] 跑通 tiny Shakespeare 或同类小语料训练。
- [ ] 打印 forward pass 中每个 tensor 的 shape。
- [ ] 实现 single-head causal self-attention。
- [ ] 扩展到 multi-head attention。
- [ ] 记录不同 context length、n_embd、n_head 对训练速度和生成质量的影响。

## 输出笔记

完成本节后应产生或更新：

- [[../../../02-Concepts/LLM/注意力机制(Attention)]]
- [[../../../02-Concepts/LLM/Transformer]]
- [[../../../02-Concepts/LLM/自回归生成(Autoregressive)]]
- [[../../../04-Projects/LLM/README|LLM 项目记录]]
- [[../../../log|维护日志]]

## 相关概念

- [[../../../02-Concepts/LLM/注意力机制(Attention)]]
- [[../../../02-Concepts/LLM/Transformer]]
- [[../../../02-Concepts/LLM/自回归生成(Autoregressive)]]
- [[../../../02-Concepts/LLM/嵌入(Embedding)]]
- [[../../../01-Maps/Karpathy AI 学习路线]]
