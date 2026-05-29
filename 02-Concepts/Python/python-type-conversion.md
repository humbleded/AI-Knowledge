---
type: concept
topic: Python
status: seed
created: 2026-05-28
tags:
  - Python
  - 编程基础
---

# Python 类型转换

类型转换是把一个值从一种类型变成另一种类型。

`input()` 默认返回字符串，所以如果要把输入当作数字使用，需要显式转换：

```python
age = int(input("请输入年龄："))
minutes = float(input("请输入每日学习分钟数："))
```

## bool(input(...)) 的坑

不要直接用 `bool(input(...))` 判断用户输入的真假。

原因是：非空字符串都会被 `bool()` 转成 `True`，即使用户输入的是 `"False"`。

更稳妥的写法是判断具体文本：

```python
answer = input("是否完成？")
is_done = answer.lower() in ["true", "yes", "1", "y"]
```

## 相关

- [[python-input-print]]
- [[python-basic-data-types]]

