---
type: course-stage
topic: AI-Agent-Learning Stage 4
status: active
created: 2026-07-10
updated: 2026-08-22
tags:
  - Agent
  - AI-Agent-Learning
  - Stage4
---

# 阶段 4：Agent 基础原理

## 定位

阶段 4 目标是理解 ReAct、Planning、Reflection，并写出最小 Agent。

阶段 3 的 T3-Gate 已通过。阶段 4 当前已完成 A4-01～A4-05；当前主任务为 `DOING` 中的 A4-Gate 最小 Agent 闯关。W4 算法已完成 4/4、内容块 `PASS`，结转债务为 0；它仍与课程任务状态分层记录。

## 任务状态

| 任务 | 状态 | 日期 | 产物 | 备注 |
|---|---|---|---|---|
| A4-01 什么是 Agent | PASS | 2026-07-09 | `notes/stage4/a4_01_what_is_agent.md` | 能定义 Agent，区分 Agent vs Chatbot，说明 Tool/Action/Observation/Final Answer 和代码硬校验 |
| A4-02 LLM 与 Agent 基础 | PASS | 2026-07-15 | `notes/stage4/a4_02_llm_agent_basics.md` | LLM/Token/架构、Chat Template、无状态、工具职责与幻觉防线均通过 |
| A4-03 ReAct | PASS | 2026-07-22 | `code/stage4/a4_03_react_agent.py` | 完整两轮轨迹与 max_steps 通过；15/15 parser/prompt/loop 边界断言通过 |
| A4-04 Plan-and-Solve | PASS | 2026-07-30 | `code/stage4/a4_04_plan_solve_demo.py` | 可运行计划→执行→事实复盘闭环；39/39 解析、history、复盘与编排边界断言通过 |
| A4-05 Reflection | PASS | 2026-08-04 | `code/stage4/a4_05_reflection_writer.py` | 初稿/反思/改进/同标准选择闭环；39/39 确定性断言、真实提前停止与真实故障修正路径通过 |
| A4-Gate 最小 Agent 闯关 | DOING | 2026-08-22 | `code/stage4/problem-contract.md`、`code/stage4/a4_gate_research_summary_agent.py` | Problem Contract、C1/C2、C3a～C3d、C4a-1、C4a-2a/2b1/2b2、C4b-1、C4b-2a、C4b-2b-1、C4b-2b-2a 与 C4b-2b-2b 已完成教学 / 实现子单元，C4b-2c 已正式 PASS；已有真实工具终点、Action correction、Candidate / Reflection / Refinement 的响应、JSON、candidate validator 与 Provider/API 受控恢复、共享 / 独立计数、完整链预算和人工证据池映射。父 Gate 仍缺 HITL、14 条 eval、五个必答题、合同总体定稿和整关复核 |

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

## A4-04 已沉淀概念与实践

- [[../../../02-Concepts/Agent/计划与求解(Plan-and-Solve)|计划与求解]]
- [[../../../02-Concepts/Agent/反思机制(Reflection)|Reflection 与运行事实复盘边界]]
- [[../../../04-Projects/Agent/AI-Agent-Learning/a4-04-plan-and-solve|A4-04 Plan-and-Solve 代码实践]]
- [[../../../07-Reviews/AI-Agent-Learning/2026-07-30-a4-04-plan-and-solve-review|A4-04 PASS 复盘]]

## A4-05 已沉淀概念与实践

- [[../../../02-Concepts/Agent/反思机制(Reflection)|反思机制：三阶段数据流、停止、成本与质量门槛]]
- [[../../../04-Projects/Agent/AI-Agent-Learning/a4-05-reflection-writer|A4-05 Reflection Writer 代码实践]]
- [[../../../07-Reviews/AI-Agent-Learning/2026-08-04-a4-05-reflection-review|A4-05 PASS 复盘]]

## A4-Gate 已沉淀进行中实践

- [[../../../04-Projects/Agent/AI-Agent-Learning/a4-gate-research-summary-agent|A4-Gate 研究摘要 Agent（C4b-2c Refinement 共享恢复已收口，父任务 DOING）]]
- [[../../../raw/conversations/2026-08-13-ai-agent-learning-a4-gate-c4a-1-session-handoff|C4a-1 会话接力摘要]]
- [[../../../02-Concepts/Agent/受控重试与人工接管(Bounded Retry and Human Handoff)|受控重试与人工接管：Action correction、完整链预算与稳定公开交接]]
- [[../../../02-Concepts/Agent/反思机制(Reflection)|Reflection 的 Observation 来源白名单与硬校验边界]]
- [[../../../02-Concepts/LLM/结构化输出(Structured Output)|结构化输出、finish_reason 与 JSON 解析分层]]
- [[../../../02-Concepts/LLM/函数调用(Function Calling)|SDK 属性对象与 Tool Calling 协议]]

