---
type: course-stage
topic: AI-Agent-Learning Stage 4
status: active
created: 2026-07-10
updated: 2026-07-10
tags:
  - Agent
  - AI-Agent-Learning
  - Stage4
---

# 阶段 4：Agent 基础原理

## 定位

阶段 4 目标是理解 ReAct、Planning、Reflection，并写出最小 Agent。

当前阶段 3 的 T3-Gate 尚未完成，因此阶段 4 先做工作日概念预习；动手交付和 A4-Gate 等 T3-Gate 通过后继续。

## 任务状态

| 任务 | 状态 | 日期 | 产物 | 备注 |
|---|---|---|---|---|
| A4-01 什么是 Agent | PASS | 2026-07-09 | `notes/stage4/a4_01_what_is_agent.md` | 能定义 Agent，区分 Agent vs Chatbot，说明 Tool/Action/Observation/Final Answer 和代码硬校验 |
| A4-02 LLM 与 Agent 基础 | TODO |  |  | 下一项概念预习 |
| A4-03 ReAct | TODO |  |  |  |
| A4-04 Plan-and-Solve | TODO |  |  |  |
| A4-05 Reflection | TODO |  |  |  |
| A4-Gate 最小 Agent 闯关 | TODO |  |  |  |

## A4-01 已沉淀概念

- [[../../../02-Concepts/Agent/智能体(Agent)|智能体(Agent)]]
- [[../../../02-Concepts/Agent/工具调用与动作(Tool Calling and Action)|工具调用与动作]]
- [[../../../02-Concepts/Agent/工具定义与执行协议(Tool Definition)|工具定义与执行协议]]

## 当前易错点

- 格式像 Observation，不代表它是真 Observation；要看代码有没有真实执行工具。
- Action JSON 要严格可解析，不能有弯引号、未加引号的字符串值、尾逗号。
- Observation 是工具结果的反馈消息，不是执行者。

## 相关执行区

- [A4-01 daily](file:///C:/Users/26823/Desktop/AI-Agent-Learning/daily/2026-07-09.md)
- [A4-01 notes](file:///C:/Users/26823/Desktop/AI-Agent-Learning/notes/stage4/a4_01_what_is_agent.md)
- [progress](file:///C:/Users/26823/Desktop/AI-Agent-Learning/tracker/progress.md)
