---
type: maintenance-log
topic: AI Knowledge
status: active
created: 2026-05-29
updated: 2026-06-21
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

## 2026-06-09

### AI-Agent-Learning P0-05 PASS

- 批改 `C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-06-09.md`，P0-05 函数、参数、返回值最终判定 `PASS`。
- 更新 [[02-Concepts/Python/python-functions|Python 函数、参数与 return]]，补充 P0-05 的函数拆分、返回值测试和 `days <= 0` 边界提醒。
- 新增 [[04-Projects/Python/AI-Agent-Learning/p0-05-plan-functions|P0-05 函数、参数、返回值]] 项目记录。
- 新增 [[07-Reviews/AI-Agent-Learning/2026-06-09-stage0-p0-05-pass-review|2026-06-09 阶段 0 复盘：P0-05]]。
- 更新 [[03-Courses/Python/AI-Agent-Learning/stage0-python-basics|阶段 0：Python 与开发环境]]、[[04-Projects/README|项目记录索引]] 和 [[index|AI Knowledge Index]]。

## 2026-06-10

### AI-Agent-Learning 路线调整：工程基础随用随补

- 调整 `C:\Users\26823\Desktop\AI-Agent-Learning` 的 tracker、progress 和 README：`B0-Gate` 不再作为进入 L1 的硬门槛。
- 新增 [[03-Courses/Agent/AI-Agent-Learning/stage0_5-engineering-basics|阶段 0.5：工程基础随用随补]]，记录 P0 后半段到 L1/API/Agent 的最短路径。
- 更新 [[01-Maps/AI 开发学习路线]] 和 [[08-Memory/AI 学习原则]]：工程基础作为支撑层，放到 API、Tool Calling、Memory、RAG、本地部署项目中按需补。
- 更新 [[03-Courses/Agent/AI-Agent-Learning/README|AI-Agent-Learning]]、[[03-Courses/README|课程笔记索引]]、[[01-Maps/AI-Agent-Learning 跳转索引]]、[[03-Courses/Python/AI-Agent-Learning/stage0-python-basics|阶段 0：Python 与开发环境]] 和 [[index|AI Knowledge Index]]。

### AI-Agent-Learning P0-06 PASS

- 批改 `C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-06-10.md`，P0-06 模块、第三方包、venv 判定 `PASS`。
- 新增 [[02-Concepts/Python/python-venv-pip-env|Python 项目环境管理：venv、pip 与 .env]]，沉淀虚拟环境、`pip install` 安装位置、`.env` 和 API Key 不硬编码。
- 新增 [[04-Projects/Python/AI-Agent-Learning/p0-06-env-check|P0-06 模块、第三方包、venv]] 项目记录。
- 新增 [[07-Reviews/AI-Agent-Learning/2026-06-10-stage0-p0-06-pass-review|2026-06-10 阶段 0 复盘：P0-06]]。
- 更新 [[03-Courses/Python/AI-Agent-Learning/stage0-python-basics|阶段 0：Python 与开发环境]]、[[03-Courses/Agent/AI-Agent-Learning/README|AI-Agent-Learning]]、[[04-Projects/README|项目记录索引]]、[[01-Maps/AI-Agent-Learning 跳转索引]] 和 [[index|AI Knowledge Index]]。

## 2026-06-11

### AI-Agent-Learning P0-07 PASS

- 批改 `C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-06-11.md`，P0-07 异常、调试、单元测试判定 `PASS`。
- 新增 [[02-Concepts/Python/python-exceptions-debugging-testing|Python 异常、调试与单元测试]]，沉淀 `try/except`、不要吞异常、调试与测试覆盖正常/异常场景。
- 新增 [[04-Projects/Python/AI-Agent-Learning/p0-07-safe-divide|P0-07 异常、调试、单元测试]] 项目记录。
- 新增 [[07-Reviews/AI-Agent-Learning/2026-06-11-stage0-p0-07-pass-review|2026-06-11 阶段 0 复盘：P0-07]]。
- 更新 [[03-Courses/Python/AI-Agent-Learning/stage0-python-basics|阶段 0：Python 与开发环境]]、[[03-Courses/Agent/AI-Agent-Learning/README|AI-Agent-Learning]]、[[04-Projects/README|项目记录索引]]、[[01-Maps/AI-Agent-Learning 跳转索引]] 和 [[index|AI Knowledge Index]]。

