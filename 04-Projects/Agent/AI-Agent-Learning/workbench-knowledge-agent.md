---
type: project
topic: Agent Workbench and Knowledge Agent
status: usable
created: 2026-09-08
updated: 2026-09-08
implementation_owner: assistant
learning_status: R6-01 DOING; G3 TODO
source:
  - https://github.com/humbleded/AI-Agent-Learning/blob/main/daily/2026-09-08.md
  - https://github.com/humbleded/AI-Agent-Learning/tree/main/code/agent_workbench
  - https://github.com/humbleded/AI-Agent-Learning/blob/main/code/stage6/engineering_docs_rag/knowledge_agent.py
tags:
  - AI/Agent
  - AI/RAG
  - Project
  - AI-Agent-Learning
  - LangChain
  - LangGraph
---

# 统一 Agent 工作台与知识库问答

> [!info] 工程已运行，课程仍在学习
> 本页记录用户明确委托助手实现并验证的产品功能。`usable` 表示这份项目记录可查阅，不代表用户独立掌握这些实现。R6-01 保持 DOING，G2 只有一个有效即时通过证据，G3 的读取节点与图仍等待用户完成；没有新增课程 PASS 或岗位能力等级。

## 为什么做这个工作台

用户希望每学会一个能力，都能在同一个前端看到输入、处理过程和结果，而不是留下一批互不相连的脚本。因此，唯一集成产品固定为 `agent_workbench`，工程文档助手与故障诊断助手保留各自的 Python 核心、测试和课程要求，共用 Vue 前端与 FastAPI 入口。

后续项目继续用 LangChain 生态的现成组件完成读取、切分、检索、模型和工具调用，由 LangGraph 连接流程。数据库、媒体编码等仍使用对应专业库。用户后续四类记忆、图片和音频需求已经纳入规划，目前尚未实现。

## 三种工作模式全部采用

用户先要求“几个模板”，随后纠正重点是整体布局、交互效果和功能组织，最后明确“可以所有的都要吗”。最终决定是三种模式全部保留，共用同一次问答。

| 模式 | 页面组织 | 适合的操作 |
| --- | --- | --- |
| 任务指挥台 `cockpit` | 左侧当前任务，中间执行与回答，右侧可收起的资料抽屉 | 快速提问，按需查看资料 |
| 知识研究工作室 `research` | 左侧检索片段与筛选，中间回答，右侧原文 | 同时对照资料、结论和出处 |
| 可视流程画布 `canvas` | 左侧问题，中间节点，右侧所选步骤的结果 | 观察真实搜索词、返回片段、答案与引用 |

- `/gallery` 是三个模式的入口，`/studio?layout=...` 可直接指定模式。
- `/studio` 不带参数时恢复上次使用的模式；首次默认 `research`。
- 切换模式不会重新提交模型请求，当前问题、答案、检索片段在同一页面会话内共享。
- 浏览器仅保存模式 ID 和独立的配色偏好；问答和资料不写入 localStorage，刷新后清空。
- 画布支持拖动、方向键移动、缩放、适应宽度和复位；拖动仅调整显示位置，不会修改后端执行流程。

## 资料怎样进入回答

可以把它理解为：本机先把笔记分成可查找的小卡片，Agent 决定搜索词，程序找到相关卡片后，把这些卡片放回模型这次实际收到的消息中。最后，模型才能依据这些内容回答。

```text
你的问题 → Vue 工作模式 → FastAPI 输入检查
                         ↓
本地笔记 → TextLoader → MarkdownTextSplitter → 内存 BM25 索引
                         ↓
                 Agent 选择搜索词
                         ↓
                 程序执行检索工具
                         ↓
              片段 + 来源 → ToolMessage → Agent
                         ↑                 │
                         └── 预算内补查 ───┤
                                           ↓
                                 生成回答 → 检查引用编号
                                           ↓
                               页面显示答案、片段与原文入口
```

`BM25` 在这里是按词语相关性给资料排序，配合中文相邻双字和英文词处理；当前没有向量数据库或按含义相似度搜索的能力。每个问题在本机重建一次内存索引，这是当前规模下的演示实现，后续再学习独立导入与增量更新。

2026-09-08 实测使用 79 份合格笔记、450 个片段。这是当次运行快照，不是固定容量或学习掌握量；后续笔记变化会改变片段数量。

## 读取范围和数据去向

