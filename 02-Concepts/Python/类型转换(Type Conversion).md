---
aliases:
  - python-type-conversion
type: concept
topic: Python
status: usable
created: 2026-05-28
updated: 2026-09-20
tags:
  - Python
  - 编程基础
---

# Python 类型转换

## 中文速读

- Type conversion（类型转换）就是把值从一种类型变成另一种类型，例如把 `"20"` 变成 `20`。
- 它最常出现在 `input()`、文件读取、JSON 读取和 API 返回之后，因为外部进来的数据经常先是字符串或松散结构。
- `bool()` 最容易误用：`bool("False")` 是 `True`，所以用户输入的真假值要按具体文本判断。

类型转换是把一个值从一种类型变成另一种类型。

`input()` 默认返回字符串，所以如果要把输入当作数字使用，需要显式转换：

```python
age = int(input("请输入年龄："))
minutes = float(input("请输入每日学习分钟数："))
```

## 常见转换

| 写法 | 作用 | 例子 |
|---|---|---|
| `int(value)` | 转成整数 | `int("20")` 得到 `20` |
| `float(value)` | 转成小数 | `float("1.5")` 得到 `1.5` |
| `str(value)` | 转成字符串 | `str(20)` 得到 `"20"` |
| `bool(value)` | 按 truthiness 转成真假 | `bool("")` 得到 `False` |

转换不是“猜意思”。例如：

```python
int("20")      # 可以
int("20.5")    # ValueError
int("abc")     # ValueError
```

处理用户输入时，可以先清理两边空白：

```python
days_text = input("请输入天数：").strip()
days = int(days_text)
```

## bool(input(...)) 的坑

不要直接用 `bool(input(...))` 判断用户输入的真假。

原因是：非空字符串都会被 `bool()` 转成 `True`，即使用户输入的是 `"False"`。

更稳妥的写法是判断具体文本：

```python
answer = input("是否完成？")
is_done = answer.lower() in ["true", "yes", "1", "y"]
```

更稳的写法通常会先规范化文本：

```python
answer = input("是否完成？").strip().lower()
is_done = answer in ["true", "yes", "1", "y"]
```

如果只允许固定答案，还要处理非法输入：

```python
if answer not in ["true", "false", "yes", "no", "1", "0", "y", "n"]:
    print("请输入 yes/no 或 true/false")
```

## 和异常处理的关系

外部输入不可靠，类型转换很容易失败。学习阶段可以先看到报错；正式脚本里要在输入边界处理：

```python
try:
    days = int(input("请输入天数：").strip())
except ValueError:
    print("天数必须是整数")
```

后续写 Agent 工具时也一样：工具参数在真正执行前要校验，不能假设模型或用户一定给了正确类型。

## 常见误解

- `str(20)` 只是把数字变成文本，不能保留“数字可计算”的能力。
- `int(1.9)` 会得到 `1`，不是四舍五入。
- `bool("0")` 也是 `True`，因为 `"0"` 是非空字符串。
- 转换应该放在输入边界；程序内部最好尽量保持同一个字段类型稳定。

## 相关

- [[输入与输出(input & print)]]
- [[基础数据类型(Data Types)]]
- [[真值判断与严格布尔校验(Truthiness)]]
- [[异常·调试·测试(Exceptions)]]
- [[strip() 与数据清洗]]

## 来源 / 证据

- [[../../raw/articles/python-3-official-documentation|Python 3 Official Documentation]]
- [[../../03-Courses/Python/AI-Agent-Learning/stage0-python-basics|阶段 0：Python 与开发环境]]
- [[../../04-Projects/Python/AI-Agent-Learning/p0-02-profile-script|P0-02 个人资料脚本]]
- [[../../04-Projects/Python/AI-Agent-Learning/p0-gate-learning-log|P0-Gate 学习日志 CLI]]