## 当前易错点

- 格式像 Observation，不代表它是真 Observation；要看代码有没有真实执行工具。
- Action JSON 要严格可解析，不能有弯引号、未加引号的字符串值、尾逗号。
- Observation 是工具结果的反馈消息，不是执行者。
- 微调效果写入新模型权重；后续请求必须调用该模型。Few-shot 只在当前上下文有效。
- 工具返回失败或超时时，模型自然语言不能覆盖权威结果；未知状态必须保持未知。
- Prompt 对文本协议只是软约束；parser/validator、非空 Finish 与 max_steps 才是客户端硬边界。
- 确定性 fake LLM 只能证明客户端代码路径，不能外推真实模型的格式遵守和工具选择质量。
- 内部 `StepResult` 必须维持 `(step, str)`，外部编排返回的 `str | None` 是另一层契约；不能因都出现 `None` 就混为同一状态污染问题。
- Replanning 的产物必须是可执行剩余计划，而不是约束清单；后续步骤只能引用前一步实际返回的结果，不能提前写死。
- Reflection prompt 负责表达评审标准与反馈协议，但仍是软约束；客户端只对已编码门槛作硬判断，`accepted_refinement=True` 不能外推为所有语义质量都改善。
- 故障注入必须如实区分测试夹具与真实模型输出；不能为了覆盖 Refinement 删除生产提前停止条件。
- 原子工具入口只知道本次尝试；是否还有重试机会、何时停止自治，必须由持有历史与预算的上层编排判断。
- 每次真实重试都应重新进入原子入口占 step、计时和记日志，不能手工增加 step 制造没有调用证据的幽灵步号。
- 自动恢复耗尽只能用专用窄信号映射；宽泛捕获 `RuntimeError` 会把不可重试失败、协议错误和真实 Python 异常错误分类为 `needs_manual`。
- Candidate API 已返回但响应不合法时，先做 `valid / recoverable / terminal` 分类；只有白名单失败、唯一恢复尚未使用且完整尾链预算足够时才恢复。
- Candidate 失败结果可以保留真实白名单来源，但它们只是人工接管证据池，不是已验证摘要引用；失败 Candidate 也不能写入 recovery 消息历史。
- Reflection recovery 成功只得到供 Refinement 使用的反馈，不是最终结果；失败响应不能进入 recovery prompt，合法 Candidate 也不能替代最终 validator。
- step 5 的 Reflection 失败虽然还剩一个调用位置，但完整可信尾链需要 recovery + Refinement 两步，因此必须在 recovery 前停止并保留未使用的 step 6。
- 一次 SDK `.create()` 是一次逻辑模型调用，不一定只有一个物理 HTTP 请求；`max_retries=2` 时单次逻辑调用极端最多有 3 次物理尝试，但 Agent 仍只记一个 step / 聚合日志。
- fake client 证明应用编排，真实 factory 对象属性证明 `max_retries` / `timeout` 配置，`_request_id` 只帮助定位 Provider 请求；三类证据不能互相替代。
- Candidate Provider recovery 与 Candidate 协议 recovery 必须分开计数；Provider 1 / 协议 0 与 Provider 0 / 协议 1 的后续禁行条件不同，不能合成一个 `retries=1`。
- Reflection Provider / protocol recovery 同样按“为什么真正发出额外调用”计数，不按错误事件或调用结果倒改角色；本地 response 分类不算模型请求。
- Reflection 首次调用在 step 4 发生 recoverable Provider 错误时，可在预算允许下走 step 5 Provider recovery → step 6 Refinement；若首次失败已到 step 5，或 step 5 protocol recovery 自身遇 Provider 错误，则必须零第三次请求并安全停止。
- Refinement 的模型 candidate 合同失败可以丢弃后受控重做一次，但非法 `allowed_sources` 或普通程序 / 调用方不变量错误必须保持上抛，不能伪装成模型失败。
- Refinement 的 Provider、响应、JSON 与 candidate-contract 跨失败域共享一次 recovery；失败类型改变不会重置额度，也不能产生第三次请求或 step 7。

## 相关执行区

