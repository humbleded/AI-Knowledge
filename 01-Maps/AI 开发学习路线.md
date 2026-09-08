---
type: learning-map
topic: AI 开发学习路线
status: active
created: 2026-06-04
updated: 2026-09-08
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

截至 2026-09-05，A4-Gate 与阶段 4.5 的 G8-00 都已正式 `PASS`。09-05 的历史安排曾要求先完成独立算法恢复和 W6 岗位审计，再启动 R6-01；该先后限制已被后续路线校准替代。当前课程、算法与岗位审计分别接力，岗位资料缺口不阻塞技术前置已满足的课程。

## A4 后依赖主线

`G8-00` 使用阶段 8 编号，是因为它属于后续 LangGraph 旗舰；课程位置实际是阶段 4.5。它只迁移已经学会的控制循环，不代表阶段 5～7 被跳过。

```text
G8-00 Graph 基础（阶段 4.5，PASS）
  → R6-01 现成 Loader 最小图、处理与切分 → BE5-01 工程结构、日志与测试
    （当前已授权的统一 Vue/FastAPI 工作台持续展示真实成果）
  → R6-02 本地检索切片 → R6-03 最小问答切片
  → B0-01/03/04/Gate → BE5-04 PostgreSQL + pgvector
  → R6-02 剩余标准/S-02 → R6-03 剩余标准/S-06 RAG 对照
  → BE5-02/03 在共享入口补齐 FastAPI、Pydantic、SSE
  → G8-01/02/03 durable Graph、恢复与 HITL
  → BE5-05/BE5-Gate → R6-Gate
  → D7-01 编排取舍 → D7-02/S-04 多 Agent 受控对照 → G8-Gate
  → D7-03 四类记忆与图片/音频 → D7-Gate
  → M9 MCP → E10 评估与系统设计
  → J11-02 冻结集成产品发布范围 → J11-03/04/05 前端、上线与观测
  → S-05 正式收口 → J11-06
  → FINAL-Gate → J11-07 → J11-08 → J11-Gate
```

以上是 2026-09-08 校准后的成果导航，精确顺序与挂载条件以执行区 [weekly-plan.md](https://github.com/humbleded/AI-Agent-Learning/blob/main/tracker/weekly-plan.md) 为准。算法恢复和 W6 岗位审计独立推进，不作为上图的额外阻塞步骤。`S-01` 可并行补第二个模型提供方，未完成时不阻塞已有能力支持的产品化工作，仍须在 FINAL 前收口。

`J11-01` 从真实项目开发开始持续累计 Git/PR/CI/review 证据，最晚在 J11-06 前收口。`H5-01` 只在真实框架调用链阻塞时追一条源码路径，不是必经阶段。

## 两个旗舰与产品边界

- 两个业务旗舰统一使用 LangChain 现成组件 + LangGraph 显式流程，分别保留业务核心、目录、测试和验收重点；文件读取也优先使用现成 Loader，不先另写一套同功能组件再迁移。
- 工程文档 RAG 助手重点证明文档导入、检索、引用、权限、固定两步与 Agentic RAG 对照、评估和部署。
- 故障诊断与变更评审 Agent 重点证明显式状态图、路由/循环/停止、stream、持久化、interrupt/resume、幂等和恢复。
- G8-00 已完成该旗舰的无持久化 v1：[[../02-Concepts/Agent/LangGraph 状态图编排(StateGraph)|StateGraph 基础概念]]与[[../04-Projects/Agent/AI-Agent-Learning/g8-00-incident-change-review-agent-v1|可运行项目]]已经闭合；持久化、恢复和 HITL 仍未提前宣称完成。
- 两个项目的后端统一使用 Python，FastAPI 是共同的 HTTP/SSE/认证/输入校验交付层，业务核心仍能脱离 HTTP 独立运行与测试。
- E10 只建设一套共享评估框架，再接两个领域适配层；不为了评估另建第三个项目。
- 唯一集成产品已固定为 `product_flagship=agent_workbench`；两个业务共享一个 Vue 应用、FastAPI 入口、发布链和观测入口。J11-02 根据两个旗舰的实际证据冻结发布范围、默认展示业务 `default_showcase` 与质量要求，不再二选一排除另一业务的前端或上线。
- 用户已采用任务指挥台、知识研究工作室、可视流程画布全部三个工作模式，按用途切换；它们共用同一后端与当前页内问答。当前助手交付见 [[04-Projects/Agent/AI-Agent-Learning/workbench-knowledge-agent|统一工作台与知识库 Agent]]，采用三个模式不表示 Memory 等未来功能已实现。
- 用户会一些 Vue，自述不替代证据。对已启动且明确授权的界面/HTTP 交付，助手审查来源、许可证、维护状态、依赖与安全边界后可以实施，用户沿真实链路补尚未证明的解释与修改能力；不逐字段等待审批，助手搭建不计用户 PASS。BE5/J11 复用已有独立证据并补齐完整标准，未启动功能不提前囤积代码。

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
- 当前课程状态只认执行区 [progress.md](https://github.com/humbleded/AI-Agent-Learning/blob/main/tracker/progress.md)；2026-09-08 接力为 R6-01 学习中、G2 单题通过、G3 Loader 最小图待用户实现。助手完成的知识库与前端演示不改变课程 PASS。
- 算法恢复与剩余债务读取 `tracker/algorithm-progress.md` 和 `tracker/weak-points.md`，不在此重新排期或扣债。09-05 历史快照的 `DEBT 4` 与 `RECOVERY_BLOCK_PENDING` 已由后续真实复测更新，不再作为当前状态。
- W6 岗位审计以 `tracker/job-readiness.md` 为准；样本不齐时保持独立待补、不计算正式匹配率，不阻塞已满足前置的 R6-01。它仍是后续求职就绪的验收事项。
- 稳定概念沉淀到 `D:\AI-Knowledge\02-Concepts`。
- 课程、路线和索引沉淀到 `D:\AI-Knowledge\03-Courses` 或 `D:\AI-Knowledge\01-Maps`。
- 长期偏好和学习原则沉淀到 `D:\AI-Knowledge\08-Memory`。

## 相关链接

- [[AI Agent 学习资源地图]]
- [[AI-Agent-Learning 跳转索引]]
- [[AI-Agent-Learning 关联方案]]
- [[04-Projects/Agent/AI-Agent-Learning/workbench-knowledge-agent|统一工作台与知识库 Agent]]
- [[../03-Courses/Agent/AI-Agent-Learning/README|AI-Agent-Learning 知识沉淀]]
- [[../07-Reviews/AI-Agent-Learning/2026-08-25-route-audit-review|2026-08-25 路线审计复盘]]
- [[../08-Memory/AI 学习原则]]
