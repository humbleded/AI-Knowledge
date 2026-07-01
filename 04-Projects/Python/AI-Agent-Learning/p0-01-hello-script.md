---
type: project-note
topic: AI-Agent-Learning P0-01
status: pass
created: 2026-05-28
tags:
  - Python
  - AI-Agent-Learning
  - PASS
---

# P0-01 环境与第一个程序

## 任务

写一个输入姓名和学习目标的 Python 脚本，并能在终端运行。

源代码位置：

- [p0_01_hello.py](file:///C:/Users/26823/Desktop/AI-Agent-Learning/code/stage0/p0_01_hello.py)

## 代码要点

```python
name = input("请输入你的姓名：")
goal = input("请输入你的学习目标：")
print("你好，" + name + "！你的学习目标是：" + goal + "。")
```

## 通过结论

P0-01 已 PASS。

通过原因：

- 能运行脚本。
- 能接收用户输入。
- 能输出包含用户姓名和学习目标的结果。
- 能解释 Python 解释器、`print()`、`input()`、终端运行和交互模式的区别。

## 可改进点

后续可以改成 f-string：

```python
print(f"你好，{name}！你的学习目标是：{goal}。")
```

## 相关概念

- [[../../../02-Concepts/Python/解释器(Interpreter)]]
- [[../../../02-Concepts/Python/输入与输出(input & print)]]
- [[../../../02-Concepts/Python/f-string 格式化]]

