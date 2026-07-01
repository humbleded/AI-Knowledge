---
type: source
topic: micrograd
status: active
created: 2026-05-29
updated: 2026-06-21
source_url: https://github.com/karpathy/micrograd
source_type: repository
tags:
  - Source
  - Karpathy
  - LLM
  - autograd
---

# karpathy/micrograd

## Source

- GitHub: https://github.com/karpathy/micrograd
- Author: Andrej Karpathy
- License: MIT
- Retrieved: 2026-05-29

## Why This Source Matters

This is the original micrograd repository used as the reference point for the Karpathy Zero to Hero micrograd practice.

The repository positions micrograd as a tiny scalar-valued autograd engine plus a small neural network library with a PyTorch-like API. Its README explains that the engine performs reverse-mode automatic differentiation over a dynamically built DAG and is primarily useful for education.

## 中文速读

- 这是 Karpathy 的原始 `micrograd` 仓库，也是本库学习反向传播和自动微分的代码基准。
- `micrograd` 用很少的代码实现标量级 autograd（自动微分）引擎，并提供一个类似 PyTorch API 的小型神经网络库。
- 它通过运行时动态构建的 DAG（有向无环图）执行 reverse-mode automatic differentiation（反向模式自动微分），主要价值是帮助学习者看清梯度如何沿计算图传播。

## 关键术语

- `autograd`（自动微分）：根据计算图自动计算梯度。
- `reverse-mode automatic differentiation`（反向模式自动微分）：从输出向输入反向传播梯度，适合神经网络训练。
- `DAG`（有向无环图）：表示运算依赖关系的计算图结构。
- `PyTorch-like API`（类似 PyTorch 的接口）：用接近主流深度学习框架的方式组织标量、参数和网络层。

## What To Compile Into Wiki

- `Value` object design -> [[../../02-Concepts/LLM/反向传播(Backprop)]]
- reverse-mode autodiff -> [[../../02-Concepts/LLM/反向传播(Backprop)]]
- SGD parameter update -> [[../../02-Concepts/LLM/梯度下降(Gradient Descent)]]
- runnable practice -> [[../../04-Projects/LLM/micrograd-backprop-from-scratch]]

## Do Not Lose

- This source is code-first. The value is not only the explanation, but the tiny executable implementation.
- Keep project notes connected to observed runs, not just conceptual summaries.
