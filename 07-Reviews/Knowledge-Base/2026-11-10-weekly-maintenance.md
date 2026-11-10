---
type: maintenance-review
topic: Knowledge-Base
status: reviewed
created: 2026-11-10
tags:
  - 知识库
  - Review
  - weekly-maintenance
  - Karpathy
---

# 2026-11-10 Weekly Maintenance

## 检查结论

- 初始严格检查通过：235 个 Markdown、2,432 个内部链接、0 个断链、0 个缺失 frontmatter、8 个 raw 非索引文件。
- [[../../00-Inbox/README|00-Inbox]] 仍只有 `README.md`；没有新的临时材料需要分拣。
- [[../../raw/README|raw]] 的 8 份非索引 source notes 均早于本轮；没有新的原始资料需要保留、编译或移动。
- 本轮开始时工作树干净；`main` 与 `origin/main` 同步，最近一次知识库提交仍为 `1f92754`（2026-10-28 周维护）。

## 本轮整理

- 复核 [[../../08-Memory/全库中文辅助阅读规则|全库中文辅助阅读规则]]：规则适用于全库 Markdown。由于本轮没有新英文资料，不额外添加中文速读；既有 English technical anchors、代码、命令、路径、URL、API 名称与 wikilink 均未被硬翻译或改写。
- 复核 `index.md`、[[../../01-Maps/AI 知识库总地图|总地图]]、[[README|维护复盘索引]]与 [[../../log|维护日志]]，将它们更新到本次已验证的维护记录。
- `status: seed` 仍为 5 个页面：两份模板、标签命名规范、历史 Claude Skills 摘记与 HelloAgents 源码阅读索引。它们缺少新的学习或源码证据，本轮不以时间推移为由升级状态或补造内容。

## 遗留关注

- 之后出现新的学习通过证据、源码阅读产出或 raw/source 时，再判断是否应新建或更新概念卡、课程页、项目页或复盘；维护检查不等同于课程 PASS 或岗位能力证据。
- 历史 Claude Skills 摘记继续只作为既有资料保留，不扩展为当前 Codex 维护范围。

## 最终检查

- `python tools\check_vault.py --root D:\AI-Knowledge --strict` 通过：235 个 Markdown、2,432 个内部链接、0 个断链、0 个缺失 frontmatter、8 个 raw 非索引文件。
- `git diff --check` 通过；无 checker warning。
