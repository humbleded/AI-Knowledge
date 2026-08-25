---
type: map
topic: AI Agent 学习资源
status: active
created: 2026-05-28
updated: 2026-08-25
tags:
  - AI-Agent
  - Python
  - 学习路线
---

# AI Agent 学习资源地图

这页用于把外部教程、GitHub 仓库和本地执行区 `C:\Users\26823\Desktop\AI-Agent-Learning` 连接起来。

## 总判断

这些资源都值得进知识库，但进入方式不同：

- Python 基础资料：沉淀为课程索引和概念卡。
- Agent 教程仓库：沉淀为中文学习索引、阶段映射和阅读顺序。
- 代码仓库：保留本地路径，不全文复制；重点整理源码阅读入口、运行目标和可复用结论。
- 英文资料：用中文摘要和翻译索引进入知识库，原文保留链接。

## 资源清单

| 资源 | 语言状态 | 知识库入口 | 对应阶段 |
|---|---|---|---|
| 廖雪峰 Python 教程 | 中文 | [[../03-Courses/Python/Python-Basics/廖雪峰 Python 教程]] | P0 |
| CS50P Weeks | 英文，已做中文索引 | [[../03-Courses/Python/Python-Basics/CS50P Weeks 中文学习索引]] | P0 |
| Datawhale hello-agents | 中文 | [[../03-Courses/Agent/AI-Agent-Learning/Datawhale hello-agents 中文学习索引]] | A4-H5-R6-M9-E10 |
| Agent-Learning-Hub | 中英混合，中文说明为主 | [[../03-Courses/Agent/AI-Agent-Learning/Agent-Learning-Hub 中文路线索引]] | 全局路线 |
| HelloAgents feature-branch-1 | 中文代码项目 | [[../04-Projects/Agent/AI-Agent-Learning/HelloAgents feature-branch-1 源码阅读索引]] | H5 |
| Agentic Design Patterns | 中文翻译项目 | [[../03-Courses/Agent/AI-Agent-Learning/Agentic Design Patterns 中文模式索引]] | D7 |
| Hugging Face agents-course | 英文为主，本地含 zh-CN | [[../03-Courses/Agent/AI-Agent-Learning/Hugging Face agents-course 中文学习索引]] | L1-G8-R6-E10 |

## 当前使用顺序

P0～A4 已完成，不再按旧的资源目录顺序重新学习。A4 后的真实顺序以执行区 `tracker/daily-plan.md` 和 `tracker/learning-resources.md` 为准：先核验当前任务的官方资料，再把本页已有教程当补充阅读。

1. G8-00：先学显式 Graph 的 typed state、node/edge、路由、停止和 stream；只迁移已通过的 Agent 控制循环。
2. R6/BE5/B0：围绕工程文档 RAG 旗舰，按需要使用 LangChain、数据库、FastAPI 和工程资料。
3. G8 durable 切片：回到 LangGraph 旗舰补持久化、恢复、HITL 和幂等。
4. D7/M9/E10：在已有两个旗舰上补编排取舍、长期 Memory、MCP 与共享评估框架。
5. H5 不是固定步骤；只有真实框架问题需要时，才阅读 HelloAgents 的一条相关调用链。

资源索引只回答“去哪里读”，不能代替任务 PASS、真实代码或可执行验证。

## 入库规则

每个资源先保留“索引笔记”，等你完成对应任务 PASS 后，再沉淀为：

- 概念卡：放入 `02-Concepts`
- 项目记录：放入 `04-Projects`
- 阶段复盘：放入 `07-Reviews`
- 提示词和流程：放入 `06-Prompts`
