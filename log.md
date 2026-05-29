---
type: maintenance-log
topic: AI Knowledge
status: active
created: 2026-05-29
updated: 2026-05-29
tags:
  - 知识库
  - log
  - Karpathy
---

# AI Knowledge Log

按时间记录知识库的重要维护、ingest、结构调整和健康检查。它是 Karpathy 式 LLM Wiki 的操作日志。

## 2026-05-29

### Karpathy 工作流基础设施补齐

- 新增 [[raw/README|Raw Sources]]，用于保存不可变原始资料。
- 新增 [[00-Inbox/README|Inbox]]，用于临时收集和分拣。
- 新增 [[index|AI Knowledge Index]]，作为人和 LLM 的全局导航入口。
- 新增本日志，记录后续 ingest、lint 和结构调整。
- 更新计划：让知识库从“Obsidian 笔记库”升级为“LLM 可维护的 Markdown Wiki”。
- 新增 `.gitignore` 并初始化 Git 仓库，用于后续版本控制和回滚。

### 当前健康结论

- Markdown 文件约 70 个。
- 内部 wikilink 约 187 个，当前未发现断链。
- 主要短板是 raw/source 层、维护日志、来源标注、seed 笔记扩写和周期性健康检查。

### LLM/Karpathy 主线内容扩写

- 将 `02-Concepts/LLM` 的 7 张核心概念卡从 seed 扩写到 usable：
  - [[02-Concepts/LLM/backpropagation]]
  - [[02-Concepts/LLM/gradient-descent]]
  - [[02-Concepts/LLM/tokenization]]
  - [[02-Concepts/LLM/embedding]]
  - [[02-Concepts/LLM/attention]]
  - [[02-Concepts/LLM/transformer]]
  - [[02-Concepts/LLM/autoregressive-generation]]
- 扩写 Karpathy Zero to Hero 三个课程页：
  - [[03-Courses/LLM/Karpathy-Zero-to-Hero/01-micrograd]]
  - [[03-Courses/LLM/Karpathy-Zero-to-Hero/02-makemore]]
  - [[03-Courses/LLM/Karpathy-Zero-to-Hero/05-gpt-from-scratch]]
- 新增 [[03-Courses/LLM/Karpathy-Zero-to-Hero/README|Karpathy Zero to Hero]] 课程索引。
- 修正并更新 [[03-Courses/README|课程笔记索引]] 和 [[04-Projects/README|项目记录索引]]。
