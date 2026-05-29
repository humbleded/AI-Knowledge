---
type: project-note
topic: AI-Agent-Learning P0-02
status: pass
created: 2026-05-28
tags:
  - Python
  - AI-Agent-Learning
  - PASS
---

# P0-02 数据类型与变量

## 任务

写一个学习档案脚本，保存姓名、年龄、学习目标、每日学习分钟数，并输出一段学习档案。

源代码位置：

- [p0_02_profile.py](file:///C:/Users/26823/Desktop/AI-Agent-Learning/code/stage0/p0_02_profile.py)

## 代码要点

脚本体现了四种基础数据类型：

- `name`、`goal`：`str`
- `age`：`int`
- `minutes`：`float`
- `flag`：`bool`

核心代码：

```python
age = int(input("请输入你的年龄："))
minutes = float(input("请输入你每天学习的分钟数："))
flag = 3 > 2
```

## 通过结论

P0-02 已 PASS。

通过原因：

- 能运行脚本。
- 能输出学习档案。
- 已体现 `str`、`int`、`float`、`bool` 四种数据类型。
- 能解释变量名、数据类型和 f-string 的作用。

## 曾经踩过的坑

最初版本中，`input()` 得到的年龄和分钟数仍是字符串，没有真正体现数值类型。

后续修正为：

```python
age = int(input(...))
minutes = float(input(...))
```

还要注意：不要直接用 `bool(input(...))` 判断用户输入真假，因为非空字符串都会变成 `True`。

## 可改进点

- 把变量名 `flage` 改成 `flag` 或更具体的 `is_valid`。
- 用更有业务意义的布尔值，例如 `is_beginner = True`。

## 相关概念

- [[../../../02-Concepts/Python/python-variables]]
- [[../../../02-Concepts/Python/python-basic-data-types]]
- [[../../../02-Concepts/Python/python-type-conversion]]
- [[../../../02-Concepts/Python/python-f-string]]

