---
type: course
topic: Python
status: active
created: 2026-06-04
updated: 2026-06-04
aliases:
  - Python 官方手册核心阅读路线
tags:
  - Python
  - 课程笔记
  - 编程基础
---

# Python 官方手册核心阅读路线

这不是完整手册摘抄，而是用 Python 官方文档做校准源的阅读路线。

## 第一阶段：能写小脚本

- [Tutorial - An Informal Introduction to Python](https://docs.python.org/3/tutorial/introduction.html)
- [Tutorial - Control Flow Tools](https://docs.python.org/3/tutorial/controlflow.html)
- [Tutorial - Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
- [Tutorial - Modules](https://docs.python.org/3/tutorial/modules.html)

对应概念卡：

- [[../../../02-Concepts/Python/python-interpreter|Python Interpreter]]
- [[../../../02-Concepts/Python/python-input-print|Python input() 与 print()]]
- [[../../../02-Concepts/Python/python-basic-data-types|Python 基础数据类型]]
- [[../../../02-Concepts/Python/python-conditionals-and-loops|Python 条件判断与循环]]
- [[../../../02-Concepts/Python/python-list-dict-set|Python list、dict、set]]

## 第二阶段：能写可维护程序

- [Tutorial - Input and Output](https://docs.python.org/3/tutorial/inputoutput.html)
- [Tutorial - Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
- [Tutorial - Classes](https://docs.python.org/3/tutorial/classes.html)
- [Tutorial - Brief Tour of the Standard Library](https://docs.python.org/3/tutorial/stdlib.html)

建议产出：

- 一个带参数、异常处理和文件读写的小 CLI。
- 一张 `try/except/else/finally` 概念卡。
- 一张 `class` 和实例状态的概念卡。

## 第三阶段：服务 Agent 工程

- [venv](https://docs.python.org/3/library/venv.html)
- [argparse](https://docs.python.org/3/library/argparse.html)
- [json](https://docs.python.org/3/library/json.html)
- [pathlib](https://docs.python.org/3/library/pathlib.html)
- [logging](https://docs.python.org/3/library/logging.html)
- [asyncio](https://docs.python.org/3/library/asyncio.html)
- [typing](https://docs.python.org/3/library/typing.html)

建议产出：

- 一个可运行的命令行工具。
- 一个读取配置、调用 HTTP API、输出 JSON 的小程序。
- 一张 `asyncio` 最小心智模型卡。

## 查阅规则

- 语法不确定时查 Language reference。
- 标准库行为不确定时查 Library reference。
- 版本差异或弃用项查 What's New 和 Deprecations。
- 工程实践优先查 HOWTOs、Packaging、Typing。

## 相关

- [[../../../01-Maps/Python/python-official-docs-map|Python Official Docs Map]]
- [[../../../02-Concepts/Python/README|Python 概念卡]]
- [[../AI-Agent-Learning/stage0-python-basics|AI-Agent-Learning 阶段 0：Python 与开发环境]]
- [[../../../raw/articles/python-3-official-documentation|Python official raw source]]
