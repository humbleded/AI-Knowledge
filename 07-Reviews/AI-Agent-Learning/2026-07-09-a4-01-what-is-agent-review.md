---
type: review
topic: AI-Agent-Learning A4-01
status: pass
created: 2026-07-10
updated: 2026-07-10
tags:
  - AI-Agent-Learning
  - Agent
  - PASS
---

# 2026-07-09 A4-01 什么是 Agent PASS 复盘

## 判定

**A4-01 PASS**。

本日是工作日概念预习，T3-Gate 仍留周末闯关。A4-01 的通过标准是“不把所有 LLM 应用都叫 Agent”。练习结果显示，已经能定义 Agent，区分 Agent vs Chatbot，说明 Tool Calling 与多步 Agent 的边界，并能把 Tool / Action / Observation / Final Answer 放回工程链路。

## 验证依据

- 阅读资料：
  - `repos/agents-course/units/zh-CN/unit1/what-are-agents.md`
  - `repos/agents-course/units/zh-CN/unit1/agent-steps-and-structure.mdx`
- 执行区产物：
  - `daily/2026-07-09.md`
  - `notes/stage4/a4_01_what_is_agent.md`

A4-01 是概念任务，无需运行代码。复核重点为问答是否覆盖 tracker 要求的三点：

1. Agent 和 chatbot 的关键区别。
2. 环境、动作、观察分别是什么意思。
3. 什么任务没必要用 Agent。

## 已掌握

- Agent 是为了完成目标，使用模型推理/计划，通过工具行动并接收 Observation 的系统。
- Chatbot 偏文本问答；Agent 偏围绕目标选择工具、执行动作、读取 Observation 后继续推进。
- Tool Calling 不等于多步 Agent；多步 Agent 还需要把 Observation 回填后继续判断目标是否完成。
- 稳定概念不必用工具；当前外部状态、私有数据、精确计算或真实副作用需要工具。
- LLM 适合做语义判断，可靠性边界要靠代码硬校验兜住。

## 订正闭环

| 点 | 初始问题 | 订正结果 |
|---|---|---|
| Action JSON 严格格式 | 弯引号、工具名未加字符串引号、字段名 `arg`、尾逗号 | 能写出合法结构：`{"tool_name": "...", "arguments": {...}}` |
| 假 Observation | 一开始只说“模型编造”，没有给工程判别法 | 能说明要看代码有没有真实解析 Action 并调用工具 |
| 主语链路 | 把“工具和 Observation 负责返回结果”混在一起 | 能分清工具返回真实结果，客户端回填 Observation，LLM 读取 Observation |

## 知识库同步

- 新增概念卡：[[../../02-Concepts/Agent/智能体(Agent)|智能体(Agent)]]
- 更新课程页：[[../../03-Courses/Agent/AI-Agent-Learning/stage4-agent-basics|阶段 4：Agent 基础原理]]

## 下一步

周末优先完成 T3-Gate Tool Calling 闯关：把 `calculator_tool`、`read_sandbox_file`、`public_api_tool` 接入一个可靠的工具注册表和分发器，并加入 eval cases。