- [A4-01 daily](file:///C:/Users/26823/Desktop/AI-Agent-Learning/daily/2026-07-09.md)
- [A4-01 notes](file:///C:/Users/26823/Desktop/AI-Agent-Learning/notes/stage4/a4_01_what_is_agent.md)
- [A4-02 daily（带读与迁移）](file:///C:/Users/26823/Desktop/AI-Agent-Learning/daily/2026-07-14.md)
- [A4-02 daily（正式练习与复核）](file:///C:/Users/26823/Desktop/AI-Agent-Learning/daily/2026-07-15.md)
- [A4-02 notes](file:///C:/Users/26823/Desktop/AI-Agent-Learning/notes/stage4/a4_02_llm_agent_basics.md)
- [A4-03 daily（带读、代码与正式练习）](file:///C:/Users/26823/Desktop/AI-Agent-Learning/daily/2026-07-21.md)
- [A4-03 daily（迁移复测与正式复核）](file:///C:/Users/26823/Desktop/AI-Agent-Learning/daily/2026-07-22.md)
- [A4-03 code](file:///C:/Users/26823/Desktop/AI-Agent-Learning/code/stage4/a4_03_react_agent.py)
- [A4-04 daily（带读启动）](file:///C:/Users/26823/Desktop/AI-Agent-Learning/daily/2026-07-22.md)
- [A4-04 daily（带读与实现）](file:///C:/Users/26823/Desktop/AI-Agent-Learning/daily/2026-07-23.md)
- [A4-04 daily（实现收口）](file:///C:/Users/26823/Desktop/AI-Agent-Learning/daily/2026-07-24.md)
- [A4-04 daily（正式练习启动）](file:///C:/Users/26823/Desktop/AI-Agent-Learning/daily/2026-07-25.md)
- [A4-04 daily（F1 与 F2 题面）](file:///C:/Users/26823/Desktop/AI-Agent-Learning/daily/2026-07-29.md)
- [A4-04 daily（正式练习与任务级复核）](file:///C:/Users/26823/Desktop/AI-Agent-Learning/daily/2026-07-30.md)
- [A4-04 code](file:///C:/Users/26823/Desktop/AI-Agent-Learning/code/stage4/a4_04_plan_solve_demo.py)
- [A4-05 daily（带读启动）](file:///C:/Users/26823/Desktop/AI-Agent-Learning/daily/2026-07-30.md)
- [A4-05 daily（带读与实现启动）](file:///C:/Users/26823/Desktop/AI-Agent-Learning/daily/2026-08-03.md)
- [A4-05 daily（实现、正式练习与任务级复核）](file:///C:/Users/26823/Desktop/AI-Agent-Learning/daily/2026-08-04.md)
- [A4-05 code](file:///C:/Users/26823/Desktop/AI-Agent-Learning/code/stage4/a4_05_reflection_writer.py)
- [A4-Gate Problem Contract（DRAFT）](file:///C:/Users/26823/Desktop/AI-Agent-Learning/code/stage4/problem-contract.md)
- [A4-Gate 当前代码](file:///C:/Users/26823/Desktop/AI-Agent-Learning/code/stage4/a4_gate_research_summary_agent.py)
- [A4-Gate C3d 正式证据（2026-08-11）](file:///C:/Users/26823/Desktop/AI-Agent-Learning/daily/2026-08-11.md)
- [A4-Gate C4a-1 前半段证据（2026-08-12）](file:///C:/Users/26823/Desktop/AI-Agent-Learning/daily/2026-08-12.md)
- [A4-Gate C4a-1 收口证据（2026-08-13）](file:///C:/Users/26823/Desktop/AI-Agent-Learning/daily/2026-08-13.md)
- [A4-Gate C4a-2a 六步恢复与 C4a-2b1 启动证据（2026-08-17）](file:///C:/Users/26823/Desktop/AI-Agent-Learning/daily/2026-08-17.md)
- [A4-Gate C4a-2b1 专用信号、15/15 与用户审核（2026-08-18）](file:///C:/Users/26823/Desktop/AI-Agent-Learning/daily/2026-08-18.md)
- [A4-Gate C4a-2b2、C4b-1 与策略 B 用户审核（2026-08-19）](file:///C:/Users/26823/Desktop/AI-Agent-Learning/daily/2026-08-19.md)
- [A4-Gate Candidate / Reflection 响应恢复、端到端回归与用户审核（2026-08-20）](file:///C:/Users/26823/Desktop/AI-Agent-Learning/daily/2026-08-20.md)
- [A4-Gate SDK retry / timeout 与 Candidate / Reflection Provider recovery（2026-08-21）](file:///C:/Users/26823/Desktop/AI-Agent-Learning/daily/2026-08-21.md)
- [A4-Gate C4b-2c Refinement 共享恢复与正式复验（2026-08-22）](file:///C:/Users/26823/Desktop/AI-Agent-Learning/daily/2026-08-22.md)
- [progress](file:///C:/Users/26823/Desktop/AI-Agent-Learning/tracker/progress.md)
