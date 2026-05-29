---
type: concept
topic: Python
status: seed
created: 2026-05-28
tags:
  - Python
  - 编程基础
---

# Python input() 与 print()

`print()` 用来把内容输出到终端。

`input()` 用来从终端接收用户输入。它有一个重要默认行为：接收到的内容默认都是字符串 `str`。

## 为什么重要

如果用户输入 `20`，`input()` 得到的不是数字 20，而是字符串 `"20"`。

需要参与数学计算或表示数值时，要用：

```python
age = int(input("请输入年龄："))
minutes = float(input("请输入每日学习分钟数："))
```

## 相关

- [[python-type-conversion]]
- [[python-basic-data-types]]

