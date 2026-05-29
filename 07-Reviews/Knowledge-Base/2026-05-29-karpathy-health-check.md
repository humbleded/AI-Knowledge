---
type: review
topic: knowledge-base-health-check
status: active
created: 2026-05-29
updated: 2026-05-29
tags:
  - 知识库
  - Review
  - Karpathy
---

# 2026-05-29 Karpathy 知识库健康检查

## 结论

当前知识库已经具备 Karpathy 式 LLM Wiki 的基本骨架：Markdown、Obsidian、规则文件、地图页、概念卡、课程页、项目页和复盘页都已经存在。

它还需要补强工作流层：raw/source、全局 index、log、健康检查、来源标注和 seed 笔记扩写。

## 已完成修正

- 新增 [[../../raw/README|Raw Sources]]。
- 新增 [[../../00-Inbox/README|Inbox]]。
- 新增 [[../../index|AI Knowledge Index]]。
- 新增 [[../../log|AI Knowledge Log]]。
- 新增 [[../../Templates/知识库健康检查模板|知识库健康检查模板]]。

## 检查结果

- Markdown 文件：约 70 个。
- 内部 wikilink：约 187 个。
- 断链：当前未发现。
- 结构：`00-08` 分层清晰。
- 内容：LLM 和 Karpathy 课程相关页面多数仍是 seed 状态，需要从课程、代码实验和原始资料继续扩写。

## 下一步优先级

1. 为 Karpathy Zero to Hero 每个课程页补来源、学习目标、代码实验、关联概念。
2. 把 LLM seed 概念卡扩写到 usable 状态。
3. 每次新增资料先进入 `raw/`，再由 LLM 编译进 wiki。
4. 每周运行一次健康检查，并把结果写入 `07-Reviews/Knowledge-Base/`。

## 相关入口

- [[../../index]]
- [[../../01-Maps/Karpathy AI 学习路线]]
- [[../../01-Maps/AI 知识库总地图]]
- [[../../02-Concepts/LLM/README]]
