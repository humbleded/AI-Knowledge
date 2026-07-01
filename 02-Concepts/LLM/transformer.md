---
aliases:
  - transformer
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
  - architecture
---

# Transformer

## 一句话解释

Transformer 是一种以 attention 为核心的神经网络架构，现代 GPT 类语言模型主要由重复堆叠的 Transformer block 组成。

## GPT 里的基本结构

一个简化的 GPT 通常包含：

- [[分词(Tokenization)]]：把文本变成 token ID。
- [[嵌入(Embedding)]]：把 token ID 和位置变成向量。
- 多层 Transformer block：混合上下文信息。
- language modeling head：输出下一个 token 的 logits。

Transformer block 常见组成：

- causal self-attention。
- feed-forward network。
- residual connection。
- layer normalization。

## 为什么 attention 是核心

RNN 需要按时间一步步处理序列，而 Transformer 可以让每个位置通过 [[注意力机制(Attention)]] 直接读取其他位置的信息。对 GPT 来说，每个位置读取的是过去位置的信息。

## residual 与 layer norm 的直觉

- residual connection：让信息和梯度更容易穿过很多层。
- layer normalization：稳定每层激活分布，让训练更容易。

## feed-forward network 的作用

Attention 负责跨 token 混合信息，feed-forward network 负责对每个位置的表示做非线性变换。两者交替堆叠，形成更强的序列建模能力。

## 易错点

- Transformer 不是只有 attention，完整 block 还包括 MLP、norm 和 residual。
- GPT 使用 causal self-attention，不能看未来 token。
- 位置编码很重要，否则模型无法区分 token 顺序。
- 层数、头数、embedding 维度、上下文长度共同影响参数量和计算量。

## 在 Karpathy 路线中的位置

[[../../03-Courses/LLM/Karpathy-Zero-to-Hero/05-gpt-from-scratch]] 把前面 bigram、MLP 和 attention 的概念组合成一个小型 GPT，是从“能训练玩具语言模型”到“理解现代 LLM 架构”的关键节点。

## 可实践任务

- 打印 GPT forward pass 中每一步 tensor shape。
- 逐个关闭 attention、MLP、residual，观察训练和生成变化。
- 手算一个很小序列的 causal attention mask。

## 相关笔记

- [[注意力机制(Attention)]]
- [[嵌入(Embedding)]]
- [[自回归生成(Autoregressive)]]
- [[../../03-Courses/LLM/Karpathy-Zero-to-Hero/05-gpt-from-scratch]]
