---
aliases:
  - python-variables
type: concept
topic: Python
status: usable
created: 2026-05-28
updated: 2026-09-20
tags:
  - Python
  - 编程基础
---

# Python 变量

## 中文速读

- Variable（变量）就是给一个值起名字，方便后面继续使用。
- `name = "张三"` 的意思不是“数学等式”，而是把右边的值绑定到左边的名字。
- 变量名要表达用途；后面写函数、Agent 工具注册表和 JSON 数据时，可读变量名会直接减少误判。

## 它是什么

变量是程序里的“标签”。它把一个名字和一个值关联起来。

例如：

```python
name = "张三"
age = 20
```

`name` 和 `age` 是变量名，右边的内容是它们保存的值。

Python 赋值语句通常按这个方向读：

```text
左边的名字 = 右边算出来的值
```

例如：

```python
days = 3
plan = make_plan("函数", days)
```

这里先让 `days` 指向整数 `3`，再把 `make_plan(...)` 返回的列表保存到 `plan`。

## 变量名为什么要有意义

有意义的变量名能让自己和别人快速看懂这个值的用途，后续修改代码时也更不容易弄错。

例如 `minutes` 比 `x` 更容易看懂，`is_beginner` 比 `flag` 更能表达布尔值含义。

## 常见命名习惯

- 普通变量用小写和下划线：`study_hours`、`task_status`。
- 布尔值常用 `is_`、`has_`、`can_` 开头：`is_done`、`has_error`、`can_retry`。
- 列表名可以用复数：`tasks`、`messages`。
- 字典名最好体现映射关系：`task_status` 表示“任务名 -> 状态”。

## 重新赋值

同一个变量名可以重新指向新值：

```python
score = "retry"
score = "pass"
```

这不是同时保存两个值；第二行执行后，`score` 当前指向 `"pass"`。

容器变量要额外小心，因为修改容器内容和重新赋值不是一回事：

```python
tasks = ["read", "code"]
tasks.append("review")      # 修改原列表
tasks = ["new task"]        # 让 tasks 指向一个新列表
```

## 常见误解

- 字符串值要加引号，变量名不要加引号：`name = "Ada"`。
- `NameError` 通常说明变量名没定义、拼错，或作用域不对。
- `time = 2` 能运行，但含义不清；`study_hours = 2` 更容易维护。
- 变量名不要遮住常用函数名，例如不要把 `list`、`dict`、`str` 当普通变量名。

## 相关

- [[基础数据类型(Data Types)]]
- [[f-string 格式化]]
- [[list·dict·set 容器]]
- [[函数与参数(Functions)]]

## 来源 / 证据

- [[../../raw/articles/python-3-official-documentation|Python 3 Official Documentation]]
- [[../../03-Courses/Python/AI-Agent-Learning/stage0-python-basics|阶段 0：Python 与开发环境]]
- [[../../04-Projects/Python/AI-Agent-Learning/p0-02-profile-script|P0-02 个人资料脚本]]
- [[../../07-Reviews/Daily-Practice/2026-06-05-review|2026-06-05 每日练习批改]]
