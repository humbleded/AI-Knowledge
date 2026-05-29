---
type: course-index
topic: Karpathy Zero to Hero
status: active
created: 2026-05-29
updated: 2026-05-29
source:
  - Karpathy Neural Networks Zero to Hero
tags:
  - Course/Karpathy
  - LLM
  - index
---

# Karpathy Zero to Hero

## 路线定位

这组课程笔记用于承接 Andrej Karpathy 的神经网络与语言模型路线：先理解 autograd 和神经网络训练，再逐步进入字符级语言模型、attention 和 GPT from scratch。

## 当前课程页

- [[01-micrograd|01 Micrograd]]
- [[02-makemore|02 Makemore]]
- [[05-gpt-from-scratch|05 GPT From Scratch]]

## 配套概念卡

- [[../../../02-Concepts/LLM/backpropagation]]
- [[../../../02-Concepts/LLM/gradient-descent]]
- [[../../../02-Concepts/LLM/tokenization]]
- [[../../../02-Concepts/LLM/embedding]]
- [[../../../02-Concepts/LLM/attention]]
- [[../../../02-Concepts/LLM/transformer]]
- [[../../../02-Concepts/LLM/autoregressive-generation]]

## 实践输出

代码实验、训练记录和复现笔记放入：

- [[../../../04-Projects/LLM/README]]
- [[../../../04-Projects/LLM/micrograd-backprop-from-scratch|Micrograd：从零实现反向传播]]

## Ingest 规则

- 课程字幕、原始摘录、代码阅读先进入 [[../../../raw/transcripts/README|raw/transcripts]] 或 [[../../../raw/repos/README|raw/repos]]。
- 编译后的学习路线和课程理解放在本目录。
- 可复用概念拆到 `02-Concepts/LLM/`。
- 每次完成课程页扩写或项目实验后更新 [[../../../log|维护日志]]。

## 下一步

- 完成 micrograd 项目复现记录中的验收项。
- 补充 makemore 字符级生成实验记录。
- 补充 GPT from scratch tensor shape 追踪记录。