- 只读 `D:/AI-Knowledge` 中 `02-Concepts`、`03-Courses`、`05-Papers` 的 Markdown。
- 排除指定的 README/index.md/规则文件、隐藏项、符号链接和 Windows junction/reparse，不沿笔记链接扩大目录范围。
- `08-Memory`、复盘、收件箱及配置目录不参与当前检索；课程目录中的计划与进度不能证明用户已掌握内容。当前论文目录只有索引时也不能说已收录论文正文。
- 每次最多 2 次搜索，每次最多 4 个片段。用户问题及有限命中片段发送给已配置的 DeepSeek；完整原文仅通过本地受限接口查看，模型密钥只在后端。
- 本查询功能不写原笔记、不把整库上传，也不执行文档中的命令。用户另外要求“同步知识库”时，是助手执行一次明确授权的知识整理，不是查询 Agent 获得了写权限。
- 服务端只接受自己生成的 `source_id` 来查原文，浏览器不能指定任意本地文件路径。引用编号检查可约束出处范围，不能代替回答是否忠实于原文的完整质量评估。

## 真实运行中发现的两个问题

1. **模型可能一次提出两个工具调用。** 即使传入 `parallel_tool_calls=False`，真实 DeepSeek 仍曾返回两个调用。修复后先校验整批工具名、参数、调用 ID 和剩余预算，再串行执行，每次单独计数并返回对应 ToolMessage。不能把模型配置当成程序一定遵守预算的保证。
2. **同一文件可能有多个不同片段。** 只按 `source_id` 保留选中项，会让 K5 在最终结果到达后跳成同文件的 K1。现在同时匹配 `citation_id` 和 `source_id`；选中引用被移除时清空选择，而不是自动换一段。

## 已验证与尚未完成

已验证的助手工程结果：

- 后端现有回归测试 42 项通过。测试使用临时资料和注入模型，真实调用单独联调。
- 真实“Tool Calling 与多步 Agent 区别”查询完成两次检索、返回 6 个出处，原文可打开。
- 真实“LangGraph 重启后恢复”查询返回 5 条过程事件、两次检索、7 个出处；原文对应已有 [[../../../02-Concepts/Agent/LangGraph 状态图编排(StateGraph)|StateGraph 笔记]]。
- 三模式切换、来源筛选、抽屉、片段/全文切换、画布拖动与缩放、模式偏好恢复均已验证；桌面与窄屏布局、类型检查和生产构建通过。
- Markdown 显示禁用原始 HTML、自动图片和链接执行，保留粗体、代码、表格等阅读格式。

仍未完成：用户 G3 读取节点、完整 R6 文档生命周期与评估、向量检索、持久历史、逐字输出、取消/断线恢复、认证、公网部署，以及记忆和媒体业务。这些沿原课程逐步补齐，助手演示不直接变成用户课程通过。

## 运行与版本证据

本次工程快照：[AI-Agent-Learning 1624eec](https://github.com/humbleded/AI-Agent-Learning/commit/1624eec8f559274ae25fc5545a517d701cec15de)。本页功能和测试结果对应这一提交；后续变化以新的项目记录为准。

从学习仓库根目录启动：

```powershell
.\.venv\Scripts\python.exe -m uvicorn main:app --app-dir code/agent_workbench/api --host 127.0.0.1 --port 8765
npm.cmd --prefix code/agent_workbench/web run dev
```

两个命令分别放在两个终端。入口为 [本地工作台](http://127.0.0.1:5173/)；依赖安装、接口、测试和许可证见 [工作台 README](https://github.com/humbleded/AI-Agent-Learning/blob/main/code/agent_workbench/README.md) 与 [选型记录](https://github.com/humbleded/AI-Agent-Learning/blob/main/resources/unified-workbench-review-2026-09-08.md)。

本轮核验日期 2026-09-08：Python 使用 core 1.6.1、LangGraph 1.2.11、community 0.4.2、langchain-openai 1.3.4、rank-bm25 0.2.2；具体依赖以仓库 requirements 和前端 package-lock 为准。community 已停止维护，本切片固定版本使用，后续解析器与检索组件扩展前需要重新核查维护状态。

官方参考：本轮实现使用 [LangGraph workflows and agents](https://docs.langchain.com/oss/python/langgraph/workflows-agents)、[LangChain ChatOpenAI](https://docs.langchain.com/oss/python/integrations/chat/openai)；界面组织参考 [Agent Chat UI](https://docs.langchain.com/oss/python/langchain/ui)、[Open WebUI Knowledge](https://docs.openwebui.com/features/workspace/knowledge/) 和 [Vue Flow](https://vueflow.dev/)，没有整套复制其应用代码。

## 相关记录

- [[README|Agent 实践索引]]
- [[../../../03-Courses/Agent/AI-Agent-Learning/README|课程接力与独立学习证据]]
- [[g8-00-incident-change-review-agent-v1|已通过的故障诊断核心]]
- [[../../../02-Concepts/Agent/智能体(Agent)|Agent 基础概念]]
- [本次原始学习回答、用户选择与运行证据](https://github.com/humbleded/AI-Agent-Learning/blob/main/daily/2026-09-08.md)
