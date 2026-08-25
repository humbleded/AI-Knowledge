---
type: maintenance-log
topic: AI Knowledge
status: active
created: 2026-05-29
updated: 2026-08-22
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
  - [[02-Concepts/LLM/反向传播(Backprop)]]
  - [[02-Concepts/LLM/梯度下降(Gradient Descent)]]
  - [[02-Concepts/LLM/分词(Tokenization)]]
  - [[02-Concepts/LLM/嵌入(Embedding)]]
  - [[02-Concepts/LLM/注意力机制(Attention)]]
  - [[02-Concepts/LLM/Transformer]]
  - [[02-Concepts/LLM/自回归生成(Autoregressive)]]
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
- 新增 [[01-Maps/MCP/mcp-official-docs-map|MCP Official Docs Map]] 和 [[02-Concepts/MCP/MCP(Model Context Protocol)|Model Context Protocol]] 概念卡。
- 新增 [[01-Maps/Python/python-official-docs-map|Python Official Docs Map]] 和 [[03-Courses/Python/Python-Basics/python-core-reading-route|Python 官方手册核心阅读路线]]。
- 更新全局索引、总地图、raw source 索引、课程索引和概念卡索引。
- 运行 `python tools\check_vault.py --root D:\AI-Knowledge --strict`：`OK: True`，`Broken links: 0`，`Missing frontmatter: 0`。

## 2026-06-05

### Daily Practice 2026-06-04 PASS

- 批改 [[07-Reviews/Daily-Practice/2026-06-04-review]] 第四轮订正，最终判定 `PASS`。
- 新增 [[02-Concepts/Python/函数与参数(Functions)|Python 函数、参数与 return]]，沉淀 `return` vs `print`、函数参数、返回值、函数拆分和 `return` 缩进位置。
- 更新 [[02-Concepts/Python/README|Python 概念卡]] 与 [[index|AI Knowledge Index]]。

## 2026-06-06

### Daily Practice 2026-06-05 PASS

- 批改 [[07-Reviews/Daily-Practice/2026-06-05-review]] 第三轮订正，最终判定 `PASS`。
- 更新 [[02-Concepts/Python/函数与参数(Functions)|Python 函数、参数与 return]]，补充可测试函数、`score_answer()`、`redirect_stdout` 手动测试和普通空格缩进注意事项。
- 更新 [[02-Concepts/Python/list·dict·set 容器|Python list、dict、set]]，补充访问方式对比和任务改名时同步迁移 `task_status` 的模式。
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
- 更新 [[02-Concepts/Python/函数与参数(Functions)|Python 函数、参数与 return]]，补充 P0-05 的函数拆分、返回值测试和 `days <= 0` 边界提醒。
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
- 新增 [[02-Concepts/Python/环境管理(venv & pip)|Python 项目环境管理：venv、pip 与 .env]]，沉淀虚拟环境、`pip install` 安装位置、`.env` 和 API Key 不硬编码。
- 新增 [[04-Projects/Python/AI-Agent-Learning/p0-06-env-check|P0-06 模块、第三方包、venv]] 项目记录。
- 新增 [[07-Reviews/AI-Agent-Learning/2026-06-10-stage0-p0-06-pass-review|2026-06-10 阶段 0 复盘：P0-06]]。
- 更新 [[03-Courses/Python/AI-Agent-Learning/stage0-python-basics|阶段 0：Python 与开发环境]]、[[03-Courses/Agent/AI-Agent-Learning/README|AI-Agent-Learning]]、[[04-Projects/README|项目记录索引]]、[[01-Maps/AI-Agent-Learning 跳转索引]] 和 [[index|AI Knowledge Index]]。

## 2026-06-11

### AI-Agent-Learning P0-07 PASS

- 批改 `C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-06-11.md`，P0-07 异常、调试、单元测试判定 `PASS`。
- 新增 [[02-Concepts/Python/异常·调试·测试(Exceptions)|Python 异常、调试与单元测试]]，沉淀 `try/except`、不要吞异常、调试与测试覆盖正常/异常场景。
- 新增 [[04-Projects/Python/AI-Agent-Learning/p0-07-safe-divide|P0-07 异常、调试、单元测试]] 项目记录。
- 新增 [[07-Reviews/AI-Agent-Learning/2026-06-11-stage0-p0-07-pass-review|2026-06-11 阶段 0 复盘：P0-07]]。
- 更新 [[03-Courses/Python/AI-Agent-Learning/stage0-python-basics|阶段 0：Python 与开发环境]]、[[03-Courses/Agent/AI-Agent-Learning/README|AI-Agent-Learning]]、[[04-Projects/README|项目记录索引]]、[[01-Maps/AI-Agent-Learning 跳转索引]] 和 [[index|AI Knowledge Index]]。

## 2026-06-13

### Python partial 概念卡

- 新增并整理 [[02-Concepts/Python/偏函数(functools.partial)|Python 偏函数 functools.partial 与默认参数]]。
- 补充 [[02-Concepts/Python/README|Python 概念卡]] 与 [[index|AI Knowledge Index]] 导航。

### Python and / or 短路与返回原值

- 新增 [[02-Concepts/Python/and-or 短路求值|Python and / or 短路与返回原值]]，沉淀 `and` / `or` 返回原始操作数、短路行为和 `not > and > or` 优先级。
- 更新 [[02-Concepts/Python/README|Python 概念卡]] 与 [[index|AI Knowledge Index]] 导航。

### AI-Agent-Learning P0-08 PASS

- 同步 `C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-06-13.md`，P0-08 文件、JSON、CSV 判定 `PASS`。
- 新增 [[02-Concepts/Python/文件读写与 JSON 序列化|Python 文件读写与 JSON 序列化]]，沉淀文本文件与 JSON 的边界、`json.dumps()` / `json.loads()`、`ensure_ascii=False`、路径排查和编码注意点。
- 新增 [[04-Projects/Python/AI-Agent-Learning/p0-08-progress-file|P0-08 文件、JSON、CSV]] 项目记录。
- 新增 [[07-Reviews/AI-Agent-Learning/2026-06-13-stage0-p0-08-pass-review|2026-06-13 阶段 0 复盘：P0-08]]。
- 更新 [[03-Courses/Python/AI-Agent-Learning/stage0-python-basics|阶段 0：Python 与开发环境]]、[[03-Courses/Agent/AI-Agent-Learning/README|AI-Agent-Learning]]、[[04-Projects/README|项目记录索引]]、[[01-Maps/AI-Agent-Learning 跳转索引]] 和 [[index|AI Knowledge Index]]。

## 2026-06-14

### AI-Agent-Learning P0-Gate + L1-01 PASS

- 同步 `C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-06-14.md`，`P0-Gate Python 基础闯关` 与 `L1-01 API Key 与 SDK` 判定 `PASS`。
- 新增 [[02-Concepts/Python/JSON 学习日志 CLI|Python JSON 学习日志 CLI：list[dict] 与输入校验]]，沉淀学习记录 CLI 的数据结构、输入校验、旧脏数据清理提醒。
- 新增 [[02-Concepts/LLM/API Key 与 SDK|API Key 与 SDK：调用模型的门禁卡和快递柜台]]，沉淀 API Key、模型名、SDK、环境变量和 GitHub 发布前的安全边界。
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
- 修复索引警告：将 [[02-Concepts/Engineering/README|Engineering 概念卡]] 与 [[02-Concepts/Engineering/调试与错误恢复(Triage)|调试与错误恢复：系统化 triage]] 补入 [[index|AI Knowledge Index]]，并同步补入 [[01-Maps/AI 知识库总地图|AI 知识库总地图]]。
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
- 将 [[02-Concepts/LLM/消息角色与指令优先级(Instruction Hierarchy)|消息角色与指令优先级]]、[[02-Concepts/LLM/LLM 本质与幻觉(Hallucination)|LLM 本质与幻觉]]、[[02-Concepts/LLM/多轮对话与无状态记忆(Stateless Memory)|多轮对话：接口无状态与客户端记忆]]、[[02-Concepts/LLM/流式输出(Streaming)|流式输出]] 补入全局索引和相关地图。
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

## 2026-06-23

### AI-Agent-Learning B0-02 网络基础与 HTTP PASS

- 检查 `C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-06-23.md`，`B0-02 网络基础与 HTTP`（阶段 0.5 工程基础穿插，6/24 顺延补做）判定 `PASS`。重跑 `code/stage0_5/b0_02_http_probe.py` 四场景（正常 2xx / 404 非 2xx / DNS 失败 / 超时）全部按预期；16 题练习全 PASS（B3/C2/C4/D1/D2 经订正）。
- 新增 [[02-Concepts/Engineering/HTTP 请求全链路与错误处理|一次 HTTP 请求的全链路与三类错误处理]]，沉淀：`requests.get` 背后 7 步、DNS/IP/端口、HTTP 报文结构、状态码（401 vs 403、4xx vs 5xx）、**requests 不对 4xx/5xx 抛异常**、三类错误 + 三层防护（timeout / try-except / 主动 check status_code）、timeout 保护客户端、`except` 子类在前基类兜底、`/` vs `//`。
- 更新 [[02-Concepts/Engineering/README|Engineering 概念卡]]（新增「网络与 HTTP」分类）、[[02-Concepts/Python/HTTP 请求(requests)|Python HTTP 请求]]（互链进阶卡）。
- 更新 [[03-Courses/Agent/AI-Agent-Learning/stage0_5-engineering-basics|阶段 0.5：工程基础随用随补]]（B0-02 已补课记录）、[[01-Maps/AI-Agent-Learning 跳转索引]]。
- 回填执行区 `tracker/progress.md`（B0-02 → `PASS`，最近日期 2026-06-23）。

## 2026-06-25

### AI-Agent-Learning PR2-02 摘要与改写（概念预习）

- 检查 `C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-06-25.md`：阶段 2 `PR2-02 摘要与改写`概念预习——读 llm-cookbook「文本概括 Summarizing」+「文本转换 Transforming」两章、记笔记 `notes/stage2/pr2_02_summarizer_notes.md`、15 题练习（A–D）全 PASS（A4/B1/C4 经一次订正）。今天纯概念无代码，动手 `code/stage2/pr2_02_summarizer.py` 按规则排 L1-Gate 后，故 `PR2-02` 判 `DOING`（非 PASS）。
- 新增概念卡 [[02-Concepts/LLM/摘要与改写(Summarize & Transform)|摘要与改写：Summarizing(压信息) vs Transforming(换外壳)]]，沉淀：信息量尺子、控长度三单位 + 软约束（要严格卡死靠代码 `len()` 截）、概括(求全) vs 提取(求专)、判断漏重点（先定义重点 + 体检三件套）、转换四类、锁 JSON 摘要 prompt 5 要素、真实场景（邮件处理器待办用提取字段兜底 / 客服历史摘要省 token）。复习点：PR2-01 老弱点 **few-shot 真实示例 ≠ schema** 本次一次答对。
- 更新 [[02-Concepts/LLM/README|LLM 概念卡索引]]（登记新卡）。
- 新增阶段课程页 [[03-Courses/LLM/AI-Agent-Learning/stage2-prompt-structured-output|阶段 2：Prompt 与结构化输出]]（覆盖 PR2-01 + PR2-02，均 `DOING`：概念完成、动手留 L1-Gate 后）。
- 更新 [[01-Maps/AI-Agent-Learning 跳转索引]]（加阶段 2 课程页链接）。
- 回填执行区 `tracker/progress.md`（PR2-02 → `DOING`，最近日期 2026-06-25）。

## 2026-06-27

### AI-Agent-Learning L1-Gate API 入门闯关 PASS（阶段 1 收尾）

- 复核 `C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-06-27.md`：实现 `code/stage1/l1_gate_cli_chatbot.py`，整合 L1-01~04（多轮 + 流式可开关 + exit + 错误兜底 + 历史限长 + timeout）。**复核实跑**流式真实 5 轮：第 2 轮答出「三玖」、第 4 轮数出「聊了 3 轮」并复述 → 多轮记忆稳；空输入提示、错误兜底不崩、exit 退出码 0。4 必答 + 完整调用链路全过。判 `PASS`，**阶段 1 全部通过**。
- 新增概念卡 [[02-Concepts/LLM/API 参数与 SDK 客户端参数|API 参数 vs SDK 客户端参数]]：API 参数（进请求体、查 DeepSeek 文档）vs SDK 客户端参数（`timeout`/`max_retries`、本机生效、查 OpenAI SDK，所以 DeepSeek API 文档搜不到 timeout）；timeout 两种写法（client 级 / create 级）；本机假服务器实测两种写法均 ~2s 触发 `APITimeoutError`。
- 更新概念卡 [[02-Concepts/LLM/流式输出(Streaming)|流式输出]]：补「底层传输：SSE」一节（SSE 单向逐块推 vs 普通请求-响应 vs WebSocket 双向；TTFT）。
- 更新 [[02-Concepts/LLM/README|LLM 概念卡索引]]（登记新卡）。
- 新增项目页 [[04-Projects/LLM/AI-Agent-Learning/l1-gate-cli-chatbot|L1-Gate CLI Chatbot]]：完整调用链路 + 5 个整合坑（含今日新坑：非流式误用 `call_model` 列表当字符串 + 丢历史 → 改 `call_messages`）+ 4 必答 + 验证结果。
- 新增复盘 [[07-Reviews/AI-Agent-Learning/2026-06-27-stage1-l1-gate-pass-review|2026-06-27 L1-Gate PASS 复盘]]：练习 15 题全 PASS（C1 漏 [SYSTEM]、C2 限长后果方向 经订正）；今天最虚 = 对列表/消息的逐条精确追踪。
- 更新课程页 [[03-Courses/LLM/AI-Agent-Learning/stage1-llm-api-basics|阶段 1：大模型 API 入门]]（加 L1-Gate 行、status → done、下一步指向阶段 2）。
- 更新 [[01-Maps/AI-Agent-Learning 跳转索引]]（加 L1-Gate 项目页、新概念卡、PASS 复盘链接）。
- 回填执行区 `tracker/progress.md`（L1-Gate → `PASS`，最近日期 2026-06-27，解锁阶段 2 动手与 PR2-Gate）。

### AI-Agent-Learning PR2-01 / PR2-02 动手交付 PASS（阶段 2 起步）

