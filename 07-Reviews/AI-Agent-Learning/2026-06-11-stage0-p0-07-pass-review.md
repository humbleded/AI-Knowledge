---
type: review
topic: AI-Agent-Learning P0-07
status: pass
created: 2026-06-11
updated: 2026-06-11
tags:
  - AI-Agent-Learning
  - Python
  - Stage0
  - P0-07
---

# 2026-06-11 阶段 0 复盘：P0-07

## 判定

`P0-07 异常、调试、单元测试`：PASS。

## 验证摘要

- `code/stage0/p0_07_safe_divide.py` 通过 `py_compile`。
- `safe_divide()` 能处理正常输入、除零、非数字输入、浮点数字符串和空字符串。
- 入口脚本通过干净标准输入验证，正常、除零、非数字场景均返回码 `0`。
- P0-07 问答能说明异常捕获、不吞异常和单元测试价值。

## 当天卡点

当天未完全理解：

- 装饰器 `@log` 的语法糖关系。
- `functools.partial()` 和普通默认参数的区别。
- MixIn 与主继承链的区别。

这些属于拓展补救点，不影响 P0-07 通过。

## 稳定结论

- `try/except` 捕获的是运行时抛出的异常对象。
- 不要用空的 `except Exception: pass` 吞掉所有错误。
- 单元测试应优先覆盖核心逻辑函数，而不是只测试交互输入输出。
- 本阶段下一项是 `P0-08 文件、JSON、CSV`。

## 同步内容

- 概念卡：[[../../02-Concepts/Python/异常·调试·测试(Exceptions)|Python 异常、调试与单元测试]]
- 项目记录：[[../../04-Projects/Python/AI-Agent-Learning/p0-07-safe-divide|P0-07 异常、调试、单元测试]]
- 阶段页：[[../../03-Courses/Python/AI-Agent-Learning/stage0-python-basics|阶段 0：Python 与开发环境]]
