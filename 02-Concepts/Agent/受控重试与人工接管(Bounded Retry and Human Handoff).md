---
type: concept
topic: Agent Bounded Retry and Human Handoff
status: usable
created: 2026-08-18
updated: 2026-08-20
source:
  - C:\Users\26823\Desktop\AI-Agent-Learning\code\stage4\problem-contract.md
  - C:\Users\26823\Desktop\AI-Agent-Learning\code\stage4\a4_gate_research_summary_agent.py
  - C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-08-17.md
  - C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-08-18.md
  - C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-08-19.md
  - C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-08-20.md
tags:
  - AI/Agent
  - Reliability
  - Retry
  - Human-Handoff
  - AI-Agent-Learning
aliases:
  - Bounded Retry
  - Auto Recovery Exhaustion
  - Human Handoff
  - Agent 受控重试
  - 有界重试
  - 自动恢复耗尽
  - 人工接管
  - needs_manual
  - Completion Budget
  - 完整链预算
  - Action Correction
  - 动作修正
  - Candidate Recovery
  - 候选摘要恢复
  - Reflection Recovery
  - Reflection 反馈恢复
  - 反思反馈恢复
  - 人工接管证据池
---

# 受控重试与人工接管（Bounded Retry and Human Handoff）

## 一句话

受控重试（bounded retry）是：客户端只对**明确可恢复**的失败，在调用预算内追加有限次数的真实尝试；当精确的恢复机会已经耗尽时，Agent 停止自治，把事实和证据缺口整理成人工接管结果，而不是无限重试、伪造成功或吞掉其他程序错误。

> [!important] 本卡的边界
> 本卡总结的是“自动恢复耗尽后停止并交接”。它不等于完整的 HITL（Human-in-the-Loop）确认门：危险动作执行前的 allow / deny 仍是另一条控制流。

> [!note] 当前项目证据边界
> `A4-Gate-C4a-2a / C4a-2b1 / C4a-2b2 / C4b-1 / C4b-2a / C4b-2b-1` 的教学、实现、决定性验证和用户审核已经闭合，但父任务 `A4-Gate` 仍为 `DOING`。C4b-2b-1 只关闭“Reflection 模型 API 已返回、反馈响应协议或正文不可用”的受控恢复；Candidate / Reflection Provider/API 异常、Refinement / 最终 validator 失败恢复、危险动作 HITL、14 条 eval、Gate 五个必答题和整关正式复核尚未完成。

## 新手比喻：一次派送、调度员与客服出口

可以把三层职责想成快递系统：

- **一次工具执行**像一名快递员的一次派送：只记录这一次是否成功、用了多久、发生了什么错误。
- **重试编排层**像调度员：它看到前一次结果、剩余机会和整张派送单，因此能决定是否按同一地址再派一次。
- **公开入口**像客服出口：当调度员确认自动处理已经耗尽时，客服才把内部事实整理成用户能理解的“需要人工处理”说明。

快递员不知道此前已经失败几次，也不拥有面向客户的最终回复合同，所以不能由“一次派送函数”直接决定整个订单是否进入人工接管。

## 三层职责必须分开

| 层 | 知道什么 | 应负责什么 | 不应负责什么 |
|---|---|---|---|
| 原子工具入口 | 本次参数、本次 step、本次真实调用与本次日志 | 参数校验、占 step、调用、计时、记录本次结果 | 查看完整重试历史、决定整个请求的最终业务状态 |
| 重试编排层 | 工具名、原始参数、前后两次结果、共享运行上下文与预算 | 只在精确条件下追加一次真实重试；识别恢复是否耗尽 | 返回面向用户的最终三字段对象 |
| 公开入口 | 对外结果合同 | 只把专用耗尽信号映射为稳定的人工接管结果 | 宽泛捕获所有运行时错误并伪装成重试耗尽 |

```text
一次原子工具尝试
  -> 重试编排层检查：失败类型 + 重试次数 + 总 step
       |-> 仍有机会：再做一次真实原子尝试
       |-> 精确耗尽：发出窄内部信号
       `-> 其他错误：保持原来的错误分类
              |
               `-> 公开入口只映射窄信号为 needs_manual
```

## 三层预算：硬保险丝、局部额度与完整链预算

生产里的预算不是一个数字解决所有问题，而是三层各管一件事：

