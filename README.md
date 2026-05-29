# AI Knowledge

这是一个面向长期学习和复用的 AI 知识库，适合用 Obsidian 打开。

核心原则：

- Obsidian 负责保存、链接、检索和沉淀知识。
- AI 负责整理、提炼、追问、生成学习任务和复盘。
- 每条知识都尽量回答三个问题：它是什么？它和什么有关？我能用它做什么？

## 快速开始

1. 安装并打开 Obsidian。
2. 选择 `Open folder as vault`。
3. 打开本目录：`D:\AI-Knowledge`。
4. 从 [[index|AI Knowledge Index]] 或 [[01-Maps/AI 知识库总地图]] 开始。

## Karpathy 式工作流

本知识库按 LLM Wiki 思路维护：原始资料先进入 `raw/` 或 `00-Inbox`，再由 AI 协助编译成互相链接的 Markdown wiki。

- [[raw/README|Raw Sources]]：不可变输入层。
- [[00-Inbox/README|Inbox]]：临时收集和待分拣资料。
- [[index|AI Knowledge Index]]：全局导航入口。
- [[log|AI Knowledge Log]]：ingest、lint、结构调整和健康检查记录。
- [[AGENTS|AGENTS]]：AI 维护本仓库时必须遵守的规则。

## 当前主线

- [[01-Maps/AI 知识库总地图]]
- [[index|AI Knowledge Index]]
- [[raw/README|Raw Sources]]
- [[log|AI Knowledge Log]]
- [[01-Maps/AI Agent 学习资源地图]]
- [[01-Maps/AI-Agent-Learning 跳转索引]]
- [[03-Courses/Agent/AI-Agent-Learning/README|AI-Agent-Learning 知识沉淀]]
- [[02-Concepts/README|概念卡片索引]]
- [[03-Courses/README|课程笔记索引]]
- [[04-Projects/README|项目记录索引]]

## 目录说明

- `00-Inbox`：临时收集区，未经整理的网页、视频、想法、AI 对话摘要。
- `raw`：不可变原始资料层，用于 Karpathy 式 ingest。
- `01-Maps`：主题地图、学习路线、索引页。
- `02-Concepts`：概念卡片，一篇笔记只讲清一个概念，并按主题域二级分类。
- `03-Courses`：课程、教程、系列学习材料。
- `04-Projects`：实践项目、源码阅读、代码练习记录。
- `05-Papers`：论文阅读笔记。
- `06-Prompts`：常用 AI 提示词。
- `07-Reviews`：周复盘、月复盘、阶段总结。
- `08-Memory`：长期记忆候选、重要偏好、可复用结论。
- `copilot`：Obsidian Copilot 插件相关提示词与配置材料。
- `Templates`：笔记模板。

## 当前分类

### 概念卡片

- [[02-Concepts/Python/README|Python 概念卡]]
- [[02-Concepts/LLM/README|LLM 概念卡]]

未来主题超过 8-10 篇笔记时，再新增：

- `02-Concepts/Agent`
- `02-Concepts/MCP`
- `02-Concepts/RAG`
- `02-Concepts/Evaluation`
- `02-Concepts/Prompting`

### 课程笔记

- [[03-Courses/README|课程笔记索引]]
- [[03-Courses/Python/Python-Basics/廖雪峰 Python 教程]]
- [[03-Courses/Python/Python-Basics/CS50P Weeks 中文学习索引]]
- [[03-Courses/Python/AI-Agent-Learning/stage0-python-basics|AI-Agent-Learning 阶段 0：Python]]
- [[03-Courses/Agent/AI-Agent-Learning/README|AI-Agent-Learning Agent 资源]]
- [[03-Courses/LLM/Karpathy-Zero-to-Hero/01-micrograd|Karpathy Zero to Hero]]
- [[03-Courses/Agent/Agent-Skills-with-Anthropic/Claude Skills：让 Agent 拥有可复用专业能力的方法]]

### 项目与复盘

- [[04-Projects/README|项目记录索引]]
- [[04-Projects/Python/AI-Agent-Learning/p0-01-hello-script]]
- [[04-Projects/Python/AI-Agent-Learning/p0-02-profile-script]]
- [[04-Projects/Agent/AI-Agent-Learning/HelloAgents feature-branch-1 源码阅读索引]]
- [[07-Reviews/AI-Agent-Learning/2026-05-27-stage0-p0-01-p0-02-pass-review]]

## 写入规则

- 临时资料先放 `00-Inbox`，整理后再移动。
- 原始资料、网页、字幕、论文摘录优先放 `raw/`，不要和编译后的知识页混在一起。
- 概念卡放 `02-Concepts/主题域/`，不要直接堆在 `02-Concepts` 根目录。
- 课程资料按知识域放入 `03-Courses/知识域/课程名/`，例如 `03-Courses/Python/Python-Basics/`。
- 代码练习、源码阅读和项目记录按知识域放入 `04-Projects/知识域/项目名/`，例如 `04-Projects/Python/AI-Agent-Learning/`。
- PASS 后的阶段总结、周复盘、问题复盘放 `07-Reviews/主题/`。
- 重要偏好、长期规则和可复用结论放 `08-Memory`。
- 新增核心资料时，视情况更新 [[01-Maps/AI 知识库总地图]] 或对应主题地图。
- 完成一次 ingest、结构调整或健康检查后，在 [[log|AI Knowledge Log]] 记录。

## 推荐插件

第一阶段只需要：

- Dataview
- Templater
- Omnisearch
- Copilot 或 Smart Connections

不用一开始装太多插件。先把输入、整理、链接、复盘跑顺。
