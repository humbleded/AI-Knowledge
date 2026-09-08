---
type: course-index
topic: AI-Agent-Learning
status: active
created: 2026-05-28
updated: 2026-09-08
tags:
  - AI-Agent
  - Python
  - 学习路线
---

# AI-Agent-Learning

这是 `C:\Users\26823\Desktop\AI-Agent-Learning` 执行区沉淀到知识库的课程索引。

## 执行区与知识库分工

- 执行区：按知识单元和 Session 写代码、跑程序、保存原始证据并接受 PASS/RETRY 判定。
- 知识库：保存已经通过的阶段总结、概念卡、代码练习复盘和长期可复用结论；课程索引保留进行中的接力，助手工程实现单独标明，二者不自动成为新的掌握证据。

## 当前进度

- [[../../Python/AI-Agent-Learning/stage0-python-basics|阶段 0：Python 与开发环境]]
- [[../../LLM/AI-Agent-Learning/stage1-llm-api-basics|阶段 1：大模型 API 入门]]
- [[../../LLM/AI-Agent-Learning/stage2-prompt-structured-output|阶段 2：Prompt 与结构化输出]]
- [[stage0_5-engineering-basics|阶段 0.5：工程基础随用随补]]
- [[stage3-tool-calling|阶段 3：Tool Calling / Function Calling]]
- [[stage4-agent-basics|阶段 4：Agent 基础原理]]
- [[stage4_5-langgraph-basics|阶段 4.5：LangGraph 基础工作流]]
- 已通过：P0-Gate、L1-Gate、PR2-Gate、T3-01、T3-02、T3-03、T3-04、T3-Gate、A4-01、A4-02、A4-03、A4-04、A4-05、A4-Gate、G8-00
- 当前项：`R6-01 = DOING`，于 2026-09-07 启动。2026-09-08 的 `R6-01-G2` 已单题 PASS：用户指出已找到的资料没有进入模型上下文，并给出问题、正文及 source/section/version；当前有效即时证据为 1 个。原 G1 是委托助手规划，不计独立证据；G2 不再换题重考。
- 下次课程起点：继续 G3，在 `code/stage6/engineering_docs_rag/ingest.py` 使用现成 LangChain `TextLoader`，由 `START → load_documents → END` 的最小 LangGraph 读取真实文件，核对返回的 documents、正文及 source/title/version。该文件仍为 TODO 骨架，等待用户实现；复用 G8-00 已通过的状态、节点和边，不重新考基础。
- 当前产品：用户已授权助手实现统一 Vue + Python/FastAPI 工作台，并全部采用任务指挥台、知识研究工作室、可视流程画布三个工作模式；它们共享同一知识问答后端和当前页内查询。实现与真实运行证据见 [[04-Projects/Agent/AI-Agent-Learning/workbench-knowledge-agent|统一工作台与知识库 Agent（助手工程实现，非课程 PASS）]]。这些产物不代替 G3，也不提前通过 R6-02/R6-03、BE5 或 J11。
- 恢复进展：2026-09-05 S2 的 `W5-ALG-R1` 已正式 PASS，`WP-27 / WP-29` 完成复测，恢复状态为 `NORMAL`；W5 剩余 `DEBT 3`（三道新题），独立推进。
- 并行欠项：W6 岗位审计仍为 `RETRY / INCOMPLETE`，尚未凑齐恰好 10 条硬门槛已核清的可投样本，不能计算正式匹配率；该资料缺口不阻塞技术前置已满足的课程。

以上是 2026-09-08 同步快照；当前状态和接力点分别以执行区 `progress.md`、`daily-plan.md` 为准。

## 当前执行策略

- 阶段 0、阶段 1、阶段 2 主线已完成。
- 阶段 3 已完成：三工具原生 Tool Calling 闭环与 14 条正式评估通过。
- 阶段 4 的 A4-01～A4-05 与 A4-Gate 已完成。A4-Gate 已具备每请求独立 context、七字段调用账本、真实工具终点、Action correction、分层预算、Candidate / Reflection / Refinement 的协议与 Provider 恢复、exact approved summary / allowed sources validator、action-bound HITL 与冻结 V5 eval；唯一 RUN-5 14/14、semantic 20/20。
- 阶段 4.5 的 G8-00 已完成：用故障诊断与变更评审 Agent v1 证明 typed State、7 个业务 Node、五路条件路由、诊断回环、稳定停止、批准的只读工具、v2 updates、12/12 maintained pytest 与一次真实 DeepSeek Node 链。checkpoint、重启恢复和 HITL 仍留给后续 G8-01～03。
- 阶段 0.5 工程基础不再整块前置，而是放到 API、Tool Calling、Memory、RAG、本地部署项目中随用随补。
- `B0-Gate` 作为后续本地栈整合关卡，不阻塞第一次进入 L1/API。

## A4 后依赖路线