- 同日 L1-Gate 通关后，带做补完阶段 2 两个动手产物（`code/stage2/pr2_01_prompt_cases.md` + `pr2_01_run_cases.py`、`code/stage2/pr2_02_summarizer.py`），真跑 DeepSeek 验证后判 `PR2-01` / `PR2-02` 均 `PASS`。
- 更新概念卡 [[02-Concepts/LLM/提示工程基础(Prompt Engineering)|Prompt 基础]]：补「实证：PR2-01 三档对比（few-shot 零增益）」+「工程坑：f-string/.format 撞 prompt 里 JSON 花括号」。
- 更新概念卡 [[02-Concepts/LLM/摘要与改写(Summarize & Transform)|摘要与改写]]：补「实证：机械版 vs 模型版」+「代码兜底 ≠ 约束模型（prompt 事前软请求 / 代码事后硬保证）」+ 常见坑两条。
- 新增项目页 [[04-Projects/LLM/AI-Agent-Learning/pr2-01-02-handson|PR2-01/02 动手：prompt 对比 + 摘要器]]。
- 新增复盘 [[07-Reviews/AI-Agent-Learning/2026-06-27-pr2-01-02-handson-review|2026-06-27 PR2-01/02 动手 PASS 复盘]]：弱点「漏看点名子项」连续两天重现（L1-Gate C1 漏 [SYSTEM] / PR2-02 漏「取值也 strip」）。
- 更新课程页 [[03-Courses/LLM/AI-Agent-Learning/stage2-prompt-structured-output|阶段 2：Prompt 与结构化输出]]（PR2-01/02 → PASS、下一步指向 PR2-03）。
- 更新 [[01-Maps/AI-Agent-Learning 跳转索引]]（加项目页 + PASS 复盘链接）。
- 回填执行区 `tracker/progress.md`（PR2-01、PR2-02 → `PASS`，最近日期 2026-06-27）。

## 2026-06-28

### Weekly Maintenance

- 复查 [[00-Inbox/README|00-Inbox]]、[[raw/README|raw]]、[[index|index.md]]、[[log|log.md]]、自动化 memory 和 2026-06-21 之后的 Git 变化。
- 初始运行 `python tools\check_vault.py --root D:\AI-Knowledge --strict`：
  - `OK: True`
  - `Markdown files: 154`
  - `Links: 1038`
  - `Broken links: 0`
  - `Missing frontmatter: 0`
  - `Raw non-index files: 6`
  - `Warnings: 0`
- 当前 [[00-Inbox/README|00-Inbox]] 仍只有 `README.md`；[[raw/README|raw]] 没有新增 source notes，6 个非索引 raw notes 均保留来源线索，且现有英文 raw notes 已有 `## 中文速读` / `## 关键术语`。
- 复核近期 Git 变化：新增内容主要是 AI-Agent-Learning 的 HTTP、LLM API、Prompt、摘要改写同步，已进入 [[02-Concepts/README|概念卡]]、[[03-Courses/README|课程路线]]、[[04-Projects/README|项目记录]] 与 [[07-Reviews/AI-Agent-Learning/2026-06-27-stage1-l1-gate-pass-review|PASS 复盘]]。
- 未发现需要移动的 stale materials，也未发现误跟踪的生成文件、临时文件或 Obsidian 本地 app state。
- 根据 [[08-Memory/全库中文辅助阅读规则|全库中文辅助阅读规则]] 复查：本轮新增核心笔记以中文为主，保留 `HTTP`、`SDK`、`SSE`、`few-shot`、`JSON`、命令、路径和 API 名等技术锚点，不需要额外硬翻译。
- 新增本次维护复盘 [[07-Reviews/Knowledge-Base/2026-06-28-weekly-maintenance]]，并更新 [[index|index.md]] 与本日志。
- 完成编辑后再次运行严格检查：
  - `OK: True`
  - `Markdown files: 155`
  - `Links: 1066`
  - `Broken links: 0`
  - `Missing frontmatter: 0`
  - `Raw non-index files: 6`
  - `Warnings: 0`

### AI-Agent-Learning PR2-03 分类与路由 PASS（同步知识库）

- 复核 `C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-06-28.md`：PR2-03 分类与路由，带读 ADP 第 2 章 Routing + Inferring；练习 15 题全 PASS；动手 `code/stage2/pr2_03_classifier.py`（规则版 dict 遍历 + `all_hits` 诊断 + 15 样例 + 自动归因 + 模型版 + 真实对比）。实跑规则版正确率 73%、4 难样例规则版 0/4→模型版 2/4。判 **PR2-03 PASS**。
- 新增概念卡 [[02-Concepts/LLM/分类与路由(Classification & Routing)|分类与路由]]：分类是路由前半步、四种路由、规则版 vs 模型版（真跑 0/4→2/4）、漏判/撞类用 `all_hits`+`len` 自动归因、模型版三件套（只输出标签词+strip+白名单）、分类质量=标签定义清晰度。
- 新增概念卡 [[02-Concepts/Python/strip() 与数据清洗|Python strip 与洗运行时脏数据]]：strip 是 str 方法（贴 list 会 `AttributeError`）、只洗运行时脏数据、自写常量改字面量、配合白名单兜底。
- 新增项目页 [[04-Projects/LLM/AI-Agent-Learning/pr2-03-classifier-routing|PR2-03 动手：分类与路由]]、复盘 [[07-Reviews/AI-Agent-Learning/2026-06-28-pr2-03-classifier-routing-review|2026-06-28 PR2-03 PASS 复盘]]。
- 更新 [[02-Concepts/LLM/README|LLM 概念卡索引]]、[[02-Concepts/Python/README|Python 概念卡索引]]、课程页 [[03-Courses/LLM/AI-Agent-Learning/stage2-prompt-structured-output|阶段 2]]（PR2-03 → PASS）、[[01-Maps/AI-Agent-Learning 跳转索引]]（加项目页/概念卡/复盘链接）。
- 回填执行区 `tracker/progress.md`（PR2-03 → PASS，2026-06-28）与 `daily/2026-06-28.md` 的 Codex 判定区。

## 2026-06-29

### AI-Agent-Learning S-03 上下文工程 PASS（同步知识库）

- 复核 `C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-06-29.md`：S-03 上下文工程，带读 Hello-Agents 第 9 章（9.1~9.2.3 / 9.7）；练习 15 题全 PASS（B1/B2/B4/C4/D1/D3 经订正闭环）；动手 `code/stage2/s03_context_experiment.py` token 对比实验真跑通。判 **S-03 PASS**。
- 实跑核验：`① 全量 100 > ③ Compaction 50 > ② 裁剪 25` token；程序检查「三玖」②=`False`（裁剪丢早期信息）/ ③=`True`（Compaction 摘要保人名），真调 DeepSeek 成功。
- 新增概念卡 [[02-Concepts/LLM/上下文工程(Context Engineering)|上下文工程：策划进窗口的整组 token]]：提示工程的演进（跨层包含）、context rot/注意力预算/最小≠最短、五手段分层表（trim/JIT ｜ Compaction/结构化笔记/子代理）+ 选择经验法则、`trim_history`=truncation 属上下文工程非提示工程、实验实证、8 个常见坑。
- 更新 [[02-Concepts/LLM/README|LLM 概念卡索引]]。
- 回填执行区 `tracker/progress.md`（S-03 → PASS，2026-06-29）与 `daily/2026-06-29.md` 的 Codex 判定区。

## 2026-07-02

### 概念卡文件名中文化（02-Concepts 全量）

- 41 张概念卡文件名由英文短横线改为「中文(短英文)」：LLM 20 张（如 tokenization → 分词(Tokenization)）、Python 18 张（如 python-functools-partial → 偏函数(functools.partial)）、Engineering 2 张、MCP 1 张（model-context-protocol → MCP(Model Context Protocol)）。
- 全库 wikilink 同步改写约 424 处 + 各 README 索引显示文字理为中文，校验零断链；每张卡 frontmatter `aliases:` 保留旧英文名（旧链接与英文搜索不受影响）。
- 更新命名规则：[[01-Maps/标签与命名规范]] 与 [[02-Concepts/README|概念卡片索引]] 改为「中文(短英文)」；AI-Agent-Learning 仓库 CLAUDE.md 同步该约定（以后新卡直接中文名）。
- 边界：03-Courses / 04-Projects / 07-Reviews 文件名保持英文任务编号锚定（L1-Gate、PR2-03 等），不改。

### DeepSeek 分享对话整理：上下文工程、路由与特殊 Token

- 整理分享页 <https://chat.deepseek.com/share/tefftbktdjn3xpztg6>，新增 raw 来源摘要 [[raw/conversations/deepseek-share-context-routing-jit|DeepSeek 分享对话：上下文工程、路由与特殊 Token]]。
- 新增概念卡 [[02-Concepts/LLM/特殊Token(Special Tokens)|特殊Token：模型词表里的控制暗号]]，沉淀 API 消息格式 vs 模型内部序列、EOS/EOT、文本结束 vs 序列结束。
- 更新 [[02-Concepts/LLM/上下文工程(Context Engineering)|上下文工程]]：补充 Compaction 的召回/精确度、JIT vs 结构化笔记、JIT 与渐进式披露、引用元数据。
- 更新 [[02-Concepts/LLM/分类与路由(Classification & Routing)|分类与路由]]：补充“标签 -> 路由 -> JIT”的上下文节约设计，以及四类路由的严格分类。
- 更新 [[02-Concepts/LLM/API Key 与 SDK|API Key 与 SDK]]、[[02-Concepts/LLM/采样参数与成本(Sampling)|采样参数与成本]]、[[02-Concepts/LLM/LLM 本质与幻觉(Hallucination)|LLM 本质与幻觉]]、[[02-Concepts/LLM/分词(Tokenization)|分词]]、[[02-Concepts/LLM/自回归生成(Autoregressive)|自回归生成]] 的相关补充和互链。

## 2026-07-03

### AI-Agent-Learning T3-01 函数调用概念 PASS（学习日 2026-07-01，同步知识库）

- 复核 `daily/2026-07-01.md`：T3-01 工作日填充预习（PR2-Gate 留周末）——带读 HF agents-course 4 节（7 题边读边练）＋共写笔记 `notes/stage3/t3_01_function_calling.md`（「概念笔记共写」新约定首跑：用户原话落盘＋⚠️订正/💡补充标注）＋练习 13 题全 PASS。判 **T3-01 PASS**。
- 实跑验证：用户 C3 分发器答案组装脚本跑通（`json.loads`→`TOOLS[name](**args)`→`role:"tool"` 拼回，asserts 全过）；坏 Action 确认抛 `JSONDecodeError`（ValueError 子类）。
- 新增概念卡 [[02-Concepts/LLM/函数调用(Function Calling)|函数调用]]：7 步链（模型决策 vs 程序执行）、停止并解析防自编 Observation、FC vs 手搓（训练焊权重 vs prompt 软请求）、最小分发器、7 条坑。
- 更新 [[02-Concepts/LLM/README|LLM 概念卡索引]]、[[01-Maps/AI-Agent-Learning 跳转索引]]。
- 回填执行区 `tracker/progress.md`（T3-01 → PASS，2026-07-01）与 `daily/2026-07-01.md` Codex 判定区。
- 错题本 `tracker/weak-points.md`：WP-02/WP-05/WP-06 独立复测通过升 ✅（下次回炉 2026-07-15）；WP-01 命中通过降 🟡；新增 WP-14（🔴 自编 Observation 代码实景识别）、WP-15（🟡 术语绑定：Observation 槽位名 / JSONDecodeError≠TypeError）。

## 2026-07-05

### Weekly Maintenance

- 复查 [[00-Inbox/README|00-Inbox]]、[[raw/README|raw]]、[[index|index.md]]、[[log|log.md]]、自动化 memory 和 2026-06-28 之后的 Git 变化。
- 初始运行 `python tools\check_vault.py --root D:\AI-Knowledge --strict`：
  - `OK: True`
  - `Markdown files: 164`
  - `Links: 1181`
  - `Broken links: 0`
  - `Missing frontmatter: 0`
  - `Raw non-index files: 7`
  - 警告：1 个重要笔记未被 `index.md` 直接引用。
- 警告明细为 [[02-Concepts/LLM/函数调用(Function Calling)|函数调用]]；该卡已在 [[02-Concepts/LLM/README|LLM 概念卡索引]] 和 [[01-Maps/AI-Agent-Learning 跳转索引]] 中，但全局索引缺直连。
- 当前 [[00-Inbox/README|00-Inbox]] 仍只有 `README.md`，没有待分拣材料。
- 当前 [[raw/README|raw]] 有 7 个非索引 source notes；新增 [[raw/conversations/deepseek-share-context-routing-jit|DeepSeek 分享对话]] 已标记 `processed`，保留 `source_url`，并链接到已编译概念卡。
- 复核近期 Git 变化：PR2-03、S-03、PR2-04、DeepSeek 分享对话、T3-01 函数调用，以及 `02-Concepts` 文件名中文化，均已沉淀到合适 wiki 层；未发现需要移动的 stale materials。
- 根据 [[08-Memory/全库中文辅助阅读规则|全库中文辅助阅读规则]] 复查：新增核心笔记以中文解释为主，保留 `Function Calling`、`Tool Calling`、`JSONDecodeError`、`TOOLS[name](**args)`、`role:"tool"`、`context engineering`、`JIT`、`Compaction`、命令、路径和 API 名等技术锚点，不硬翻译代码。
- 更新 [[index|index.md]]：补入 [[02-Concepts/LLM/函数调用(Function Calling)|函数调用]]、[[04-Projects/LLM/AI-Agent-Learning/pr2-03-classifier-routing|PR2-03 项目页]]、[[07-Reviews/AI-Agent-Learning/2026-06-28-pr2-03-classifier-routing-review|PR2-03 PASS 复盘]] 和本周维护入口。
- 更新 [[01-Maps/AI 知识库总地图|AI 知识库总地图]]：将 `Tool calling` 占位改为函数调用概念卡链接。
- 修正 [[01-Maps/AI-Agent-Learning 跳转索引]] frontmatter 中重复的 `updated` 字段。
- 新增本次维护复盘 [[07-Reviews/Knowledge-Base/2026-07-05-weekly-maintenance]]。
- 完成编辑后再次运行严格检查：
  - `OK: True`
  - `Markdown files: 165`
  - `Links: 1216`
  - `Broken links: 0`
  - `Missing frontmatter: 0`
  - `Raw non-index files: 7`
  - `Warnings: 0`

