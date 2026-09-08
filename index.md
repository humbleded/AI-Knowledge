---
type: global-index
topic: AI Knowledge
status: active
created: 2026-05-29
updated: 2026-09-08
tags:
  - 知识库
  - index
  - Karpathy
---

# AI Knowledge Index

这是给人和 LLM 都能快速导航的全局索引。新增核心资料、完成 ingest、更新学习路线后，优先同步这里或相应地图页。

## 先按问题找入口

- [[01-Maps/按问题查知识#模型要求调用工具以后程序接下来做什么|模型要求调用工具，程序接下来做什么？]]
- [[01-Maps/按问题查知识#工具一直失败什么时候重试什么时候停止|工具一直失败，什么时候重试或停止？]]
- [[01-Maps/按问题查知识#程序重启后怎样继续之前的任务|程序重启后，怎样继续之前的任务？]]
- [[01-Maps/按问题查知识#配置改了为什么没有生效|配置改了，为什么没有生效？]]
- [[01-Maps/按问题查知识#几个 Agent 方案应该怎样选|几个 Agent 方案应该怎样选？]]
- [[01-Maps/按问题查知识#资料导入后为什么回答时还找不到|资料导入后，为什么回答时还找不到？]]

这张导航只连接已有资料与项目记录。想继续学习时，直接读取执行区的 [当前接力](<C:/Users/26823/Desktop/AI-Agent-Learning/tracker/daily-plan.md>) 和 [课程进度](<C:/Users/26823/Desktop/AI-Agent-Learning/tracker/progress.md>)；笔记状态不代替学习验收。

## 最高频入口

- [[README|知识库说明]]
- [[01-Maps/按问题查知识|按问题查知识]]
- [[03-Courses/Agent/AI-Agent-Learning/README|Agent 应用开发课程与资料]]
- [[04-Projects/Agent/AI-Agent-Learning/workbench-knowledge-agent|统一工作台工程记录（助手实现）]]
- [[01-Maps/AI 知识库总地图]]
- [[01-Maps/Karpathy AI 学习路线|Karpathy 路线（模型原理选读）]]
- [[raw/README|Raw Sources]]
- [[raw/initial-link-sources|Initial Link Sources]]
- [[00-Inbox/README|Inbox]]
- [[log|维护日志]]

## 主线地图

- [[01-Maps/AI 知识库总地图]]
- [[01-Maps/AI 开发学习路线]]
- [[01-Maps/AI Agent 学习资源地图]]
- [[01-Maps/AI-Agent-Learning 跳转索引]]
- [[01-Maps/AI-Agent-Learning 关联方案]]
- [[01-Maps/AI + Obsidian 工作流]]
- [[01-Maps/Python/python-official-docs-map|Python Official Docs Map]]
- [[01-Maps/MCP/mcp-official-docs-map|MCP Official Docs Map]]
- [[01-Maps/标签与命名规范]]

## 概念卡片

- [[02-Concepts/README|概念卡片总索引]]
- [[02-Concepts/Python/README|Python 概念卡]]
- [[02-Concepts/Python/真值判断与严格布尔校验(Truthiness)|Python 真值判断与严格布尔校验：truthiness / equality / identity]]
- [[02-Concepts/Python/and-or 短路求值|Python and / or 短路与返回原值]]
- [[02-Concepts/Python/函数与参数(Functions)|Python 函数、参数与 return]]
- [[02-Concepts/Python/偏函数(functools.partial)|Python 偏函数 functools.partial 与默认参数]]
- [[02-Concepts/Python/list·dict·set 容器|Python list、dict、set]]
- [[02-Concepts/Python/环境管理(venv & pip)|Python 项目环境管理：venv、pip 与 .env]]
- [[02-Concepts/Python/异常·调试·测试(Exceptions)|Python 异常、调试与单元测试]]
- [[02-Concepts/Python/文件读写与 JSON 序列化|Python 文件读写与 JSON 序列化]]
- [[02-Concepts/Python/JSON 学习日志 CLI|Python JSON 学习日志 CLI：list[dict] 与输入校验]]
- [[02-Concepts/Python/strip() 与数据清洗|Python strip 与洗运行时脏数据]]
- [[02-Concepts/LLM/API Key 与 SDK|API Key 与 SDK：调用模型的门禁卡和快递柜台]]
- [[02-Concepts/LLM/调用 chat.completions|调用 LLM：chat.completions 与取回复]]
- [[02-Concepts/LLM/消息角色与指令优先级(Instruction Hierarchy)|消息角色与指令优先级]]
- [[02-Concepts/LLM/LLM 本质与幻觉(Hallucination)|LLM 本质与幻觉]]
- [[02-Concepts/LLM/多轮对话与无状态记忆(Stateless Memory)|多轮对话：接口无状态与客户端记忆]]
- [[02-Concepts/LLM/流式输出(Streaming)|流式输出：stream=True 与逐 chunk 处理]]
- [[02-Concepts/LLM/采样参数与成本(Sampling)|采样参数与成本：temperature 与 token 计费]]
- [[02-Concepts/LLM/特殊Token(Special Tokens)|特殊Token：模型词表里的控制暗号]]
- [[02-Concepts/LLM/提示工程基础(Prompt Engineering)|Prompt 工程基础：角色扮演 / few-shot / CoT / 清晰指令]]
- [[02-Concepts/LLM/摘要与改写(Summarize & Transform)|摘要与改写：Summarizing vs Transforming]]
- [[02-Concepts/LLM/分类与路由(Classification & Routing)|分类与路由：Classification 与 Routing]]
- [[02-Concepts/LLM/上下文工程(Context Engineering)|上下文工程：策划进窗口的整组 token]]
- [[02-Concepts/LLM/结构化输出(Structured Output)|结构化输出：让模型吐出程序能吃的 JSON]]
- [[02-Concepts/LLM/函数调用(Function Calling)|函数调用：模型点菜、程序炒菜（Tool Calling）]]
- [[02-Concepts/Agent/README|Agent 概念卡]]
- [[02-Concepts/Agent/智能体(Agent)|智能体：LLM + 工具 + 客户端调度 + Observation 反馈循环]]
- [[02-Concepts/Agent/ReAct推理与行动循环(ReAct)|ReAct：Thought / Action / Observation 循环与停止条件]]
- [[02-Concepts/Agent/计划与求解(Plan-and-Solve)|Plan-and-Solve：Planner / Executor、history 与 Replanning 边界]]
- [[02-Concepts/Agent/反思机制(Reflection)|Reflection：三阶段改进闭环、反馈恢复完整尾链、质量门槛与运行事实复盘边界]]
- [[02-Concepts/Agent/工具调用与动作(Tool Calling and Action)|工具调用与动作：Tool / Tool Calling / Action]]
- [[02-Concepts/Agent/工具定义与执行协议(Tool Definition)|工具定义与执行协议：Name / Description / Execution Logic]]
- [[02-Concepts/Agent/文件工具沙箱(File Tool Sandbox)|文件工具沙箱：resolve + relative_to 的安全边界]]
- [[02-Concepts/Agent/外部 API 工具(External API Tool)|外部 API 工具：timeout / 错误兜底 / 必要字段摘要]]
- [[02-Concepts/Agent/受控重试与人工接管(Bounded Retry and Human Handoff)|受控重试与人工接管：判断能否重试、共享预算、停止与交接]]
- [[02-Concepts/Agent/动作绑定人工确认(Action-Bound Confirmation)|动作绑定人工确认：冻结动作深绑定、一次性消费与重放防护]]
- [[02-Concepts/Agent/冻结评估与不可补偿硬门(Frozen Evaluation)|冻结评估与不可补偿硬门：唯一正式运行、版本指纹、holdout 与 exact / semantic 分层]]
- [[02-Concepts/Agent/LangGraph 状态图编排(StateGraph)|LangGraph StateGraph：State / Node / Edge、条件路由、stream 与应用控制边界]]
- [[02-Concepts/LLM/API 参数与 SDK 客户端参数|API 参数 vs SDK 客户端参数]]
- [[02-Concepts/LLM/README|LLM 概念卡]]
- [[02-Concepts/MCP/README|MCP 概念卡]]
- [[02-Concepts/MCP/MCP(Model Context Protocol)|Model Context Protocol]]
- [[02-Concepts/Engineering/README|Engineering 概念卡]]
- [[02-Concepts/Engineering/调试与错误恢复(Triage)|调试与错误恢复：系统化 triage]]
- [[02-Concepts/Engineering/HTTP 请求全链路与错误处理|一次 HTTP 请求的全链路与三类错误处理]]
- [[02-Concepts/Engineering/服务端请求伪造(SSRF)|服务端请求伪造：服务器替攻击者访问内网目标]]

已可复习的 LLM 基础概念（原 seed 已转 `usable`）：

- [[02-Concepts/LLM/反向传播(Backprop)]]
- [[02-Concepts/LLM/梯度下降(Gradient Descent)]]
- [[02-Concepts/LLM/分词(Tokenization)]]
- [[02-Concepts/LLM/嵌入(Embedding)]]
- [[02-Concepts/LLM/注意力机制(Attention)]]
- [[02-Concepts/LLM/Transformer]]
- [[02-Concepts/LLM/自回归生成(Autoregressive)]]

模型原理的选读候选：`cross entropy`、`softmax`、`logits`、`train/validation split`、`overfitting`、`layer normalization`、`residual connection`。需要解释当前项目或主动选读时再补，不自动加入当前学习队列。

## 课程与路线

- [[03-Courses/README|课程笔记索引]]
- [[03-Courses/LLM/Karpathy-Zero-to-Hero/README|Karpathy Zero to Hero]]
- [[03-Courses/LLM/Karpathy-Zero-to-Hero/01-micrograd]]
- [[03-Courses/LLM/Karpathy-Zero-to-Hero/02-makemore]]
- [[03-Courses/LLM/Karpathy-Zero-to-Hero/05-gpt-from-scratch]]
- [[03-Courses/LLM/AI-Agent-Learning/stage1-llm-api-basics]]
- [[03-Courses/LLM/AI-Agent-Learning/stage2-prompt-structured-output]]
- [[03-Courses/Python/Python-Basics/python-core-reading-route|Python 官方手册核心阅读路线]]
- [[03-Courses/Python/AI-Agent-Learning/stage0-python-basics]]
- [[03-Courses/Agent/AI-Agent-Learning/README]]
- [[03-Courses/Agent/AI-Agent-Learning/stage3-tool-calling]]
- [[03-Courses/Agent/AI-Agent-Learning/stage4-agent-basics]]
- [[03-Courses/Agent/AI-Agent-Learning/stage4_5-langgraph-basics|阶段 4.5：LangGraph 基础工作流]]
- [[03-Courses/Agent/AI-Agent-Learning/stage0_5-engineering-basics]]

## 论文

- [[05-Papers/README|论文笔记索引]]
- [[raw/papers/README|论文原始资料]]

## 项目与实践

- [[04-Projects/README|项目记录索引]]
- [[04-Projects/LLM/README|LLM 项目记录]]
- [[04-Projects/LLM/micrograd-backprop-from-scratch|Micrograd：从零实现反向传播]]
- [[04-Projects/Python/AI-Agent-Learning/p0-01-hello-script]]
- [[04-Projects/Python/AI-Agent-Learning/p0-02-profile-script]]
- [[04-Projects/Python/AI-Agent-Learning/p0-03-scheduler]]
- [[04-Projects/Python/AI-Agent-Learning/p0-04-tasks]]
- [[04-Projects/Python/AI-Agent-Learning/p0-05-plan-functions]]
- [[04-Projects/Python/AI-Agent-Learning/p0-06-env-check]]
- [[04-Projects/Python/AI-Agent-Learning/p0-07-safe-divide]]
- [[04-Projects/Python/AI-Agent-Learning/p0-08-progress-file]]
- [[04-Projects/Python/AI-Agent-Learning/p0-09-http-request]]
- [[04-Projects/Python/AI-Agent-Learning/p0-gate-learning-log]]
- [[04-Projects/Python/AI-Agent-Learning/w4-01-two-sum|W4-01 两数之和]]
- [[04-Projects/Python/AI-Agent-Learning/w4-02-contains-duplicate|W4-02 存在重复元素]]
- [[04-Projects/Python/AI-Agent-Learning/w4-03-valid-anagram|W4-03 有效的字母异位词]]
- [[04-Projects/Python/AI-Agent-Learning/w4-04-contains-nearby-duplicate|W4-04 存在相近的重复元素]]
- [[04-Projects/LLM/AI-Agent-Learning/l1-01-first-call]]
- [[04-Projects/LLM/AI-Agent-Learning/l1-gate-cli-chatbot]]
- [[04-Projects/LLM/AI-Agent-Learning/pr2-01-02-handson]]
- [[04-Projects/LLM/AI-Agent-Learning/pr2-03-classifier-routing]]
- [[04-Projects/LLM/AI-Agent-Learning/pr2-gate-email-processor]]
- [[04-Projects/Agent/AI-Agent-Learning/README]]
- [[04-Projects/Agent/AI-Agent-Learning/workbench-knowledge-agent|统一 Agent 工作台与知识库问答（三模式全部采用，助手工程记录）]]
- [[04-Projects/Agent/AI-Agent-Learning/t3-02-calculator-tool]]
- [[04-Projects/Agent/AI-Agent-Learning/t3-03-file-reader-tool]]
- [[04-Projects/Agent/AI-Agent-Learning/t3-04-public-api-tool]]
- [[04-Projects/Agent/AI-Agent-Learning/t3-gate-tool-assistant]]
- [[04-Projects/Agent/AI-Agent-Learning/a4-03-react-agent]]
- [[04-Projects/Agent/AI-Agent-Learning/a4-04-plan-and-solve]]
- [[04-Projects/Agent/AI-Agent-Learning/a4-05-reflection-writer]]
- [[04-Projects/Agent/AI-Agent-Learning/a4-gate-research-summary-agent|A4-Gate 研究摘要 Agent（正式 PASS，完整学习流程）]]
- [[04-Projects/Agent/AI-Agent-Learning/a4-gate-function-call-reference|A4-Gate 函数调用参考]]
- [[04-Projects/Agent/AI-Agent-Learning/g8-00-incident-change-review-agent-v1|G8-00 故障诊断与变更评审 Agent v1]]
- [[04-Projects/Agent/AI-Agent-Learning/HelloAgents feature-branch-1 源码阅读索引]]

## 复盘与记忆

- [[07-Reviews/Knowledge-Base/2026-09-08-question-navigation-check|问题导航、模板与重点笔记整理检查]]
- [[07-Reviews/Knowledge-Base/2026-09-08-workbench-sync-check|工作台同步后的知识库检查]]

- [[07-Reviews/AI-Agent-Learning/2026-05-27-stage0-p0-01-p0-02-pass-review]]
- [[07-Reviews/AI-Agent-Learning/2026-05-28-stage0-p0-03-pass-review]]
- [[07-Reviews/AI-Agent-Learning/2026-06-02-stage0-p0-04-pass-review]]
- [[07-Reviews/AI-Agent-Learning/2026-06-09-stage0-p0-05-pass-review]]
- [[07-Reviews/AI-Agent-Learning/2026-06-10-stage0-p0-06-pass-review]]
- [[07-Reviews/AI-Agent-Learning/2026-06-11-stage0-p0-07-pass-review]]
- [[07-Reviews/AI-Agent-Learning/2026-06-13-stage0-p0-08-pass-review]]
- [[07-Reviews/AI-Agent-Learning/2026-06-14-stage0-p0-gate-l1-01-pass-review]]
- [[07-Reviews/AI-Agent-Learning/2026-06-27-stage1-l1-gate-pass-review]]
- [[07-Reviews/AI-Agent-Learning/2026-06-27-pr2-01-02-handson-review]]
- [[07-Reviews/AI-Agent-Learning/2026-06-28-pr2-03-classifier-routing-review]]
- [[07-Reviews/AI-Agent-Learning/2026-07-05-pr2-gate-email-processor-review]]
- [[07-Reviews/AI-Agent-Learning/2026-07-06-t3-02-calculator-tool-review]]
- [[07-Reviews/AI-Agent-Learning/2026-07-07-t3-03-file-reader-tool-review]]
- [[07-Reviews/AI-Agent-Learning/2026-07-08-t3-04-public-api-tool-review]]
- [[07-Reviews/AI-Agent-Learning/2026-07-09-a4-01-what-is-agent-review]]
- [[07-Reviews/AI-Agent-Learning/2026-07-12-t3-gate-tool-calling-review]]
- [[07-Reviews/AI-Agent-Learning/2026-07-15-a4-02-llm-agent-basics-review]]
- [[07-Reviews/AI-Agent-Learning/2026-07-22-a4-03-react-review]]
- [[07-Reviews/AI-Agent-Learning/2026-07-30-a4-04-plan-and-solve-review]]
- [[07-Reviews/AI-Agent-Learning/2026-08-04-a4-05-reflection-review]]
- [[07-Reviews/AI-Agent-Learning/2026-08-06-w4-alg-f2-contains-duplicate-review]]
- [[07-Reviews/AI-Agent-Learning/2026-08-06-w4-alg-f3-valid-anagram-review]]
- [[07-Reviews/AI-Agent-Learning/2026-08-07-w4-alg-f1-two-sum-review]]
- [[07-Reviews/AI-Agent-Learning/2026-08-08-w4-alg-f4-contains-nearby-duplicate-review]]
- [[07-Reviews/AI-Agent-Learning/2026-08-24-a4-gate-pass-review|A4-Gate 正式 PASS 复盘]]
- [[07-Reviews/AI-Agent-Learning/2026-08-25-route-audit-review|AI-Agent-Learning 路线审计复盘（未新增课程 PASS）]]
- [[07-Reviews/AI-Agent-Learning/2026-09-05-g8-00-langgraph-v1-review|G8-00 LangGraph v1 正式 PASS 复盘]]
- [[07-Reviews/Daily-Practice/2026-06-04-review]]
- [[07-Reviews/Daily-Practice/2026-06-05-review]]
- [[07-Reviews/Knowledge-Base/README|Knowledge-Base 维护复盘索引]]
- [[07-Reviews/Knowledge-Base/2026-05-29-karpathy-health-check]]
- [[07-Reviews/Knowledge-Base/2026-05-29-vault-check-automation]]
- [[07-Reviews/Knowledge-Base/2026-05-31-weekly-maintenance]]
- [[07-Reviews/Knowledge-Base/2026-06-07-weekly-maintenance]]
- [[07-Reviews/Knowledge-Base/2026-06-08-weekly-maintenance]]
- [[07-Reviews/Knowledge-Base/2026-06-15-weekly-maintenance]]
- [[07-Reviews/Knowledge-Base/2026-06-21-weekly-maintenance]]
- [[07-Reviews/Knowledge-Base/2026-06-28-weekly-maintenance]]
- [[07-Reviews/Knowledge-Base/2026-07-05-weekly-maintenance]]
- [[07-Reviews/Knowledge-Base/2026-07-12-weekly-maintenance]]
- [[07-Reviews/Knowledge-Base/2026-07-19-weekly-maintenance]]
- [[07-Reviews/Knowledge-Base/2026-07-27-weekly-maintenance]]
- [[07-Reviews/Knowledge-Base/2026-08-02-weekly-maintenance]]
- [[07-Reviews/Knowledge-Base/2026-08-09-weekly-maintenance]]
- [[07-Reviews/Knowledge-Base/2026-08-16-weekly-maintenance]]
- [[07-Reviews/Knowledge-Base/2026-08-23-weekly-maintenance]]
- [[08-Memory/知识库长期记忆规则]]
- [[08-Memory/全库中文辅助阅读规则]]
- [[08-Memory/AI 学习原则]]

## 提示词

- [[06-Prompts/全库中文辅助阅读提示词]]

## 维护任务

- 每次 ingest：更新相关笔记、补链接、记录 [[log]]。
- 每周健康检查：检查断链、seed 过多、孤立页、缺来源、重复概念。
- 每次学习任务 PASS：同步 `02-Concepts`、`03-Courses`、`04-Projects`、`07-Reviews` 中应更新的部分。

## 当前优先扩展

- 优先维护 [[01-Maps/按问题查知识|按问题查知识]]：用当前常见问题串起概念、例子与实际项目，已有内容准确时直接引用。
- 沿工程文档问答的真实学习进展整理资料：读取 → 切分 → 检索 → 回答与引用。当前起点和未覆盖内容只认执行区 [daily-plan.md](<C:/Users/26823/Desktop/AI-Agent-Learning/tracker/daily-plan.md>)，完整依赖见 [weekly-plan.md](<C:/Users/26823/Desktop/AI-Agent-Learning/tracker/weekly-plan.md>)，本页不复制易过时的检查点快照。
- 在实际复习或修改时，用 [[Templates/概念笔记模板|概念笔记模板]] 补齐使用场景、最小例子、常见误解、适用条件与来源；先维护经常使用的卡片。
- 已有工程能力和待学内容分别查 [[04-Projects/Agent/AI-Agent-Learning/workbench-knowledge-agent|工作台项目记录]] 与 [[03-Courses/Agent/AI-Agent-Learning/README|课程资料索引]]。系统答不好的问题与用户学习弱点分开处理，不把演示或笔记整理算作课程 PASS。
- Karpathy、micrograd 与其他模型原理材料继续作为 [[01-Maps/Karpathy AI 学习路线|选读路线]] 保留，按需要补来源或实验，不自动扩成第二条主线。
