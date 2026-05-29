---
type: source-index
topic: raw sources
status: active
created: 2026-05-29
updated: 2026-05-29
tags:
  - 知识库
  - source
  - Karpathy
---

# Raw Sources

这里保存未改写的原始资料，作为 Karpathy 式 LLM Wiki 的输入层。

## 原则

- 原始资料尽量保持不可变：不要在这里直接改写结论。
- 编译后的知识放入 `01-Maps`、`02-Concepts`、`03-Courses`、`04-Projects`、`05-Papers`、`07-Reviews`。
- 每次从 raw 资料生成或更新知识页后，在 [[../log|log]] 记录一次操作。
- 如果资料只是临时想法或待分拣内容，先放 [[../00-Inbox/README|00-Inbox]]。

## 建议子目录

- `articles/`：网页文章、博客、教程。
- `papers/`：论文 PDF 转 Markdown、论文摘录。
- `transcripts/`：视频字幕、课程转写。
- `repos/`：代码仓库阅读摘录。
- `conversations/`：值得沉淀的 AI 对话摘要。

## Ingest 检查

处理一份 raw 资料时，至少回答：

- 这份资料的主张是什么？
- 它更新了哪些已有笔记？
- 它应该产生哪些新概念卡、课程页、项目记录或复盘？
- 哪些内容需要保留来源，不应当只靠记忆复述？

## 相关入口

- [[initial-link-sources|Initial Link Sources]]
- [[../index|全局索引]]
- [[../01-Maps/AI 知识库总地图]]
- [[../01-Maps/Karpathy AI 学习路线]]
