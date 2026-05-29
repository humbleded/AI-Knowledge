---
type: project
topic: LLM
status: planned
created: 2026-05-29
updated: 2026-05-29
source:
  - Karpathy Neural Networks Zero to Hero
tags:
  - LLM
  - Project
  - Karpathy
  - autograd
---

# Micrograd：从零实现反向传播

## 项目目标

用最小代码复现 micrograd 的核心思想：构建标量计算图，执行 forward pass，调用 `backward()` 反向传播梯度，再用 [[../../02-Concepts/LLM/gradient-descent]] 更新参数。

这个项目用于把 [[../../03-Courses/LLM/Karpathy-Zero-to-Hero/01-micrograd]] 从课程理解推进到可运行实验。

## 最小验收标准

- [ ] 实现 `Value` 类，至少支持 `+`、`*`、`tanh`。
- [ ] 每个 `Value` 节点保存 `data`、`grad`、`_prev`、`_backward`。
- [ ] `backward()` 能按拓扑顺序反向传播。
- [ ] 能手写一个 `a * b + c` 的例子，并打印每个节点梯度。
- [ ] 能训练一个极小 MLP 或 toy neuron，并观察 loss 下降。

## 推荐文件结构

```text
micrograd/
  engine.py
  nn.py
  demo_scalar_graph.py
  demo_toy_mlp.py
```

## 核心实现拆解

### 1. Value 节点

`Value` 是计算图的节点。它既保存当前数值，也保存 loss 对自己的梯度。

```text
data: 当前节点数值
grad: d(loss) / d(this node)
_prev: 当前节点依赖的前驱节点
_backward: 如何把当前梯度传给前驱节点
```

### 2. 运算符重载

每次执行 `+`、`*`、`tanh` 等操作时，都创建一个新的 `Value` 节点，并记录它依赖哪些旧节点。

关键不是“算出数值”，而是保留“这个数值是怎么来的”。

### 3. 反向传播

`backward()` 的核心流程：

```text
从 loss 节点出发
构建拓扑排序
设置 loss.grad = 1
按反向拓扑顺序执行每个节点的 _backward()
```

这对应 [[../../02-Concepts/LLM/backpropagation]] 中的链式法则。

### 4. 参数更新

反向传播只负责计算梯度，参数更新由梯度下降完成：

```text
param.data -= learning_rate * param.grad
```

训练循环里还要清空旧梯度，否则梯度会累加。

## 观察记录

| 实验 | 观察项 | 结果 |
| --- | --- | --- |
| scalar graph | 每个中间节点的 `grad` | 待记录 |
| toy neuron | loss 是否下降 | 待记录 |
| toy MLP | learning rate 对训练的影响 | 待记录 |

## 常见问题

- 同一个节点被多个路径复用时，梯度要累加。
- `backward()` 前要先完成 forward pass。
- 更新参数前后要关注 `grad` 是否被清零。
- learning rate 过大时 loss 可能不降反升。

## 相关笔记

- [[../../03-Courses/LLM/Karpathy-Zero-to-Hero/01-micrograd]]
- [[../../02-Concepts/LLM/backpropagation]]
- [[../../02-Concepts/LLM/gradient-descent]]
- [[../../01-Maps/Karpathy AI 学习路线]]