| 预算层 | A4-Gate 中的例子 | 作用 |
|---|---|---|
| 全局硬上限 | `MAX_STEPS = 6` | 防止整个 Agent 循环失控，是最后一道硬保险丝 |
| 局部恢复额度 | `MAX_ACTION_CORRECTIONS = 1`、`MAX_TOOL_RETRIES = 1` | 限制某一类失败最多自动修正或重试几次 |
| 完整链预算（completion budget） | 发起修正或重试前检查剩余 step | 只有剩余预算足以走到可信终态时，才开始下一次恢复动作 |

`MAX_STEPS` 是“绝对不能越过”的上限，不是“必须把它烧完”的目标。已经能证明剩余 step 不足以完成工具调用、候选摘要、Reflection 和 Refinement 时，继续发模型或工具请求只会增加费用、延迟和副作用风险，不会产生完整成功结果。

当前链条冻结为：

```text
Action correction 前：
  1 次 correction 模型 + 1 次真实工具 + Candidate + Reflection + Refinement
  = 至少还需要 5 个调用位置

第一次真实工具出现 retryable failure 后：
  1 次 retry 工具 + Candidate + Reflection + Refinement
  = 至少还需要 4 个调用位置

Candidate 响应不可用且属于恢复白名单时：
  1 次 Candidate recovery + Reflection + Refinement
  = 至少还需要 3 个调用位置

Reflection 反馈响应不可用且属于恢复白名单时：
  1 次 Reflection recovery + Refinement
  = 至少还需要 2 个调用位置
```

因此，step 1 的非法 Action 可以使用一次 correction，因为还剩 5 步；若 correction 后的首次真实工具在 step 3 返回可重试失败，剩余只有 3 步，已不足以容纳“再试工具 + 三段下游模型”，必须在第二次工具副作用前停止。

## Action correction 的账本与消息接力

Action correction 只处理**模型已经给出一个可关联的 Tool Action，但 Action 内容未通过客户端预执行校验**的情况，例如未知工具、坏 JSON、Schema 缺字段或多字段、字段类型错误、工具路由错误，以及参数值偏离规范化请求。

它的账本边界是：

- 产生非法 Action 的模型调用照常占一个 model step，并写一条 model log；
- 客户端的预执行拒绝不调用真实后端，因此不占 tool step、不写 tool log、没有工具副作用；
- 请求一次修正本身是新的真实模型调用，必须再占一个 model step/log；
- 只有修正后的 Action 通过校验并真正执行时，才产生 tool step/log。

消息历史必须保持协议级配对：

```text
system
user（规范化请求）
assistant（原始完整 invalid tool_call）
tool（同一 tool_call_id 的安全 validation Observation）
assistant（修正后的完整 tool_call）
tool（同一修正后 ID 的真实工具 Observation）
```

`tool_call_id` 只能用 `.strip()` 判断是否全空白，回填时必须逐字符保留原 ID，不能自行规范化。安全 validation Observation 只说明错误类别、需要修正的字段和返回一个合法调用的要求；不得回显 raw arguments、原始 request、完整 prompt/messages、request ID、日志或密钥。

同形的 `{ok: false, retryable: false, error: ...}` 不能仅凭三个字段判断来源。调用前后 step/log 都没有变化，才可证明它是预执行拒绝；若 step/log 精确增加 `+1/+1`，才证明真实工具已经执行并可进入工具终点分类。

## 为什么必须使用窄信号

在 A4-Gate 中，正常的 `generate_candidate_summary()` 返回内部接力数据：

```text
candidate_summary / tool_name / tool_result
```

公开的 `run_research_summary_once()` 才返回：

```text
status / summary / sources
```

这两个合同服务于不同层。如果把普通成功和人工接管塞进一个没有判别标签的 `dict`，调用方无法安全区分“继续进入下一阶段”还是“立即结束”。当前实现按失败职责使用一组窄内部异常：

- `AutoRecoveryExhaustedError`：全局 step 硬上限或一次工具重试额度耗尽；
- `ActionCorrectionBudgetError`：Action correction 局部额度耗尽，或剩余 step 不足以完成修正后的可信结果链；
- `ToolRetryCompletionBudgetError`：第一次真实工具可重试失败后，剩余 step 不足以容纳“第二次工具 + 完整下游链”。
- `CandidateRecoveryCompletionBudgetError`：Candidate 属于可恢复分类，但剩余 step 不足以容纳“Candidate recovery + Reflection + Refinement”。
- `CandidateSummaryStageStopError`：Candidate 阶段已经按 `terminal_response / recovery_exhausted / insufficient_completion_steps` 安全停止，并携带公开入口所需的安全原因、恢复次数、当前 step 与真实来源白名单。
- `ReflectionRecoveryCompletionBudgetError`：Reflection 反馈属于可恢复分类，但剩余 step 不足以同时容纳“Reflection recovery + Refinement”。
- `ReflectionFeedbackStageStopError`：Reflection 反馈阶段已经按 `terminal_response / recovery_exhausted / insufficient_completion_steps` 安全停止，只携带公开入口所需的阶段事实，不携带失败反馈正文。

