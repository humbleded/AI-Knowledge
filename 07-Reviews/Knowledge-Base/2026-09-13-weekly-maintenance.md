---
type: review
topic: Knowledge-Base Weekly Maintenance
status: usable
created: 2026-09-13
updated: 2026-09-13
source:
  - tools/check_vault.py
  - git log --since='2026-08-23'
tags:
  - 知识库
  - Review
  - weekly-maintenance
  - Karpathy
---

# 2026-09-13 Weekly Maintenance

## 范围与结论

本轮按 Karpathy 式 LLM Wiki 维护流程检查 `00-Inbox`、`raw`、`index.md`、`log.md`、近期 Git 历史和全库结构。结论是：知识库结构健康，9 月 8 日新增的问题导航、工作台项目页和重点概念整理已经接入主索引，本轮只补周维护记录与维护入口，不移动原始资料。

- 初始运行 `python tools\check_vault.py --root D:\AI-Knowledge --strict` 通过：232 个 Markdown、2303 个内部链接、0 个断链、0 个缺失 frontmatter、8 个 raw 非索引文件。
- [[../../00-Inbox/README|00-Inbox]] 仍只有 `README.md`，没有待分拣材料。
- [[../../raw/README|raw]] 仍是 8 个非索引 source notes，最近的原始会话资料仍是 2026-08-13 的 A4-Gate handoff；没有新 raw 需要编译或移动。
- 复核 2026-08-23 周维护后的 Git 变化：A4-Gate 正式 PASS、A4-Gate Canvas / SVG、路线审计、G8-00 LangGraph PASS、RAG 学习订正、统一工作台同步和问题导航整理都已经进入对应概念、课程、项目、复盘、索引与日志。
- 复核 [[2026-09-08-workbench-sync-check|工作台同步后的知识库检查]] 与 [[2026-09-08-question-navigation-check|问题导航与重点笔记整理检查]]：两份记录已经说明来源、范围、验证方式和不新增课程 PASS / 岗位证据的边界，本轮不重复建 raw 副本。
- 按 [[../../08-Memory/全库中文辅助阅读规则|全库中文辅助阅读规则]]抽查新增入口，保留 `LangGraph`、`StateGraph`、`Tool Calling`、`RAG`、`Provider/API`、`MAX_STEPS`、路径、命令和代码标识；没有发现需要硬翻译或补中文速读的英文块。

## 待清理队列

当前 `status: seed` 仍主要是模板、早期 Python 基础概念、Claude Skills 课程摘记和 HelloAgents 源码阅读索引。本轮没有新的学习证据证明这些 seed 可以升级，因此只记录为后续队列，不为了凑进度扩写。

- 模板类：[[../../Templates/课程笔记模板|课程笔记模板]]、[[../../Templates/概念笔记模板|概念笔记模板]]。
- Python 基础 seed：[[../../02-Concepts/Python/解释器(Interpreter)|解释器]]、[[../../02-Concepts/Python/输入与输出(input & print)|输入与输出]]、[[../../02-Concepts/Python/基础数据类型(Data Types)|基础数据类型]]、[[../../02-Concepts/Python/变量(Variables)|变量]]、[[../../02-Concepts/Python/类型转换(Type Conversion)|类型转换]]、[[../../02-Concepts/Python/f-string 格式化|f-string 格式化]]。
- 旧课程 / 项目 seed：[[../../03-Courses/Agent/Agent-Skills-with-Anthropic/Claude Skills：让 Agent 拥有可复用专业能力的方法|Claude Skills 课程摘记]]、[[../../04-Projects/Agent/AI-Agent-Learning/HelloAgents feature-branch-1 源码阅读索引|HelloAgents feature-branch-1 源码阅读索引]]。
- 旧 draft：[[../../03-Courses/Daily-Practice/2026-06-05-practice|2026-06-05 practice]] 仍是历史练习手册草稿，本轮没有改写。

## 本轮更新

- 新增本周维护记录，并更新 [[README|Knowledge-Base 维护复盘索引]]、[[../../index|全局索引]]、[[../../01-Maps/AI 知识库总地图|总地图]]与 [[../../log|维护日志]]。
- 不修改课程 PASS、用户独立能力证据、岗位证据、执行区进度或工作台实现。
- 最终严格检查通过：233 个 Markdown、2337 个内部链接、0 个断链、0 个缺失 frontmatter、8 个 raw 非索引文件。

返回 [[README|维护索引]]、[[../../index|全局索引]]、[[../../log|维护日志]]。
