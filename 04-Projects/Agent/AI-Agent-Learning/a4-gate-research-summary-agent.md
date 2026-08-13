---
type: project
topic: AI-Agent-Learning A4-Gate Research Summary Agent
status: doing
created: 2026-08-11
updated: 2026-08-13
source:
  - C:\Users\26823\Desktop\AI-Agent-Learning\code\stage4\problem-contract.md
  - C:\Users\26823\Desktop\AI-Agent-Learning\code\stage4\a4_gate_research_summary_agent.py
  - C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-08-11.md
  - C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-08-12.md
  - C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-08-13.md
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
> `A4-Gate-C4a-1` 已于 2026-08-13 收口；父任务 `A4-Gate` 仍为 `DOING`。本页记录可复查的进行中项目进展，不是整关 PASS 复盘，也不升级求职证据。

## 目标与当前产物

- 目标：接收 `topic` 或受沙箱约束的 `relative_path`，只执行一个与请求匹配的工具，再基于本轮真实 Observation 生成带来源的三字段研究摘要。
- 设计合同：`C:\Users\26823\Desktop\AI-Agent-Learning\code\stage4\problem-contract.md`，整关通过前保持 `DRAFT`。
- 当前实现：`C:\Users\26823\Desktop\AI-Agent-Learning\code\stage4\a4_gate_research_summary_agent.py`。
- 证据链：`C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-08-11.md`、`2026-08-12.md`、`2026-08-13.md`。

最终成功对象只能包含：

```json
{
  "status": "success",
  "summary": "非空摘要",
  "sources": ["本轮真实来源"]
}
```

## A4-Gate 完整流程图

> [!info] 图例与范围
> `✅` 表示已经获得当前项目证据，`⏳` 表示 Problem Contract 已冻结但实现或正式验收尚未完成。第二张图展示 **A4-Gate 最终目标控制流**；尚未完成的分支不能当成当前代码已经具备的能力。

### 1. 从需求合同到正式过关

```mermaid
flowchart LR
    PC["Problem Contract<br/>第 1～11 节已完成<br/>整关前保持 DRAFT"] --> C1["C1<br/>输入校验 + 固定三字段 PASS"]
    C1 --> C2["C2<br/>read_material / search_web PASS"]
    C2 --> C3A["C3a<br/>工具 Schema PASS"]
    C3A --> C3B["C3b<br/>白名单调度 + 参数硬校验 PASS"]
    C3B --> C3C["C3c<br/>模型 → 工具 → 候选摘要<br/>正常路径 PASS"]
    C3C --> C3D["C3d<br/>Reflection → Refinement<br/>→ 最终 validator PASS"]
    C3D --> C4A1["C4a-1<br/>共享 context、七字段日志、MAX、协议守门 PASS"]
    C4A1 --> C4A2["C4a-2<br/>一次工具 retry + 失败状态映射 ⏳"]
    C4A2 --> REC["Action / candidate<br/>校验失败恢复与安全停止 ⏳"]
    REC --> HITL["HITL<br/>危险 fake allow / deny ⏳"]
    HITL --> DATA["eval_cases.json<br/>10 normal + 3 failure + 1 danger<br/>至少 3 holdout ⏳"]
    DATA --> REVIEW{"A4-Gate 正式复核 ⏳"}
    REVIEW -->|"确定性合同与安全全过；语义阈值达标"| PASS["A4-Gate PASS"]
    REVIEW -->|"存在缺口"| RETRY["保留 A4-Gate = DOING<br/>修复失败项并重跑对应回归"]
    RETRY --> C4A2

    classDef designed fill:#d9eaf7,stroke:#0b5394,color:#1f1f1f;
    classDef done fill:#d9ead3,stroke:#38761d,color:#1f1f1f;
    classDef pending fill:#fff2cc,stroke:#bf9000,color:#1f1f1f;
    classDef gate fill:#d9eaf7,stroke:#0b5394,color:#1f1f1f;
    class PC designed;
    class C1,C2,C3A,C3B,C3C,C3D,C4A1 done;
    class C4A2,REC,HITL,DATA,RETRY pending;
    class REVIEW,PASS gate;
```

### 2. 目标运行时完整控制流