它们只携带构造安全交接说明所需的受控事实，例如精确 `reason`、当前 step、实际尝试/修正次数和已经安全化的最后错误。公开入口必须同时按**精确异常类型**和**精确 reason** fail-closed 地分流；未知 reason、异常子类、普通 `RuntimeError` / `ValueError`、模型 API 异常、工具 Python 异常和协议结构错误继续按原路径传播，不能被一把兜成“达到重试上限”。

> [!warning] 不要按异常文案做字符串匹配
> 应使用独立类型或明确 tagged outcome。依赖 `"retry exhausted" in str(exc)` 之类的文本匹配，会把文案变化和控制流绑在一起，也容易误识别无关异常。

## A4-Gate 的恢复停止终点

本项目冻结 `MAX_STEPS = 6`、`MAX_ACTION_CORRECTIONS = 1`、`MAX_TOOL_RETRIES = 1`。这里的“重试上限 1”表示**首次尝试后最多额外重试一次**，所以工具总尝试数最多为 2；“修正上限 1”表示一个非法 Action 最多向模型请求一次修正。

### 1. 第二次工具尝试仍是可重试失败

```text
首次工具失败（ok=False, retryable=True）
  -> 同工具名、同原始参数做第二次真实尝试
  -> 第二次仍是 ok=False, retryable=True
  -> reason=max_tool_retries
  -> attempts=2
  -> last_error=第二次真实错误
```

第二次尝试必须继续通过同一个原子工具入口，让它自己占下一 step、计时和写日志。不能手工 `step += 1`，否则会产生没有真实调用和日志对应的“幽灵 step”。

### 2. 第二次尝试前已经没有剩余 step

```text
首次工具失败（ok=False, retryable=True）
  -> 当前 step 已等于 MAX_STEPS
  -> 不执行第二次工具
  -> reason=max_steps
  -> attempts=1
  -> last_error=第一次真实错误
```

这个分支必须在第二次工具副作用、计时和日志之前停止。它与“第二次已经执行但仍失败”不是同一条轨迹，实际工具次数和账本证据必须不同。

### 3. Action correction 的局部额度已用完

第一次 Action 被客户端预执行拒绝后，可以请求一次 correction。如果修正结果仍然非法，调用方会再次进入同一个 correction helper，并携带 `corrections_used=1`；局部预算门在新模型调用之前发出 `max_action_corrections`，因此不会出现第二次 correction 模型调用或任何真实工具副作用。

### 4. 恢复后无法完成可信结果链

即使局部次数额度尚未用完，剩余 step 不足时也必须提前停止：

- Action correction 前不足 5 步：发出 `insufficient_completion_steps`，不再请求 correction；
- 第一次真实工具可重试失败后不足 4 步：发出工具重试完整链预算停止，不执行第二次工具。

这两个终点表达的是“无法完成可信链”，不是“已经达到工具重试次数上限”。公开说明必须区分这两件事。

## Candidate 响应：先分类，再决定是否恢复

Candidate recovery 处理的不是“模型调用根本没有发生”，而是：**模型 API 已经返回并正常记账，但返回对象不能形成可用的候选摘要**。Provider / HTTP / SDK 抛出的调用异常属于另一类故障，不能被本分支顺手吞成业务状态。

第一步应使用无副作用分类器，把不可信响应压缩成固定三键内部结果：

```text
classification / reason / candidate_summary
```

当前冻结的分类如下：

| 分类 | 安全原因 | 行为 |
|---|---|---|
| `valid` | `None` | `finish_reason=stop`、没有 Tool Action、正文为非空字符串；保留原始正文并继续 Reflection |
| `recoverable` | `invalid_response_shape`、`invalid_candidate_content`、`length`、`unexpected_tool_calls` | 只有完整链预算允许时，依据同一份真实 Tool Observation 恢复一次 |
| `terminal` | `content_filter`、`insufficient_system_resource`、`missing_finish_reason`、`unknown_finish_reason` | 不尝试用内容修订绕过安全过滤、资源故障或未知协议状态，立即安全停止 |

分类必须先检查 `finish_reason` 的 terminal 语义，再读取 `message / tool_calls / content`。否则，一个已经明确标记为安全过滤或资源不足的响应，可能因为正文结构同时损坏而被错误降级成普通格式重试。

