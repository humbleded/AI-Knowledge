---
type: maintenance-log
topic: AI Knowledge
status: active
created: 2026-05-29
updated: 2026-06-08
tags:
  - 知识库
  - log
  - Karpathy
---

# AI Knowledge Log

按时间记录知识库的重要维护、ingest、结构调整和健康检查。它是 Karpathy 式 LLM Wiki 的操作日志。

## 2026-05-29

### Karpathy 工作流基础设施补齐

- 新增 [[raw/README|Raw Sources]]，用于保存不可变原始资料。
- 新增 [[00-Inbox/README|Inbox]]，用于临时收集和分拣。
- 新增 [[index|AI Knowledge Index]]，作为人和 LLM 的全局导航入口。
- 新增本日志，记录后续 ingest、lint 和结构调整。
- 更新计划：让知识库从“Obsidian 笔记库”升级为“LLM 可维护的 Markdown Wiki”。
- 新增 `.gitignore` 并初始化 Git 仓库，用于后续版本控制和回滚。

### 当前健康结论

- Markdown 文件约 70 个。
- 内部 wikilink 约 187 个，当前未发现断链。
- 主要短板是 raw/source 层、维护日志、来源标注、seed 笔记扩写和周期性健康检查。

### LLM/Karpathy 主线内容扩写

- 将 `02-Concepts/LLM` 的 7 张核心概念卡从 seed 扩写到 usable：
  - [[02-Concepts/LLM/backpropagation]]
  - [[02-Concepts/LLM/gradient-descent]]
  - [[02-Concepts/LLM/tokenization]]
  - [[02-Concepts/LLM/embedding]]
  - [[02-Concepts/LLM/attention]]
  - [[02-Concepts/LLM/transformer]]
  - [[02-Concepts/LLM/autoregressive-generation]]
- 扩写 Karpathy Zero to Hero 三个课程页：
  - [[03-Courses/LLM/Karpathy-Zero-to-Hero/01-micrograd]]
  - [[03-Courses/LLM/Karpathy-Zero-to-Hero/02-makemore]]
  - [[03-Courses/LLM/Karpathy-Zero-to-Hero/05-gpt-from-scratch]]
- 新增 [[03-Courses/LLM/Karpathy-Zero-to-Hero/README|Karpathy Zero to Hero]] 课程索引。
- 修正并更新 [[03-Courses/README|课程笔记索引]] 和 [[04-Projects/README|项目记录索引]]。

### Micrograd 项目记录入口

- 新增 [[04-Projects/LLM/micrograd-backprop-from-scratch|Micrograd：从零实现反向传播]]，作为 Karpathy Zero to Hero 第一段的实践记录。
- 更新 [[04-Projects/LLM/README|LLM 项目记录]]、[[03-Courses/LLM/Karpathy-Zero-to-Hero/01-micrograd|01 Micrograd]] 和 [[index|AI Knowledge Index]] 的反向链接。

### Raw Source、实验输出与健康检查自动化

- 从知识库已有外部链接抽取 [[raw/initial-link-sources|Initial Link Sources]]，作为 raw/source 的初始资料清单。
- 新增 Karpathy 相关 source notes：
  - [[raw/repos/karpathy-micrograd]]
  - [[raw/repos/karpathy-nn-zero-to-hero]]
  - [[raw/transcripts/karpathy-micrograd-video]]
- 新增可运行 micrograd 最小实现：
  - `04-Projects/LLM/micrograd/engine.py`
  - `04-Projects/LLM/micrograd/nn.py`
  - `04-Projects/LLM/micrograd/demo_scalar_graph.py`
  - `04-Projects/LLM/micrograd/demo_toy_mlp.py`
- 运行 micrograd demo，toy MLP loss 从 `5.230518` 降到 `0.021629`。
- 新增 `tools/check_vault.py`，用于自动检查 Markdown 数量、断链、frontmatter、status/type 分布和 raw source 数量。
- 本次健康检查结果写入 [[07-Reviews/Knowledge-Base/2026-05-29-vault-check-automation]]。

