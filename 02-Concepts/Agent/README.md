---
type: concept-index
topic: Agent
status: active
created: 2026-07-06
updated: 2026-09-08
tags:
  - Agent
  - 概念卡
---

# Agent 概念卡索引

这里保存 Agent 应用开发中的可复用概念：工具、执行器、ReAct 流程、安全边界、调度与评估等。

## 从当前问题进入

- 模型已经提出工具请求，接下来谁执行：[[工具调用与动作(Tool Calling and Action)|工具调用与动作]]。
- 工具一直失败，怎样重试、停止或交给人：[[受控重试与人工接管(Bounded Retry and Human Handoff)|受控重试与人工接管]]。
- 怎样连接步骤，以及哪些恢复能力还需要另做：[[LangGraph 状态图编排(StateGraph)|LangGraph 状态图编排]]。
- 配置排查、方案选择和文档问答：[[01-Maps/按问题查知识|完整问题导航]]。

## 卡片

- [[智能体(Agent)|智能体：LLM + 工具 + 客户端调度 + Observation 反馈循环]]
- [[ReAct推理与行动循环(ReAct)|ReAct：Thought / Action / Observation 循环、停止条件与最大步数]]
- [[计划与求解(Plan-and-Solve)|Plan-and-Solve：Planner 拆解、Executor 执行、history 与 Replanning 边界]]
- [[反思机制(Reflection)|Reflection：三阶段闭环、证据白名单、反馈恢复完整尾链、软评审 / 硬门与事实复盘边界]]
- [[工具调用与动作(Tool Calling and Action)|工具调用与动作：Tool Calling / Function Calling / Action / Execution 边界]]
- [[工具定义与执行协议(Tool Definition)|工具定义与执行协议：tools schema / TOOLS 注册表 / 客户端校验与执行]]
- [[文件工具沙箱(File Tool Sandbox)|文件工具沙箱：resolve + relative_to 的安全边界]]
- [[外部 API 工具(External API Tool)|外部 API 工具：HTTPS allowlist / 443 / SSRF / 重定向 / timeout]]
- [[受控重试与人工接管(Bounded Retry and Human Handoff)|受控重试与人工接管：判断能否重试、共享预算、停止与交接]]
- [[动作绑定人工确认(Action-Bound Confirmation)|动作绑定人工确认：冻结动作深绑定、一次性 nonce、先消费后副作用与重放防护]]
- [[冻结评估与不可补偿硬门(Frozen Evaluation)|冻结评估与不可补偿硬门：版本指纹、唯一正式运行、holdout、exact / semantic 分层与不可补偿失败]]
- [[LangGraph 状态图编排(StateGraph)|LangGraph 状态图编排：State / Node / Edge、条件路由、stream 与应用控制边界]]