DeepSeek Chat Completions 当前官方响应 schema 把 `stop / length / content_filter / tool_calls / insufficient_system_resource` 列为 `finish_reason` 值，并允许 assistant `content` 为 nullable；这是版本敏感的 Provider 协议事实，检查日期为 2026-08-20。项目自己的 `missing_* / unknown_*` 原因码则是客户端 fail-closed 分类，不是 Provider 原生枚举。

### 一次恢复的消息边界

恢复消息从 Candidate 调用前的历史构造：

```text
system
user（规范化请求）
assistant（合法 Tool Action）
tool（本轮真实 Tool Observation）
user（按失败原因生成的证据受限修订指令）
```

这里有三个关键边界：

1. 失败的 Candidate 响应不加入历史，避免截断文本、坏外壳或未配对 Tool Action 污染下一次调用；
2. 原 Tool Observation 按对象 identity 浅复用，不重建、不重新序列化，也不再次执行工具；
3. recovery 调用显式使用 `tool_choice="none"`，只允许根据既有 Observation 从头生成更短或更合规的纯文本摘要。

恢复调用返回后必须再走同一个分类器：第二次结果为 `valid` 才进入 Reflection；第二次为 `terminal` 或仍为 `recoverable` 都立即停止，不能递归、循环或再发第二次 recovery。

### 为什么 step 3 能恢复、step 4 必须停止

正常链的 Candidate 在 step 3 返回失败时，`MAX_STEPS=6` 还剩 step 4～6，刚好容纳：

```text
step 4 Candidate recovery -> step 5 Reflection -> step 6 Refinement
```

如果前面已经发生一次 Action correction 或 tool retry，Candidate 会到 step 4 才返回；此时只剩两个调用位置，少于可信尾链所需的三个。即使局部 recovery 次数尚未使用，也必须在新的模型调用、计时和日志之前返回 `needs_manual`。

## Reflection 反馈响应：只恢复同一评审，不重做整条链

Reflection recovery 处理的是：**Reflection API 已经返回并完成记账，但响应协议或反馈正文不能形成可用反馈**。它不处理网络、HTTP、SDK 或 Provider 在调用期间直接抛出的异常，也不处理后续 Refinement 响应和最终 validator 失败；这些边界继续保持原异常 identity，等待各自切片冻结策略。

Reflection 反馈先进入无副作用的严格三键分类：

```text
classification / reason / feedback
```

| 分类 | 安全原因 | 行为 |
|---|---|---|
| `valid` | `None` | `finish_reason=stop`、无 Tool Action、反馈为非空字符串；清理首尾空白后进入 Refinement |
| `recoverable` | `invalid_response_shape`、`invalid_feedback_content`、`length`、`unexpected_tool_calls` | 只有完整尾链还容纳 recovery 与 Refinement 时，恢复同一次评审一次 |
| `terminal` | `content_filter`、`insufficient_system_resource`、`missing_finish_reason`、`unknown_finish_reason` | 不绕过安全过滤、资源故障或未知协议状态，立即安全停止 |

这些 `recoverable / terminal` 标签是 A4-Gate 客户端基于冻结合同作出的本地策略分类，不是 Provider 对所有模型、版本或场景的通用重试保证。

恢复 prompt 完整保留原 Reflection prompt，所以仍能看到可信的原始请求、真实 Tool Observation、合法 Candidate、`allowed_sources` 和评审要求；但它的函数签名不接收失败响应或失败反馈，因此不可能把截断文本、坏外壳或异常 Tool Action 回填给模型。恢复调用也不重跑工具，只要求重新完成**同一个 Reflection**，输出非空纯文本反馈，而不是 JSON 或最终 `status / summary / sources`。

恢复响应必须再走同一个分类器：只有 `valid` 才进入 Refinement；第二次仍为 `recoverable` 或转为 `terminal` 都停止。整条链最多只有一个 Reflection recovery 调用点，没有循环、递归或“成功后再临时检查 Refinement 预算”。

### 为什么 step 4 能恢复、step 5 必须停止

在无前序恢复的正常链中，首次 Reflection 位于 step 4。它返回可恢复失败后，剩余两个位置恰好组成完整尾链：

```text
step 5 Reflection recovery -> step 6 Refinement
```

如果 Candidate recovery 已占用 step 4，首次 Reflection 会在 step 5 返回失败，此时 `remaining_steps = 6 - 5 = 1`。若贸然恢复，step 6 只能完成 Reflection recovery，Refinement 将需要不存在的 step 7，因此必须在 recovery prompt、模型调用、计时和日志之前停止，并让 step 6 保持未使用。

