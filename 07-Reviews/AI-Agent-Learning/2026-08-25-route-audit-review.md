---
type: review
topic: AI-Agent-Learning 路线审计
status: usable
created: 2026-08-25
updated: 2026-08-25
source:
  - C:\Users\26823\Desktop\AI-Agent-Learning\AGENTS.md
  - C:\Users\26823\Desktop\AI-Agent-Learning\CLAUDE.md
  - C:\Users\26823\Desktop\AI-Agent-Learning\tracker\ai-agent-learning-tracker.md
  - C:\Users\26823\Desktop\AI-Agent-Learning\tracker\daily-plan.md
  - C:\Users\26823\Desktop\AI-Agent-Learning\tracker\weekly-plan.md
  - C:\Users\26823\Desktop\AI-Agent-Learning\tracker\progress.md
  - C:\Users\26823\Desktop\AI-Agent-Learning\tracker\learning-resources.md
  - C:\Users\26823\Desktop\AI-Agent-Learning\tracker\job-readiness.md
  - C:\Users\26823\Desktop\AI-Agent-Learning\tracker\algorithm-progress.md
tags:
  - AI-Agent-Learning
  - Review
  - 学习路线
---

# 2026-08-25 AI-Agent-Learning 路线审计复盘

## 结论

本次完成的是**整条学习路线的纠偏与依赖审计**，不是新的课程学习或项目实现。因此：

- A4-Gate 继续保持 2026-08-24 的正式 `PASS`；
- G8-00 继续为 `TODO`，尚未开始带读、实现或验收；
- 不新增概念卡，不把路线计划升级成作品或岗位证据；
- 已发现的 W5 算法债务和 W6 岗位审计缺口按原状态公开保留。

## 修正的主要差异

### 1. 阶段编号不再冒充学习顺序

G8-00 虽然使用阶段 8 的编号，但课程位置是阶段 4.5。它只把 A4 已经通过的 Agent Loop、ReAct、Plan-and-Solve 与 Reflection 迁移到显式 Graph，不表示阶段 5、6、7 被跳过，也不重新教学或重考 A4 内容。

后续唯一依赖主线为：

```text
G8-00
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

`J11-01` 随真实项目持续积累并在 J11-06 前收口；H5-01 只在真实框架调用链阻塞时触发，不阻塞主线。

### 2. 两个旗舰不再重复造项目

- LangChain 旗舰固定为工程文档 RAG 助手，重点证明 Document/Loader/Splitter、Retriever、Tool/Agent Harness、引用、权限、对照评估和部署。
- LangGraph 旗舰固定为故障诊断与变更评审 Agent，重点证明 StateGraph、路由/循环/停止、stream、持久化、interrupt/resume、幂等和恢复。
- FastAPI 只是两个 Python core 的 HTTP/SSE/认证/输入校验交付层，不承担 Agent 编排职责。
- E10 建一套共享评估框架，再接两个领域适配层；不新增第三个“评估项目”。

### 3. Vue 与开源项目的边界写清了

用户会一些 Vue，因此后续先做最小切片复核，不机械重学已经能独立证明的部分。进入真实界面任务时，助手可以先核查许可证、维护状态、依赖与安全风险，再从 GitHub 选择并组合开源 Vue 骨架。

这项协助不算用户独立掌握证据。用户仍需审核来源、许可证、依赖与关键改动，并能解释或修改组件状态、SSE、认证、错误处理、数据流和密钥边界。J11-02 只冻结一个 `product_flagship`：只有它建设正式 Vue、公网部署和产品级观测；另一个旗舰保留可复现 API/demo、容器和完整 E10 评估。

### 4. 并行债务不再被课程 PASS 遮住

- W5 没有 `3 新 + 1 旧` 的合格算法证据，正式结转 `DEBT 4`。它不撤销 A4 课程 PASS；下一次独立算法 Session 先逐题清债，清零前不启动 W6 完整配额。
- W6 岗位审计的 10 条候选只有 `4 HARD_ELIGIBLE + 6 UNKNOWN`，因此判为 `RETRY / INCOMPLETE`，不能报告正式匹配率或 `/10` 能力频率。
- W6 债务不阻塞 G8-00，但最晚必须在 G8-00 正式 PASS 后、R6-01 启动前补足恰好 10 条硬门槛已核清的可投样本。

## 审计与验证

执行区完成了以下一致性检查：

- 79 个唯一任务 ID；45 个未完成任务都能在主队列或挂载规则中找到去向；
- 43 个有先后顺序的队列标记与可选/持续挂载任务分开，没有把 H5、J11-01 或岗位审计伪装成已完成主线；
- `product_flagship` 只有一个正式选择点，E10 只有一套共享评估框架；
- AGENTS/CLAUDE 孪生规则、Markdown 表格、任务引用与 `git diff --check` 均通过；
- 另一位独立复核者重新检查阶段 4.5～8、Vue、算法和岗位审计边界后，没有发现未关闭的高风险差异。

## 下一步

课程下一口令仍是“开始今天的学习”进行 G8-00 预览；只有用户随后说“开始带读”或“开始动手”，才会建立实际 Session 并把任务从 `TODO` 改为 `DOING`。

## 关联

- [[../../03-Courses/Agent/AI-Agent-Learning/README|AI-Agent-Learning 课程索引]]
- [[../../01-Maps/AI 开发学习路线]]
- [[../../01-Maps/AI-Agent-Learning 跳转索引]]
- [[2026-08-24-a4-gate-pass-review|A4-Gate 正式 PASS 复盘]]
