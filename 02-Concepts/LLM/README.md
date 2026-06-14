---
type: concept-index
topic: LLM
status: active
created: 2026-05-28
updated: 2026-06-14
tags:
  - LLM
  - 概念卡
---

# LLM 概念卡

## 训练基础

- [[backpropagation|Backpropagation]]：usable，理解计算图和梯度传播。
- [[gradient-descent|Gradient Descent]]：usable，理解如何用梯度更新参数。

## 语言建模基础

- [[tokenization|Tokenization]]：usable，理解文本如何变成 token ID。
- [[embedding|Embedding]]：usable，理解 token/position 如何变成向量表示。
- [[autoregressive-generation|Autoregressive Generation]]：usable，理解下一个 token 预测和生成循环。

## Transformer 基础

- [[attention|Attention]]：usable，理解 Q/K/V、causal mask 和上下文读取。
- [[transformer|Transformer]]：usable，理解 GPT 类模型的基本 block。

## 调用与工程

- [[api-key-and-sdk|API Key 与 SDK：调用模型的门禁卡和快递柜台]]：usable，理解 key、模型名、SDK 和环境变量的分工。
- [[chat-completions-call|调用 LLM：chat.completions 与取回复]]：usable，传 `messages`、取 `response.choices[0].message.content`，含 key/`load_dotenv`、错误提示、封装复用等易错点。

## 对应课程

- [[../../03-Courses/LLM/Karpathy-Zero-to-Hero/README|Karpathy Zero to Hero]]
- [[../../03-Courses/LLM/Karpathy-Zero-to-Hero/01-micrograd]]
- [[../../03-Courses/LLM/Karpathy-Zero-to-Hero/02-makemore]]
- [[../../03-Courses/LLM/Karpathy-Zero-to-Hero/05-gpt-from-scratch]]

## 下一批可新增概念

- cross entropy
- logits
- softmax
- train/validation split
- overfitting
- layer normalization
- residual connection