## 公开人工接管合同

窄信号到达公开入口后，统一返回严格三字段：

```json
{
  "status": "needs_manual",
  "summary": "说明触发阈值、实际尝试次数、最后错误、证据缺口和停止交接",
  "sources": []
}
```

`summary` 至少回答五件事：

1. 达到了哪个具体阈值；
2. 实际发起了几次修正或工具尝试；
3. 最后一个已经安全化的阶段失败原因、校验错误或工具错误是什么；
4. 为什么当前证据不足以继续生成可信结论；
5. Agent 已停止自治，并把下一步交给人工决定。

没有本轮实际取得且通过白名单校验的来源时必须使用 `sources=[]`。安全化的失败原因或 `last_error` 可以被整理进说明，但 raw arguments、原始请求值、prompt/messages、日志、request ID、密钥、异常整串和内部运行上下文不得泄漏，也不应扩展为新的公开字段。

### 同一个 `sources` 字段在成功与失败中的语义

固定三字段 V1 没有单独的 `answer_citations` 与 `retrieved_evidence`，因此客户端必须结合 `status` 解释 `sources`：

- `status=success`：`sources` 表示已通过校验的摘要实际采用的来源；
- 非成功状态：若失败前尚未取得真实来源，使用 `[]`；若 Candidate 或 Reflection 阶段失败前已经取得真实来源，可以保留它们，但它们只表示**供人工接管复核的证据池**。

阶段失败时的 `summary` 必须准确说明停在哪一层：Candidate 阶段失败表示没有 Candidate / 摘要通过校验；Reflection 阶段失败表示已有合法 Candidate，但没有最终摘要完成 Reflection → Refinement → 客户端 validator。两种情况下，非空 `sources` 都不代表存在一份已验证摘要，也不是失败摘要的 citations。未来若允许扩展公开 schema，更清晰的做法是把“回答引用”和“已检索证据”拆成不同字段。

> [!warning] 原始理解 → 当前结论
> 原始偏好是保留这些来源，同时仍把它们理解成“已验证摘要采用的来源”。两句话不能同时成立：既然没有摘要通过 validator，就不存在“已验证摘要采用的引用”。当前合同保留来源值，但把语义订正为“已真实取得、供人工接管复核的证据池”。

```json
{
  "status": "needs_manual",
  "summary": "唯一一次候选恢复仍未得到合法摘要；没有摘要通过校验。sources 仅供人工复核，Agent 已停止自治。",
  "sources": ["sample.txt"]
}
```

来源必须由规范化请求与真实工具结果派生，不能从失败 Candidate、失败 Reflection、自述引用或异常正文中提取。公开入口还应把内部停止信号声明的 step、恢复次数和来源与本轮 `run_context`、阶段起始 step 及重新派生的真实来源逐值、逐顺序对账；最终返回重新派生来源的新副本，而不是再次信任异常对象里的列表。即使异常类型和 reason 都合法，字段语义被篡改时也必须原样上抛。

## 四条决定性端到端轨迹

这里用 `M` 表示一次真实模型调用，用 `T` 表示一次真实工具后端调用：

| 场景 | 轨迹 | 真实工具次数 | 最终行为 |
|---|---|---:|---|
| 非法 Action → 修正合法 → 工具与下游成功 | `M,M,T,M,M,M`，step/log `6/6` | 1 | 严格三字段 `success` |
| 非法 Action → 修正仍非法 | `M,M`，step/log `2/2` | 0 | `needs_manual`；Action 修正局部上限；无第三次模型 |
| 初始合法 → 首次工具可重试失败 → 第二次成功 | `M,T,T,M,M,M`，step/log `6/6` | 2 | 严格三字段 `success`；只把第二次成功结果写入真实 Tool Observation |
| 修正合法 → 首次真实工具可重试失败 | `M,M,T`，step/log `3/3` | 1 | `needs_manual`；完整链预算不足；第二次工具零副作用 |

第一次失败仍应进入内部调用账本，但不能作为成功的 Tool Observation 写入模型消息历史。失败证据“可审计”不等于失败结果“可作为下一模型的正常工具内容”。

## Candidate recovery 的四条决定性轨迹

