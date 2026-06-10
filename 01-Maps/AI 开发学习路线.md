---
type: learning-map
topic: AI 开发学习路线
status: active
created: 2026-06-04
updated: 2026-06-10
tags:
  - 学习路线
  - AI工程
  - AI-Agent
---

# AI 开发学习路线

这条路线面向长期成为 AI 开发工程师，目标不是追热点，而是持续提升工程能力和 AI 项目落地能力。

## 第一层：AI 开发主线

这些是当前重点学习内容，优先通过小项目和代码练习推进。

- Python 最小开发能力：函数、文件、异常、JSON、HTTP、venv。
- 大模型 API：环境变量、SDK、单轮、多轮、流式输出、错误处理。
- Prompt 与结构化输出：摘要、分类、JSON、schema。
- Tool Calling：让模型选择工具，让程序执行工具。
- 最小 Agent：ReAct、Planning、Reflection、停止条件和错误恢复。
- RAG、LangGraph、MCP：在有最小 Agent 经验后逐步推进。
- 项目实战

当前最短进入 Agent 的路径：

`P0-06 -> P0-07 -> P0-08 -> P0-09 -> P0-Gate -> L1 -> PR2 -> T3 -> A4`

阶段 0.5 的工程基础改为随用随补，不再整块卡住第一次进入大模型 API 和 Agent。

## 第二层：工程基础支撑

这些内容需要加入学习框架，但作为支撑层逐步补齐，不抢占 AI 主线。判断标准不是“先完整学完”，而是“当前 Agent/API 项目是否用得到”。

- 环境和命令行：在 `venv`、包安装、环境变量、路径、进程和日志排错时补。
- 网络基础：在 HTTP 请求、API 调用、tool API、timeout、status code 出问题时补。
- 数据库：在 Memory、学习记录持久化、RAG 元数据或聊天历史需要保存时补。
- Docker：在需要 PostgreSQL、本地多服务、部署、volume、network、logs 时补。
- FastAPI、Git、CI、日志、测试、部署：随着项目需要逐步补。

暂不深入：

- 数据库内核
- Linux 内核
- 高级网络协议
- 大规模分布式系统
- 复杂 Kubernetes

## 第三层：技术动态关注

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

## 第四层：只记录不深入

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

- 连续性比时长重要。
- 每天学习 10 分钟也算完成。
- 身体累就休息。
- 不追求每天学习很多。
- 避免因为压力过大而放弃学习。

## 当前执行方式

- 每日执行和代码练习继续放在 `C:\Users\26823\Desktop\AI-Agent-Learning`。
- 当前执行顺序：先补完 Python 后半段，再进入 L1 大模型 API；工程基础嵌入 Agent/API 项目中补齐。
- 稳定概念沉淀到 `D:\AI-Knowledge\02-Concepts`。
- 课程、路线和索引沉淀到 `D:\AI-Knowledge\03-Courses` 或 `D:\AI-Knowledge\01-Maps`。
- 长期偏好和学习原则沉淀到 `D:\AI-Knowledge\08-Memory`。

## 相关链接

- [[AI Agent 学习资源地图]]
- [[AI-Agent-Learning 跳转索引]]
- [[AI-Agent-Learning 关联方案]]
- [[../03-Courses/Agent/AI-Agent-Learning/README|AI-Agent-Learning 知识沉淀]]
- [[../08-Memory/AI 学习原则]]