### AI-Agent-Learning PR2-Gate 邮件处理器 PASS（同步知识库）

- 复核 `daily/2026-07-05.md`：PR2-Gate 邮件处理器带读 + 14 题练习全部闭环；判 **PR2-Gate PASS**。
- 实跑 `code/stage2/pr2_gate_email_processor.py`：成功输出 `category/points/summary/todo` 并保存 `resources/stage2_email_result.json`；结果文件可被 `json.loads` 解析，`todo` 五字段齐全。
- 额外断言：缺 `deadline` 被 `validate_payload` 拦截；按行邮件和普通长文摘要都能产出 3 条；撞类样例按 `RULES` 顺序返回 `投诉`。
- 更新概念卡 [[02-Concepts/LLM/结构化输出(Structured Output)|结构化输出]]：补 PR2-Gate 工程链路 `json.loads` -> dict -> `validate_payload` -> `json.dump`。
- 更新概念卡 [[02-Concepts/Python/文件读写与 JSON 序列化|文件读写与 JSON 序列化]]：补 `dict` / JSON 字符串 / JSON 文件三层边界，以及 `dumps` vs `dump` 易错点。
- 新增项目页 [[04-Projects/LLM/AI-Agent-Learning/pr2-gate-email-processor|PR2-Gate 邮件处理器]]。
- 新增复盘 [[07-Reviews/AI-Agent-Learning/2026-07-05-pr2-gate-email-processor-review|2026-07-05 PR2-Gate 邮件处理器 PASS 复盘]]。
- 更新 [[03-Courses/LLM/AI-Agent-Learning/stage2-prompt-structured-output|阶段 2：Prompt 与结构化输出]]：PR2-Gate 标记 PASS，阶段 2 收尾，下一步 T3-02。
- 更新 [[02-Concepts/LLM/README|LLM 概念卡索引]]、[[02-Concepts/Python/README|Python 概念卡索引]]、[[04-Projects/LLM/README|LLM 项目记录]]、[[01-Maps/AI-Agent-Learning 跳转索引]]、[[index|全局索引]]。
- 同步后运行 `python tools\check_vault.py --root D:\AI-Knowledge --strict`：
  - `OK: True`
  - `Markdown files: 167`
  - `Links: 1249`
  - `Broken links: 0`
  - `Missing frontmatter: 0`

## 2026-07-06

### AI-Agent-Learning T3-02 计算器工具 PASS（同步知识库）

- 复核 `daily/2026-07-06.md`：T3-02 带读 Hello-Agents 4.2.1/4.2.2，完成计算器工具代码与必答问答，判 **T3-02 PASS**。
- 实跑 `code/stage3/t3_02_calculator_tool.py`：
  - `CALCULATOR_SCHEMA` 包含 `name/description/parameters`，参数为 `operation/a/b`。
  - 7 组函数级测试全 PASS：加、减、乘、除、除零、非法操作、非数字。
  - 交互入口能打印调用参数和结果。
- 新增概念卡 [[02-Concepts/Agent/工具定义与执行协议(Tool Definition)|工具定义与执行协议]]。
- 新增 Agent 概念索引 [[02-Concepts/Agent/README|Agent 概念卡索引]]。
- 新增项目页 [[04-Projects/Agent/AI-Agent-Learning/t3-02-calculator-tool|T3-02 计算器工具]]，并补 [[04-Projects/Agent/README|Agent 项目记录]] 与 [[04-Projects/Agent/AI-Agent-Learning/README|AI-Agent-Learning Agent 实践]]。
- 新增复盘 [[07-Reviews/AI-Agent-Learning/2026-07-06-t3-02-calculator-tool-review|2026-07-06 T3-02 计算器工具 PASS 复盘]]。
- 新增课程页 [[03-Courses/Agent/AI-Agent-Learning/stage3-tool-calling|阶段 3：Tool Calling / Function Calling]]，并更新 [[03-Courses/Agent/AI-Agent-Learning/README|AI-Agent-Learning 课程索引]]。
- 更新 [[02-Concepts/README|概念卡片索引]]、[[04-Projects/README|项目记录索引]]、[[01-Maps/AI-Agent-Learning 跳转索引]] 和 [[index|全局索引]]。
- 同步后运行 `python tools\check_vault.py --root D:\AI-Knowledge --strict`：
  - `OK: True`
  - `Markdown files: 175`
  - `Links: 1302`
  - `Broken links: 0`
  - `Missing frontmatter: 0`
  - `Raw non-index files: 7`
  - `Raw non-index files: 7`

## 2026-07-07

### AI-Agent-Learning T3-03 文件工具 PASS（同步知识库）

- 复核 `daily/2026-07-07.md`：T3-03 文件工具练习与代码实现达标，判 **T3-03 PASS**。
- 实跑 `code/stage3/t3_03_file_reader_tool.py`：
  - `python -m py_compile` 语法通过。
  - CLI 读取 `sample.txt` 正常。
  - 函数级覆盖正常读取、长文件截断、文件不存在、目录误读、`..` 沙箱逃逸拒绝、沙箱内归一化允许。
- 新增概念卡 [[02-Concepts/Agent/文件工具沙箱(File Tool Sandbox)|文件工具沙箱]]。
- 新增项目页 [[04-Projects/Agent/AI-Agent-Learning/t3-03-file-reader-tool|T3-03 文件工具]]。
- 新增复盘 [[07-Reviews/AI-Agent-Learning/2026-07-07-t3-03-file-reader-tool-review|2026-07-07 T3-03 文件工具 PASS 复盘]]。
- 更新 [[02-Concepts/Agent/README|Agent 概念卡索引]]、[[04-Projects/Agent/README|Agent 项目记录]]、[[04-Projects/Agent/AI-Agent-Learning/README|AI-Agent-Learning Agent 实践]]、[[03-Courses/Agent/AI-Agent-Learning/stage3-tool-calling|阶段 3：Tool Calling / Function Calling]]、[[03-Courses/Agent/AI-Agent-Learning/README|AI-Agent-Learning 课程索引]]、[[01-Maps/AI-Agent-Learning 跳转索引]] 和 [[index|全局索引]]。
- 同步后运行 `python tools\check_vault.py --root D:\AI-Knowledge --strict`：
  - `OK: True`
  - `Markdown files: 178`
  - `Links: 1325`
  - `Broken links: 0`
  - `Missing frontmatter: 0`
  - `Raw non-index files: 7`

## 2026-07-10

### AI-Agent-Learning A4-01 什么是 Agent PASS（同步知识库）

- 复核 `daily/2026-07-09.md`：A4-01 什么是 Agent 带读与练习闭环，判 **A4-01 PASS**。
- A4-01 为概念任务，无需运行代码；已检查问答覆盖 Agent vs Chatbot、Tool/Action/Observation/Final Answer、Tool Calling vs 多步 Agent、代码硬校验。
- 新增执行区笔记 `notes/stage4/a4_01_what_is_agent.md`。
- 新增概念卡 [[02-Concepts/Agent/智能体(Agent)|智能体]]。
- 新增课程阶段页 [[03-Courses/Agent/AI-Agent-Learning/stage4-agent-basics|阶段 4：Agent 基础原理]]。
- 新增复盘 [[07-Reviews/AI-Agent-Learning/2026-07-09-a4-01-what-is-agent-review|2026-07-09 A4-01 什么是 Agent PASS 复盘]]。
- 更新 [[02-Concepts/Agent/README|Agent 概念卡索引]]、[[03-Courses/Agent/AI-Agent-Learning/README|AI-Agent-Learning 课程索引]]、[[01-Maps/AI-Agent-Learning 跳转索引]] 和 [[index|全局索引]]。
- 同步后运行 `python tools\check_vault.py --root D:\AI-Knowledge --strict`：
  - `OK: True`
  - `Markdown files: 185`
  - `Links: 1406`
  - `Broken links: 0`
  - `Missing frontmatter: 0`
  - `Raw non-index files: 7`

## 2026-07-08

### AI-Agent-Learning T3-04 外部 API 工具 PASS（同步知识库）

- 复核 `daily/2026-07-08.md`：T3-04 外部 API 工具带读、实现与练习闭环，判 **T3-04 PASS**。
- 实跑 `code/stage3/t3_04_public_api_tool.py`：
  - `python -m py_compile` 语法通过。
  - 默认请求 `https://api.github.com` 返回 `ok=True`、`status_code=200`、`server="github.com"`。
  - 404 路径稳定返回 `ok=False/status_code=404`，不进入异常分支。
  - 非法 URL、模拟 `requests.Timeout`、模拟 `requests.RequestException` 均返回稳定 `ok/error`。
- 新增概念卡 [[02-Concepts/Agent/外部 API 工具(External API Tool)|外部 API 工具]]。
- 新增项目页 [[04-Projects/Agent/AI-Agent-Learning/t3-04-public-api-tool|T3-04 外部 API 工具]]。
- 新增复盘 [[07-Reviews/AI-Agent-Learning/2026-07-08-t3-04-public-api-tool-review|2026-07-08 T3-04 外部 API 工具 PASS 复盘]]。
- 更新 [[02-Concepts/Agent/README|Agent 概念卡索引]]、[[04-Projects/Agent/README|Agent 项目记录]]、[[04-Projects/Agent/AI-Agent-Learning/README|AI-Agent-Learning Agent 实践]]、[[03-Courses/Agent/AI-Agent-Learning/stage3-tool-calling|阶段 3：Tool Calling / Function Calling]]、[[03-Courses/Agent/AI-Agent-Learning/README|AI-Agent-Learning 课程索引]]、[[01-Maps/AI-Agent-Learning 跳转索引]] 和 [[index|全局索引]]。
- 同步后运行 `python tools\check_vault.py --root D:\AI-Knowledge --strict`：
  - `OK: True`
  - `Markdown files: 181`
  - `Links: 1374`
  - `Broken links: 0`
  - `Missing frontmatter: 0`
  - `Raw non-index files: 7`

## 2026-07-12

### AI-Agent-Learning T3-Gate Tool Calling PASS（同步知识库）

- 复核 `daily/2026-07-11.md` 与 `tracker/progress.md`：T3-Gate 于 2026-07-12 正式判定 **PASS**，阶段 3 全部完成。
- 新增执行区整合笔记 `notes/stage3/t3_gate_tool_assistant.md`，并按当前代码修订 `notes/stage3/t3_04_public_api_tool.md` 的重定向说明。
- 更新 [[02-Concepts/LLM/函数调用(Function Calling)|函数调用]]：补多 `tool_call`、独立 ID 回填、五种计数、直接回答与最大轮数语义。
- 更新 [[02-Concepts/Agent/工具定义与执行协议(Tool Definition)|工具定义与执行协议]]：补小写 `tools` schema、大写 `TOOLS` 注册表及客户端校验顺序。
- 更新 [[02-Concepts/Agent/外部 API 工具(External API Tool)|外部 API 工具]]：补 HTTPS/host/443 allowlist、空端口、SSRF、禁止重定向及剩余 DNS 风险。
- 新增项目页 [[04-Projects/Agent/AI-Agent-Learning/t3-gate-tool-assistant|T3-Gate 三工具助手]]。
- 新增复盘 [[07-Reviews/AI-Agent-Learning/2026-07-12-t3-gate-tool-calling-review|2026-07-12 T3-Gate Tool Calling PASS 复盘]]。
- 更新阶段 3 课程页、课程索引、Agent/LLM 概念索引、项目索引、AI-Agent-Learning 跳转索引与全局索引。
- 正式证据：`t3-gate-v2` SHA-256 `76664937408435087A48691EE6EBE6287F0127E154CFB51671823950C67C042F`；normal 10/10、failure 3/3、danger 1/1、holdout 3/3；两个独立 evaluator 均为 14/14 PASS，真实 DeepSeek 请求 19 次。
- 同步后运行 `python tools\check_vault.py --root D:\AI-Knowledge --strict`：
  - `OK: True`
  - `Markdown files: 187`
  - `Links: 1441`
  - `Broken links: 0`
  - `Missing frontmatter: 0`
  - `Raw non-index files: 7`

### SSRF 独立概念卡

- 新增 [[02-Concepts/Engineering/服务端请求伪造(SSRF)|服务端请求伪造（SSRF）]]：整理服务器代发请求的攻击链、`@` hostname 伪装、302 重定向绕过、常见影响与分层防护。
- 更新 [[02-Concepts/Agent/外部 API 工具(External API Tool)|外部 API 工具]]、[[02-Concepts/Engineering/README|Engineering 概念卡索引]] 和 [[index|全局索引]]，建立 Agent 工具安全与通用 HTTP 安全概念之间的链接。
- 严格检查 `python tools\check_vault.py --root D:\AI-Knowledge --strict`：`OK: True`，Markdown 188，链接 1455，断链 0，缺失 frontmatter 0。

### Weekly Maintenance

- 复查 [[00-Inbox/README|00-Inbox]]、[[raw/README|raw]]、[[index|index.md]]、[[log|log.md]]、自动化 memory、[[08-Memory/全库中文辅助阅读规则|全库中文辅助阅读规则]] 和 2026-07-05 之后的 Git 变化。
- 初始运行 `python tools\check_vault.py --root D:\AI-Knowledge --strict`：
  - `OK: True`
  - `Markdown files: 187`
  - `Links: 1441`
  - `Broken links: 0`
  - `Missing frontmatter: 0`
  - `Raw non-index files: 7`
  - `Warnings: 0`
