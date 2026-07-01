---
aliases:
  - python-conditionals-and-loops
type: concept
topic: Python conditionals and loops
status: active
created: 2026-05-29
tags:
  - Python
  - 条件判断
  - 循环
  - AI-Agent-Learning
---

# Python 条件判断与循环

条件判断和循环是脚本自动化的基础。

条件判断负责让程序根据不同情况选择不同路线。常见写法是 `if/elif/else`：

```python
study_hours = int(input("请输入今天的学习时长（小时）："))

if study_hours < 2:
    print("学习时长不足，请加油！")
elif study_hours < 4:
    print("学习时长合格，继续保持！")
else:
    print("学习时长优秀，太棒了！")
```

这里的判断顺序很重要。程序会从上到下检查条件，命中第一条后就执行对应分支，后面的分支不会再执行。

循环负责把重复动作交给程序自动完成。`for` 适合次数明确，或者遍历 `list`、`dict`、`range` 等对象：

```python
for day in range(1, 8):
    print(f"第{day}天：继续努力学习！")
```

这比复制 7 次 `print()` 更好，因为代码更短，也更容易修改。如果以后要打印 14 天计划，只需要改 `range(1, 15)`。

`while` 更适合次数不确定，只知道某个条件成立时继续执行。例如用户没有输入 `exit` 就持续运行。

## 学习检查点

- 能说清楚 `if/elif/else` 是在做分支选择。
- 能说清楚 `for` 常用于次数明确或遍历数据。
- 能说清楚 `while` 常用于次数未知但条件明确的循环。
- 能解释为什么重复逻辑应该用循环，而不是复制多行代码。

## 关联

- [[match-case 分支]]
- [[../../04-Projects/Python/AI-Agent-Learning/p0-03-scheduler]]
- [[../../07-Reviews/AI-Agent-Learning/2026-05-28-stage0-p0-03-pass-review]]
