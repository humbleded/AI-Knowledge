---
type: course-note
topic: AI-Agent-Learning Stage 3
status: active
created: 2026-07-06
updated: 2026-07-06
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
| T3-03 | 文件工具 | TODO | `code/stage3/t3_03_file_reader_tool.py` | 下一步：限制只能读取 `resources/sandbox/` |

## 已掌握概念

- [[../../../02-Concepts/LLM/函数调用(Function Calling)|函数调用 / Tool Calling]]
- [[../../../02-Concepts/Agent/工具定义与执行协议(Tool Definition)|工具定义与执行协议]]

## 下一步

`T3-03 文件工具`：

- 工具读取文件。
- 限制只能访问沙箱目录。
- 对长文件做截断或摘要。
- 对敏感路径返回稳定错误。