## 2026-06-13

### Python partial 概念卡

- 新增并整理 [[02-Concepts/Python/python-functools-partial|Python 偏函数 functools.partial 与默认参数]]。
- 补充 [[02-Concepts/Python/README|Python 概念卡]] 与 [[index|AI Knowledge Index]] 导航。

### Python and / or 短路与返回原值

- 新增 [[02-Concepts/Python/python-and-or-short-circuit|Python and / or 短路与返回原值]]，沉淀 `and` / `or` 返回原始操作数、短路行为和 `not > and > or` 优先级。
- 更新 [[02-Concepts/Python/README|Python 概念卡]] 与 [[index|AI Knowledge Index]] 导航。

### AI-Agent-Learning P0-08 PASS

- 同步 `C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-06-13.md`，P0-08 文件、JSON、CSV 判定 `PASS`。
- 新增 [[02-Concepts/Python/python-file-json-serialization|Python 文件读写与 JSON 序列化]]，沉淀文本文件与 JSON 的边界、`json.dumps()` / `json.loads()`、`ensure_ascii=False`、路径排查和编码注意点。
- 新增 [[04-Projects/Python/AI-Agent-Learning/p0-08-progress-file|P0-08 文件、JSON、CSV]] 项目记录。
- 新增 [[07-Reviews/AI-Agent-Learning/2026-06-13-stage0-p0-08-pass-review|2026-06-13 阶段 0 复盘：P0-08]]。
- 更新 [[03-Courses/Python/AI-Agent-Learning/stage0-python-basics|阶段 0：Python 与开发环境]]、[[03-Courses/Agent/AI-Agent-Learning/README|AI-Agent-Learning]]、[[04-Projects/README|项目记录索引]]、[[01-Maps/AI-Agent-Learning 跳转索引]] 和 [[index|AI Knowledge Index]]。

## 2026-06-14

### AI-Agent-Learning P0-Gate + L1-01 PASS

- 同步 `C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-06-14.md`，`P0-Gate Python 基础闯关` 与 `L1-01 API Key 与 SDK` 判定 `PASS`。
- 新增 [[02-Concepts/Python/python-json-learning-log-cli|Python JSON 学习日志 CLI：list[dict] 与输入校验]]，沉淀学习记录 CLI 的数据结构、输入校验、旧脏数据清理提醒。
- 新增 [[02-Concepts/LLM/api-key-and-sdk|API Key 与 SDK：调用模型的门禁卡和快递柜台]]，沉淀 API Key、模型名、SDK、环境变量和 GitHub 发布前的安全边界。
- 新增 [[04-Projects/Python/AI-Agent-Learning/p0-09-http-request|P0-09 HTTP 请求]]、[[04-Projects/Python/AI-Agent-Learning/p0-gate-learning-log|P0-Gate Python 基础闯关]] 与 [[04-Projects/LLM/AI-Agent-Learning/l1-01-first-call|L1-01 API Key 与 SDK]] 项目记录。
- 新增 [[03-Courses/LLM/AI-Agent-Learning/stage1-llm-api-basics|阶段 1：大模型 API 入门]]。
- 新增 [[07-Reviews/AI-Agent-Learning/2026-06-14-stage0-p0-gate-l1-01-pass-review|2026-06-14 阶段 0 / 阶段 1 复盘：P0-Gate + L1-01]]。
- 更新 [[03-Courses/Python/AI-Agent-Learning/stage0-python-basics|阶段 0：Python 与开发环境]]、[[03-Courses/Agent/AI-Agent-Learning/README|AI-Agent-Learning]]、[[03-Courses/README|课程笔记索引]]、[[04-Projects/README|项目记录索引]]、[[04-Projects/LLM/README|LLM 项目记录]]、[[01-Maps/AI-Agent-Learning 跳转索引]] 和 [[index|AI Knowledge Index]]。
- 完成后运行 `python tools\check_vault.py --root D:\AI-Knowledge --strict`：
  - `OK: True`
  - `Markdown files: 135`
  - `Links: 832`
  - `Broken links: 0`
  - `Missing frontmatter: 0`