### Vault Check 严格模式升级

- 升级 `tools/check_vault.py`，新增 `errors` / `warnings` 分级和 `--strict` 模式。
- 新增检查：
  - raw source note 是否有 `source_url`。
  - raw/source 是否至少链接一个编译目标。
  - `usable`、`pass` 和核心索引页是否进入 `index.md`。
  - Git 是否跟踪了 `__pycache__`、`.pyc` 等生成文件。
  - `log.md` 是否记录 `check_vault.py`。
- 严格检查发现 `04-Projects/Python/AI-Agent-Learning/p0-03-scheduler.md` 未进入 `index.md`，已补入。
- 当前 `python tools\check_vault.py --root D:\AI-Knowledge --strict` 通过：0 errors，0 warnings。

### Web Clipper Raw Source Templates

- 新增 `Templates/web-clipper-ai-knowledge-raw-source.json`，用于无 API key 场景下把网页保存到 `raw/articles`。
- 新增 `Templates/web-clipper-ai-knowledge-raw-source-with-interpreter.json`，用于启用 Web Clipper Interpreter 后自动生成中文摘要和知识库整理建议。
- 两个模板均面向 `D:\AI-Knowledge` 的 raw/source 工作流，默认保存原文、来源、highlight、compile targets 和 next steps。

## 2026-05-30

### 全库中文辅助阅读规则

- 新增 [[08-Memory/全库中文辅助阅读规则]]，规定全库都可以补充中文辅助阅读，不限于 `raw/`。
- 核心策略：原文保留，中文理解追加；术语保留英文，中文解释辅助；代码永不翻译。
- 新增 [[06-Prompts/全库中文辅助阅读提示词]]，用于整理英文笔记时生成 `## 中文速读` 和 `## 关键术语`。
- 更新 `AGENTS.md`，让后续知识库维护和自动化任务遵守该翻译策略。

## 2026-05-31

### Weekly Maintenance

- 复查 [[00-Inbox/README|00-Inbox]]、[[raw/README|raw]]、[[index|index.md]]、[[log|log.md]] 和最近 Git 变更。
- 运行严格检查：
  - `& 'C:\Users\26823\AppData\Local\uv\cache\archive-v0\9__1AdRplGGYGwVO\Scripts\python.exe' tools\check_vault.py --root D:\AI-Knowledge --strict`
  - 结果：`OK: True`，`Markdown files: 93`，`Links: 451`，`Broken links: 0`，`Missing frontmatter: 0`。
- 当前没有新的 Inbox 条目或 raw/source 散落资料需要整理。
- 发现 `2026-05-30` 的备份提交意外删除了两份 Web Clipper 模板，现已恢复：
  - `Templates/web-clipper-ai-knowledge-raw-source.json`
  - `Templates/web-clipper-ai-knowledge-raw-source-with-interpreter.json`
- 本次维护结论写入 [[07-Reviews/Knowledge-Base/2026-05-31-weekly-maintenance]]。

## 2026-06-02

- 同步 AI-Agent-Learning 2026-06-02 P0-04 PASS：更新 Python 容器概念卡、阶段 0 课程页、项目记录和复盘记录。

## 2026-06-04

### AI 开发学习路线与学习原则

- 新增 [[01-Maps/AI 开发学习路线]]，把 AI 开发主线、工程基础支撑层、技术动态关注层和只记录不深入层合并成当前学习框架。
- 新增 [[08-Memory/AI 学习原则]]，记录长期目标、学习节奏和新技术处理规则。
- 同步更新 [[index]]、[[README]] 和 [[01-Maps/AI 知识库总地图]] 的入口链接。

### MCP 与 Python 官方文档入口整理

