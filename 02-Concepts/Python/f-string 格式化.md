---
aliases:
  - python-f-string
type: concept
topic: Python
status: usable
created: 2026-05-28
updated: 2026-09-20
tags:
  - Python
  - 编程基础
---

# Python f-string

## 中文速读

- f-string 是 Python 里把变量放进字符串的常用写法。
- 它解决的是“生成给人看的文本”，比如命令行提示、学习计划、日志摘要。
- 记住两个关键点：字符串前要有 `f`，变量或表达式放在 `{}` 里。

f-string 用来把变量方便地放进字符串里。

```python
age = 20
print(f"年龄：{age}")
```

## 解决什么问题

f-string 比字符串拼接更清楚，也能避免字符串和数字直接拼接时报错。

对比：

```python
print("年龄：" + str(age))
print(f"年龄：{age}")
```

第二种更简洁，也更适合输出学习档案、日志、提示信息。

## 最小用法

```python
goal = "函数"
day = 1
line = f"第{day}天：学习 {goal}"
print(line)
```

输出：

```text
第1天：学习 函数
```

`{day}` 和 `{goal}` 会被当前变量值替换。花括号里也可以放简单表达式：

```python
print(f"下一天是第{day + 1}天")
```

## 常见格式化

保留两位小数：

```python
score = 0.875
print(f"得分：{score:.2f}")
```

输出：

```text
得分：0.88
```

对齐宽度在命令行表格里偶尔有用：

```python
name = "read"
status = "done"
print(f"{name:<10} {status}")
```

学习阶段不需要记很多格式细节；先熟练掌握变量插入和小数位控制就够用。

## 常见误解

- 忘记字符串前面的 `f` 时，`"{age}"` 会原样输出，不会替换变量。
- `{}` 里写的是 Python 表达式，不是随便的说明文字。
- f-string 适合生成人类可读文本，不适合手写 JSON；生成 JSON 应该用 `json.dumps()`。
- 如果字符串里真的要显示 `{` 或 `}`，需要写成 `{{` 或 `}}`。

## 在学习项目里的用法

`make_plan(goal, days)` 这类函数经常用 f-string 生成列表内容：

```python
def make_plan(goal, days):
    plan = []
    for i in range(days):
        plan.append(f"第{i + 1}天：学习 {goal}")
    return plan
```

这里 f-string 只负责生成每一天的文本；函数是否直接打印，仍由 `return` / `print()` 的职责边界决定。

## 相关

- [[变量(Variables)]]
- [[基础数据类型(Data Types)]]
- [[输入与输出(input & print)]]
- [[函数与参数(Functions)]]
- [[文件读写与 JSON 序列化]]

## 来源 / 证据

- [[../../raw/articles/python-3-official-documentation|Python 3 Official Documentation]]
- [[../../03-Courses/Python/AI-Agent-Learning/stage0-python-basics|阶段 0：Python 与开发环境]]
- [[../../04-Projects/Python/AI-Agent-Learning/p0-05-plan-functions|P0-05 函数计划脚本]]
- [[../../07-Reviews/Daily-Practice/2026-06-05-review|2026-06-05 每日练习批改]]