- [[00-Inbox/README|00-Inbox]] 当前仍只有 `README.md`，没有待分拣资料。
- [[raw/README|raw]] 当前有 7 个非索引 source notes；本周没有新增 raw source，已有 source notes 保留原始资料层位置。
- 复核近期 Git 变化：PR2-Gate、T3-02、T3-03、T3-04、A4-01、T3-Gate 相关内容已沉淀到概念卡、课程页、项目记录、复盘页、主题 README、[[01-Maps/AI-Agent-Learning 跳转索引|AI-Agent-Learning 跳转索引]] 和 [[index|全局索引]]。
- 根据中文辅助阅读规则复查：本周新增 Agent / Tool Calling 笔记以中文解释为主，保留 `Tool Calling`、`Function Calling`、`Agent`、`Observation`、`Final Answer`、`tools` schema、`TOOLS` registry、`SSRF`、命令、路径、API 名和代码片段。
- 更新 [[01-Maps/AI 知识库总地图|AI 知识库总地图]]：补入 [[02-Concepts/Agent/README|Agent 概念卡]]，并把 AI 工程能力中的 `Agent` 占位改为 [[02-Concepts/Agent/智能体(Agent)|智能体]] 入口。
- 更新 [[index|index.md]]：补入本周维护复盘 [[07-Reviews/Knowledge-Base/2026-07-12-weekly-maintenance|2026-07-12 Weekly Maintenance]]。
- 新增本维护复盘 [[07-Reviews/Knowledge-Base/2026-07-12-weekly-maintenance|2026-07-12 Weekly Maintenance]]。
- 完成编辑后再次运行严格检查：
  - `OK: True`
  - `Markdown files: 188`
  - `Links: 1470`
  - `Broken links: 0`
  - `Missing frontmatter: 0`
  - `Raw non-index files: 7`
  - `Warnings: 0`

## 2026-07-15

### AI-Agent-Learning A4-02 LLM 与 Agent 基础 PASS（同步知识库）

- 复核执行区 `daily/2026-07-14.md`、`daily/2026-07-15.md`、指定 Hello-Agents / Hugging Face 资料与定稿 notes，正式判定 **A4-02 PASS**。
- 更新 [[02-Concepts/LLM/提示工程基础(Prompt Engineering)|提示工程基础]]：补 Instruction Data / Instruction Tuning / Prompting / Few-shot 的对象、参数变化和模型版本持久性边界。
- 更新 [[02-Concepts/LLM/特殊Token(Special Tokens)|特殊 Token]]：补 Chat Template、模板错配风险与 `apply_chat_template()` 输入转换。
- 更新 [[02-Concepts/LLM/LLM 本质与幻觉(Hallucination)|LLM 本质与幻觉]]：补三类幻觉、Agent 风险放大、权威事实、客户端硬校验、人工确认和超时保持未知。
- 去重检查 [[02-Concepts/LLM/多轮对话与无状态记忆(Stateless Memory)|无状态记忆]]、[[02-Concepts/Agent/工具调用与动作(Tool Calling and Action)|工具调用与动作]]、[[02-Concepts/Agent/智能体(Agent)|智能体]]：已有内容准确完整，保持不改。
- 更新 [[03-Courses/Agent/AI-Agent-Learning/stage4-agent-basics|阶段 4：Agent 基础原理]] 与 [[03-Courses/Agent/AI-Agent-Learning/README|课程索引]]，当前任务切换为 A4-03 ReAct。
- 新增复盘 [[07-Reviews/AI-Agent-Learning/2026-07-15-a4-02-llm-agent-basics-review|2026-07-15 A4-02 PASS 复盘]]。
- 更新 [[02-Concepts/LLM/README|LLM 概念索引]]、[[01-Maps/AI-Agent-Learning 跳转索引]] 与 [[index|全局索引]]；未新建重复概念卡。
- 同步后运行 `python tools\check_vault.py --root D:\AI-Knowledge --strict`：
  - `OK: True`
  - `Markdown files: 189`
  - `Links: 1505`
  - `Broken links: 0`
  - `Missing frontmatter: 0`
  - `Raw non-index files: 7`

## 2026-07-19

### Weekly Maintenance

- 复查 [[00-Inbox/README|00-Inbox]]、[[raw/README|raw]]、[[index|index.md]]、[[log|log.md]]、[[08-Memory/全库中文辅助阅读规则|全库中文辅助阅读规则]] 和 2026-07-12 之后的 Git 变化。
- 初始运行 `python tools\check_vault.py --root D:\AI-Knowledge --strict`：
  - `OK: True`
  - `Markdown files: 189`
  - `Links: 1505`
  - `Broken links: 0`
  - `Missing frontmatter: 0`
  - `Raw non-index files: 7`
  - `Warnings: 0`
- [[00-Inbox/README|00-Inbox]] 当前仍只有 `README.md`，没有待分拣资料。
- [[raw/README|raw]] 当前有 7 个非索引 source notes；本周没有新增 raw source，已有 source notes 保留原始资料层位置。
- 复核近期 Git 变化：2026-07-12 之后只有 `13c7aa6` A4-02 同步提交，已沉淀到 LLM 概念卡、Agent 课程页、AI-Agent-Learning 复盘页、主题 README、[[01-Maps/AI-Agent-Learning 跳转索引|AI-Agent-Learning 跳转索引]] 和 [[index|全局索引]]。
- 根据中文辅助阅读规则复查：最近新增核心页以中文解释为主，保留 `Instruction Tuning`、`Prompting`、`Few-shot`、`Chat Template`、`apply_chat_template()`、`Hallucination`、`Agent`、`Tool Calling`、路径、命令、API 名和代码片段。英文占比较高的 `copilot/copilot-custom-prompts/` 属于可执行 prompt assets，本次不硬翻译其指令正文。
- 记录 seed backlog：6 个 Python 入门概念卡、1 个 Claude Skills 课程 seed、1 个 HelloAgents 源码阅读索引 seed，均已在正确目录，后续按学习证据扩写。
- 新增本维护复盘 [[07-Reviews/Knowledge-Base/2026-07-19-weekly-maintenance|2026-07-19 Weekly Maintenance]]。
- 更新 [[index|index.md]]：补入本周维护复盘入口。
- 完成编辑后再次运行严格检查：
  - `OK: True`
  - `Markdown files: 190`
  - `Links: 1528`
  - `Broken links: 0`
  - `Missing frontmatter: 0`
  - `Raw non-index files: 7`
  - `Warnings: 0`

## 2026-07-21

### Function Calling / Tool Calling 术语边界补充

- 更新 [[02-Concepts/LLM/函数调用(Function Calling)|函数调用（Function Calling）]]：将“两个名字完全同义”订正为“Tool Calling 是上位概念，Function Calling 是常见的函数型具体形式”。
- 补充原生 API Function Calling 的判断条件，并明确 `{"name":"get_weather","arguments":{"city":"Singapore"}}` 只是简化调用表示，不是跨厂商统一的完整响应标准；普通正文中的同形 JSON 也不自动等于原生 Function Calling。
- 更新 [[02-Concepts/Agent/工具调用与动作(Tool Calling and Action)|工具调用与动作]]：补齐 Tool Calling / Function Calling / Action / Tool Execution 的层级关系，以及 ReAct 手写 Action 与原生 API 调用的边界。
- 更新 [[02-Concepts/LLM/README|LLM 概念索引]]、[[02-Concepts/Agent/README|Agent 概念索引]]、[[01-Maps/AI 知识库总地图|AI 知识库总地图]] 与相关链接显示名；复用已有概念卡，未新建重复页面。
- 运行 `python tools\check_vault.py --root D:\AI-Knowledge --strict`：
  - `OK: True`
  - `Markdown files: 190`
  - `Links: 1535`
  - `Broken links: 0`
  - `Missing frontmatter: 0`
  - `Raw non-index files: 7`

## 2026-07-22

### AI-Agent-Learning A4-03 ReAct PASS（同步知识库）

- 复核执行区 `daily/2026-07-21.md`、`daily/2026-07-22.md` 与 `code/stage4/a4_03_react_agent.py`，正式判定 **A4-03 PASS**；真实脚本完整两轮轨迹通过，内存边界断言 15/15。
- 新增 [[02-Concepts/Agent/ReAct推理与行动循环(ReAct)|ReAct 推理与行动循环]]：补 Thought / Action / Observation 职责链、成功停止与安全停止、`max_steps`、客户端硬校验及 fake LLM 证据边界。
- 新增 [[04-Projects/Agent/AI-Agent-Learning/a4-03-react-agent|A4-03 ReAct Agent 项目页]] 与 [[07-Reviews/AI-Agent-Learning/2026-07-22-a4-03-react-review|A4-03 PASS 复盘]]。
- 更新 [[03-Courses/Agent/AI-Agent-Learning/stage4-agent-basics|阶段 4 课程页]]、课程/项目/概念索引、[[01-Maps/AI-Agent-Learning 跳转索引|跳转索引]]、[[01-Maps/AI 知识库总地图|总地图]] 与 [[index|全局索引]]；下一项切换为 A4-04 Plan-and-Solve。
- 去重检查 [[02-Concepts/Agent/智能体(Agent)|智能体]] 与 [[02-Concepts/Agent/工具定义与执行协议(Tool Definition)|工具定义与执行协议]]：保留已有通用职责说明，只补 ReAct 关联入口，没有复制整页内容。
- 项目侧复习路由：新增 `CD-004` 与稳定错题 `WP-24`（首轮均 2026-08-05）；`WP-12` 复测通过并升到 `+1月`（2026-08-21）。W4 算法仍为 `DEBT` 0/4，普通课程 PASS 不升级岗位证据。
- 同步后运行 `python tools\check_vault.py --root D:\AI-Knowledge --strict`：
  - `OK: True`
  - `Markdown files: 193`
  - `Links: 1577`
  - `Broken links: 0`
  - `Missing frontmatter: 0`
  - `Raw non-index files: 7`

## 2026-07-23

### Reflection 与运行事实复盘的术语边界

- 新增 [[02-Concepts/Agent/反思机制(Reflection)|反思机制（Reflection）]]，沉淀 A4-04-G6 已通过的术语区分。
- 明确运行复盘回答“发生了什么”，`Reflection` 对照目标评价过程或结果并提出改进；发生时间不是两者的唯一分界。
- 补充 `Observation -> Reflection -> 重试 / 重写 / 重新 Planning / Memory` 的职责关系，并说明重新规划不自动等于 Reflection。
- 更新 [[02-Concepts/Agent/README|Agent 概念卡索引]] 与 [[index|全局索引]]。
- 运行 `python tools\check_vault.py --root D:\AI-Knowledge --strict`：
  - `OK: True`
  - `Markdown files: 194`
  - `Links: 1585`
  - `Broken links: 0`
  - `Missing frontmatter: 0`

### Planner 模型输出的安全解析

- 更新 [[02-Concepts/LLM/结构化输出(Structured Output)|结构化输出]]，补充 Markdown Python 代码围栏属于弱文本协议，不等于 API 强制的 Structured Outputs。
- 记录 `index()` 与链式 `split()` 在缺少开头/结束围栏时的失败差异，并推荐用 `find()` 显式进入失败返回路径。
- 补充分层防线：围栏完整性检查 -> `ast.literal_eval()` -> 外层类型检查 -> 元素与业务约束检查。
- 记录两个运行时陷阱：`list[str]` 类型标注不执行校验，且 `all([]) == True`，空计划需要单独拒绝。
- 运行 `python tools\check_vault.py --root D:\AI-Knowledge --strict`：
  - `OK: True`
  - `Markdown files: 194`
  - `Links: 1586`
  - `Broken links: 0`
  - `Missing frontmatter: 0`

## 2026-07-27

### Weekly Maintenance

- 复查 [[00-Inbox/README|00-Inbox]]、[[raw/README|raw]]、[[index|index.md]]、[[log|log.md]]、[[08-Memory/全库中文辅助阅读规则|全库中文辅助阅读规则]] 和 2026-07-19 之后的 Git 变化。
- 初始运行 `python tools\check_vault.py --root D:\AI-Knowledge --strict`：
  - `OK: True`
  - `Markdown files: 194`
  - `Links: 1586`
  - `Broken links: 0`
  - `Missing frontmatter: 0`
  - `Raw non-index files: 7`
- [[00-Inbox/README|00-Inbox]] 当前仍只有 `README.md`，没有待分拣资料。
- [[raw/README|raw]] 当前有 7 个非索引 source notes；本周没有新增 raw source，已有 source notes 保留原始资料层位置。
- 复核近期 Git 变化：`676f3cb` 为 Function Calling / Tool Calling 术语边界备份修订；`64236c5` 同步 A4-03 ReAct PASS 成果，已沉淀到 Agent 概念卡、课程页、项目页、复盘页、主题索引和 [[01-Maps/AI 知识库总地图|总地图]]。
- 复核并纳入 2026-07-23 未提交知识沉淀：新增 [[02-Concepts/Agent/反思机制(Reflection)|反思机制（Reflection）]]，更新 [[02-Concepts/LLM/结构化输出(Structured Output)|结构化输出]] 的 Planner 模型输出安全解析边界，并同步 [[02-Concepts/Agent/README|Agent 概念卡索引]]、[[index|全局索引]] 和本日志。
- 根据中文辅助阅读规则复查：新增与更新页以中文解释为主，保留 `Reflection`、`Observation`、`Planning`、`Structured Outputs`、`JSON mode`、`ast.literal_eval()`、`index()`、`split()`、`find()`、`list[str]`、`all([])`、路径、命令和代码片段。
- `函数调用(Function Calling).md` 仅出现 Git 状态/行尾提示，文件 hash 与索引一致，没有实质内容差异；`.obsidian/`、`.claudian/`、本地 app state 与生成缓存未纳入维护提交。
- 新增本维护复盘 [[07-Reviews/Knowledge-Base/2026-07-27-weekly-maintenance|2026-07-27 Weekly Maintenance]]。
- 更新 [[01-Maps/AI 知识库总地图|AI 知识库总地图]]：补入 [[02-Concepts/Agent/反思机制(Reflection)|Reflection 反思机制]] 入口。
- 更新 [[index|index.md]]：补入本周维护复盘入口。
- 完成编辑后再次运行严格检查：
  - `OK: True`
  - `Markdown files: 195`
  - `Links: 1620`
  - `Broken links: 0`
  - `Missing frontmatter: 0`
  - `Raw non-index files: 7`

## 2026-07-30

### AI-Agent-Learning A4-04 Plan-and-Solve PASS（同步知识库）

