---
type: concept
topic: Python functions
status: seed
created: 2026-06-05
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
