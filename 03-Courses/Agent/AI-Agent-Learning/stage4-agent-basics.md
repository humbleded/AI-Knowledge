---
type: course-stage
topic: AI-Agent-Learning Stage 4
status: active
created: 2026-07-10
updated: 2026-07-22
tags:
  - Agent
  - AI-Agent-Learning
  - Stage4
---

# 阶段 4：Agent 基础原理

## 定位

阶段 4 目标是理解 ReAct、Planning、Reflection，并写出最小 Agent。

阶段 3 的 T3-Gate 已通过。阶段 4 当前已完成 Agent 定义、LLM/Agent 基础和 A4-03 ReAct；下一步进入 A4-04 Plan-and-Solve。

## 任务状态

| 任务 | 状态 | 日期 | 产物 | 备注 |
|---|---|---|---|---|
| A4-01 什么是 Agent | PASS | 2026-07-09 | `notes/stage4/a4_01_what_is_agent.md` | 能定义 Agent，区分 Agent vs Chatbot，说明 Tool/Action/Observation/Final Answer 和代码硬校验 |
| A4-02 LLM 与 Agent 基础 | PASS | 2026-07-15 | `notes/stage4/a4_02_llm_agent_basics.md` | LLM/Token/架构、Chat Template、无状态、工具职责与幻觉防线均通过 |
| A4-03 ReAct | PASS | 2026-07-22 | `code/stage4/a4_03_react_agent.py` | 完整两轮轨迹与 max_steps 通过；15/15 parser/prompt/loop 边界断言通过 |
| A4-04 Plan-and-Solve | TODO |  |  |  |
| A4-05 Reflection | TODO |  |  |  |
| A4-Gate 最小 Agent 闯关 | TODO |  |  |  |

## A4-01 已沉淀概念

- [[../../../02-Concepts/Agent/智能体(Agent)|智能体(Agent)]]
- [[../../../02-Concepts/Agent/工具调用与动作(Tool Calling and Action)|工具调用与动作]]
- [[../../../02-Concepts/Agent/工具定义与执行协议(Tool Definition)|工具定义与执行协议]]

## A4-02 已沉淀概念

- [[../../../02-Concepts/LLM/LLM 本质与幻觉(Hallucination)|LLM 本质与幻觉]]
- [[../../../02-Concepts/LLM/特殊Token(Special Tokens)|特殊 Token 与 Chat Template]]
- [[../../../02-Concepts/LLM/提示工程基础(Prompt Engineering)|Instruction Data / Tuning / Prompting 与 Few-shot]]
- [[../../../02-Concepts/LLM/多轮对话与无状态记忆(Stateless Memory)|多轮对话与无状态记忆]]
- [[../../../02-Concepts/Agent/工具调用与动作(Tool Calling and Action)|工具调用与动作]]

## A4-03 已沉淀概念与实践

- [[../../../02-Concepts/Agent/ReAct推理与行动循环(ReAct)|ReAct 推理与行动循环]]
- [[../../../02-Concepts/Agent/工具定义与执行协议(Tool Definition)|工具定义与执行协议]]
- [[../../../04-Projects/Agent/AI-Agent-Learning/a4-03-react-agent|A4-03 ReAct Agent 代码实践]]
- [[../../../07-Reviews/AI-Agent-Learning/2026-07-22-a4-03-react-review|A4-03 PASS 复盘]]

## 当前易错点

- 格式像 Observation，不代表它是真 Observation；要看代码有没有真实执行工具。
- Action JSON 要严格可解析，不能有弯引号、未加引号的字符串值、尾逗号。
- Observation 是工具结果的反馈消息，不是执行者。
- 微调效果写入新模型权重；后续请求必须调用该模型。Few-shot 只在当前上下文有效。
- 工具返回失败或超时时，模型自然语言不能覆盖权威结果；未知状态必须保持未知。
- Prompt 对文本协议只是软约束；parser/validator、非空 Finish 与 max_steps 才是客户端硬边界。
- 确定性 fake LLM 只能证明客户端代码路径，不能外推真实模型的格式遵守和工具选择质量。

## 相关执行区

- [A4-01 daily](file:///C:/Users/26823/Desktop/AI-Agent-Learning/daily/2026-07-09.md)
- [A4-01 notes](file:///C:/Users/26823/Desktop/AI-Agent-Learning/notes/stage4/a4_01_what_is_agent.md)
- [A4-02 daily（带读与迁移）](file:///C:/Users/26823/Desktop/AI-Agent-Learning/daily/2026-07-14.md)
- [A4-02 daily（正式练习与复核）](file:///C:/Users/26823/Desktop/AI-Agent-Learning/daily/2026-07-15.md)
- [A4-02 notes](file:///C:/Users/26823/Desktop/AI-Agent-Learning/notes/stage4/a4_02_llm_agent_basics.md)
- [A4-03 daily（带读、代码与正式练习）](file:///C:/Users/26823/Desktop/AI-Agent-Learning/daily/2026-07-21.md)
- [A4-03 daily（迁移复测与正式复核）](file:///C:/Users/26823/Desktop/AI-Agent-Learning/daily/2026-07-22.md)
- [A4-03 code](file:///C:/Users/26823/Desktop/AI-Agent-Learning/code/stage4/a4_03_react_agent.py)
- [progress](file:///C:/Users/26823/Desktop/AI-Agent-Learning/tracker/progress.md)