- 复核执行区 `daily/2026-07-22.md`～`daily/2026-07-30.md` 与 `code/stage4/a4_04_plan_solve_demo.py`，正式判定 **A4-04 PASS**；真实脚本完整输出计划、3 步结果、事实性复盘和最终答案，聚焦边界断言 39/39。
- 新增 [[02-Concepts/Agent/计划与求解(Plan-and-Solve)|计划与求解]]：沉淀 Planner/Executor 职责、四类执行上下文、`StepResult` 状态合同、静态 Planning/Replanning 边界、事实性复盘和确定性 demo 证据边界。
- 新增 [[04-Projects/Agent/AI-Agent-Learning/a4-04-plan-and-solve|A4-04 Plan-and-Solve 项目页]] 与 [[07-Reviews/AI-Agent-Learning/2026-07-30-a4-04-plan-and-solve-review|A4-04 PASS 复盘]]。
- 更新 [[03-Courses/Agent/AI-Agent-Learning/stage4-agent-basics|阶段 4 课程页]]、课程/项目/概念索引、[[01-Maps/AI-Agent-Learning 跳转索引|跳转索引]]、[[01-Maps/AI 知识库总地图|总地图]] 与 [[index|全局索引]]；下一项切换为 A4-05 Reflection。
- 去重检查 [[02-Concepts/Agent/反思机制(Reflection)|反思机制]] 与 [[02-Concepts/LLM/结构化输出(Structured Output)|结构化输出]]：既有页面已准确覆盖 Reflection/事实复盘和 Planner 文本安全解析，本次只补反向链接，不复制同义章节。
- 项目侧复习路由：`WP-08` 回炉通过并转入稳定池；新增活跃弱点 `WP-25`、`WP-26` 和核心定义 `CD-005`。WS-02、WS-05 达到 `DIAGNOSED_AND_FIXED`；W4 算法仍为 `DEBT` 0/4，普通课程 PASS 不升级岗位证据。
- 同步后运行 `python tools\check_vault.py --root D:\AI-Knowledge --strict`：
  - `OK: True`
  - `Markdown files: 198`
  - `Links: 1660`
  - `Broken links: 0`
  - `Missing frontmatter: 0`
  - `Raw non-index files: 7`

## 2026-08-02

### Weekly Maintenance

- 复查 [[00-Inbox/README|00-Inbox]]、[[raw/README|raw]]、[[index|index.md]]、[[log|log.md]]、[[08-Memory/全库中文辅助阅读规则|全库中文辅助阅读规则]] 和 2026-07-26T23:43:36Z 之后的 Git 变化。
- 初始运行 `python tools\check_vault.py --root D:\AI-Knowledge --strict`：
  - `OK: True`
  - `Markdown files: 198`
  - `Links: 1660`
  - `Broken links: 0`
  - `Missing frontmatter: 0`
  - `Raw non-index files: 7`
- [[00-Inbox/README|00-Inbox]] 当前仍只有 `README.md`，没有待分拣资料。
- [[raw/README|raw]] 当前有 7 个非索引 source notes；本周没有新增 raw source，已有 source notes 保留原始资料层位置。
- 复核近期 Git 变化：`cdae99e` 是上次周维护收口提交；`22ede4e` 同步 A4-04 Plan-and-Solve PASS 成果，已沉淀到 [[02-Concepts/Agent/计划与求解(Plan-and-Solve)|计划与求解]]、项目页、复盘页、课程页、主题索引、跳转索引、总地图、[[index|全局索引]] 和本日志。
- 根据中文辅助阅读规则复查：A4-04 新增与更新页以中文解释为主，保留 `Plan-and-Solve`、`Planner`、`Executor`、`history`、`StepResult`、`None`、`str | None`、`Replanning`、`Reflection`、`ast.literal_eval()`、路径、命令和代码片段。
- 新增 [[07-Reviews/Knowledge-Base/README|Knowledge-Base 维护复盘索引]] 与本维护复盘 [[07-Reviews/Knowledge-Base/2026-08-02-weekly-maintenance|2026-08-02 Weekly Maintenance]]。
- 更新 [[01-Maps/AI 知识库总地图|AI 知识库总地图]]：补入 [[07-Reviews/Knowledge-Base/README|Knowledge-Base 维护复盘索引]] 入口。
- 更新 [[index|index.md]]：补入 Knowledge-Base 复盘索引、本周维护复盘入口和 A4-05 / Memory 当前关注项。
- 完成编辑后再次运行严格检查：
  - `OK: True`
  - `Markdown files: 200`
  - `Links: 1704`
  - `Broken links: 0`
  - `Missing frontmatter: 0`
  - `Raw non-index files: 7`

## 2026-08-04

### AI-Agent-Learning A4-05 Reflection PASS（同步知识库）

- 复核执行区 `daily/2026-07-23.md`、`daily/2026-07-30.md`、`daily/2026-08-03.md`、`daily/2026-08-04.md` 与 `code/stage4/a4_05_reflection_writer.py`，正式判定 **A4-05 PASS**。
- 正式证据：确定性边界断言 39/39；真实正常路径为合格初稿、Reflection“无需改进”和 2 次调用提前停止；受控坏初稿后的 Reflection/Refinement 为真实 DeepSeek 调用，12/12 断言通过并接受合格候选稿。
- 扩写 [[02-Concepts/Agent/反思机制(Reflection)|反思机制]]：在原有 Reflection/事实复盘边界上，新增 `Execution → Reflection → Refinement` 数据依赖、停止轨迹、调用/延迟成本、同标准回退、prompt 软评审/客户端硬门槛和故障注入证据边界。
- 新增 [[04-Projects/Agent/AI-Agent-Learning/a4-05-reflection-writer|A4-05 Reflection Writer 项目页]] 与 [[07-Reviews/AI-Agent-Learning/2026-08-04-a4-05-reflection-review|A4-05 PASS 复盘]]；未创建同义 Reflection 概念卡。
- 更新 [[03-Courses/Agent/AI-Agent-Learning/stage4-agent-basics|阶段 4 课程页]]、课程/项目/概念索引、[[01-Maps/AI-Agent-Learning 跳转索引|跳转索引]] 与 [[index|全局索引]]；[[01-Maps/AI 知识库总地图|总地图]] 已有正确 Reflection 入口，本次 no-op。
- 项目侧复习路由：到期 `CD-003` 首答未独立闭合，已从核心定义间隔池移除并合并回活跃 `WP-12`；WS-03 维持 `DIAGNOSED_AND_FIXED`，WS-05 的坏模型输出子场景达到 `RECOVERED_UNDER_FAULT`；W4 算法仍为 `DEBT` 0/4，普通课程 PASS 不升级岗位证据。
- 同步后运行 `python tools\check_vault.py --root D:\AI-Knowledge --strict`：
  - `OK: True`
  - `Markdown files: 202`
  - `Links: 1728`
  - `Broken links: 0`
  - `Missing frontmatter: 0`
  - `Raw non-index files: 7`

## 2026-08-06

### AI-Agent-Learning W4-ALG-F2 存在重复元素 PASS（同步知识库）

- 复核 `code/algorithms/w4_02_contains_duplicate.py` 与 `daily/2026-08-06.md`，正式判定 **W4-ALG-F2 PASS**；显式测试 8/8、隐藏边界 9/9，返回类型为 `bool` 且不修改输入。
- 扩写 [[02-Concepts/Python/list·dict·set 容器|Python list、dict、set]]：新增成员检查复杂度、“已见元素”模式、`dict`/`set` 选型、平均哈希复杂度与精确整数相等语义。
- 新增 [[04-Projects/Python/AI-Agent-Learning/w4-02-contains-duplicate|W4-02 存在重复元素项目页]] 与 [[07-Reviews/AI-Agent-Learning/2026-08-06-w4-alg-f2-contains-duplicate-review|W4-ALG-F2 PASS 复盘]]；更新项目索引与全局索引，没有新建同义哈希表概念卡。
- W4 算法由 0/4 更新为 1/4，仍为 `DEBT`：两数之和待 2026-08-07～2026-08-11 独立复测，另 2 道新题未开始。
- A4-Gate 只完成 Problem Contract 设计静态核验，任务仍为 `DOING`；未把未实现的 Agent 循环或 14 条 eval 同步成 PASS 成果。
- 同步后运行 `python tools\check_vault.py --root D:\AI-Knowledge --strict`：
  - `OK: True`
  - `Markdown files: 204`
  - `Links: 1739`
  - `Broken links: 0`
  - `Missing frontmatter: 0`
  - `Raw non-index files: 7`

### AI-Agent-Learning W4-ALG-F3 有效的字母异位词 PASS（同步知识库）

- 复核 `code/algorithms/w4_03_valid_anagram.py` 与 `daily/2026-08-06.md`，正式判定 **W4-ALG-F3 PASS**；显式测试 8/8、穷举性质对照 14641/14641、万字符真假用例 2/2，返回类型均为 `bool`。
- 扩写 [[02-Concepts/Python/list·dict·set 容器|Python list、dict、set]]：新增字符频次计数，区分单次平均 `O(1)` 字典操作、`n` 次输入扫描和 `k` 个不同键的存储规模。
- 扩写 [[02-Concepts/Python/异常·调试·测试(Exceptions)|Python 异常、调试与单元测试]]：新增“断言必须调用交付接口”的假绿灯检查。
- 新增 [[04-Projects/Python/AI-Agent-Learning/w4-03-valid-anagram|W4-03 有效的字母异位词项目页]] 与 [[07-Reviews/AI-Agent-Learning/2026-08-06-w4-alg-f3-valid-anagram-review|W4-ALG-F3 PASS 复盘]]；更新项目索引与全局索引，没有新建同义哈希表或复杂度概念卡。
- W4 算法由 1/4 更新为 2/4，仍为 `DEBT`：两数之和待 2026-08-07～2026-08-11 独立复测，另 1 道新题未开始。
- 项目侧复习路由：`WP-28` 转入稳定错题间隔池，2026-08-20 首次回炉；新增活跃弱点 `WP-29`。本题不升级生产工作场景或岗位证据。
- 同步后运行 `python tools\check_vault.py --root D:\AI-Knowledge --strict`：
  - `OK: True`
  - `Markdown files: 206`
  - `Links: 1754`
  - `Broken links: 0`
  - `Missing frontmatter: 0`
  - `Raw non-index files: 7`

## 2026-08-07

### AI-Agent-Learning W4-ALG-F1 两数之和独立复测 PASS（同步知识库）

- 保留 2026-08-05 首次 `RETRY` 历史；2026-08-07 在规定窗口内脱离旧答案重建思路与函数，正式判定 **W4-ALG-F1 PASS（复测）**。
- 正式证据：项目文件规定案例 3/3；独立函数隐藏检查 5/5；自设计顶层测试 6/6；穷举性质检查 35154/35154，输入未修改。
- 扩写 [[02-Concepts/Python/list·dict·set 容器|Python list、dict、set]]：新增补数查询、“值 → 下标”映射、先查后存防同一下标自用及平均 `O(n)` / 额外 `O(n)` 因果。
- 扩写 [[02-Concepts/Python/异常·调试·测试(Exceptions)|Python 异常、调试与单元测试]]：补充断言可达性、顶层缩进、编译检查与真实执行证据的区别。
- 新增 [[04-Projects/Python/AI-Agent-Learning/w4-01-two-sum|W4-01 两数之和项目页]] 与 [[07-Reviews/AI-Agent-Learning/2026-08-07-w4-alg-f1-two-sum-review|W4-ALG-F1 PASS 复盘]]；更新项目索引与全局索引，没有新建同义哈希表概念卡。
- W4 算法由 2/4 更新为 3/4，仍为 `DEBT 1`；两数之和债务已经清除，只剩第 4 道新题。
- A4-Gate 只正式通过 C1 输入切片，整关仍为 `DOING`，未把 DRAFT 合同或未实现循环同步成 PASS 成果。
- 项目侧复习路由：`WP-17` 升到 `+1月`；`WP-20` 因到期首答失败退回活跃 🟡；`WP-27` 转入稳定池；新增活跃 `WP-30`。回收块虽已完成，dated backlog 仍有 8 项并重新签发 `RECOVERY_BLOCK_PENDING`。
- 同步后运行 `python tools\check_vault.py --root D:\AI-Knowledge --strict`：
  - `OK: True`
  - `Markdown files: 208`
  - `Links: 1769`
  - `Broken links: 0`
  - `Missing frontmatter: 0`
  - `Raw non-index files: 7`

## 2026-08-08

### AI-Agent-Learning W4-ALG-F4 存在相近的重复元素 PASS（同步知识库）

- 复核 `code/algorithms/w4_04_contains_nearby_duplicate.py` 与 `daily/2026-08-08.md`，正式判定 **W4-ALG-F4 PASS**；规定断言 8/8、性质对照 136717/136717，返回类型与输入未修改均通过。
- 扩写 [[02-Concepts/Python/list·dict·set 容器|Python list、dict、set]]：新增“值 → 最近下标”、在线比较后更新、最近记录充分性、`k=0` 边界及平均 `O(n)` / 额外 `O(n)` 因果；没有新建同义哈希表概念卡。
- 新增 [[04-Projects/Python/AI-Agent-Learning/w4-04-contains-nearby-duplicate|W4-04 存在相近的重复元素项目页]] 与 [[07-Reviews/AI-Agent-Learning/2026-08-08-w4-alg-f4-contains-nearby-duplicate-review|W4-ALG-F4 PASS 复盘]]；更新项目索引、AI-Agent-Learning 跳转索引、课程状态页与全局索引。
- W4 算法由 3/4、`DEBT 1` 收口为 4/4、内容块 `PASS`，结转债务 0；`WP-29` 升入稳定池，2026-08-22 首次回炉，新增活跃 `WP-31`。
- [[02-Concepts/LLM/采样参数与成本(Sampling)|采样参数与成本]] 已准确覆盖本日通过的 `WP-05/WP-06`，本次保持 no-op；A4-Gate 仍为 `DOING`，未把尚未实现的真实模型循环或 14 条 eval 写成 PASS。
- 同步后运行 `python tools\check_vault.py --root D:\AI-Knowledge --strict`：
  - `OK: True`
  - `Markdown files: 210`
  - `Links: 1791`
  - `Broken links: 0`
  - `Missing frontmatter: 0`
  - `Raw non-index files: 7`

### Knowledge-Base Weekly Maintenance

