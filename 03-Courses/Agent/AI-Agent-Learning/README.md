---
type: course-index
topic: AI-Agent-Learning
status: active
created: 2026-05-28
updated: 2026-09-05
tags:
  - AI-Agent
  - Python
  - 学习路线
---

# AI-Agent-Learning

这是 `C:\Users\26823\Desktop\AI-Agent-Learning` 执行区沉淀到知识库的课程索引。

## 执行区与知识库分工

- 执行区：按知识单元和 Session 写代码、跑程序、保存原始证据并接受 PASS/RETRY 判定。
- 知识库：保存已经通过的阶段总结、概念卡、代码练习复盘和长期可复用结论。

## 当前进度

- [[../../Python/AI-Agent-Learning/stage0-python-basics|阶段 0：Python 与开发环境]]
- [[../../LLM/AI-Agent-Learning/stage1-llm-api-basics|阶段 1：大模型 API 入门]]
- [[../../LLM/AI-Agent-Learning/stage2-prompt-structured-output|阶段 2：Prompt 与结构化输出]]
- [[stage0_5-engineering-basics|阶段 0.5：工程基础随用随补]]
- [[stage3-tool-calling|阶段 3：Tool Calling / Function Calling]]
- [[stage4-agent-basics|阶段 4：Agent 基础原理]]
- [[stage4_5-langgraph-basics|阶段 4.5：LangGraph 基础工作流]]
- 已通过：P0-Gate、L1-Gate、PR2-Gate、T3-01、T3-02、T3-03、T3-04、T3-Gate、A4-01、A4-02、A4-03、A4-04、A4-05、A4-Gate、G8-00
- 当前项：G8-00 已于 2026-09-05 正式 `PASS`；下一主线是 R6-01，但必须先完成已签发的独立算法恢复 Session，并关闭 W6 岗位审计债务。
- 并行债务：W5 仍为 `DEBT 4`；`WP-27 / WP-29` 触发 `RECOVERY_BLOCK_PENDING`；W6 岗位审计仍为 `RETRY / INCOMPLETE`，目前只有 `4 HARD_ELIGIBLE + 6 UNKNOWN`，不能计算正式匹配率。

## 当前执行策略

- 阶段 0、阶段 1、阶段 2 主线已完成。
- 阶段 3 已完成：三工具原生 Tool Calling 闭环与 14 条正式评估通过。
- 阶段 4 的 A4-01～A4-05 与 A4-Gate 已完成。A4-Gate 已具备每请求独立 context、七字段调用账本、真实工具终点、Action correction、分层预算、Candidate / Reflection / Refinement 的协议与 Provider 恢复、exact approved summary / allowed sources validator、action-bound HITL 与冻结 V5 eval；唯一 RUN-5 14/14、semantic 20/20。
- 阶段 4.5 的 G8-00 已完成：用故障诊断与变更评审 Agent v1 证明 typed State、7 个业务 Node、五路条件路由、诊断回环、稳定停止、批准的只读工具、v2 updates、12/12 maintained pytest 与一次真实 DeepSeek Node 链。checkpoint、重启恢复和 HITL 仍留给后续 G8-01～03。
- 阶段 0.5 工程基础不再整块前置，而是放到 API、Tool Calling、Memory、RAG、本地部署项目中随用随补。
- `B0-Gate` 作为后续本地栈整合关卡，不阻塞第一次进入 L1/API。

## A4 后依赖路线

`G8-00` 虽然沿用阶段 8 的任务编号，但课程位置是阶段 4.5：它只把已经通过的 Agent 控制循环迁移到显式 Graph，不表示跳过阶段 5～7。后续按依赖推进，而不是按编号机械排序：

```text
G8-00（PASS）
→ 独立算法恢复（WP-27 / WP-29）
→ W6 岗位审计补全
→ R6-01 → BE5-01
→ B0-01/03/04/Gate → BE5-04
→ R6-02/S-02 → R6-03/S-06
→ BE5-02/03 → G8-01/02/03
→ BE5-05/BE5-Gate → R6-Gate
→ D7-02/S-04 → G8-Gate
→ D7-01/03/Gate → M9 → E10
→ S-01（若待完成）
→ J11-02 → J11-03 → J11-04 → J11-05
→ S-05 正式收口 → J11-06
→ FINAL-Gate → J11-07 → J11-08 → J11-Gate
```

- `H5-01` 只在真实框架调用链阻塞时触发，不阻塞主线；`J11-01` 随真实项目持续积累，最晚在 J11-06 前收口。
- 两个旗舰分别是 LangChain 工程文档 RAG 助手和 LangGraph 故障诊断/变更评审 Agent。E10 复用一套评估框架、接两个领域适配层，不新建第三个项目。
- J11-02 由用户冻结唯一 `product_flagship`。只有它继续建设正式 Vue、公网部署和产品级观测；另一旗舰保留可复现 API/demo、容器与完整评估。
- 用户会一些 Vue，进入真实界面任务时先用最小切片复核。助手可以在核查许可证、维护状态、依赖与安全风险后组合 GitHub 开源 Vue 骨架；用户仍需审核关键改动，并在 J11-03 独立解释和修改组件状态、SSE、认证、错误处理及密钥边界。
- W5 算法债务使用独立 Session 逐题清理；2026-09-05 已因旧复习积压签发 `RECOVERY_BLOCK_PENDING`，下一次只用一个问题复测 WP-27 / WP-29，未 PASS 前仍是 `DEBT 4`。之后必须关闭 W6 岗位审计，补足恰好 10 条硬门槛已核清的可投样本，才能启动 R6-01。

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