| 场景 | 轨迹 | 最终行为 |
|---|---|---|
| Candidate 首次合法 | `M,T,M,M,M`，step/log `5/5` | 不发生 recovery；正常进入 Reflection / Refinement 并返回 `success` |
| step 3 Candidate 可恢复 → recovery 合法 | `M,T,M,M,M,M`，step/log `6/6` | 恢复恰好一次；随后完成 Reflection / Refinement |
| Candidate 首次 terminal | `M,T,M`，step/log `3/3` | recovery 为 0；保留真实来源证据池并返回 `needs_manual` |
| Action correction 或 tool retry 后的 step 4 Candidate 可恢复 | 候选失败已占 step 4 | 完整尾链预算不足；recovery 模型调用、计时和日志均为 0，返回 `needs_manual` |

## Reflection recovery 的四条决定性轨迹

| 场景 | 轨迹 | 最终行为 |
|---|---|---|
| step 4 Reflection 首次合法 | 正常五步链 | recovery 为 0；反馈进入 step 5 Refinement 并返回 `success` |
| step 4 Reflection 可恢复 → recovery 合法 | step 4 失败 → step 5 recovery → step 6 Refinement | 恢复恰好一次；完整可信尾链完成 |
| step 4 Reflection 首次 terminal，或唯一 recovery 后仍失败 | 首次 terminal 停在 step 4；恢复后停止在 step 5 | 不再恢复、不进入 Refinement；保留真实来源证据池并返回 `needs_manual` |
| Candidate recovery 后的 step 5 Reflection 可恢复 | Reflection 失败已占 step 5 | 只剩 1 步而完整尾链需要 2 步；recovery 和 Refinement 均为 0，step 6 保持未使用 |

### 用 spy 证明消息历史没有被失败结果污染

只断言“最终没有崩溃”不够，因为非法的 Python `None` 或第一次失败字典可能已经进入 `messages`，只是尚未在当前路径触发异常。测试应捕获**下一次模型调用实际收到的消息列表**，再检查 Tool Message：

```python
tool_messages = [
    message
    for message in captured_messages
    if isinstance(message, dict) and message.get("role") == "tool"
]

assert all(
    isinstance(message.get("content"), str)
    for message in tool_messages
)

expected_content = json.dumps(second_success, ensure_ascii=False)
assert [message["content"] for message in tool_messages] == [expected_content]
```

第一条断言守住 Tool Message 的字符串合同，能拒绝缺失字段或 Python `None`；第二条断言进一步证明历史中恰好只有第二次成功结果，没有把第一次失败 Observation、错误文案或内部 retry 状态交给下游模型。Python `None` 与字符串 `"None"` 不同：前者属于 `NoneType` 且不能调用 `.strip()`，后者虽然是字符串，但也不能仅凭类型就把它当成有效证据。

## 不要扩大映射范围

专用人工接管信号只代表已经验证的恢复停止条件，不能顺便接管所有失败：

- 只有调用前后的 `run_context` 与七字段账本能够证明**真实工具已经执行**时，执行后返回的 `ok=False, retryable=False` 才属于已经闭合的 C4a-2b2 `tool_failure`；
- 未注册工具、坏 JSON、Schema、工具路由或参数值漂移等执行前拒绝也可能返回同形的 `ok=False, retryable=False`，但真实工具调用次数为 0，应进入已经闭合的 C4b-1 Action correction，不能只看两个布尔字段就误映射为 `tool_failure`；
- 工具调用成功但结果为空属于 `insufficient_evidence`，不是工具失败；
- `choices` / `finish_reason` / tool_calls 数量、缺失 ID 等**模型响应协议结构错误**无法构造可靠的配对 Observation，仍由窄协议异常原样传播，不属于 Action correction；
- 模型 API 异常、真实 Python 异常、未知预算 reason 和异常子类也继续按原类型传播；
- 将来新增第三种耗尽原因时，应显式增加分支，不能让 `else` 默认冒充已有原因。

这些分支是否最终返回业务状态，要由各自冻结的 Problem Contract 和验收证据决定。

## 迁移到其他系统前还要检查什么

“同参数重试”并不天然安全。迁移到写操作、支付、发消息或部署动作前，至少检查：

- 工具是否只读或具备幂等性（idempotency）；
- 是否使用 idempotency key、防重表或去重标识；
- 第一次超时是否可能实际已经成功，只是响应丢失；
- 重试是否会重复扣款、重复发送或重复修改状态；
- 高风险动作是否需要执行前人工确认，而不是失败后才交接。

A4-Gate 当前重试的是受控只读工具，这个证据不能直接外推为所有副作用工具都可以原参数重试。

## 常见错误

