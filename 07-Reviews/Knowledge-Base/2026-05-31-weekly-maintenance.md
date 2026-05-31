---
type: review
topic: knowledge-base-weekly-maintenance
status: pass
created: 2026-05-31
updated: 2026-05-31
tags:
  - 知识库
  - Review
  - weekly-maintenance
  - Karpathy
---

# 2026-05-31 Weekly Maintenance

## 结论

本周维护以健康检查和一致性修复为主。`00-Inbox` 当前为空，`raw/` 没有新增待编译资料；严格检查通过，知识库仍保持可导航、可维护、可继续扩写的状态。

## 本次严格检查

命令：

```powershell
& 'C:\Users\26823\AppData\Local\uv\cache\archive-v0\9__1AdRplGGYGwVO\Scripts\python.exe' tools\check_vault.py --root D:\AI-Knowledge --strict
```

结果：

```text
OK: True
Markdown files: 93
Links: 451
Broken links: 0
Missing frontmatter: 0
Raw non-index files: 4
Statuses: {'active': 47, 'pass': 8, 'seed': 10, 'usable': 10}
```

## 材料巡检

- [[../../00-Inbox/README|00-Inbox]] 当前没有新增临时资料。
- [[../../raw/README|raw]] 当前只有既有 source notes，没有新散落网页、论文或对话摘录需要搬运。
- [[../../index|index.md]] 与 [[../../log|log.md]] 仍覆盖核心入口和最近维护事项。

## 最近 Git 变化观察

- 最近的结构性变更集中在 `Add bilingual reading policy`、`Strengthen vault quality checks` 和 Web Clipper 模板。
- `2026-05-30` 的 `vault backup` 提交把两份 `Templates/web-clipper-ai-knowledge-raw-source*.json` 删掉了，但 [[../../log|log.md]] 仍把它们当作现存工作流能力记录。
- 本次已恢复这两份模板，避免“日志声称存在，但仓库实际缺失”的状态继续存在。

## 本次处理

- 恢复：
  - `Templates/web-clipper-ai-knowledge-raw-source.json`
  - `Templates/web-clipper-ai-knowledge-raw-source-with-interpreter.json`
- 补记本次周维护复盘，并更新全局索引与维护日志。
- 本轮未新增中文辅助阅读段落，因为本次没有新增英文主内容需要整理；既有“全库中文辅助阅读”规则继续适用。

## 下一步

- 下次 ingest 新网页或英文资料时，优先使用已恢复的 Web Clipper 模板进入 `raw/articles`。
- 后续若 `python` 仍不在 PATH，可考虑单独整理一条本机运行约定，避免维护脚本调用不稳定。
