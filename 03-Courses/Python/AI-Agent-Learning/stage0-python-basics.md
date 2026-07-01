---
type: course-note
topic: AI-Agent-Learning Stage 0
status: active
created: 2026-05-28
updated: 2026-06-14
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
| P0-05 | 函数、参数、返回值 | PASS | [[../../../04-Projects/Python/AI-Agent-Learning/p0-05-plan-functions]] | 能用函数参数接收输入，用 `return` 交回结果，并在 `main()` 中调用函数 |
| P0-06 | 模块、第三方包、venv | PASS | [[../../../04-Projects/Python/AI-Agent-Learning/p0-06-env-check]] | 能用 `.venv` 隔离依赖，安装第三方包，并用 `.env` 读取本地配置 |
| P0-07 | 异常、调试、单元测试 | PASS | [[../../../04-Projects/Python/AI-Agent-Learning/p0-07-safe-divide]] | 能用 `try/except` 处理除零和非数字输入，并用样例覆盖正常与异常场景 |
| P0-08 | 文件、JSON、CSV | PASS | [[../../../04-Projects/Python/AI-Agent-Learning/p0-08-progress-file]] | 能读任务文本、写入 JSON，并确认 JSON 可被 Python 重新解析 |
| P0-09 | HTTP 请求 | PASS | [[../../../04-Projects/Python/AI-Agent-Learning/p0-09-http-request]] | 能用 `requests` 请求公开 API，理解 URL、headers、status code、JSON 和 timeout |
| P0-Gate | Python 基础闯关 | PASS | [[../../../04-Projects/Python/AI-Agent-Learning/p0-gate-learning-log]] | 能做最小学习日志 CLI：输入记录、保存 JSON、查看最近 7 条并处理异常输入 |

## 已掌握概念

- [[../../../02-Concepts/Python/解释器(Interpreter)]]
- [[../../../02-Concepts/Python/输入与输出(input & print)]]
- [[../../../02-Concepts/Python/变量(Variables)]]
- [[../../../02-Concepts/Python/基础数据类型(Data Types)]]
- [[../../../02-Concepts/Python/类型转换(Type Conversion)]]
- [[../../../02-Concepts/Python/f-string 格式化]]
- [[../../../02-Concepts/Python/函数与参数(Functions)]]
- [[../../../02-Concepts/Python/list·dict·set 容器]]
- [[../../../02-Concepts/Python/环境管理(venv & pip)]]
- [[../../../02-Concepts/Python/异常·调试·测试(Exceptions)]]
- [[../../../02-Concepts/Python/文件读写与 JSON 序列化]]
- [[../../../02-Concepts/Python/HTTP 请求(requests)]]
- [[../../../02-Concepts/Python/JSON 学习日志 CLI]]

## 下一步

阶段 0 主线已完成，下一项是阶段 1 的 `L1-02 单轮问答`。

阶段 1 当前入口：

- [[../../../03-Courses/LLM/AI-Agent-Learning/stage1-llm-api-basics|阶段 1：大模型 API 入门]]

## 和工程基础的关系

阶段 0 完成后，不再要求先整块学完 Linux、网络、数据库、Docker 才进入 AI/Agent。新的执行规则是：

- `P0-07` 到 `P0-Gate` 已补齐 Python 的最小开发能力。
- `P0-Gate` 已通过，当前已进入 L1：大模型 API 入门。
- 工程基础放到后续任务里按需补：API 调用时补 HTTP，Memory/RAG 时补数据库，本地多服务或部署时补 Docker。

关联路线：[[../../Agent/AI-Agent-Learning/stage0_5-engineering-basics|阶段 0.5：工程基础随用随补]]

## 注意

递归属于函数进阶内容。P0-05 已经通过，但当前阶段仍然只需要知道“函数可以调用自己”，不需要深入递归算法。
