---
aliases:
  - python-if-not-in
  - Python not in 成员检查
type: concept
topic: Python
status: active
created: 2026-07-06
updated: 2026-07-06
tags:
  - Python
  - 条件判断
  - 成员检查
---

# Python `if operation not in OPERATORS`：成员检查

这句代码的意思是：检查 `operation` 这个值是否**不在** `OPERATORS` 里面。

```python
if operation not in OPERATORS:
    print("不支持这个运算符")
```

可以把它想成门卫查名单：

- `operation`：用户拿来的通行证，例如 `"+"`、`"-"`、`"%"`
- `OPERATORS`：允许进入的名单，例如 `["+", "-", "*", "/"]`
- `not in`：不在名单里

所以：

```python
OPERATORS = ["+", "-", "*", "/"]

operation = "%"

if operation not in OPERATORS:
    print("不支持这个运算符")
```

因为 `"%"` 不在 `OPERATORS` 里，所以上面的 `if` 条件成立，会执行缩进里的代码。

如果换成：

```python
operation = "+"

if operation not in OPERATORS:
    print("不支持这个运算符")
```

因为 `"+"` 在 `OPERATORS` 里，所以 `operation not in OPERATORS` 的结果是 `False`，`if` 下面的代码不会执行。

## 核心记忆

`in` 和 `not in` 用来做**成员检查**：

```python
"+" in ["+", "-", "*", "/"]       # True
"%" in ["+", "-", "*", "/"]       # False
"%" not in ["+", "-", "*", "/"]   # True
```

`if operation not in OPERATORS:` 常用于输入校验：如果用户输入了不支持的值，就提前报错或拒绝继续执行。

## 字典里的特殊点

如果 `OPERATORS` 是字典：

```python
OPERATORS = {
    "+": "加法",
    "-": "减法",
    "*": "乘法",
    "/": "除法",
}
```

那么：

```python
operation not in OPERATORS
```

默认检查的是字典的 **key**，也就是 `"+"`、`"-"`、`"*"`、`"/"`，不是 `"加法"`、`"减法"` 这些 value。

## 易错点

- 错误理解：`if operation not in OPERATORS:` 是“在里面就执行”。
- 正确理解：只有 `operation` **不在** `OPERATORS` 里，`if` 下面的代码才会执行。
- 如果 `operation = "+"` 且 `OPERATORS` 里有 `"+"`，那么条件是 `False`，不会执行错误处理代码。

## 关联

- [[条件判断与循环(if & for)]]
- [[list·dict·set 容器]]