```mermaid
flowchart TD
    START["请求：input_type + value"] --> PRE{"C1 输入校验与规范化 ✅"}
    PRE -->|"非法"| INVALID["invalid_input<br/>固定三字段；零 context / 零模型 / 零工具"]
    PRE -->|"合法"| INIT["创建一个 client + 一个独立 run_context ✅"]

    INIT --> M1["step 1：模型选择工具<br/>reserve → clock → create → 七字段日志 ✅"]
    M1 --> F1{"choice.finish_reason<br/>精确等于 tool_calls？ ✅"}
    F1 -->|"否"| ACTION_REC["把协议/动作错误交回模型修正 ⏳"]
    F1 -->|"是"| ACTION{"工具名、JSON、Schema、类型<br/>和规范化请求值都匹配？ ✅"}
    ACTION -->|"否"| ACTION_REC
    ACTION_REC --> BUDGET_A{"仍有 step 预算？ ⏳"}
    BUDGET_A -->|"是"| M1
    BUDGET_A -->|"否"| MANUAL["needs_manual<br/>说明达到上限或需人工决定 ⏳"]

    ACTION -->|"是"| RISK{"动作是否高风险？"}
    RISK -->|"当前两个只读生产工具：否 ✅"| TOOL1["真实工具尝试 1<br/>每次尝试独立占 step / 计时 / 记日志 ✅"]
    RISK -->|"未来危险动作 / eval fake：是"| CONFIRM{"展示工具名、参数、影响<br/>本次明确确认？ ⏳"}
    CONFIRM -->|"拒绝 / 未确认"| MANUAL
    CONFIRM -->|"确认；参数未变化"| TOOL1

    TOOL1 --> RESULT1{"工具尝试 1 的结果"}
    RESULT1 -->|"ok=False 且 retryable=False"| TOOL_FAIL["tool_failure<br/>不做无意义同参数重试 ⏳"]
    RESULT1 -->|"ok=False 且 retryable=True"| RETRY_OK{"重试次数与总 step<br/>都还有预算？ ⏳"}
    RETRY_OK -->|"否"| MANUAL
    RETRY_OK -->|"是"| TOOL2["真实工具尝试 2<br/>同一参数；独立占下一 step / 记新日志 ⏳"]
    TOOL2 --> RESULT2{"第二次结果 ⏳"}
    RESULT2 -->|"仍失败"| MANUAL
    RESULT2 -->|"成功"| EVIDENCE
    RESULT1 -->|"ok=True"| EVIDENCE{"取得足够真实证据？"}
    EVIDENCE -->|"零结果 / 不足以支持摘要"| INSUFFICIENT["insufficient_evidence<br/>不得用模型常识补齐 ⏳"]
    EVIDENCE -->|"是"| OBS["Observation<br/>保存真实 content / results 与 allowed_sources ✅"]

    OBS --> M2["模型生成候选摘要<br/>无重试正常链为 step 3 ✅"]
    M2 --> CANDIDATE{"第二模型响应：finish_reason=stop<br/>无 tool_calls、正文非空？ ✅"}
    CANDIDATE -->|"是"| REFLECT["Reflection：按真实证据与输出合同评审<br/>无重试正常链为 step 4 ✅"]
    CANDIDATE -->|"否"| CAND_REC
    REFLECT --> REF_OK{"Reflection 响应：finish_reason=stop<br/>无 tool_calls、反馈非空？ ✅"}
    REF_OK -->|"是"| REFINE["Refinement：JSON Output<br/>无重试正常链为 step 5 ✅"]
    REF_OK -->|"否"| CAND_REC
    REFINE --> REFINE_OK{"Refinement 响应：finish_reason=stop<br/>无 tool_calls、正文非空？ ✅"}
    REFINE_OK -->|"是"| PARSE["json.loads：只解析 JSON 语法 ✅"]
    REFINE_OK -->|"否"| CAND_REC
    PARSE --> JSON_OK{"JSON 语法可解析？ ✅"}
    JSON_OK -->|"否"| CAND_REC
    JSON_OK -->|"是"| VALID{"最终 validator<br/>精确三键、类型、状态、非空、来源子集 ✅"}
    VALID -->|"合法且证据充分"| SUCCESS["success<br/>summary + 本轮真实 sources ✅"]
    VALID -->|"候选不合法但仍可修订"| CAND_REC["仅依据本轮证据修订候选 ⏳"]
    CAND_REC --> BUDGET_C{"仍有 step 预算？ ⏳"}
    BUDGET_C -->|"是"| CAND_FIX["重新调用失败的候选 / Reflection / Refinement 阶段<br/>新调用独立占 step / 计时 / 记日志 ⏳"]
    BUDGET_C -->|"否"| MANUAL
    CAND_FIX -.回到对应阶段的后置守门.-> CANDIDATE

    GUARD["全局护栏<br/>每次真实模型/工具调用前 reserve_call_step<br/>MAX_STEPS=6；禁止第 7 次调用 ✅"] -.约束.-> M1
    GUARD -.约束.-> TOOL1
    GUARD -.约束.-> TOOL2
    GUARD -.约束.-> M2
    GUARD -.约束.-> REFLECT
    GUARD -.约束.-> REFINE

    INVALID --> OUT["所有最终结果都恰好：status / summary / sources"]
    TOOL_FAIL --> OUT
    INSUFFICIENT --> OUT
    MANUAL --> OUT
    SUCCESS --> OUT

    classDef done fill:#d9ead3,stroke:#38761d,color:#1f1f1f;
    classDef pending fill:#fff2cc,stroke:#bf9000,color:#1f1f1f;
    classDef terminalDone fill:#d9eaf7,stroke:#0b5394,color:#1f1f1f;
    classDef terminalPending fill:#fce5cd,stroke:#cc4125,color:#1f1f1f;
    classDef note fill:#f3f3f3,stroke:#666666,color:#1f1f1f;
    class PRE,INIT,M1,F1,ACTION,TOOL1,OBS,M2,CANDIDATE,REFLECT,REF_OK,REFINE,REFINE_OK,PARSE,JSON_OK,VALID done;
    class ACTION_REC,BUDGET_A,RISK,CONFIRM,RESULT1,RETRY_OK,TOOL2,RESULT2,EVIDENCE,CAND_REC,BUDGET_C,CAND_FIX pending;
    class INVALID,SUCCESS terminalDone;
    class TOOL_FAIL,INSUFFICIENT,MANUAL terminalPending;
    class START,GUARD,OUT note;
```

