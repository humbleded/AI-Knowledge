---
type: course-note
topic: AI-Agent-Learning Stage 3
status: active
created: 2026-07-06
updated: 2026-07-08
tags:
  - Agent
  - Tool-Calling
  - AI-Agent-Learning
  - Stage3
---

# 阶段 3：Tool Calling / Function Calling

## 阶段目标

让模型选择工具、生成参数，由客户端程序真实执行工具，并把 Observation 放回上下文。

## 当前进度

| 编号 | 任务 | 状态 | 产物 | 关键结论 |
|---|---|---|---|---|
| T3-01 | 函数调用概念 | **PASS** (2026-07-01) | [[../../../02-Concepts/LLM/函数调用(Function Calling)]] | 模型不执行工具，只生成 Action；解析、执行、Observation 回填都在客户端程序 |
| T3-02 | 计算器工具 | **PASS** (2026-07-06) | [[../../../04-Projects/Agent/AI-Agent-Learning/t3-02-calculator-tool]] | 完成工具 schema、参数校验、真实计算、稳定错误返回；7 组测试全 PASS |
| T3-03 | 文件工具 | **PASS** (2026-07-07) | [[../../../04-Projects/Agent/AI-Agent-Learning/t3-03-file-reader-tool]] | 完成沙箱限制、路径归一化校验、长文件截断、稳定错误返回；覆盖 `..` 逃逸与目录误读 |
| T3-04 | 外部 API 工具 | **PASS** (2026-07-08) | [[../../../04-Projects/Agent/AI-Agent-Learning/t3-04-public-api-tool]] | 完成公开 API 请求、`timeout`、必要字段摘要、Timeout/RequestException 稳定错误返回 |

## 已掌握概念

- [[../../../02-Concepts/LLM/函数调用(Function Calling)|函数调用 / Tool Calling]]
- [[../../../02-Concepts/Agent/工具定义与执行协议(Tool Definition)|工具定义与执行协议]]
- [[../../../02-Concepts/Agent/文件工具沙箱(File Tool Sandbox)|文件工具沙箱]]
- [[../../../02-Concepts/Agent/外部 API 工具(External API Tool)|外部 API 工具]]

## 下一步

`T3-Gate Tool Calling 闯关`：

- 注册计算器、读文件、外部 API 三个工具。
- 设计工具注册表与客户端分发流程。
- 准备正常、失败和危险输入评估用例。
- 把工具结果作为 Observation 回填给模型。