`G8-00` 虽然沿用阶段 8 的任务编号，但课程位置是阶段 4.5：它只把已经通过的 Agent 控制循环迁移到显式 Graph，不表示跳过阶段 5～7。后续按依赖推进，而不是按编号机械排序：

完整任务顺序、扩展挂载和收口条件只在执行区 [weekly-plan.md](https://github.com/humbleded/AI-Agent-Learning/blob/main/tracker/weekly-plan.md) 维护；下一次具体操作只读 [daily-plan.md](https://github.com/humbleded/AI-Agent-Learning/blob/main/tracker/daily-plan.md)。本页不复制第二套未来队列。

- 后续 Agent/RAG 项目统一采用 **LangChain 现成组件 + LangGraph 显式流程**：组件负责文档、模型、检索与工具，图负责连接步骤和控制执行。工程文档 RAG 助手与故障诊断/变更评审 Agent 保留各自业务目录、测试和验收证据；框架统一不让两项验收互相替代。
- 后端统一 Python/FastAPI。两个业务核心可脱离 HTTP 单独运行和测试，通过共享 API 接入同一个 Vue 入口；本轮助手已按授权搭建，后续课程沿真实产物补独立操作与工程能力，不再等到 J11 才第一次看见界面。
- 唯一产品已确定为 `product_flagship=agent_workbench`，包含两个持续演化的业务项目。J11-02 再冻结发布范围、默认展示业务 `default_showcase` 与质量要求；“唯一前端”表示共用一套 Vue 应用与公网发布链，不表示只能保留一个业务模块。
- 三个已采用的工作模式是同一产品的不同操作入口，配色设置是附加功能。J11-03 仍需用户独立解释和修改组件状态、流式事件展示、认证、错误处理及密钥边界；助手实现与运行检查不能代替这些学习证据。
- 工作、情景、语义、感知四类 Memory，以及真实图片/音频存储与检索，已纳入 D7-03 规划，**尚未启动、尚未实现**。当前页内问答状态和工作流 checkpoint 都不能冒充跨会话长期记忆。
- `H5-01` 只在真实框架调用链阻塞时触发；`J11-01` 随真实项目持续积累。算法债务与岗位审计继续分别按各自台账推进，不因增加界面或知识库功能而清零或升级证据。

## 本轮同步依据

- [2026-09-08 学习与助手工程交付记录](https://github.com/humbleded/AI-Agent-Learning/blob/main/daily/2026-09-08.md)
- [课程进度事实源](https://github.com/humbleded/AI-Agent-Learning/blob/main/tracker/progress.md)、[当前 Session 接力](https://github.com/humbleded/AI-Agent-Learning/blob/main/tracker/daily-plan.md)
- [2026-09-07 学习与维护记录](https://github.com/humbleded/AI-Agent-Learning/blob/main/daily/2026-09-07.md)
- [学习方法评审](https://github.com/humbleded/AI-Agent-Learning/blob/main/resources/learning-method-review-2026-09-07.md)
- [2026-09-05 算法复测原始证据](https://github.com/humbleded/AI-Agent-Learning/blob/main/daily/2026-09-05.md)
- 本次承认已记录的 G2 单题 PASS，并同步 G3 接力、统一产品路线及助手实现归属；`R6-01` 仍为 DOING，没有新增整项课程 PASS 或岗位证据。

## 相关执行区文件

- [学习执行区](file:///C:/Users/26823/Desktop/AI-Agent-Learning/)
- [总 tracker](file:///C:/Users/26823/Desktop/AI-Agent-Learning/tracker/ai-agent-learning-tracker.md)
- [进度表](file:///C:/Users/26823/Desktop/AI-Agent-Learning/tracker/progress.md)
- [当前入口与主队列](file:///C:/Users/26823/Desktop/AI-Agent-Learning/tracker/daily-plan.md)
- [依赖内容块](file:///C:/Users/26823/Desktop/AI-Agent-Learning/tracker/weekly-plan.md)
- [岗位证据与审计](file:///C:/Users/26823/Desktop/AI-Agent-Learning/tracker/job-readiness.md)
- [算法台账](file:///C:/Users/26823/Desktop/AI-Agent-Learning/tracker/algorithm-progress.md)
- [Session 原始记录](file:///C:/Users/26823/Desktop/AI-Agent-Learning/daily/)
- [代码目录](file:///C:/Users/26823/Desktop/AI-Agent-Learning/code/)

## 已沉淀内容

- [[../../Python/AI-Agent-Learning/stage0-python-basics]]
- [[../../LLM/AI-Agent-Learning/stage1-llm-api-basics]]
- [[../../LLM/AI-Agent-Learning/stage2-prompt-structured-output]]
- [[stage0_5-engineering-basics]]
- [[stage3-tool-calling]]
- [[stage4-agent-basics]]
- [[stage4_5-langgraph-basics|阶段 4.5：LangGraph 基础工作流]]
- [[../../../04-Projects/Python/AI-Agent-Learning/p0-01-hello-script]]
- [[../../../04-Projects/Python/AI-Agent-Learning/p0-02-profile-script]]
- [[../../../04-Projects/Python/AI-Agent-Learning/p0-03-scheduler]]
- [[../../../04-Projects/Python/AI-Agent-Learning/p0-04-tasks]]
- [[../../../04-Projects/Python/AI-Agent-Learning/p0-05-plan-functions]]
- [[../../../04-Projects/Python/AI-Agent-Learning/p0-06-env-check]]
- [[../../../04-Projects/Python/AI-Agent-Learning/p0-07-safe-divide]]
- [[../../../04-Projects/Python/AI-Agent-Learning/p0-08-progress-file]]
- [[../../../04-Projects/Python/AI-Agent-Learning/p0-09-http-request]]
- [[../../../04-Projects/Python/AI-Agent-Learning/p0-gate-learning-log]]
- [[../../../04-Projects/LLM/AI-Agent-Learning/l1-01-first-call]]
- [[../../../04-Projects/Agent/AI-Agent-Learning/t3-02-calculator-tool]]
- [[../../../04-Projects/Agent/AI-Agent-Learning/t3-03-file-reader-tool]]
- [[../../../04-Projects/Agent/AI-Agent-Learning/t3-04-public-api-tool]]
- [[../../../04-Projects/Agent/AI-Agent-Learning/t3-gate-tool-assistant]]
- [[../../../04-Projects/Agent/AI-Agent-Learning/a4-03-react-agent]]
- [[../../../04-Projects/Agent/AI-Agent-Learning/a4-04-plan-and-solve]]
- [[../../../04-Projects/Agent/AI-Agent-Learning/a4-05-reflection-writer]]
- [[../../../04-Projects/Agent/AI-Agent-Learning/a4-gate-research-summary-agent|A4-Gate 研究摘要 Agent（正式 PASS）]]
- [[../../../04-Projects/Agent/AI-Agent-Learning/a4-gate-function-call-reference|A4-Gate 函数调用参考]]
- [[../../../04-Projects/Agent/AI-Agent-Learning/g8-00-incident-change-review-agent-v1|G8-00 故障诊断与变更评审 Agent v1]]
- [[04-Projects/Agent/AI-Agent-Learning/workbench-knowledge-agent|统一工作台与知识库 Agent（助手工程实现，非课程 PASS）]]
- [[../../../07-Reviews/AI-Agent-Learning/2026-05-27-stage0-p0-01-p0-02-pass-review]]
- [[../../../07-Reviews/AI-Agent-Learning/2026-05-28-stage0-p0-03-pass-review]]
- [[../../../07-Reviews/AI-Agent-Learning/2026-06-02-stage0-p0-04-pass-review]]
- [[../../../07-Reviews/AI-Agent-Learning/2026-06-09-stage0-p0-05-pass-review]]
- [[../../../07-Reviews/AI-Agent-Learning/2026-06-10-stage0-p0-06-pass-review]]
- [[../../../07-Reviews/AI-Agent-Learning/2026-06-11-stage0-p0-07-pass-review]]
- [[../../../07-Reviews/AI-Agent-Learning/2026-06-13-stage0-p0-08-pass-review]]
- [[../../../07-Reviews/AI-Agent-Learning/2026-06-14-stage0-p0-gate-l1-01-pass-review]]
- [[../../../07-Reviews/AI-Agent-Learning/2026-07-06-t3-02-calculator-tool-review]]
- [[../../../07-Reviews/AI-Agent-Learning/2026-07-07-t3-03-file-reader-tool-review]]
- [[../../../07-Reviews/AI-Agent-Learning/2026-07-08-t3-04-public-api-tool-review]]
- [[../../../07-Reviews/AI-Agent-Learning/2026-07-09-a4-01-what-is-agent-review]]
- [[../../../07-Reviews/AI-Agent-Learning/2026-07-12-t3-gate-tool-calling-review]]
- [[../../../07-Reviews/AI-Agent-Learning/2026-07-15-a4-02-llm-agent-basics-review]]
- [[../../../07-Reviews/AI-Agent-Learning/2026-07-22-a4-03-react-review]]
- [[../../../07-Reviews/AI-Agent-Learning/2026-07-30-a4-04-plan-and-solve-review]]
- [[../../../07-Reviews/AI-Agent-Learning/2026-08-04-a4-05-reflection-review]]
- [[../../../07-Reviews/AI-Agent-Learning/2026-08-24-a4-gate-pass-review|A4-Gate 正式 PASS 复盘]]
- [[../../../07-Reviews/AI-Agent-Learning/2026-08-25-route-audit-review|2026-08-25 路线审计复盘]]
- [[../../../07-Reviews/AI-Agent-Learning/2026-09-05-g8-00-langgraph-v1-review|G8-00 LangGraph v1 正式 PASS 复盘]]