- 新增 MCP 官方文档 raw source：[[raw/articles/mcp-official-docs-intro]]。
- 新增 Python 3 官方文档 raw source：[[raw/articles/python-3-official-documentation]]。
- 新增 [[01-Maps/MCP/mcp-official-docs-map|MCP Official Docs Map]] 和 [[02-Concepts/MCP/model-context-protocol|Model Context Protocol]] 概念卡。
- 新增 [[01-Maps/Python/python-official-docs-map|Python Official Docs Map]] 和 [[03-Courses/Python/Python-Basics/python-core-reading-route|Python 官方手册核心阅读路线]]。
- 更新全局索引、总地图、raw source 索引、课程索引和概念卡索引。
- 运行 `python tools\check_vault.py --root D:\AI-Knowledge --strict`：`OK: True`，`Broken links: 0`，`Missing frontmatter: 0`。

## 2026-06-05

### Daily Practice 2026-06-04 PASS

- 批改 [[07-Reviews/Daily-Practice/2026-06-04-review]] 第四轮订正，最终判定 `PASS`。
- 新增 [[02-Concepts/Python/python-functions|Python 函数、参数与 return]]，沉淀 `return` vs `print`、函数参数、返回值、函数拆分和 `return` 缩进位置。
- 更新 [[02-Concepts/Python/README|Python 概念卡]] 与 [[index|AI Knowledge Index]]。

## 2026-06-06

### Daily Practice 2026-06-05 PASS

- 批改 [[07-Reviews/Daily-Practice/2026-06-05-review]] 第三轮订正，最终判定 `PASS`。
- 更新 [[02-Concepts/Python/python-functions|Python 函数、参数与 return]]，补充可测试函数、`score_answer()`、`redirect_stdout` 手动测试和普通空格缩进注意事项。
- 更新 [[02-Concepts/Python/python-list-dict-set|Python list、dict、set]]，补充访问方式对比和任务改名时同步迁移 `task_status` 的模式。
- 更新 [[index|AI Knowledge Index]]，补入容器概念卡入口。

## 2026-06-07

### Weekly Maintenance

- 复查 [[00-Inbox/README|00-Inbox]]、[[raw/README|raw]]、[[index|index.md]]、[[log|log.md]] 和最近 Git 变更。
- 运行 `python tools\check_vault.py --root D:\AI-Knowledge --strict`：
  - `OK: True`
  - `Markdown files: 110`
  - `Links: 576`
  - `Broken links: 0`
  - `Missing frontmatter: 0`
- 当前 `00-Inbox` 仍只有 `README.md`，没有新的临时资料待分拣。
- `raw/` 本周新增的官方文档 source notes 已有对应编译目标：
  - [[raw/articles/python-3-official-documentation]]
  - [[raw/articles/mcp-official-docs-intro]]
- 为上述两份英文 raw source 补充 `## 中文速读` 和 `## 关键术语`，落实全库中文辅助阅读规则。
- 新增本次周维护复盘 [[07-Reviews/Knowledge-Base/2026-06-07-weekly-maintenance]] 并更新全局索引。
- 完成编辑后再次运行严格检查：
  - `OK: True`
  - `Markdown files: 111`
  - `Links: 594`
  - `Broken links: 0`
  - `Missing frontmatter: 0`

## 2026-06-08

### Weekly Maintenance

- 复查 [[00-Inbox/README|00-Inbox]]、[[raw/README|raw]]、[[index|index.md]]、[[log|log.md]] 和最近 Git 变更。
- 运行 `python tools\check_vault.py --root D:\AI-Knowledge --strict`：
  - `OK: True`
  - `Markdown files: 111`
  - `Links: 594`
  - `Broken links: 0`
  - `Missing frontmatter: 0`
- 当前 `00-Inbox` 仍只有 `README.md`，没有新的临时资料待整理。
- `raw/` 当前没有新增 source notes 或失联编译目标；2026-06-07 已补中文辅助阅读的两份官方文档 raw notes 本轮继续保持有效。
- 新增本次周维护复盘 [[07-Reviews/Knowledge-Base/2026-06-08-weekly-maintenance]] 并更新全局索引。
