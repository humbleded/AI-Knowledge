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

已新增 `tools/check_vault.py`，可以自动检查 Obsidian/LLM Wiki 的基础健康状态。

## 本次运行结果

```text
Markdown files: 90
Links: 435
Broken links: 0
Missing frontmatter: 2
Raw non-index files: 4
```

缺 frontmatter 的文件：

- `AGENTS.md`
- `README.md`

这两个文件是仓库级说明文件，当前可以接受。

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
```

## 下一步

- 把健康检查脚本纳入每次提交前的手动检查。
- 后续可以增加“新增核心页是否更新 `index.md` / `log.md`”的检查。
- 后续可以增加“raw source 是否至少链接一个 compile target”的检查。