- 运行 `python tools\check_vault.py --root D:\AI-Knowledge --strict`，初始结果通过：210 个 Markdown、1791 个链接、0 断链、0 缺 frontmatter、7 个 raw 非索引文件。
- 复核 [[00-Inbox/README|00-Inbox]] 和 [[raw/README|raw]]：Inbox 仍只有 `README.md`；raw 没有新增 source note，本次不移动原始资料。
- 复核 2026-08-02T12:01:05Z 之后的 Git 变化：A4-05 Reflection、W4 哈希/容器算法四题、[[08-Memory/AI 学习原则|AI 学习原则]]更新已经进入对应概念卡、课程页、项目页、复盘、索引和日志。
- 按 [[08-Memory/全库中文辅助阅读规则|全库中文辅助阅读规则]]复核新增内容，保留 `Reflection`、`self-critique`、`list`、`dict`、`set`、`O(n)`、`O(1)`、路径、命令和代码块等 English technical anchors。
- 新增 [[07-Reviews/Knowledge-Base/2026-08-09-weekly-maintenance|2026-08-09 Weekly Maintenance]]，更新 [[07-Reviews/Knowledge-Base/README|Knowledge-Base 维护复盘索引]]、[[01-Maps/AI 知识库总地图|总地图]]和 [[index|全局索引]]。
- 工作树中已有 [[02-Concepts/LLM/提示工程基础(Prompt Engineering)|Prompt Engineering]] 表格对齐改动；本次维护保留但不纳入维护提交。
- 最终严格检查通过：211 个 Markdown、1824 个链接、0 断链、0 缺 frontmatter、7 个 raw 非索引文件。

## 2026-08-10

### Python 真值判断与严格布尔校验

- 去重检查 [[02-Concepts/Python/类型转换(Type Conversion)|Python 类型转换]]、[[02-Concepts/Python/and-or 短路求值|and / or 短路求值]] 与 [[02-Concepts/Python/异常·调试·测试(Exceptions)|异常、调试与测试]]：已有页面只覆盖 `bool(input(...))`、真值运算或测试返回类型的局部边界，没有系统区分 truthiness、equality 与 identity。
- 新增 [[02-Concepts/Python/真值判断与严格布尔校验(Truthiness)|Python 真值判断与严格布尔校验]]：沉淀普通真假判断、`== True` 与 `is True` 的职责边界，记录 `.get("ok", False)` 仍会放行 truthy 非布尔值的坑，以及 Agent 工具结果的 fail-closed 严格布尔模式。
- 来源证据为 AI-Agent-Learning `daily/2026-08-10.md` 与 `code/stage4/a4_gate_research_summary_agent.py`；R4b `5/5 PASS`，并有 topic / relative_path 两条真实 DeepSeek 正常链。A4-Gate 仍为 `DOING`，未把 C3c 子切片写成整个 Gate PASS。
- 更新 [[02-Concepts/Python/README|Python 概念卡索引]] 与 [[index|全局索引]]；总地图已有 Python 概念索引入口，本次保持 no-op；保留既有 Prompt Engineering 未提交改动。
- 同步后运行 `python tools\check_vault.py --root D:\AI-Knowledge --strict`：
  - `OK: True`
  - `Markdown files: 212`
  - `Links: 1838`
  - `Broken links: 0`
  - `Missing frontmatter: 0`
  - `Raw non-index files: 7`

### AI-Agent-Learning A4-Gate C3d 来源白名单与 Reflection 边界

- 正式复核 A4-Gate 当日切片：C3c 与 C3d-C1 / C2a / C2b / C3a 均通过；整个 A4-Gate 仍为 `DOING`，未把尚未实现的模型调用、JSON 集成、日志、恢复、HITL 或 14 条 eval 记为完成。
- 合并更新 [[02-Concepts/Agent/反思机制(Reflection)|反思机制]]：补充 `allowed_sources` 必须从本轮真实 Observation 派生，prompt 中的 allowlist 仍是软约束，解析后的客户端必须硬校验 `sources ⊆ allowed_sources`；同时明确“来源身份在白名单内”不等于“摘要事实已获正文支持”。
- 更新 [[02-Concepts/Agent/README|Agent 概念卡索引]]；结构化输出、函数调用、HTTP 与严格布尔既有页面已经准确覆盖 S3 回收和当天其他稳定结论，本次保持 no-op，未新建重复概念页、项目 PASS 页或阶段复盘页。
- 同步后运行 `python tools\check_vault.py --root D:\AI-Knowledge --strict`：
  - `OK: True`
  - `Markdown files: 212`
  - `Links: 1840`
  - `Broken links: 0`
  - `Missing frontmatter: 0`
  - `Raw non-index files: 7`

## 2026-08-13

### AI-Agent-Learning A4-Gate C4a-1 会话接力与进行中项目同步

- 来源为执行区的 `problem-contract.md`、当前 Agent 代码与 2026-08-12 / 2026-08-13 两份 daily；新建 [[raw/conversations/2026-08-13-ai-agent-learning-a4-gate-c4a-1-session-handoff|C4a-1 会话接力摘要]]，只保存跨会话恢复所需的范围、订正链、最终证据与下一起点，不复制完整聊天，也不替代 `tracker/progress.md`。
- 合并更新 [[04-Projects/Agent/AI-Agent-Learning/a4-gate-research-summary-agent|A4-Gate 研究摘要 Agent]]：加入 C4a-1a～1k、每请求共享 context、固定七字段日志、MAX 硬门、精确 `finish_reason == "tool_calls"`、A4-Gate 步骤表与当前运行 Mermaid 图。
- 更新 [[03-Courses/Agent/AI-Agent-Learning/README|AI-Agent-Learning 课程索引]]、[[03-Courses/Agent/AI-Agent-Learning/stage4-agent-basics|阶段 4]]、[[04-Projects/Agent/README|Agent 项目索引]]、[[01-Maps/AI-Agent-Learning 跳转索引|AI-Agent-Learning 跳转索引]]和 [[index|全局索引]]。用户澄清“整个项目”特指 A4-Gate 后，已从跳转索引移除误加的全课程路线图，改为在 A4-Gate 项目页提供“合同 → C1～C4 → HITL → 14 条 eval → 正式复核”的交付总图，以及包含输入、动作修正、retry、证据、Reflection/Refinement、五种结果与 MAX 硬门的完整运行时图。
- 精确状态边界：`C4a-1` 教学实现单元已收口，父 `A4-Gate` 仍为 `DOING`。topic/path 正常链均为 step 1～5，事件为 model/tool/model/model/model；两请求 context/logs/request ID 隔离，初始 step 2 时 Refinement 的第 7 次尝试在计时和真实副作用前拒绝。
- 下一项固定为 `C4a-2a`：可重试工具首次失败后，用同一参数至多再真实尝试一次并成功；每次尝试独立占步、计时、写日志。失败状态映射、HITL、14 条 eval 与父 Gate 正式复核仍未完成。
- 本次对概念卡、总地图和 `07-Reviews` 保持 no-op：稳定概念已有页面可承载，父 Gate 未 PASS，不能提前新建整关复盘或求职证据。
- 同步后运行 `python tools\check_vault.py --root D:\AI-Knowledge --strict`：
  - `OK: True`
  - `Markdown files: 215`
  - `Links: 1882`
  - `Broken links: 0`
  - `Missing frontmatter: 0`
  - `Raw non-index files: 8`

## 2026-08-16

### Knowledge-Base Weekly Maintenance

- 运行 `python tools\check_vault.py --root D:\AI-Knowledge --strict`，初始结果通过：215 个 Markdown、1882 个链接、0 断链、0 缺 frontmatter、8 个 raw 非索引文件。
- 复核 [[00-Inbox/README|00-Inbox]] 和 [[raw/README|raw]]：Inbox 仍只有 `README.md`；raw 新增的 [[raw/conversations/2026-08-13-ai-agent-learning-a4-gate-c4a-1-session-handoff|A4-Gate C4a-1 会话接力摘要]] 已标记为 `processed`，并已编译到 A4-Gate 项目页与 Stage 4 课程页，本次不移动原始资料。
- 复核 2026-08-09T12:02:14Z 之后的 Git 变化：Python truthiness、A4-Gate C3d / C4a-1、Reflection 来源白名单、项目流程图和索引修正已经进入对应概念卡、课程页、项目页、raw conversation、索引和日志。
- 按 [[08-Memory/全库中文辅助阅读规则|全库中文辅助阅读规则]]复核新增内容，保留 `truthiness`、`allowed_sources`、`Observation`、`Reflection`、`Refinement`、`finish_reason == "tool_calls"`、`MAX_STEPS`、路径、命令和代码块等 English technical anchors。
- 新增 [[07-Reviews/Knowledge-Base/2026-08-16-weekly-maintenance|2026-08-16 Weekly Maintenance]]，更新 [[07-Reviews/Knowledge-Base/README|Knowledge-Base 维护复盘索引]]、[[01-Maps/AI 知识库总地图|总地图]]和 [[index|全局索引]]。
- 收口工作树中已有的 [[01-Maps/AI-Agent-Learning 跳转索引|AI-Agent-Learning 跳转索引]] UTF-8 BOM 移除改动；该改动只影响 frontmatter 文件头编码，不改变正文内容。
- 最终严格检查通过：216 个 Markdown、1909 个链接、0 断链、0 缺 frontmatter、8 个 raw 非索引文件。

## 2026-08-11

### AI-Agent-Learning A4-Gate C3d 模型与 JSON 集成（进行中项目记录）

- 按用户明确要求，把今天的学习情况记录到知识库；新增 [[04-Projects/Agent/AI-Agent-Learning/a4-gate-research-summary-agent|A4-Gate 研究摘要 Agent（进行中）]]。页面明确区分：`A4-Gate-C3d = PASS`，父任务 `A4-Gate = DOING`，没有提前新建整关 PASS 复盘。
- 记录 C3d 决定性证据：主审离线 129/129、独立合同 40/40 + fail-closed 3/3 + 入口 7/7；真实 topic 与 `relative_path=sample.txt` 两条 DeepSeek 路径均为 4 次模型调用、恰好 1 次对应工具，结束序列为 `tool_calls → stop → stop → stop`。
- 记录关键订正与边界：SDK 属性对象层级、`finish_reason` 位于 choice、Reflection 普通文本与 Refinement JSON Output 分工、`json.loads` 与业务 validator 分层、Observation 来源 allowlist 硬门以及 shared client。
- 更新 Agent 项目 README、Stage 4 课程页、课程索引、AI-Agent-Learning 跳转索引与全局索引；下一切片固定为 C4a 的统一步数、七字段日志、一次重试与安全停止，随后仍需 HITL、14 条 eval 和整关复核。
- 现有 Reflection、结构化输出、函数调用、分类与 ReAct 概念卡已经准确覆盖今天的稳定概念和两个回收目标，本次保持 no-op，不为日期重复改写。
- 同步后运行 `python tools\check_vault.py --root D:\AI-Knowledge --strict`：
  - `OK: True`
  - `Markdown files: 214`
  - `Links: 1867`
  - `Broken links: 0`
  - `Missing frontmatter: 0`
  - `Raw non-index files: 7`

## 2026-08-18

### AI-Agent-Learning A4-Gate C4a-2 受控重试与人工接管同步

