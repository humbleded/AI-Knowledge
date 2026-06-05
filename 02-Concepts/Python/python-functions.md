---
type: concept
topic: Python functions
status: usable
created: 2026-06-05
updated: 2026-06-06
tags:
  - Python
  - 函数
  - AI-Agent-Learning
---

# Python 函数、参数与 return

函数把一段可复用逻辑封装起来。学习阶段先抓住三件事：

- 输入：函数参数，例如 `goal`、`days`、`answer`。
- 处理：函数内部的循环、判断、拼接、计算。
- 输出：用 `return` 把结果交给调用者。

## return 和 print 的区别

`print()` 只是把内容显示到屏幕上，适合给人看。

`return` 会把函数结果交给调用者，适合被变量保存、被测试代码比较、被后续逻辑继续使用。

```python
def build_message(name):
    return f"你好，{name}"


result = build_message("Codex")
print(result)
```

这里 `result = build_message("Codex")` 保存函数返回值，`print(result)` 只是显示它。

## 最小例子

```python
def make_plan(goal, days):
    plan = []
    for i in range(days):
        plan.append(f"第{i + 1}天：学习 {goal}")
    return plan
```

调用 `make_plan("练习函数", 3)` 会返回：

```python
[
    "第1天：学习 练习函数",
    "第2天：学习 练习函数",
    "第3天：学习 练习函数",
]
```

注意 `return plan` 要和 `for` 对齐。如果它缩进到循环内部，函数会在第 1 次循环时提前返回，只得到第 1 条计划。

## 可测试函数检查清单

写函数时先让核心逻辑返回值，再由主程序决定是否打印。这样可以做四类最小检查：

- 返回类型是否正确，例如 `isinstance(result, list)`。
- 返回长度是否正确，例如 `len(result) == 3`。
- 关键字符串是否精确匹配，例如 `"第1天：学习 练习函数"`。
- 函数内部是否没有直接 `print()`，必要时用 `redirect_stdout` 捕获输出。

```python
from contextlib import redirect_stdout
from io import StringIO

buf = StringIO()

with redirect_stdout(buf):
    result = make_plan("练习函数", 3)

assert isinstance(result, list)
assert len(result) == 3
assert result[0] == "第1天：学习 练习函数"
assert buf.getvalue() == ""
```

写 Python 代码块时，缩进优先用 4 个普通空格。不要从富文本里复制不间断空格 `U+00A0`，否则代码可能报 `SyntaxError: invalid non-printable character`。

## 根据回答打分

`answer` 是用户写出的回答文本，不是标准答案。可以用字符串长度和关键词做一个最小评分函数：

```python
def score_answer(answer):
    if len(answer) < 10:
        return "retry"
    if "结果" in answer and "调用者" in answer:
        return "good"
    return "pass"
```

这种函数返回评分标签，方便测试代码直接比较返回值，而不是捕获屏幕输出。

## 为什么拆成函数

把“生成计划”“评分答案”“打印报告”等逻辑拆成小函数，有三个直接好处：

- 复用：别的主程序可以直接调用同一段逻辑。
- 测试：测试代码可以比较返回值，例如 `make_plan("练习函数", 3) == expected`。
- 修改：以后计划格式变化时，主要改 `make_plan()`，不用到处找重复代码。

## 关联

- [[python-input-print]]
- [[python-f-string]]
- [[python-conditionals-and-loops]]
- [[python-list-dict-set]]
- [[../../07-Reviews/Daily-Practice/2026-06-04-review]]
- [[../../07-Reviews/Daily-Practice/2026-06-05-review]]