> [!warning] 当前代码与目标图的差异
> 当前已验证的是无重试正常链、调用日志、请求隔离、协议守门和 MAX 硬门。图中的 action/candidate 恢复、工具第二次尝试、失败状态映射与 HITL 仍为 `⏳`；在这些切片完成前，部分异常仍会以内部 `RuntimeError` 停止，不能宣称已经统一返回五种业务状态。

正常无重试路径只使用 step 1～5，不伪造 step 6。一次工具重试成功路径的目标是正好使用 step 1～6：模型选择 → 工具失败 → 工具重试成功 → 候选模型 → Reflection → Refinement。任何第 7 次模型或工具调用都必须在计时与副作用之前拒绝。

未注入客户端时只创建一个 client；四次模型请求共用这个对象。每次公开请求只创建一个 `run_context`，其中保存非空 `request_id`、共享 `step` 和独立 `logs` 列表；内部账本不会进入最终三字段业务结果。

## A4-Gate 实现步骤

| 阶段 | 当前状态 | 可观察结果 |
|---|---|---|
| Problem Contract | 已固定，整关前仍为 DRAFT | 输入、输出、工具、停止、日志、HITL 与 eval 边界明确 |
| C1 输入与三字段结果 | PASS | 非法请求零副作用；成功/失败结果都只用冻结字段 |
| C2 工具适配器 | PASS | `read_material` / `search_web` 的正常、失败与安全边界闭合 |
| C3 Schema、调度、生成/反思/改进/校验 | PASS | topic/path 四模型 + 一工具正常链及来源子集硬门闭合 |
| C4a-1 共享 context、日志、MAX、协议守门 | 已收口 | 无重试正常链 step 1～5、七字段日志、请求隔离与第 7 次调用硬门通过 |
| C4a-2 retry 与失败状态映射 | 下一 Session | 首先完成一次同参数工具 retry 成功的六步轨迹 |
| 动作/候选校验恢复 | 未开始 | 未知动作或候选失败时受控修正/停止 |
| HITL allow/deny | 未开始 | 危险 fake 在确认门前零执行 |
| 14 条 eval | 未开始 | 固定 normal/failure/danger/holdout 案例与阈值 |
| A4-Gate 正式复核 | 未开始 | 只有整关复核通过才可把父任务改为 PASS |

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
| C4a-1a～1d | 已收口 | 每请求独立 context、统一占步、固定七字段日志 helper 与 `MAX_STEPS=6` 硬门 |
| C4a-1e～1i | 已收口 | 四次模型与一次工具的真实调用点全部接入同一本调用账本 |
| C4a-1j | 已收口 | 首次响应只接受精确 `finish_reason == "tool_calls"` 后才读取/执行工具 |
| C4a-1k | 已收口 | topic/path 五步链、双请求隔离与第 7 次调用零副作用拒绝通过 |

