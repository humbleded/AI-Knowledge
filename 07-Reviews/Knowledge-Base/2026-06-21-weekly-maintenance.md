---
type: review
topic: knowledge-base-weekly-maintenance
status: pass
created: 2026-06-21
updated: 2026-06-21
tags:
  - 知识库
  - Review
  - weekly-maintenance
  - Karpathy
---

# 2026-06-21 Weekly Maintenance

## 结论

本次维护完成了索引补齐、英文 raw source 中文辅助阅读，以及一处易变 API 规则的来源核验。

初始严格检查没有断链或 frontmatter 错误，但发现 4 个新增 `usable` LLM 概念卡未被 [[../../index|AI Knowledge Index]] 直接引用。它们已经进入 [[../../02-Concepts/LLM/README|LLM 概念卡索引]]，本轮继续补入全局索引和总地图，恢复严格模式通过条件。

## 本次严格检查

巡检命令：

```powershell
python tools\check_vault.py --root D:\AI-Knowledge --strict
```

初始结果：

```text
OK: True
Markdown files: 142
Links: 881
Broken links: 0
Missing frontmatter: 0
Raw non-index files: 6
Warnings: 4 important notes not referenced by index.md
```

涉及的 4 个概念卡：

- [[../../02-Concepts/LLM/message-roles-and-instruction-hierarchy|消息角色与指令优先级]]
- [[../../02-Concepts/LLM/llm-essence-and-hallucination|LLM 本质与幻觉]]
- [[../../02-Concepts/LLM/multi-turn-stateless-memory|多轮对话：接口无状态与客户端记忆]]
- [[../../02-Concepts/LLM/streaming-output|流式输出：stream=True 与逐 chunk 处理]]

修复后结果：

```text
OK: True
Markdown files: 143
Links: 920
Broken links: 0
Missing frontmatter: 0
Raw non-index files: 6
Warnings: 0
```

## 材料巡检

- [[../../00-Inbox/README|00-Inbox]] 当前仍只有说明页，没有新条目需要分拣。
- [[../../raw/README|raw]] 没有新增 source notes；6 个非索引 raw notes 均有 `source_url` 和 wiki 编译目标。
- [[../../raw/initial-link-sources|Initial Link Sources]] 仍作为后续 ingest 队列，本轮没有发现必须立即拆分的新材料。
- 2026-06-15 之后只有一次知识库备份提交，主要新增上述 4 个 LLM 概念卡，并扩充 Python JSON 序列化概念。
- 没有发现误跟踪的 `__pycache__`、`.pyc`、临时文件或 Obsidian workspace 本地状态。

## 中文辅助阅读

以下英文 source notes 已保留原文，并追加 `## 中文速读` 与 `## 关键术语`：

- [[../../raw/repos/karpathy-micrograd]]
- [[../../raw/repos/karpathy-nn-zero-to-hero]]
- [[../../raw/transcripts/karpathy-micrograd-video]]

代码、命令、路径、URL、API 名和英文专业词均保持原样，只在旁边补充中文解释。

## 来源核验与修正

[[../../02-Concepts/LLM/message-roles-and-instruction-hierarchy|消息角色与指令优先级]] 原先把 `system` 与 `developer` 写成完全同级的新旧名称。2026-06-21 对照 OpenAI 官方资料后，修正为：

- 当前 OpenAI Text Generation 文档明确 `developer` instructions 优先于 `user`。
- Reasoning Best Practices 说明从 `o1-2024-12-17` 开始，推理模型使用 `developer` messages 取代 `system` messages。
- Chat Completions、Responses API、不同模型和兼容供应商的角色支持不同，因此代码迁移时必须查对应供应商与模型文档。

来源：

- [OpenAI Text generation](https://developers.openai.com/api/docs/guides/text)
- [OpenAI Reasoning best practices](https://developers.openai.com/api/docs/guides/reasoning-best-practices)
- [OpenAI Model Spec](https://model-spec.openai.com/)

## 本次处理

- 更新 [[../../index|index.md]]：补入 4 个 LLM 概念卡和本次周维护入口。
- 更新 [[../../01-Maps/AI 知识库总地图|AI 知识库总地图]]：补入 LLM 幻觉、消息角色、多轮记忆和流式输出入口。
- 更新 [[../../02-Concepts/LLM/README|LLM 概念卡索引]]：修正 `system` / `developer` 摘要。
- 更新 [[../../log|log.md]]：记录巡检、来源核验、中文辅助阅读和健康检查。

## 下一步

- 后续学习 LLM API 时，优先使用供应商官方文档确认角色、流式字段和推理字段，不把兼容接口行为直接推广到所有模型。
- 继续按需处理 [[../../raw/initial-link-sources|Initial Link Sources]]，但保持 raw 输入层不被编译笔记覆盖。
