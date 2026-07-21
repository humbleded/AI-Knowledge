---
type: maintenance-log
topic: AI Knowledge
status: active
created: 2026-05-29
updated: 2026-07-12
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
