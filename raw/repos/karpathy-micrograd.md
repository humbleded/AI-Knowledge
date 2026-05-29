---
type: source
topic: micrograd
status: active
created: 2026-05-29
updated: 2026-05-29
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

## What To Compile Into Wiki

- `Value` object design -> [[../../02-Concepts/LLM/backpropagation]]
- reverse-mode autodiff -> [[../../02-Concepts/LLM/backpropagation]]
- SGD parameter update -> [[../../02-Concepts/LLM/gradient-descent]]
- runnable practice -> [[../../04-Projects/LLM/micrograd-backprop-from-scratch]]

## Do Not Lose

- This source is code-first. The value is not only the explanation, but the tiny executable implementation.
- Keep project notes connected to observed runs, not just conceptual summaries.