| 错误做法 | 为什么错 | 正确边界 |
|---|---|---|
| 在重试前手工增加 step | 原子入口还会再次占 step，产生步号缺口或提前撞上限 | 每次真实调用只由原子入口占一步 |
| 调用第二次工具但丢弃返回值 | 无法区分第二次成功、可重试失败和不可重试失败 | 保存第二次真实结果，再按精确字段分流 |
| 第二次调用后无条件进入人工接管 | 会把恢复成功也误报为耗尽 | 仅对第二次精确 `ok is False and retryable is True` 发信号 |
| 用当前 step 数字充当 reason | 计数不是稳定的业务原因 | 使用 `max_steps` / `max_tool_retries` 等明确内部原因码 |
| 捕获所有 `RuntimeError` | 协议错误和程序错误会被错误分类 | 只捕获专用窄信号 |
| 把内部异常字段直接公开为嵌套字典 | 破坏公开 `summary: str` 合同并泄漏实现细节 | 将事实整理成用户可读说明，再经统一 result builder 返回 |
| 把失败工具结果写入成功 Observation | 会用错误或 `None` 污染消息历史 | 失败留在账本；只有有效成功结果进入 Tool Message |
| 把 `MAX_STEPS` 当成必须耗尽的额度 | 会发起明知无法完成尾链的调用，徒增成本与副作用风险 | 每次恢复前同时检查局部额度和完整链预算 |
| 修正 `tool_call_id` 时顺手 `.strip()` | Tool Observation 无法与原 assistant tool call 精确关联 | 只用 strip 判空，回填时保留原始 ID |
| 用工具结果再次调用 Action response parser | parser 负责模型响应外壳，工具结果属于另一数据层 | correction response 只解析一次；工具结果交给终点分类 |
| corrected Action 再错时直接返回成功形状 | 绕过局部修正上限，可能让无证据状态继续下游 | 再进同一预算门，在新模型调用前窄停止 |
| 把失败 Candidate 加入 recovery 历史 | 截断内容、坏外壳或未配对 Tool Action 可能继续污染模型 | 从既有真实 Tool Observation 末尾追加新的修订指令 |
| Candidate 只要失败就原样重试 | 会错误重试安全过滤、资源不足或未知协议漂移 | 先做 `valid / recoverable / terminal` 纯分类，再同时检查完整链预算 |
| 唯一 recovery 仍失败后继续循环 | 局部次数失控，并挤占 Reflection / Refinement 的可信尾链 | 第二次分类非 `valid` 就停止并交还人工 |
| 把 `needs_manual.sources` 写成已验证摘要引用 | 没有摘要通过 validator，引用对象并不存在 | 明确它只是实际取得的人工接管证据池，失败说明写清证据缺口 |
| 把失败 Reflection 正文拼入 recovery prompt | 截断文本、坏外壳或越权 Tool Action 会继续污染同一评审 | recovery helper 不接收失败响应，只复用原可信 Reflection prompt |
| step 5 先恢复一次，再看能否 Refinement | recovery 会占 step 6，最终稿需要不存在的 step 7 | 发起 recovery 前一次性为 recovery + Refinement 预留 2 步 |
| 已有合法 Candidate 就宣称成功 | Candidate 尚未完成 Reflection、Refinement 与最终 validator | 公开说明准确标记缺失的下游阶段，并进入人工接管 |
| 只看异常类型，直接相信其中的 step / attempts / sources | 合法类型的信号仍可能携带伪造语义 | 与当前账本、阶段起点和重新派生的真实来源对账；不一致就上抛 |

## 验证清单

