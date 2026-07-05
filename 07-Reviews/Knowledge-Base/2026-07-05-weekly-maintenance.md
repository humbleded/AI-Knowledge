---
type: review
topic: knowledge-base-weekly-maintenance
status: pass
created: 2026-07-05
updated: 2026-07-05
tags:
  - 知识库
  - Review
  - weekly-maintenance
  - Karpathy
---

# 2026-07-05 Weekly Maintenance

## 结论

本次维护确认知识库主体健康：没有断链、没有缺失 frontmatter，也没有误跟踪的生成文件。初始 strict check 只有 1 条索引覆盖警告，来源是 [[../../02-Concepts/LLM/函数调用(Function Calling)|函数调用]] 已进入主题 README 和 AI-Agent-Learning 跳转索引，但还没有被 [[../../index|AI Knowledge Index]] 直接引用。

已补全全局索引和总地图入口，并记录本周维护状态。

## 本次严格检查

巡检命令：

```powershell
python tools\check_vault.py --root D:\AI-Knowledge --strict
```

初始结果：

```text
OK: True
Markdown files: 164
Links: 1181
Broken links: 0
Missing frontmatter: 0
Raw non-index files: 7
Warnings:
- 1 important notes not referenced by index.md
```

警告明细：

- [[../../02-Concepts/LLM/函数调用(Function Calling)|函数调用：模型点菜、程序炒菜（Tool Calling）]]

完成索引修复和本维护复盘后的最终结果：

```text
OK: True
Markdown files: 165
Links: 1216
Broken links: 0
Missing frontmatter: 0
Raw non-index files: 7
Warnings: 0
```

## 材料巡检

- [[../../00-Inbox/README|00-Inbox]] 当前仍只有 `README.md`，没有新资料需要移动。
- [[../../raw/README|raw]] 当前有 7 个非索引 source notes；新增的 [[../../raw/conversations/deepseek-share-context-routing-jit|DeepSeek 分享对话]] 已标记 `processed`，保留 `source_url`，并链接到已编译的概念卡。
- 最近 Git 变化主要包括：PR2-03 分类与路由、S-03 上下文工程、PR2-04 结构化输出、DeepSeek 分享对话整理、T3-01 函数调用，以及 02-Concepts 文件名中文化。内容已沉淀到概念卡、课程页、项目记录、复盘页和地图。
- `.obsidian/`、`.claudian/` 与 `__pycache__/` 仍处于 ignored 状态，没有纳入本次提交。

## 中文辅助阅读

已复查 [[../../08-Memory/全库中文辅助阅读规则|全库中文辅助阅读规则]]。本周新增核心笔记以中文解释为主，同时保留 `Function Calling`、`Tool Calling`、`JSONDecodeError`、`TOOLS[name](**args)`、`role:"tool"`、`context engineering`、`JIT`、`Compaction`、路径、命令和 API 名等技术锚点。

raw 层新增对话摘要使用中文整理，但保留原始分享 URL 和已编译目标，不替换技术术语或代码。

## 本次处理

- 更新 [[../../index|index.md]]：补入 [[../../02-Concepts/LLM/函数调用(Function Calling)|函数调用]]、PR2-03 项目页、PR2-03 PASS 复盘和本周维护复盘。
- 更新 [[../../01-Maps/AI 知识库总地图|AI 知识库总地图]]：将 `Tool calling` 从占位文本改为函数调用概念卡入口。
- 修正 [[../../01-Maps/AI-Agent-Learning 跳转索引|AI-Agent-Learning 跳转索引]] frontmatter 中重复的 `updated` 字段。
- 新增本维护复盘页：[[2026-07-05-weekly-maintenance]]。

## 下一步

- 继续按 AI-Agent-Learning PASS 同步规则维护 `02-Concepts`、`03-Courses`、`04-Projects` 和 `07-Reviews`。
- 后续可优先补 `cross entropy`、`softmax`、`logits` 等 LLM 基础概念卡。
