---
type: concept
topic: Python boolean operators
status: usable
created: 2026-06-13
updated: 2026-06-13
tags:
  - Python
  - boolean
  - short-circuit
  - AI-Agent-Learning
aliases:
  - Python and or 短路
  - Python 逻辑运算符
---

# Python and / or 短路与返回原值

`and` 和 `or` 是 Python 的逻辑运算符。它们会根据对象的真假值判断表达式，但结果不一定是 `True` 或 `False`，而是返回参与运算的某个原始值。

常见假值包括：

```python
False
None
0
""
[]
{}
set()
```

其他大多数对象都按真值处理。

## 核心规则

`A and B`：

- 如果 `A` 是假值，直接返回 `A`。
- 如果 `A` 是真值，返回 `B`。

```python
1 and 2       # 2
0 and 2       # 0
"" and "ok"   # ""
```

`A or B`：

- 如果 `A` 是真值，直接返回 `A`。
- 如果 `A` 是假值，返回 `B`。

```python
1 or 2           # 1
0 or 2           # 2
"" or "default"  # "default"
```

## 短路

短路指的是：如果左边已经足够决定结果，右边就不会执行。

```python
x = 0

x and 10 / x   # 0，不会报 ZeroDivisionError
x or 10        # 10
```

这里 `x and 10 / x` 不会报错，因为 `x` 是假值，`and` 直接返回 `x`，右边的 `10 / x` 不会执行。

## 优先级

混用 `not`、`and`、`or` 时，优先级是：

```text
not > and > or
```

所以：

```python
True or False and False        # True
(True or False) and False      # False
```

第一行等价于：

```python
True or (False and False)
```

## 常见坑

- 错误理解：`and` / `or` 只会返回布尔值。
- 正确理解：`and` / `or` 返回的是某个原始操作数；如果确实需要布尔值，可以显式写 `bool(expr)`。

- 错误理解：`value or default` 只在 `value is None` 时使用默认值。
- 正确理解：只要 `value` 是假值，都会使用默认值，包括 `0`、`""`、`[]`。如果只想处理 `None`，应该写：

```python
result = default if value is None else value
```

- 混用 `and` 和 `or` 时不要只靠记忆优先级。为了可读性，复杂表达式优先加括号。

## 来源与验证

- 2026-06-13 AI-Agent-Learning 学习对话：用户能够正确预测 `and` / `or` 返回原值、短路行为，以及 `and` 优先于 `or` 的例子。
- 本次沉淀的可复用坑点：不要把 `and` / `or` 理解成“只返回 `True` / `False`”。

## 相关

- [[python-basic-data-types|Python 基础数据类型]]
- [[python-conditionals-and-loops|Python 条件判断与循环]]