- [ ] 每次真实模型或工具调用都由统一入口占 step、计时和写日志。
- [ ] 第一次和第二次工具尝试使用相同工具名、原始参数、规范化请求与同一本运行上下文。
- [ ] 首败后成功能继续完成完整下游链，没有被人工接管分支截断。
- [ ] 二次失败恰好两次工具调用，没有第三次调用。
- [ ] 无剩余 step 时没有第二次工具副作用、计时或日志。
- [ ] 公开结果严格只有 `status / summary / sources`。
- [ ] 普通运行时错误、协议错误和不可重试失败没有被窄映射误吞。
- [ ] 在把 `retryable=False` 映射为 `tool_failure` 前，账本能够证明真实工具已经执行；执行前同形拒绝仍走动作校验 / 修正。
- [ ] Action correction 的消息顺序为原 invalid assistant → 同 ID 安全 Tool Observation；ID 原样保留。
- [ ] Action correction 与工具 retry 都在新调用前检查局部额度和完整链预算。
- [ ] 修正后首次工具若在 step 3 可重试失败，不会执行第二次工具，也不会把“完整链不足”误写成“重试次数耗尽”。
- [ ] 公开入口按精确异常类型和精确 reason 分支；未知 reason、异常子类、API/协议错误仍原样传播。
- [ ] `needs_manual` 仍严格只有 `status / summary / sources`，且无真实证据时 `sources=[]`。
- [ ] Candidate 响应先按固定三键分类；terminal reason 不会被正文结构错误降级成 recoverable。
- [ ] Candidate recovery 只从既有真实 Tool Observation 构造消息，失败 Candidate 不进入历史，工具不会重跑。
- [ ] step 3 恰好允许一次 recovery + Reflection + Refinement；step 4 在 recovery 调用前因完整链不足停止。
- [ ] 唯一 recovery 的第二次分类无论 terminal 还是 recoverable 都不会触发第二次 recovery。
- [ ] Candidate 失败时，非空 `sources` 只来自真实白名单来源，公开说明明确其为人工接管证据池而非已验证摘要引用。
- [ ] Reflection 反馈先按固定三键分类；terminal reason 优先，Provider / SDK 异常不被本分支吞掉。
- [ ] step 4 Reflection 可恢复时轨迹精确为 step 5 recovery → step 6 Refinement；step 5 失败时在 recovery 前停止且不消耗 step 6。
- [ ] 唯一 Reflection recovery 后的 terminal / recoverable 都不会再次恢复或进入 Refinement；Refinement / validator 失败仍按原异常边界传播。
- [ ] Reflection `needs_manual` 明确“已有合法 Candidate，但没有最终结果通过 Reflection → Refinement → validator”；来源仍只是人工证据池。
- [ ] 公开入口重新核对 Reflection 信号的 step、恢复次数与真实来源；伪造字段和异常子类都保持原样传播。
- [ ] 不同请求的 step、request ID 和日志相互隔离。

## 来源与证据

- [A4-Gate Problem Contract](file:///C:/Users/26823/Desktop/AI-Agent-Learning/code/stage4/problem-contract.md)
- [A4-Gate 当前实现](file:///C:/Users/26823/Desktop/AI-Agent-Learning/code/stage4/a4_gate_research_summary_agent.py)
- [2026-08-17：同参数重试成功与 C4a-2b1 启动](file:///C:/Users/26823/Desktop/AI-Agent-Learning/daily/2026-08-17.md)
- [2026-08-18：专用信号、窄映射、15/15 与用户审核](file:///C:/Users/26823/Desktop/AI-Agent-Learning/daily/2026-08-18.md)
- [2026-08-19：Action correction、完整链预算、公开映射与用户审核](file:///C:/Users/26823/Desktop/AI-Agent-Learning/daily/2026-08-19.md)
- [2026-08-20：Candidate / Reflection 响应分类、唯一恢复、公开证据池与用户审核](file:///C:/Users/26823/Desktop/AI-Agent-Learning/daily/2026-08-20.md)
- [DeepSeek Chat Completions API：Responses](https://api-docs.deepseek.com/api/create-chat-completion/#responses)（检查日期：2026-08-20）
- [实现提交 `1434adc`](https://github.com/humbleded/AI-Agent-Learning/commit/1434adcdd6af3ab14c55dff547c08baea9059340)
- [C4a-2b2 / C4b-1 实现提交 `da7751f`](https://github.com/humbleded/AI-Agent-Learning/commit/da7751f2525c5de3a2ecb7a9da9d94bed7d7f7d3)
- [C4b-2a Candidate 响应恢复提交 `c8ad8cf`](https://github.com/humbleded/AI-Agent-Learning/commit/c8ad8cf063340d0ac30d8c0d0b48f6add379c145)
- [C4b-2b-1 Reflection 反馈恢复提交 `e4a5681`](https://github.com/humbleded/AI-Agent-Learning/commit/e4a56813aa6b4e68ffee4ab7b45d5a3a2c1d2a5f)

## 相关链接

- [[智能体(Agent)|智能体]]
- [[工具调用与动作(Tool Calling and Action)|工具调用与动作]]
- [[工具定义与执行协议(Tool Definition)|工具定义与执行协议]]
- [[外部 API 工具(External API Tool)|外部 API 工具]]
- [[ReAct推理与行动循环(ReAct)|ReAct 推理与行动循环]]
- [[反思机制(Reflection)|反思机制]]
- [[../LLM/结构化输出(Structured Output)|结构化输出]]
- [[../../04-Projects/Agent/AI-Agent-Learning/a4-gate-research-summary-agent|A4-Gate 研究摘要 Agent]]
