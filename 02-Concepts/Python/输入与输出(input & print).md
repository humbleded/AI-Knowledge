---
aliases:
  - python-input-print
type: concept
topic: Python
status: usable
created: 2026-05-28
updated: 2026-09-20
tags:
  - Python
  - 编程基础
---

# Python input() 与 print()

## 中文速读

- `print()` 负责把内容显示到终端，适合给人看运行结果。
- `input()` 负责从终端接收用户输入；它拿到的内容永远先是 `str`，也就是字符串。
- 后续要做计算、判断或测试时，别把 `print()` 和 `return` 混在一起：`print()` 是显示，`return` 是把结果交回给调用者。

## 它们分别做什么

`print()` 用来输出内容：

```python
name = "Ada"
print(name)
print(f"你好，{name}")
```

`input()` 用来等待用户输入，并把输入结果保存成字符串：

```python
name = input("请输入姓名：")
print(f"你好，{name}")
```

括号里的 `"请输入姓名："` 是提示文本，它会显示给用户看，但不会自动参与计算。

## `input()` 的关键规则

如果用户输入 `20`，`input()` 得到的不是数字 20，而是字符串 `"20"`。

需要参与数学计算或表示数值时，要用：

```python
age = int(input("请输入年龄："))
minutes = float(input("请输入每日学习分钟数："))
```

如果用户输入的内容不能转换，`int()` 或 `float()` 会抛出 `ValueError`。正式程序里通常要配合 `try/except` 做错误处理。

## `print()` 和 `return` 的区别

| 写法 | 面向谁 | 适合什么时候 |
|---|---|---|
| `print(value)` | 给人看 | 命令行提示、调试、最终展示 |
| `return value` | 给代码继续用 | 函数拆分、单元测试、让调用者拿到结果 |

学习任务里常见的边界是：生成计划的函数应该 `return plan`，主程序拿到 `plan` 后再决定要不要逐行 `print()`。

```python
def make_plan(goal, days):
    plan = []
    for i in range(days):
        plan.append(f"第{i + 1}天：学习 {goal}")
    return plan


for item in make_plan("函数", 3):
    print(item)
```

## 常见误解

- `input()` 不会自动把 `"20"` 变成 `20`。
- `print()` 的返回值是 `None`，不能拿它当函数结果继续算。
- 在可测试函数里到处写 `input()` / `print()` 会让测试变难；更稳的做法是函数接收参数、返回结果，输入输出放在 `main()`。
- 提示文本不是校验规则；用户仍然可能输入空字符串、中文、负数或不合法数字。

## 相关

- [[类型转换(Type Conversion)]]
- [[基础数据类型(Data Types)]]
- [[f-string 格式化]]
- [[函数与参数(Functions)]]
- [[异常·调试·测试(Exceptions)]]

## 来源 / 证据

- [[../../raw/articles/python-3-official-documentation|Python 3 Official Documentation]]
- [[../../03-Courses/Python/AI-Agent-Learning/stage0-python-basics|阶段 0：Python 与开发环境]]
- [[../../04-Projects/Python/AI-Agent-Learning/p0-01-hello-script|P0-01 第一个脚本]]
- [[../../07-Reviews/Daily-Practice/2026-06-05-review|2026-06-05 每日练习批改]]