- 来源为执行区 `problem-contract.md`、当前 Agent 代码、`daily/2026-08-17.md` 与 `daily/2026-08-18.md`；对应实现提交为 [`1434adc`](https://github.com/humbleded/AI-Agent-Learning/commit/1434adcdd6af3ab14c55dff547c08baea9059340)。
- `C4a-2a` 已闭合一次同工具名、同原始参数的真实重试成功：模型 4 次、工具 2 次、step / 日志 `[1,2,3,4,5,6]`，第一次失败不进入成功 Tool Observation；2026-08-17 另有内存首败注入配合真实 DeepSeek 下游调用的受控恢复证据。
- `C4a-2b1` 已闭合两种自动恢复耗尽：二次可重试失败为工具 2 次、日志 `[1,2,3]`；重试前无剩余 step 为工具 1 次、日志 `[5,6]`，没有第二次工具副作用。两者都窄映射为严格三字段 `needs_manual`，完整无落盘矩阵 `15/15 PASS`，用户已确认最终轨迹符合意图。
- 新增 [[02-Concepts/Agent/受控重试与人工接管(Bounded Retry and Human Handoff)|受控重试与人工接管]]：拆分原子工具尝试、重试编排、专用耗尽信号与公开人工交接职责，补充精确终点、公开合同、不可扩大映射范围、幂等性迁移边界、验证清单，以及用 spy 检查下一次模型实际收到的 Tool Message、证明首次失败与 Python `None` 未污染消息历史的方法。
- 合并更新 [[04-Projects/Agent/AI-Agent-Learning/a4-gate-research-summary-agent|A4-Gate 研究摘要 Agent]] 的交付图、运行图、完成切片、决定性证据、当前状态与后续范围；同步更新 [[03-Courses/Agent/AI-Agent-Learning/stage4-agent-basics|阶段 4]]、[[03-Courses/Agent/AI-Agent-Learning/README|课程索引]]、[[04-Projects/Agent/README|Agent 项目索引]]、[[04-Projects/Agent/AI-Agent-Learning/README|Agent 实践索引]]、[[02-Concepts/Agent/README|Agent 概念索引]]、[[01-Maps/AI-Agent-Learning 跳转索引|跳转索引]]与 [[index|全局索引]]。
- 精确状态边界：本次只同步 `C4a-2a / C4a-2b1` 的教学实现成果；父 `A4-Gate` 继续 `DOING`。未新建整关 PASS 复盘、求职证据或 raw 对话副本，危险动作 HITL 与 14 条 eval 也未标为完成。
- 2026-08-18 S2 已启动 `A4-Gate-C4a-2b2`，当前为 `DOING / 尚未通过`：只处理有 `run_context` / 七字段账本来源证明的真实工具执行后 `retryable=False → tool_failure`，以及工具成功但空结果 `→ insufficient_evidence`；执行前的同形拒绝仍属动作校验 / 修正范围，未知动作 / 候选恢复、HITL、eval 和父 Gate 正式复核继续留后。
- 同步后运行 `python tools\check_vault.py --root D:\AI-Knowledge --strict`：
  - `OK: True`
  - `Markdown files: 217`
  - `Links: 1931`
  - `Broken links: 0`
  - `Missing frontmatter: 0`
  - `Raw non-index files: 8`

## 2026-08-19

### `if not response`、`is None` 与 Action 分层校验

- 按用户明确要求，合并更新 [[02-Concepts/Python/真值判断与严格布尔校验(Truthiness)|Python 真值判断与严格布尔校验]]，没有新建重复概念页。
- 补充 `if not response` 与 `response is None` 的语义边界：前者执行 truthiness（真值）判断，可能调用对象的 `__bool__()` 或 `__len__()`；后者只检查对象身份。加入一个属性完整但 falsey 的 `ApiResponse` 最小示例。
- 补充 Agent 分层校验结论：严格不等于每层重复全部校验。只负责结构提取的 parser 可以用 `is None` 拦截缺失值并透传其他原始未信任值；执行 / validator 层再检查类型、空白、白名单、Schema 与业务约束。`tool_name=123` 原样进入 `execute_tool_call()` 不代表它合法，而是为了在正确责任层生成具体、安全的错误并保留 Action correction 路径。
- 来源同时使用 Python 官方 Truth Value Testing / Identity comparisons 文档，以及 AI-Agent-Learning 2026-08-19 的代码与 daily 设计证据；明确标注该实现切片仍在复核中，没有据此宣称父 `A4-Gate` PASS。
- 该概念卡已由 [[02-Concepts/Python/README|Python 概念索引]]收录，本次索引保持 no-op。完成后运行 `python tools\check_vault.py --root D:\AI-Knowledge --strict` 做全库结构检查。
- 严格检查结果：`OK: True`；217 个 Markdown、1933 个链接、0 个断链、0 个缺 frontmatter、8 个 raw 非索引文件。

### AI-Agent-Learning A4-Gate C4a-2b2 / C4b-1 Action correction 同步

- 来源为执行区 `problem-contract.md`、当前 Agent 代码与 `daily/2026-08-18.md` / `daily/2026-08-19.md`；对应实现与学习证据提交为 [`da7751f`](https://github.com/humbleded/AI-Agent-Learning/commit/da7751f2525c5de3a2ecb7a9da9d94bed7d7f7d3)。`C4a-2b2` 与 `C4b-1 G1 / I1a～I2d / U1` 已完成教学实现、决定性验证和用户审核；父 `A4-Gate` 继续 `DOING`。
- 合并更新 [[02-Concepts/Agent/受控重试与人工接管(Bounded Retry and Human Handoff)|受控重试与人工接管]]，没有新建同义卡：新增 `MAX_STEPS` 全局硬门、Action correction / tool retry 局部额度与 completion budget 三层预算，补充预执行拒绝 provenance、同 ID 安全 Tool Observation、窄异常公开映射和 fail-closed 边界。
- 四条审核轨迹为：非法后修正成功 `M,M,T,M,M,M`；修正仍非法 `M,M` 且工具 0；初始合法后 retry 成功 `M,T,T,M,M,M`；修正后首工具可重试失败 `M,M,T` 且第二次工具 0。其中两条停止分支分别区分局部上限与完整链预算不足，不能都写成工具重试次数耗尽。
- 合并更新 [[04-Projects/Agent/AI-Agent-Learning/a4-gate-research-summary-agent|A4-Gate 研究摘要 Agent]] 的交付图、运行图、步骤表、决定性证据、关键订正、安全边界和剩余范围；同步更新 Truthiness 状态证据、Agent 概念索引、课程页、项目索引、跳转索引和全局索引。
- I2d 原始公开映射矩阵 `15/15` 场景、`138/138` 断言通过；机械清理后 `15/15` 场景、`150/150` 断言通过，`py_compile` / `git diff --check` 均通过。U1 用户审核通过，当前源码 SHA-256 为 `D212A8A6A5B1C70F80B33B420C2253AD2A1F19714FA98984689A81A8CD57B173`，源码 `TODO / NotImplementedError = 0 / 0`。
- 状态边界：本次没有新建 raw、整关 review 或求职证据。父 Gate 仍缺 candidate / Reflection / final validator 恢复、HITL、14 条 eval、五个必答题与正式复核。
- 同步后运行 `python tools\check_vault.py --root D:\AI-Knowledge --strict`：`OK: True`，217 个 Markdown、1935 个链接、0 个断链、0 个缺 frontmatter、8 个 raw 非索引文件。

## 2026-08-20

### AI-Agent-Learning A4-Gate C4b-2a Candidate 响应恢复同步

- 来源为执行区 `problem-contract.md`、Agent 代码与 `daily/2026-08-20.md`；对应实现和学习证据提交为 [`c8ad8cf`](https://github.com/humbleded/AI-Agent-Learning/commit/c8ad8cf063340d0ac30d8c0d0b48f6add379c145)。`C4b-2a G1～G3 / I1a～I1h / I2 / U1` 已完成教学实现、决定性验证和用户审核；父 `A4-Gate` 继续 `DOING`。
- 合并更新 [[02-Concepts/Agent/受控重试与人工接管(Bounded Retry and Human Handoff)|受控重试与人工接管]]，没有新建同义卡：新增 Candidate `valid / recoverable / terminal` 三分法、四类恢复白名单与四类 terminal 原因、terminal 优先级、一次证据受限 recovery、三步完整尾链预算和三个 stage stop kind。
- Candidate recovery 只复用同一份真实 Tool Observation，不重新执行工具，也不把失败 Candidate 写入消息历史；正常 step 3 可以用 step 4～6 完成 recovery + Reflection + Refinement，Action correction 或 tool retry 后的 step 4 Candidate 则在新模型调用前停止。
- 固定三字段 V1 保留用户选择：Candidate 最终失败时，`needs_manual.sources` 可以保留本轮真实白名单来源，但只解释为供人工接管复核的证据池，不是已验证摘要引用；`summary` 必须明确没有 Candidate / 摘要通过校验。DeepSeek `finish_reason` 与 nullable content 依据官方 Chat Completions Responses schema 于 2026-08-20 复核。
- 决定性证据为内存端到端 16 类场景、`123/123 PASS`，覆盖正常五步、Candidate recovery 六步、首次 / 恢复后 terminal、恢复耗尽、step 4 预算停止、旧 Action correction / tool retry 回归、Provider 异常和无第 7 步副作用；真实 DeepSeek `relative_path=sample.txt` 正常链退出码 0，返回非空摘要与 `sources=["sample.txt"]`。
- 合并更新 [[04-Projects/Agent/AI-Agent-Learning/a4-gate-research-summary-agent|A4-Gate 研究摘要 Agent]] 的交付图、运行图、状态表、决定性证据、关键订正、安全边界和剩余范围；同步更新 [[03-Courses/Agent/AI-Agent-Learning/stage4-agent-basics|阶段 4 课程页]]、课程索引、Agent 概念 / 项目索引、[[01-Maps/AI-Agent-Learning 跳转索引|跳转索引]]与 [[index|全局索引]]。
- [[02-Concepts/Agent/反思机制(Reflection)|Reflection 概念卡]]、AI Agent 学习资源地图和 AI-Agent-Learning 关联方案保持 no-op；Reflection 失败恢复尚未实现。没有新建 raw、整关 PASS review、求职证据或新概念页。
- 同步后运行 `python tools\check_vault.py --root D:\AI-Knowledge --strict`：`OK: True`，217 个 Markdown、1941 个链接、0 个断链、0 个缺 frontmatter、8 个 raw 非索引文件。

### AI-Agent-Learning A4-Gate C4b-2b-1 Reflection 反馈恢复同步

- 来源为执行区 `problem-contract.md`、Agent 代码与 `daily/2026-08-20.md`；对应实现和学习证据提交为 [`e4a5681`](https://github.com/humbleded/AI-Agent-Learning/commit/e4a56813aa6b4e68ffee4ab7b45d5a3a2c1d2a5f)。`C4b-2b-1 G1 / I1a～I1d / U1 = PASS`，`I1e / I1f / I2` 是依据既有 PASS 证据完成的同构整理与工程验证；父 `A4-Gate` 继续 `DOING`。
- 合并更新 [[02-Concepts/Agent/受控重试与人工接管(Bounded Retry and Human Handoff)|受控重试与人工接管]]，没有新建 Reflection recovery 同义卡：新增 Reflection 反馈 `valid / recoverable / terminal` 三分法、至多一次安全恢复、两步完整尾链预算、失败反馈隔离、阶段停止与公开 step / attempts / sources 防篡改对账。
- 合并更新 [[02-Concepts/Agent/反思机制(Reflection)|反思机制]]：明确 recovery 只恢复供 Refinement 使用的中间反馈，合法 Candidate 不是最终成功；step 5 虽剩一个位置，也不能启动需要 recovery + Refinement 两步的半条链。
- 决定性证据包括 I1d 主矩阵 `223`、独立矩阵 `217`，resolver `136`、公开 mapper `158`、完整入口 fake SDK `50`、topic fake search `5`，以及最终独立终审 `83/83`、`16/16`、AST `11/11`。真实 DeepSeek 只证明 `sample.txt` 正常五步链没有回归；坏协议恢复分支使用确定性 fake / spy 注入，没有冒充真实 Provider 故障。
- 合并更新 [[04-Projects/Agent/AI-Agent-Learning/a4-gate-research-summary-agent|A4-Gate 研究摘要 Agent]] 的交付图、运行图、状态表、决定性证据、关键订正、安全边界与剩余范围；同步更新 [[03-Courses/Agent/AI-Agent-Learning/stage4-agent-basics|阶段 4 课程页]]、课程索引、Agent 概念 / 项目索引、[[01-Maps/AI-Agent-Learning 跳转索引|跳转索引]]与 [[index|全局索引]]。
- `AI 知识库总地图`、`AI Agent 学习资源地图`、`AI-Agent-Learning 关联方案`保持 no-op；本次没有新建 raw、整关 PASS review 或岗位证据。Candidate / Reflection Provider/API、Refinement / validator、HITL、14 条 eval、五个必答题与正式整关复核继续留后。
- 同步后运行 `python tools\check_vault.py --root D:\AI-Knowledge --strict`：`OK: True`，217 个 Markdown、1949 个链接、0 个断链、0 个缺 frontmatter、8 个 raw 非索引文件。

## 2026-08-21

### AI-Agent-Learning A4-Gate C4b-2b-2a Candidate Provider/API 恢复同步

- 来源为执行区 `problem-contract.md`、当前 Agent 代码与 `daily/2026-08-21.md`；对应实现与学习证据提交为 [`5fac2ba`](https://github.com/humbleded/AI-Agent-Learning/commit/5fac2bab123ed31232ca9d96a05d2dca51509d96)。`G1～G4 / I1a / I1b / U1 = PASS`；I1c / I2 是依据已通过合同完成的机械接线与可执行验证，不冒充用户独立编码证据。父 `A4-Gate` 继续 `DOING`，Problem Contract 总体仍为 `DRAFT`。
- 合并更新 [[02-Concepts/Agent/受控重试与人工接管(Bounded Retry and Human Handoff)|受控重试与人工接管]]，没有新建同义卡：新增 SDK 内部 retry 与 Agent Provider recovery 两层账本、Provider/API 白名单与 fail-closed 分类、Candidate Provider / 协议恢复双计数、同一实际 client 复用，以及 narrow signal 对 cause、step、预算和真实来源的防篡改对账。
- 合并更新 [[02-Concepts/LLM/API 参数与 SDK 客户端参数|API 参数 vs SDK 客户端参数]]：`max_retries=2` 表示首次物理请求之外最多再重试两次；一次逻辑调用极端最多 3 次物理 HTTP 尝试，初始 Candidate + 唯一 Agent recovery 极端为 2 次逻辑调用 / 2 条聚合日志 / 最多 6 次物理尝试。fake / spy 只证明编排，真实 factory 属性证明 `max_retries=2` 与 `timeout=60.0` 配置，`_request_id` 只用于请求定位，真实物理次数仍需 transport / 服务端计数。
- 合并更新 [[04-Projects/Agent/AI-Agent-Learning/a4-gate-research-summary-agent|A4-Gate 研究摘要 Agent]] 的交付图、运行图、状态表、2026-08-21 决定性证据、关键订正、安全边界和剩余范围；同步更新 [[03-Courses/Agent/AI-Agent-Learning/stage4-agent-basics|阶段 4 课程页]]、课程索引、Agent / LLM 概念索引、Agent 项目索引、[[01-Maps/AI-Agent-Learning 跳转索引|跳转索引]]与 [[index|全局索引]]。
- 决定性证据为生产 fake/spy 故障矩阵 `14/14 PASS`、停止信号安全矩阵 `5/5 PASS`、factory / client identity 回归 `4/4 PASS`、零 HTTP 真实 factory 配置探针、`py_compile` / `git diff --check`，以及一次真实 DeepSeek `sample.txt` 正常 smoke `status=success` / `sources=["sample.txt"]` / `8.952s`。6 次物理尝试是配置推导上限，不是本轮真实网络故障计数；正常 smoke 也没有冒充 timeout / 429 / 5xx 恢复证据。
- `AI 知识库总地图`、`AI Agent 学习资源地图`、`AI-Agent-Learning 关联方案`保持 no-op；本次没有新建概念卡、raw、整关 PASS review 或岗位证据。Reflection Provider/API、Refinement / validator、HITL、14 条 eval、五个必答题和正式整关复核继续留后。
- 同步后运行 `python tools\check_vault.py --root D:\AI-Knowledge --strict`：`OK: True`，217 个 Markdown、1959 个链接、0 个断链、0 个缺 frontmatter、8 个 raw 非索引文件。

### AI-Agent-Learning A4-Gate C4b-2b-2b Reflection Provider/API 恢复同步

- 来源为执行区 `problem-contract.md`、当前 Agent 代码与 `daily/2026-08-21.md`；对应实现与学习证据提交为 [`427d60c`](https://github.com/humbleded/AI-Agent-Learning/commit/427d60c)。`G1 / I1 / U1 = PASS`；I1b / I2 是依据已通过合同完成的机械接线与可执行验证，不冒充新的用户独立编码证据。
- 合并更新 [[02-Concepts/Agent/受控重试与人工接管(Bounded Retry and Human Handoff)|受控重试与人工接管]] 与 [[02-Concepts/Agent/反思机制(Reflection)|反思机制]]，没有新建同义卡：明确 Provider 错误事件不等于 recovery 动作，两套 counter 按额外调用的发起原因归属，本地分类不计模型调用，Reflection recovery 还必须预留后续 Refinement。
- A / B / C 决定性轨迹分别为 Provider / 协议 `1/0`、`0/0`、`0/1`：正常 step 4 首败可在 step 5 Provider recovery 后进入 step 6 Refinement；首次失败已到 step 5 时因完整链预算不足而零新请求停止；step 5 protocol recovery 自身遇 Provider 错误时不倒改调用角色，也不发第三次请求。
- 合并更新 [[04-Projects/Agent/AI-Agent-Learning/a4-gate-research-summary-agent|A4-Gate 研究摘要 Agent]] 的完成图、运行图、状态表、决定性证据、关键订正、安全边界和剩余范围；同步更新阶段 4 课程页、课程 / Agent 概念 / Agent 项目索引、AI-Agent-Learning 跳转索引与全局索引。
- 决定性工程证据为主组合矩阵 `109/109`、独立终审 `96/96`、`py_compile` / `git diff --check`，以及真实 DeepSeek `sample.txt` 正常 smoke `status=success` / `sources=["sample.txt"]` / `6.778s`；正常 smoke 没有冒充真实 Provider 故障注入证据。
- 状态边界：本次只同步 `C4b-2b-2b` 教学 / 实现子单元；父 `A4-Gate` 继续 `DOING`，Problem Contract 总体仍为 `DRAFT`。没有新建整关 PASS review、raw 或岗位证据；Refinement / validator 恢复、HITL、14 条 eval、五个必答题、合同定稿和正式整关复核继续留后。
- 同步后运行 `python tools\check_vault.py --root D:\AI-Knowledge --strict`：`OK: True`，217 个 Markdown、1962 个链接、0 个断链、0 个缺 frontmatter、8 个 raw 非索引文件。

## 2026-08-22

### AI-Agent-Learning A4-Gate C4b-2c Refinement 恢复同步

- 来源为执行区 `daily/2026-08-22.md`、`code/stage4/problem-contract.md` 与 `a4_gate_research_summary_agent.py`；对应实现与学习证据已提交为 [`838adba`](https://github.com/humbleded/AI-Agent-Learning/commit/838adba79295c9505885b414977aadfdaf1ae918)。`A4-Gate-C4b-2c` 已正式 `PASS`，但父 `A4-Gate` 继续 `DOING`，Problem Contract 总体仍为 `DRAFT`。
- 合并更新 [[02-Concepts/Agent/受控重试与人工接管(Bounded Retry and Human Handoff)|受控重试与人工接管]]，没有新建 Refinement recovery 同义卡：新增 Provider、响应、JSON 与 candidate-contract 共用一次 recovery、`MAX_STEPS=6` 独立守门、Provider 原 prompt / 其他固定安全 prompt、坏输出隔离、新 candidate 全量重校验、普通程序错误上抛与来源防御复制。
- 最小更新 [[02-Concepts/Agent/反思机制(Reflection)|反思机制]] 的下游职责边界；最小纠正 [[02-Concepts/LLM/结构化输出(Structured Output)|结构化输出]] 中“`message.content` 永远是字符串”的过强表述，明确 nullable / 空正文、`finish_reason` 与“响应守门 → JSON 语法解析 → 业务 validator”分层。完整 Refinement 编排仍只放在受控重试主卡，不复制到结构化输出页。
- 合并更新 [[04-Projects/Agent/AI-Agent-Learning/a4-gate-research-summary-agent|A4-Gate 研究摘要 Agent]] 的完成图、运行控制图、步骤表、完成切片、2026-08-22 决定性证据、关键订正、安全边界与剩余范围；同步更新 [[03-Courses/Agent/AI-Agent-Learning/stage4-agent-basics|阶段 4 课程页]]、课程索引、Agent 概念 / 项目两级 README、[[01-Maps/AI-Agent-Learning 跳转索引|跳转索引]]与 [[index|全局索引]]。
- 决定性工程证据边界：实现阶段主矩阵 `94/94`、补丁回归 `5/5`、独立行为 `45/45`、stop / mapper 对抗 `22/22`、第二套独立对抗 `102/102`；正式 reviewer 另跑 `49/49`，独立代码复核 `10/10`、失败 ID `NONE`。`py_compile` / `git diff --check` 退出 0，真实 DeepSeek `sample.txt` 正常 smoke 返回 exact 三字段 `success` 与 `sources=["sample.txt"]`；真实 smoke 不冒充 Provider 故障注入或 14 条 Gate eval。
- no-op：[[02-Concepts/Agent/计划与求解(Plan-and-Solve)|Plan-and-Solve]] 已准确覆盖静态 history 与显式 Replanning 边界；本轮 `CD-005` 首答重现误区、经多级提示后才题级 PASS，因此不把该不稳定证据写成知识增量。API 参数 / SDK 客户端、HTTP、Triage、LLM README、总地图、资源地图、关联方案、开发路线、`07-Reviews`、raw 与岗位证据也保持 no-op。
- 本次共更新 12 个既有文件（含本日志），零新建概念页、raw、整关 PASS review 或岗位证据。父任务剩余仅记录为 HITL allow / deny、14 条 eval、五个 Gate 必答题、合同总体定稿和整关正式复核。
- 同步并追加本日志后运行 `python tools\check_vault.py --root D:\AI-Knowledge --strict`：`OK: True`，217 个 Markdown、1971 个链接、0 个断链、0 个缺 frontmatter、8 个 raw 非索引文件。

## 2026-08-23

### Knowledge-Base Weekly Maintenance

- 运行 `python tools\check_vault.py --root D:\AI-Knowledge --strict`，初始结果通过：217 个 Markdown、1971 个链接、0 断链、0 缺 frontmatter、8 个 raw 非索引文件。
- 复核 [[00-Inbox/README|00-Inbox]] 和 [[raw/README|raw]]：Inbox 仍只有 `README.md`；raw 仍有 8 个非索引 source notes，本周没有新增 raw source note，本次不移动原始资料。
- 复核 2026-08-16 周维护后的 Git 变化：`34c4276`、`8fcc225`、`b01a4ee`、`1c65098`、`c3303cf`、`6f27a60` 均围绕 A4-Gate C4a-2 / C4b 受控恢复链同步概念、课程、项目、索引和日志；父 `A4-Gate` 仍为 `DOING`，没有提前新建整关 PASS 复盘或求职证据。
- 按 [[08-Memory/全库中文辅助阅读规则|全库中文辅助阅读规则]]复核新增内容，保留 `bounded retry`、`human handoff`、`Action correction`、`Candidate recovery`、`Reflection recovery`、`Refinement recovery`、`Provider/API`、`MAX_STEPS`、`completion budget`、`finish_reason`、`json.loads()`、路径、命令和代码块等 English technical anchors。
- 修正 [[index|全局索引]] 中一个 stale navigation：`backpropagation`、`gradient descent`、`tokenization`、`embedding`、`attention`、`Transformer` 和 `autoregressive generation` 当前已是 `usable`，不再标为“优先扩写中的 seed 概念”；下一批待新增 LLM 概念保留为 `cross entropy`、`softmax`、`logits`、`train/validation split`、`overfitting`、`layer normalization` 与 `residual connection`。
- 新增 [[07-Reviews/Knowledge-Base/2026-08-23-weekly-maintenance|2026-08-23 Weekly Maintenance]]，更新 [[07-Reviews/Knowledge-Base/README|Knowledge-Base 维护复盘索引]]、[[01-Maps/AI 知识库总地图|总地图]]和 [[index|全局索引]]。
- 最终严格检查通过：218 个 Markdown、1997 个链接、0 个断链、0 个缺 frontmatter、8 个 raw 非索引文件。

## 2026-08-24

### AI-Agent-Learning A4-Gate 完整学习流程与正式 PASS 同步

- 用户明确授权整理全部 13 个 A4-Gate Codex 任务并同步知识库；已逐个读取完整任务内容，以执行区的 final Contract、源码、V5 eval、全链 daily 与 tracker 做事实对账，没有把任务标题或单段聊天当作权威结论。
- 合并定稿 [[04-Projects/Agent/AI-Agent-Learning/a4-gate-research-summary-agent|A4-Gate 研究摘要 Agent]]：从 Problem Contract、C1～C4、HITL、V5 RUN-5 到正式复核形成一条完整学习流程，同时保留 V4 `RETRY` 和逐题订正的历史语义。
- 新增 [[04-Projects/Agent/AI-Agent-Learning/a4-gate-function-call-reference|A4-Gate 函数调用参考]]，覆盖源码中的 62 个顶层函数、6 个嵌套 helper 与 11 个自定义构造器，并区分主编排、动态工具注册表、SDK 逻辑调用、物理 GET retry 与独立 HITL 注入分支。
- 新增 [[02-Concepts/Agent/动作绑定人工确认(Action-Bound Confirmation)|动作绑定人工确认]] 与 [[02-Concepts/Agent/冻结评估与不可补偿硬门(Frozen Evaluation)|冻结评估与不可补偿硬门]]；合并更新 [[02-Concepts/Agent/受控重试与人工接管(Bounded Retry and Human Handoff)|受控重试与人工接管]]、[[02-Concepts/Agent/反思机制(Reflection)|反思机制]]和 [[02-Concepts/LLM/LLM 本质与幻觉(Hallucination)|LLM 本质与幻觉]]，明确 exact 一致性不等于证据真实、安全或相关。
- 新增 [[07-Reviews/AI-Agent-Learning/2026-08-24-a4-gate-pass-review|A4-Gate 正式 PASS 复盘]]。V5 唯一 RUN-5 为 14/14：normal 10/10、exact 10/10、supportedness 10/10、semantic 20/20、holdout 3/3、failure 3/3、danger 1/1；没有选择性重跑、重采样、best-of 或失败替换。
- 同步课程页、课程索引、Agent 概念与项目索引、AI-Agent-Learning 跳转索引和全局索引；未创建 13 份 raw 聊天副本，也未把 `COURSE_PASS` 自动升级为 `JOB_EVIDENCE`。
- Obsidian CLI 在当前环境不可用，因此按 skill fallback 使用仓库文件、索引和严格 vault checker 完成核验；`python tools\check_vault.py --root D:\AI-Knowledge --strict` 最终为 `OK: True`：222 个 Markdown、2061 个链接、0 个断链、0 个缺 frontmatter、8 个 raw 非索引文件。

### A4-Gate 流程图可读性修复

- 针对单张 Mermaid 运行图约 95 个节点、在普通笔记视口中无法完整阅读的问题，新增 [[04-Projects/Agent/AI-Agent-Learning/a4-gate-flow.canvas|A4-Gate 可缩放全景 Canvas]]：使用 Obsidian 已启用的核心 Canvas，无需安装第三方插件；按 `Shift+1` 可适配全图，再局部缩放浏览。
- 新增 [[04-Projects/Agent/AI-Agent-Learning/a4-gate-diagrams|A4-Gate 流程图图源]]，保留权威完整运行图，并拆成请求总览以及输入/Action、工具恢复、Candidate、Reflection、Refinement/validator、HITL 六张细节图。跨图接口节点只用于连续阅读，不表示额外调用。
- 由固定版本 `@mermaid-js/mermaid-cli@11.16.0` 生成 9 张无损 SVG，主项目页改为优先嵌入 SVG 与 Canvas；旧 Mermaid 快照折叠保留。补画 `GUARD → M1_CORR` 与 `GUARD → DANGER` 两条原合同已有但旧图漏画的调用前 step 约束，没有改变 Agent 运行语义。
- 实际在 Obsidian `1.13.7` 中打开 Canvas，21 个节点、5 个分组、9 条连线与 14 个文件节点均正常加载；`Shift+1` 全图适配与主项目页 SVG 渲染通过。Canvas 和 9 张 SVG 的结构化校验全部通过，SVG 总计 `630688 bytes`。
- 窄化更新 `tools/check_vault.py`：明确带 `.canvas` / `.svg` 等受支持附件扩展名的 wikilink 必须解析到真实文件，不再被旧的强制 `.md` 后缀逻辑误判；存在/缺失附件的定向解析断言 `5/5 PASS`。最终严格检查为 `OK: True`：223 个 Markdown、2089 个链接、0 个断链、0 个缺 frontmatter、8 个 raw 非索引文件。

## 2026-08-25

### AI-Agent-Learning A4 后路线审计同步

- 来源为执行区的 `daily-plan.md`、`weekly-plan.md`、`progress.md`、`job-readiness.md`、`algorithm-progress.md` 及配套路线规则；对应路线审计提交为 [`0db733f`](https://github.com/humbleded/AI-Agent-Learning/commit/0db733f8bef176e4ea93a4f94b04fad253f22a82)。本次只同步路线审计，没有启动 G8-00，没有新增课程 PASS，也没有升级作品或岗位证据。
- 新增 [[07-Reviews/AI-Agent-Learning/2026-08-25-route-audit-review|2026-08-25 路线审计复盘]]：明确 G8-00 是仍为 `TODO` 的阶段 4.5 迁移切片，并保存 A4 后完整依赖链、H5 可选触发点与 J11-01 持续挂载规则。
- 更新 [[03-Courses/Agent/AI-Agent-Learning/README|AI-Agent-Learning 课程索引]]、[[01-Maps/AI 开发学习路线|AI 开发学习路线]]、[[01-Maps/AI-Agent-Learning 跳转索引|跳转索引]]与 [[01-Maps/AI Agent 学习资源地图|学习资源地图]]：两个旗舰分别固定为 LangChain 工程文档 RAG 助手和 LangGraph 故障诊断/变更评审 Agent；E10 复用一套共享评估框架和两个领域适配层，不另建第三项目。
- 更新 [[08-Memory/AI 学习原则|AI 学习原则]]：记录用户会一些 Vue、进入真实任务时可由助手先审计并组合 GitHub 开源 Vue 骨架，以及用户仍需审核关键改动和独立解释/修改的边界；J11-02 只冻结一个 `product_flagship`，避免重复建设两套正式前端与公网产品。
- 更新 [[01-Maps/AI-Agent-Learning 关联方案|关联方案]]：默认 RETRY 不沉淀为稳定知识，但用户明确要求同步时可以保存路线审计、失败复盘和未关闭债务，前提是如实标记状态。本次据此保留 W5 `DEBT 4` 与 W6 `RETRY / INCOMPLETE`，没有包装成 PASS。
- no-op：`02-Concepts`、`04-Projects`、raw 与岗位证据页均无新稳定成果，不为本次路线审计创建概念卡或项目记录。
- 同步更新 [[index|全局索引]]与本维护日志。
- Obsidian CLI 在当前环境不可用，因此使用仓库文件和严格 vault checker 核验；`python tools\check_vault.py --root D:\AI-Knowledge --strict` 为 `OK: True`：224 个 Markdown、2106 个链接、0 个断链、0 个缺 frontmatter、8 个 raw 非索引文件。
