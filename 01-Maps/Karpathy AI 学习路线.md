---
type: map
topic: Karpathy AI 学习路线
status: active
created: 2026-05-28
tags:
  - Karpathy
  - LLM
  - 学习路线
---

# Karpathy AI 学习路线

## 定位

这条路线围绕 Andrej Karpathy 的公开课程和代码实践，目标是从神经网络基础一路走到自己理解并实现一个小型 GPT。

本路线同时作为知识库的 Karpathy 式 LLM Wiki 试验主线：原始课程资料、字幕、代码阅读和实验结果先进入 [[../raw/README|Raw Sources]]，再编译为概念卡、课程页、项目记录和复盘。

## 维护方式

- 课程原始资料放入 `raw/transcripts/`、`raw/articles/` 或 `raw/repos/`。
- 课程学习页放入 `03-Courses/LLM/Karpathy-Zero-to-Hero/`。
- 概念拆解放入 `02-Concepts/LLM/`。
- 代码实验和复现记录放入 `04-Projects/LLM/`。
- 每次完成一段学习后更新 [[../index|全局索引]] 和 [[../log|维护日志]]。

## 阶段 1：神经网络直觉

目标：理解神经网络不是魔法，而是可微分函数和梯度下降。

建议笔记：

- [[../02-Concepts/LLM/反向传播(Backprop)]]
- [[../02-Concepts/LLM/梯度下降(Gradient Descent)]]
- [[../03-Courses/LLM/Karpathy-Zero-to-Hero/01-micrograd]]

实践任务：

- 跑通 micrograd
- 手写一个简单的标量反向传播例子
- 解释 `loss.backward()` 做了什么

## 阶段 2：字符级语言模型

目标：理解模型如何从字符序列中学习统计规律。

建议笔记：

- [[../02-Concepts/LLM/分词(Tokenization)]]
- [[../02-Concepts/LLM/嵌入(Embedding)]]
- [[../03-Courses/LLM/Karpathy-Zero-to-Hero/02-makemore]]

实践任务：

- 训练一个名字生成器
- 改变上下文长度并观察结果
- 记录 loss 变化和样本质量变化

## 阶段 3：Transformer 与 GPT

目标：理解 attention、block、positional embedding 和自回归生成。

建议笔记：

- [[../02-Concepts/LLM/注意力机制(Attention)]]
- [[../02-Concepts/LLM/Transformer]]
- [[../02-Concepts/LLM/自回归生成(Autoregressive)]]
- [[../03-Courses/LLM/Karpathy-Zero-to-Hero/05-gpt-from-scratch]]

实践任务：

- 从零实现一个小 GPT
- 训练 tiny Shakespeare
- 解释 forward pass 中每个 tensor 的 shape

## 阶段 4：AI 工程化

目标：从“能跑模型”走向“能把 AI 能力做成系统”。

建议主题：

- RAG
- Agent
- Tool calling
- MCP
- 本地知识库
- 评估与复盘
