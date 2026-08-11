---
type: project
topic: AI-Agent-Learning A4-Gate Research Summary Agent
status: doing
created: 2026-08-11
updated: 2026-08-11
source:
  - C:\Users\26823\Desktop\AI-Agent-Learning\code\stage4\problem-contract.md
  - C:\Users\26823\Desktop\AI-Agent-Learning\code\stage4\a4_gate_research_summary_agent.py
  - C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-08-11.md
tags:
  - Agent
  - Tool-Calling
  - Reflection
  - Structured-Output
  - DeepSeek
  - AI-Agent-Learning
---

# A4-Gate 研究摘要 Agent（进行中）

> [!important] 状态边界
> `A4-Gate-C3d` 已于 2026-08-11 正式 `PASS`；父任务 `A4-Gate` 仍为 `DOING`。本页记录可复查的项目进展，不是整关 PASS 复盘。

## 目标与当前产物

- 目标：接收 `topic` 或受沙箱约束的 `relative_path`，只执行一个与请求匹配的工具，再基于本轮真实 Observation 生成带来源的三字段研究摘要。
- 设计合同：`C:\Users\26823\Desktop\AI-Agent-Learning\code\stage4\problem-contract.md`，整关通过前保持 `DRAFT`。
- 当前实现：`C:\Users\26823\Desktop\AI-Agent-Learning\code\stage4\a4_gate_research_summary_agent.py`。
- 当日正式证据：`C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-08-11.md`。

最终成功对象只能包含：

```json
{
  "status": "success",
  "summary": "非空摘要",
  "sources": ["本轮真实来源"]
}
```

## 当前可信数据流

```text
原始请求
  -> prepare_request：规范化或零副作用返回 invalid_input
  -> 模型 1：提出恰好一个 Tool Call
  -> 客户端：执行 read_material 或 search_web 恰好一次
  -> Observation：把真实工具结果送回同一会话
  -> 模型 2：生成不可信候选摘要
  -> Reflection：普通文本反馈，不开放工具、不要求 JSON
  -> Refinement：JSON Output，不开放工具，max_tokens=1600
  -> json.loads：只负责 JSON 语法解析
  -> validate_success_result：硬校验精确三键、非空摘要和来源子集
```

未注入客户端时只创建一个 client；四次模型请求共用这个对象。输入校验、allowlist 派生和 prompt 构造等纯 Python 边界在 client factory 之前执行，失败时不会误触发模型或工具。

## 已完成切片

| 切片 | 状态 | 结果 |
|---|---|---|
| Problem Contract | 已冻结设计，仍为 DRAFT | 固定输入、输出、工具、停止、日志、HITL 与 eval 边界 |
| C1 / C2 | PASS | 请求准备、文件工具、搜索工具与错误边界闭合 |
| C3a / C3b / C3c | PASS | 工具 schema、白名单分发、两次模型 + 一次工具候选链闭合 |
| C3d-I1 | PASS | Reflection 单次调用与 SDK 响应外壳 fail-closed |
| C3d-I2 | PASS | Refinement JSON Output、`finish_reason`、`json.loads` 分层闭合 |
| C3d-I3 | PASS | Reflection → Refinement → validator 编排闭合 |
| C3d-I4 | PASS | 原始请求到可信三字段结果的 topic/path 正常链闭合 |

## 2026-08-11 决定性证据

- 主审离线矩阵：`129/129`，包括 Reflection 47、Refinement 52、I3 编排 12、I4 wrapper 16、正则复测 2。
- 独立复核：冻结范围合同 `40/40`、实际 fail-closed 链 `3/3`、入口与异常传播 `7/7`，`FAILED_IDS=[]`。
- 真实 DeepSeek topic 路径：模型 4 次、`search_web` 1 次，结束序列为 `tool_calls → stop → stop → stop`，最终 2 个来源均来自本轮搜索结果。
- 真实 DeepSeek `relative_path=sample.txt` 路径：模型 4 次、`read_material` 1 次，结束序列相同，最终来源精确为 `sample.txt`。
- 两条真实路径的 Reflection 请求均无 `response_format`；Refinement 均使用 `response_format={"type":"json_object"}`、`max_tokens=1600`。
- `max_tokens=1600` 继续作为观测期上限：反复出现 `finish_reason="length"` 才增大；长期代表性输出远低于上限且质量持续通过，才考虑调小。

## 关键订正

1. OpenAI 兼容 SDK 返回的是属性对象，不是嵌套 `dict`；响应必须按 `response → choices[0] → message` 读取。
2. `finish_reason` 位于 `choice`，不是 `message`；Reflection 与 Refinement 当前只接受 `stop`。
3. 外部响应缺字段、非 `stop`、意外 tool calls、空正文或坏 JSON 都属于运行时协议失败，应 fail-closed 为 `RuntimeError`，不能泄漏 `AttributeError` 或伪造成功。
4. `prepare_request()` 返回二项结果，入口必须先解包规范化请求与非法结果；C3c 返回三键字典，必须按精确键取值，不能直接迭代解包字典。
5. `response_format={"type":"json_object"}` 只约束模型输出形式，SDK 仍返回字符串；必须经过 `json.loads`，再由 validator 做业务合同校验。

## 安全边界

- `allowed_sources` 只能从本轮真实 Observation 派生；最终 `sources` 必须是它的非空子集。
- Prompt 中的来源名单是软约束，客户端 validator 才是硬门。
- 来源身份属于 allowlist 只能证明“引用来自本轮工具结果”，不能单独证明摘要中的每个事实都被正文支持；语义真实性仍需固定 eval 与人工抽查。
- 非法输入会在 client、模型和工具之前返回；Reflection 与 Refinement 均不暴露工具。

## 尚未完成与下一切片

父任务仍缺：

- `C4a`：统一 `request_id/step`、七字段日志、`max_steps=6`、一次可重试工具故障与 `needs_manual` 安全收口。
- 候选响应边界：C3c 第二次响应目前只检查非空正文，尚未拒绝或受控处理 `finish_reason="length"`。
- 空证据边界：`search_web` 返回 `ok=True, results=[]` 时应提前映射为 `insufficient_evidence`，避免继续浪费后续模型调用。
- HITL：高风险 fake 工具的 allow/deny 可执行证据。
- `eval_cases.json`：14 条固定案例、至少 3 条 holdout 和正式 Gate 阈值。

下一 Session 从 `A4-Gate-C4a` 开始；完成这些范围并通过整关复核前，不新建 A4-Gate PASS 复盘，也不升级岗位证据。

## 相关链接

- [[../../../02-Concepts/Agent/反思机制(Reflection)|反思机制]]
- [[../../../02-Concepts/LLM/结构化输出(Structured Output)|结构化输出]]
- [[../../../02-Concepts/LLM/函数调用(Function Calling)|函数调用 / Tool Calling]]
- [[../../../03-Courses/Agent/AI-Agent-Learning/stage4-agent-basics|阶段 4：Agent 基础原理]]
