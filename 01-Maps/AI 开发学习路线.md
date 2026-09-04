---
type: learning-map
topic: AI 开发学习路线
status: active
created: 2026-06-04
updated: 2026-09-05
tags:
  - 学习路线
  - AI工程
  - AI-Agent
---

# AI 开发学习路线

这条路线面向初级/初中级 Agent 应用开发岗位，次方向是大模型应用后端与 RAG/知识库工程。目标不是追热点或按阶段编号机械上课，而是按真实项目依赖逐步形成可运行、可测试、可部署、可解释的作品证据。

## 已完成的基础主线

以下内容已经有正式课程 PASS，后续只迁移到新项目，不换名字重新教学或重考：

- Python 最小开发能力、文件/JSON、HTTP、异常与测试。
- 大模型 API、Prompt、结构化输出与 Tool Calling。
- Agent Loop、ReAct、Plan-and-Solve、Reflection、停止条件、受控恢复与人工确认。

截至 2026-09-05，A4-Gate 与阶段 4.5 的 G8-00 都已正式 `PASS`。当前先处理已经签发的独立算法恢复 Session，再关闭 W6 岗位审计债务；两项完成后才启动 R6-01。

## A4 后依赖主线

`G8-00` 使用阶段 8 编号，是因为它属于后续 LangGraph 旗舰；课程位置实际是阶段 4.5。它只迁移已经学会的控制循环，不代表阶段 5～7 被跳过。

```text
G8-00 Graph 基础（阶段 4.5，PASS）
  → 独立算法恢复（WP-27 / WP-29）→ W6 岗位审计补全
  → R6-01 文档导入与切分 → BE5-01 工程结构、日志与测试
  → B0-01/03/04/Gate → BE5-04 PostgreSQL + pgvector
  → R6-02/S-02 检索 → R6-03/S-06 RAG 对照
  → BE5-02/03 FastAPI、Pydantic、SSE
  → G8-01/02/03 durable Graph、恢复与 HITL
  → BE5-05/BE5-Gate → R6-Gate
  → D7-02/S-04 多 Agent 取舍与受控对照 → G8-Gate
  → D7-01/03/Gate 编排模式与长期 Memory
  → M9 MCP → E10 评估与系统设计
  → S-01（若待完成）
  → J11-02 → J11-03 → J11-04 → J11-05
  → S-05 正式收口 → J11-06
  → FINAL-Gate → J11-07 → J11-08 → J11-Gate
```

`J11-01` 从真实项目开发开始持续累计 Git/PR/CI/review 证据，最晚在 J11-06 前收口。`H5-01` 只在真实框架调用链阻塞时追一条源码路径，不是必经阶段。

## 两个旗舰与产品边界

- LangChain 旗舰：工程文档 RAG 助手，重点证明文档导入、检索、引用、权限、固定两步与 Agentic RAG 对照、评估和部署。
- LangGraph 旗舰：故障诊断与变更评审 Agent，重点证明显式状态图、路由/循环/停止、stream、持久化、interrupt/resume、幂等和恢复。
- G8-00 已完成该旗舰的无持久化 v1：[[../02-Concepts/Agent/LangGraph 状态图编排(StateGraph)|StateGraph 基础概念]]与[[../04-Projects/Agent/AI-Agent-Learning/g8-00-incident-change-review-agent-v1|可运行项目]]已经闭合；持久化、恢复和 HITL 仍未提前宣称完成。
- FastAPI 是两个项目共同的 HTTP/SSE/认证/输入校验交付层，不是 Agent 编排框架。
- E10 只建设一套共享评估框架，再接两个领域适配层；不为了评估另建第三个项目。
- J11-02 由用户冻结唯一 `product_flagship`。只有它继续建设正式 Vue、公网部署和产品级观测；另一旗舰保留可复现 API/demo、容器与完整评估。
- 用户会一些 Vue。真正进入界面任务时，助手可以先审计许可证、维护状态、依赖和安全风险，再从 GitHub 选择并组合开源 Vue 骨架；用户仍要审核关键改动，并在 J11-03 独立解释和修改状态、SSE、认证、错误处理与密钥边界。

## 工程基础支撑

这些内容需要加入学习框架，但作为支撑层逐步补齐，不抢占 AI 主线。判断标准不是“先完整学完”，而是“当前 Agent/API 项目是否用得到”。

- 环境和命令行：在 `venv`、包安装、环境变量、路径、进程和日志排错时补。
- 网络基础：在 HTTP 请求、API 调用、tool API、timeout、status code 出问题时补。
- 数据库：在 pgvector、RAG 元数据、长期 Memory 或聊天历史需要保存时补。
- Docker：在需要 PostgreSQL、本地多服务、部署、volume、network、logs 时补。
- FastAPI、Git、CI、日志、测试、部署：随着项目需要逐步补。

暂不深入：

- 数据库内核
- Linux 内核
- 高级网络协议
- 大规模分布式系统
- 复杂 Kubernetes

## 技术动态关注

这些方向保持关注，但不因为有更新就自动进入学习计划。

- OpenAI 更新
- Anthropic 更新
- Gemini 更新
- MCP 生态更新

判断顺序：

1. 它是什么。
2. 和当前目标、项目、工作有没有关系。
3. 社区或生产采用度如何。
4. 是否值得关注。
5. 是否进入学习队列。

## 只记录不深入

默认只记录，不深入学习：

- 刚发布的新框架
- 新 Agent 产品
- 新模型
- 短期热点

例外条件：

- 工作需要
- 项目需要
- 社区大量采用

## 学习节奏原则

- 以知识单元和 Session 接力，不按自然日清零，也不把 W 当日历周。
- 先读取已经覆盖、RETRY 和未覆盖证据，再从明确起点继续；已经通过的内容不机械重学。
- 连续性比单次时长重要，身体状态差时允许缩短或暂停。
- 课程 PASS、算法债务和岗位证据分别记账，不能互相冒充或静默覆盖。

## 当前执行状态

- 实际学习和代码练习继续放在 `C:\Users\26823\Desktop\AI-Agent-Learning`。
- 当前课程状态：G8-00 已 `PASS`；R6-01 尚未启动。
- W5 算法审计仍为 `DEBT 4`（3 道新题 + 1 道旧题）；`WP-27 / WP-29` 已触发 `RECOVERY_BLOCK_PENDING`，下一独立算法 Session 一次只推进一个问题，未实际 PASS 前不扣债。
- W6 岗位审计仍为 `RETRY / INCOMPLETE`：10 条候选中只有 `4 HARD_ELIGIBLE + 6 UNKNOWN`，不计算正式匹配率。独立恢复 Session 后必须补齐恰好 10 条硬门槛已核清的可投样本，才能启动 R6-01。
- 稳定概念沉淀到 `D:\AI-Knowledge\02-Concepts`。
- 课程、路线和索引沉淀到 `D:\AI-Knowledge\03-Courses` 或 `D:\AI-Knowledge\01-Maps`。
- 长期偏好和学习原则沉淀到 `D:\AI-Knowledge\08-Memory`。

## 相关链接

- [[AI Agent 学习资源地图]]
- [[AI-Agent-Learning 跳转索引]]
- [[AI-Agent-Learning 关联方案]]
- [[../03-Courses/Agent/AI-Agent-Learning/README|AI-Agent-Learning 知识沉淀]]
- [[../07-Reviews/AI-Agent-Learning/2026-08-25-route-audit-review|2026-08-25 路线审计复盘]]
- [[../08-Memory/AI 学习原则]]
