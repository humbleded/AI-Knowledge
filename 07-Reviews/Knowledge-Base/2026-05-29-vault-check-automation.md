---
type: review
topic: knowledge-base-health-check
status: pass
created: 2026-05-29
updated: 2026-05-29
tags:
  - 知识库
  - Review
  - Karpathy
  - automation
---

# 2026-05-29 Vault Check Automation

## 结论

已将 `tools/check_vault.py` 从基础统计脚本升级为提交前质量门禁。现在它不仅检查断链，还检查 raw/source 编译闭环、重要页是否进入 `index.md`、生成文件是否被 Git 跟踪，以及 `log.md` 是否记录自动化脚本。

本次 `--strict` 检查通过：0 errors，0 warnings。

## 本次运行结果

```text
OK: True
Markdown files: 90
Links: 436
Broken links: 0
Missing frontmatter: 0
Raw non-index files: 4
Warnings: 0
Errors: 0
```

## 自动化能力

当前脚本检查：

- 是否存在 `index.md`、`log.md`、`AGENTS.md`。
- Obsidian wikilink 是否断链。
- Markdown frontmatter 是否缺失，允许 `README.md` 和 `AGENTS.md` 作为仓库级说明例外。
- raw source note 是否有 `source_url`。
- raw/source 是否至少链接一个编译目标，例如 `02-Concepts`、`03-Courses`、`04-Projects`。
- `usable` / `pass` / 核心索引页是否被 `index.md` 引用。
- Git 是否跟踪了 `__pycache__`、`.pyc` 等生成文件。
- `log.md` 是否记录 `check_vault.py`。

## Raw Source 进展

当前已有 raw 非索引资料：

- [[../../raw/initial-link-sources]]
- [[../../raw/repos/karpathy-micrograd]]
- [[../../raw/repos/karpathy-nn-zero-to-hero]]
- [[../../raw/transcripts/karpathy-micrograd-video]]

## 自动化命令

```powershell
cd D:\AI-Knowledge
python tools\check_vault.py --root D:\AI-Knowledge
python tools\check_vault.py --root D:\AI-Knowledge --json
python tools\check_vault.py --root D:\AI-Knowledge --strict
```

## 修复记录

- `--strict` 首次运行发现 `04-Projects/Python/AI-Agent-Learning/p0-03-scheduler.md` 没有进入 `index.md`。
- 已将它补入全局索引。
- 再次运行 `--strict` 后通过。

## 下一步

- 后续可以把 `--strict` 检查接入 Git pre-commit hook。
- 后续可以增加外部 URL 可达性检查。
- 后续可以增加“source note 的 source_url 是否可访问”的网络检查模式。
