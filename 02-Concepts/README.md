---
type: map
topic: Concepts
status: active
created: 2026-05-28
tags:
  - 知识库
  - 概念卡
---

# 概念卡片索引

概念卡按主题域分目录保存，避免所有概念堆在根目录。

## 分类

- [[Python/README|Python]]
- [[LLM/README|LLM]]
- [[Agent/README|Agent]]
- [[MCP/README|MCP]]
- [[Engineering/README|Engineering]]

## 规则

- 一张卡只讲一个概念。
- 文件名使用「中文(短英文)」，如 `分词(Tokenization).md`；本身就是英文术语的保留英文（如 `Transformer.md`、`match-case 分支.md`）。旧英文名保留在 frontmatter `aliases:`。
- 新增概念时优先放进已有主题目录；如果主题目录不存在，再新建目录和 `README.md`。
- 课程笔记不要直接堆到这里，应放到 `03-Courses`，只把可复用概念抽成卡片。
