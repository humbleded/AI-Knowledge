---
aliases:
  - python-basic-data-types
type: concept
topic: Python
status: usable
created: 2026-05-28
updated: 2026-09-20
tags:
  - Python
  - 编程基础
---

# Python 基础数据类型

## 中文速读

- Data type（数据类型）决定一个值能做什么操作。
- 初学阶段先抓住 `str`、`int`、`float`、`bool` 四类：文本、整数、小数、真假。
- 选类型不要只看输入长什么样，要看后面要怎么用：显示、计算、比较，还是表示状态。

阶段 0 先掌握四种基础类型：

| 类型 | 适合表示 | 示例 |
|---|---|---|
| `str` | 文本 | 姓名、学习目标 |
| `int` | 整数 | 年龄、次数、天数 |
| `float` | 小数 | 每天学习 1.5 小时 |
| `bool` | 真或假 | 是否完成、是否通过 |

## 选择类型的关键

不要只看用户输入长什么样，要看这个值后面要怎么用。

- 要显示文字：用 `str`
- 要做整数计算：用 `int`
- 要保留小数：用 `float`
- 要表达真假状态：用 `bool`

## 最小例子

```python
name = "Ada"          # str
days = 7              # int
hours = 1.5           # float
is_done = False       # bool
```

可以用 `type()` 临时检查值的类型：

```python
print(type(days))     # <class 'int'>
```

`type()` 适合学习和调试，不适合把程序写成到处判断类型。正式代码更常见的是在输入边界先转换和校验，让内部数据保持稳定。

## 和容器的关系

`list`、`dict`、`set` 不是这张卡的主角，但它们会装着这些基础值：

```python
tasks = ["read", "code"]                    # list[str]
task_status = {"read": "done"}              # dict[str, str]
tags = {"Python", "Agent"}                  # set[str]
```

这也是后面做工具注册表、学习日志和 RAG 索引时的基础。

## 常见误解

- `input()` 得到的 `"20"` 是 `str`，不是 `int`。
- `"20" + "1"` 得到 `"201"`，不是 `21`。
- `bool("False")` 是 `True`，因为非空字符串在 truthiness（真值判断）里会被看成真。
- `float` 适合普通小数，但不适合精确金额计算；需要金额精算时要用专门方案。
- 类型转换失败通常会抛 `ValueError`，要用 `try/except` 处理不合法输入。

## 相关

- [[类型转换(Type Conversion)]]
- [[变量(Variables)]]
- [[真值判断与严格布尔校验(Truthiness)]]
- [[list·dict·set 容器]]
- [[JSON 学习日志 CLI]]

## 来源 / 证据

- [[../../raw/articles/python-3-official-documentation|Python 3 Official Documentation]]
- [[../../03-Courses/Python/AI-Agent-Learning/stage0-python-basics|阶段 0：Python 与开发环境]]
- [[../../04-Projects/Python/AI-Agent-Learning/p0-02-profile-script|P0-02 个人资料脚本]]
- [[../../04-Projects/Python/AI-Agent-Learning/p0-gate-learning-log|P0-Gate 学习日志 CLI]]
