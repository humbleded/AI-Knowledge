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
  - autograd
---

# 01 Micrograd

## 定位

Micrograd 是 Karpathy 路线的神经网络最小闭环：用很少的代码实现标量级 autograd，亲手看见 forward pass、backward pass、梯度和参数更新如何连成训练过程。

这节不是为了得到强模型，而是为了拆掉“神经网络训练是黑盒”的感觉。

## 学习目标

- 理解计算图如何记录运算依赖。
- 理解链式法则如何在图上反向传播。
- 理解 `loss.backward()` 本质上做了什么。
- 理解 [[../../../02-Concepts/LLM/backpropagation]] 和 [[../../../02-Concepts/LLM/gradient-descent]] 的分工。
- 从零实现一个极小 autograd 引擎。

## 关键概念

- `Value`：保存数值、梯度、前驱节点和反向函数。
- forward pass：根据当前参数计算输出和 loss。
- backward pass：从 loss 开始反向传播梯度。
- topological order：保证子节点的梯度先准备好，再传播给前驱。
- gradient descent：使用梯度更新参数。

## 最小训练闭环

```text
构建计算图
计算 loss
loss.backward()
更新参数
清空梯度
重复
```

## 应该能回答的问题

- 为什么同一个节点被多条路径使用时，梯度要累加？
- 为什么 backward 需要拓扑排序？
- `data` 和 `grad` 分别代表什么？
- 为什么反向传播只算梯度，不负责更新参数？
- learning rate 太大会发生什么？

## 实践记录

- [ ] 跑通原始代码。
- [ ] 自己重写一遍 `Value` 类。
- [ ] 画出 `a * b + c` 的计算图并手算梯度。
- [ ] 用自己的话解释 `backward()`。
- [ ] 写一个两层 MLP，并用 toy data 训练。

## 输出笔记

完成本节后应产生或更新：

- [[../../../02-Concepts/LLM/backpropagation]]
- [[../../../02-Concepts/LLM/gradient-descent]]
- [[../../../04-Projects/LLM/README|LLM 项目记录]]
- [[../../../log|维护日志]]

## 相关概念

- [[../../../02-Concepts/LLM/backpropagation]]
- [[../../../02-Concepts/LLM/gradient-descent]]
- [[../../../01-Maps/Karpathy AI 学习路线]]
