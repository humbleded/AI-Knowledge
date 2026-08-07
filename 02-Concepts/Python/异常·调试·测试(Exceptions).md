---
aliases:
  - python-exceptions-debugging-testing
type: concept
topic: Python exceptions debugging testing
status: usable
created: 2026-06-11
updated: 2026-08-07
tags:
  - Python
  - 异常处理
  - 调试
  - 单元测试
---

# Python 异常、调试与单元测试

## 核心结论

异常处理、调试和测试解决的是同一个问题的不同阶段：

- 异常处理：程序遇到可预期错误时，不直接崩溃，而是给出可理解的处理结果。
- 调试：程序行为不符合预期时，定位变量、分支和执行路径哪里出了问题。
- 单元测试：把正常场景和异常场景写成可重复运行的检查，防止以后改代码时破坏已有行为。

## `try/except` 捕获什么

`try/except` 捕获的是 `try` 块运行过程中抛出的异常对象。

例如字符串转数字时：

```python
try:
    value = float(text)
except ValueError:
    return "错误：请输入数字。"
```

这里不是“预测所有错误”，而是明确知道 `float(text)` 可能因为非法输入抛出 `ValueError`，所以只处理这个异常。

## 不要吞掉所有异常

不要随手写：

```python
try:
    ...
except Exception:
    pass
```

这样会把真正的 bug 也藏起来。更好的方式是：

- 只捕获你知道如何处理的异常。
- 给用户或调用方返回清楚的错误信息。
- 对无法处理的异常保留错误，让它暴露出来，方便修复。

## 单元测试的价值

单元测试优先检查“核心逻辑函数”，而不是只检查命令行输入输出。

例如 `safe_divide(a_text, b_text)` 至少应该覆盖：

```python
assert safe_divide("10", "2") == 5.0
assert safe_divide("10", "0") == "错误：除数不能为 0。"
assert safe_divide("abc", "2") == "错误：请输入数字。"
```

这样以后即使重写交互层，核心逻辑仍然可以快速验证。

## 断言必须调用交付接口，避免“假绿灯”

测试通过只证明“断言实际调用的代码”通过，不会自动证明题目或调用方要求的函数已经实现。

例如交付接口是 `is_anagram()`，但断言全部调用另建的 `is_anagram_dict()`；即使脚本显示 `All tests passed.`，空函数 `is_anagram()` 仍会隐式返回 `None`。这属于假绿灯：测试是绿色，但真正的交付路径没有被覆盖。

最低检查顺序：

1. 所有核心断言直接调用规定的函数名和参数合同。
2. 检查返回值，也检查返回类型，例如要求布尔值时验证 `is True` / `is False`。
3. 加入最容易混淆语义的反例，而不只覆盖普通成功案例。例如字母异位词要覆盖“字符种类相同但次数不同”和“长度不同”。
4. 再用隐藏、性质或大规模测试补覆盖；这些补充测试不能替代交付文件中长期保留的关键断言。

## 断言还必须处于可达位置并真正运行

测试代码“写在文件里”不等于它执行过。下面的断言位于函数内部，并排在无条件 `return` 之后，因此调用函数时永远走不到：

```python
def solve(...):
    ...
    return result
    assert solve(...) == expected  # 不可达
```

应把测试放到函数外，并保持合法的顶层缩进；也可以放入 `if __name__ == "__main__":` 入口：

```python
def solve(...):
    ...
    return result


if __name__ == "__main__":
    assert solve(...) == expected
    print("All test cases passed.")
```

三个证据要分开看：

1. `py_compile` 能发现 `IndentationError` 等语法/缩进错误。
2. 编译成功不能发现“断言在 `return` 后不可达”这类执行路径问题。
3. 必须真实运行测试入口，并检查退出码和决定性输出；只有实际执行过的断言才能成为测试证据。

## P0-07 练习模式

在 `P0-07` 中，稳定做法是：

1. 把核心逻辑写成函数，例如 `safe_divide()`。
2. 在函数内部处理明确的异常，例如 `ValueError` 和 `ZeroDivisionError`。
3. 用样例覆盖正常输入和异常输入。
4. 交互入口 `main()` 只负责 `input()` 和 `print()`，不要把所有逻辑都堆在输入输出里。

## 相关链接

- [[函数与参数(Functions)|Python 函数、参数与 return]]
- [[环境管理(venv & pip)|Python 项目环境管理：venv、pip 与 .env]]
- [[../../03-Courses/Python/AI-Agent-Learning/stage0-python-basics|阶段 0：Python 与开发环境]]
- [[../../04-Projects/Python/AI-Agent-Learning/p0-07-safe-divide|P0-07 异常、调试、单元测试]]
- [[../../04-Projects/Python/AI-Agent-Learning/w4-03-valid-anagram|W4-03 有效的字母异位词项目记录]]
- [[../../04-Projects/Python/AI-Agent-Learning/w4-01-two-sum|W4-01 两数之和项目记录]]
