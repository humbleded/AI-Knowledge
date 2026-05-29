---
type: concept
topic: LLM
status: usable
created: 2026-05-28
updated: 2026-05-29
source:
  - Karpathy Zero to Hero
tags:
  - LLM
  - training
  - autograd
---

# Backpropagation

## 一句话解释

反向传播是一种在计算图上高效计算每个中间变量和参数对最终 loss 影响的方法。

## 它解决什么问题

神经网络训练需要知道每个参数应该怎么调。直接逐个参数试错太慢，反向传播利用链式法则，从 loss 往前一层层传播梯度。

可以把它看成两步：

- forward pass：用当前参数计算预测和 loss。
- backward pass：从 loss 开始，沿计算图反向计算梯度。

## 计算图直觉

如果有：

```text
z = x * y
loss = z + b
```

那么 loss 对 `x` 的影响需要经过 `z` 传回来。复杂神经网络只是把这种局部链式法则重复很多次。

## 在 autograd 里的角色

在 Karpathy 的 micrograd 中，每个 `Value` 节点通常保存：

- `data`：当前数值。
- `grad`：loss 对该节点的梯度。
- `_prev`：它依赖的前驱节点。
- `_backward`：如何把当前梯度传给前驱节点。

`backward()` 的关键是按拓扑顺序反向执行每个节点的 `_backward`。

## 和梯度下降的关系

[[backpropagation]] 只负责算梯度，[[gradient-descent]] 才负责更新参数。

```text
loss.backward()
param.data -= learning_rate * param.grad
```

## 易错点

- 梯度表示局部敏感度，不是参数本身的重要程度。
- 同一个节点可能被多个路径使用，梯度需要累加。
- 反向传播前要保证 forward graph 已经构建好。
- 参数更新前通常要清零旧梯度。

## 在 Karpathy 路线中的位置

[[../../03-Courses/LLM/Karpathy-Zero-to-Hero/01-micrograd]] 是理解 backpropagation 的最小实验场：先在标量计算图上理解链式法则，再把同一思想推广到神经网络。

## 可实践任务

- 手写一个 `a * b + c` 的计算图。
- 手算每个变量的梯度。
- 实现一个最小 `Value` 类，支持 `+`、`*`、`tanh` 和 `backward()`。

## 相关笔记

- [[gradient-descent]]
- [[../../03-Courses/LLM/Karpathy-Zero-to-Hero/01-micrograd]]