## 2026-08-12～13 C4a-1 决定性证据

- S6 独立协议矩阵 `102/102`；S7 主审 115 条断言、独立矩阵 `46/46`，独立 S6/S7/静态合计 `150/150`。
- topic 与 relative_path 两路日志步号均严格为 `[1, 2, 3, 4, 5]`，事件为 `model_call → tool_call → model_call → model_call → model_call`；每条事件恰好固定七字段，同一请求共享一个 request ID。
- 两次公开入口调用的 context、logs 列表与 request ID 彼此独立，各自从 step 1 开始；最终公开结果仍精确为 `status / summary / sources`。
- context 初始 step 2 时，前四次真实调用占 3～6；Refinement 的第 7 次尝试在计时、模型调用与日志追加之前拒绝，既有日志保持不变。
- 首次模型缺少结束原因或其值不是精确 `"tool_calls"` 时，只保留 step 1 的 API 成功日志，message 读取、工具和全部下游调用均为 0。
- 本轮没有重跑真实 DeepSeek；决定性 C4a-1 证据来自无网络内存 fake/spy。2026-08-11 的两条真实正常链证据继续有效，但不能冒充本轮重跑。

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
6. 调用前顺序必须是 `reserve → clock → 真实调用`；硬门晚于计时或副作用，就无法证明第 7 次调用为零副作用。
7. `try` 只包真实模型/工具调用；成功日志放 `else`，异常日志记录 `type(exc).__name__` 后裸抛。`finally return` 会覆盖原异常，原异常对象也不能直接写入只接受安全字符串的日志合同。
8. 首次模型工具选择的结束原因是精确协议字面值 `"tool_calls"`。应采用一个 allow 条件统一拒绝其他值，不能把单数 `"tool_call"` 或互斥的 `"stop"` 分支混进正常路径。

## 安全边界

- `allowed_sources` 只能从本轮真实 Observation 派生；最终 `sources` 必须是它的非空子集。
- Prompt 中的来源名单是软约束，客户端 validator 才是硬门。
- 来源身份属于 allowlist 只能证明“引用来自本轮工具结果”，不能单独证明摘要中的每个事实都被正文支持；语义真实性仍需固定 eval 与人工抽查。
- 非法输入会在 client、模型和工具之前返回；Reflection 与 Refinement 均不暴露工具。

## 尚未完成与下一切片

父任务仍缺：

- `C4a-2`：一次同参数工具 retry；不可重试、二次失败、无预算与空证据的冻结状态映射。
- 未知动作 / 坏参数与候选验证失败的受控修正或安全停止。
- HITL：高风险 fake 工具的 allow/deny 可执行证据。
- `eval_cases.json`：14 条固定案例、至少 3 条 holdout 和正式 Gate 阈值。
- 正式 Gate 复核；在此之前不新建 A4-Gate PASS 复盘，也不升级岗位证据。

下一 Session 从 `A4-Gate-C4a-2a` 开始：只证明“可重试工具首次失败 → 使用同一参数最多重试一次并成功”，使两次真实工具尝试分别占步、计时和写日志，形成正好六步的成功恢复轨迹。

## 相关链接

- [[../../../02-Concepts/Agent/反思机制(Reflection)|反思机制]]
- [[../../../02-Concepts/LLM/结构化输出(Structured Output)|结构化输出]]
- [[../../../02-Concepts/LLM/函数调用(Function Calling)|函数调用 / Tool Calling]]
- [[../../../03-Courses/Agent/AI-Agent-Learning/stage4-agent-basics|阶段 4：Agent 基础原理]]
- [[../../../raw/conversations/2026-08-13-ai-agent-learning-a4-gate-c4a-1-session-handoff|C4a-1 会话接力摘要]]