## 2026-06-15

### Weekly Maintenance

- 复查 [[00-Inbox/README|00-Inbox]]、[[raw/README|raw]]、[[index|index.md]]、[[log|log.md]] 和最近 Git 变更。
- 初始运行 `python tools\check_vault.py --root D:\AI-Knowledge --strict`：
  - `OK: True`
  - `Markdown files: 137`
  - `Links: 835`
  - `Broken links: 0`
  - `Missing frontmatter: 0`
  - 警告：1 个重要笔记未被 `index.md` 引用。
- 当前 `00-Inbox` 仍只有 `README.md`，没有新的临时资料待分拣。
- `raw/` 当前没有新增 source notes 或失联编译目标；非索引 raw notes 仍为 6 个。
- 6 月 8 日之后的主要变化来自 AI-Agent-Learning PASS 同步，已沉淀到概念卡、课程页、项目记录和复盘页。
- 修复索引警告：将 [[02-Concepts/Engineering/README|Engineering 概念卡]] 与 [[02-Concepts/Engineering/debugging-triage|调试与错误恢复：系统化 triage]] 补入 [[index|AI Knowledge Index]]，并同步补入 [[01-Maps/AI 知识库总地图|AI 知识库总地图]]。
- 新增本次周维护复盘 [[07-Reviews/Knowledge-Base/2026-06-15-weekly-maintenance]]。
- 完成编辑后再次运行严格检查：
  - `OK: True`
  - `Markdown files: 138`
  - `Links: 859`
  - `Broken links: 0`
  - `Missing frontmatter: 0`
  - `Warnings: 0`

## 2026-06-21

### Weekly Maintenance

- 复查 [[00-Inbox/README|00-Inbox]]、[[raw/README|raw]]、[[index|index.md]]、[[log|log.md]] 和 2026-06-15 之后的 Git 变化。
- 初始运行 `python tools\check_vault.py --root D:\AI-Knowledge --strict`：
  - `OK: True`
  - `Markdown files: 142`
  - `Links: 881`
  - `Broken links: 0`
  - `Missing frontmatter: 0`
  - 警告：4 个 `usable` LLM 概念卡未被 `index.md` 直接引用。
- 当前 `00-Inbox` 仍只有 `README.md`；`raw/` 没有新增 source notes，6 个非索引 raw notes 均有来源和编译目标。
- 将 [[02-Concepts/LLM/message-roles-and-instruction-hierarchy|消息角色与指令优先级]]、[[02-Concepts/LLM/llm-essence-and-hallucination|LLM 本质与幻觉]]、[[02-Concepts/LLM/multi-turn-stateless-memory|多轮对话：接口无状态与客户端记忆]]、[[02-Concepts/LLM/streaming-output|流式输出]] 补入全局索引和相关地图。
- 根据 OpenAI 官方文档修正 `system` / `developer` 的版本边界：`developer` 高于 `user`，但不能把 `system` 与 `developer` 无条件视为跨模型、跨供应商完全同义。
- 为 3 份英文 raw source 补充 `## 中文速读` 和 `## 关键术语`，保留原文、URL、技术术语和编译目标：
  - [[raw/repos/karpathy-micrograd]]
  - [[raw/repos/karpathy-nn-zero-to-hero]]
  - [[raw/transcripts/karpathy-micrograd-video]]
- 新增本次维护复盘 [[07-Reviews/Knowledge-Base/2026-06-21-weekly-maintenance]]。
- 完成编辑后再次运行严格检查：
  - `OK: True`
  - `Markdown files: 143`
  - `Links: 920`
  - `Broken links: 0`
  - `Missing frontmatter: 0`
  - `Warnings: 0`
