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
  - optimization
---

# Gradient Descent

## 一句话解释

梯度下降是一种用 loss 对参数的梯度来更新参数的方法：如果梯度告诉我们“往这个方向会让 loss 变大”，就沿相反方向走一小步。

## 它解决什么问题

训练神经网络时，模型有很多参数。我们无法靠手工猜出每个参数应该是多少，只能定义一个目标：

- 模型预测和真实答案越接近，loss 越小。
- 参数应该被调整到让 loss 下降的位置。
- 梯度告诉我们每个参数对 loss 的局部影响。

所以梯度下降把“训练模型”转化成反复执行：

```text
计算 loss -> 计算梯度 -> 更新参数 -> 再计算 loss
```

## 核心公式

```text
param = param - learning_rate * param.grad
```

- `param`：模型参数。
- `param.grad`：loss 对这个参数的梯度。
- `learning_rate`：每次更新迈多大一步。

## 和反向传播的关系

[[backpropagation]] 负责计算 `param.grad`，梯度下降负责使用 `param.grad` 更新参数。

可以记成：

- backpropagation：回答“每个参数该负责多少？”
- gradient descent：回答“知道责任后，参数应该怎么动？”

## 易错点

- 梯度不是全局最优方向，只是当前位置附近最陡的局部方向。
- learning rate 太大可能震荡或发散，太小会训练很慢。
- loss 下降不等于模型真的学到可泛化规律，还要看验证集和生成效果。
- 参数更新前通常要清空旧梯度，否则梯度会累积。

## 在 Karpathy 路线中的位置

在 [[../../03-Courses/LLM/Karpathy-Zero-to-Hero/01-micrograd]] 中，先手写计算图和反向传播，再用梯度下降更新参数，这是理解神经网络训练的最小闭环。

## 可实践任务

- 手写一个单参数模型：`y = w * x`，用梯度下降拟合 `w`。
- 改变 learning rate，观察 loss 下降、震荡或发散。
- 在 micrograd 中打印每次 `param.data` 和 `param.grad` 的变化。

## 相关笔记

- [[backpropagation]]
- [[../../03-Courses/LLM/Karpathy-Zero-to-Hero/01-micrograd]]
