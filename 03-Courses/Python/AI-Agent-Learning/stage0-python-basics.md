---
type: course-note
topic: AI-Agent-Learning Stage 0
status: active
created: 2026-05-28
tags:
  - Python
  - AI-Agent
  - Stage0
---

# 阶段 0：Python 与开发环境

## 阶段目标

阶段 0 的目标是打好 Python 基础：能写基础脚本，能理解输入、输出、变量、数据类型、条件判断、循环、函数、文件、异常、包管理和 HTTP 请求。

这不是为了“学完 Python 全部语法”，而是为了后面能写 Agent、调用 API、处理文件、接工具、做自动化。

## 当前通过项

| 编号 | 任务 | 状态 | 产物 | 关键结论 |
|---|---|---|---|---|
| P0-01 | 环境与第一个程序 | PASS | [[../../../04-Projects/Python/AI-Agent-Learning/p0-01-hello-script]] | 能运行 `.py` 文件，理解 `input()` / `print()` |
| P0-02 | 数据类型与变量 | PASS | [[../../../04-Projects/Python/AI-Agent-Learning/p0-02-profile-script]] | 能使用 `str`、`int`、`float`、`bool` |
| P0-03 | 条件判断、模式匹配、循环 | PASS | [[../../../04-Projects/Python/AI-Agent-Learning/p0-03-scheduler]] | 能使用分支判断和固定次数循环 |
| P0-04 | list、tuple、dict、set | PASS | [[../../../04-Projects/Python/AI-Agent-Learning/p0-04-tasks]] | 能用 list/dict/set 管理任务、状态和去重 |

## 已掌握概念

- [[../../../02-Concepts/Python/python-interpreter]]
- [[../../../02-Concepts/Python/python-input-print]]
- [[../../../02-Concepts/Python/python-variables]]
- [[../../../02-Concepts/Python/python-basic-data-types]]
- [[../../../02-Concepts/Python/python-type-conversion]]
- [[../../../02-Concepts/Python/python-f-string]]
- [[../../../02-Concepts/Python/python-list-dict-set]]

## 下一步

下一项是 P0-05：函数、参数、返回值。

要做的代码是：

- `code/stage0/p0_05_plan_functions.py`

要能回答：

- 为什么要把代码封装成函数？
- `return` 和 `print` 有什么区别？
- 如何判断一个函数是否职责过多？

## 注意

递归属于函数进阶内容。当前阶段只需要知道“函数可以调用自己”，等学到 P0-05 函数、参数、返回值之后再回头深入。
