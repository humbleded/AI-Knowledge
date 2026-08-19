---
type: concept
topic: Agent Bounded Retry and Human Handoff
status: usable
created: 2026-08-18
updated: 2026-08-19
source:
  - C:\Users\26823\Desktop\AI-Agent-Learning\code\stage4\problem-contract.md
  - C:\Users\26823\Desktop\AI-Agent-Learning\code\stage4\a4_gate_research_summary_agent.py
  - C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-08-17.md
  - C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-08-18.md
  - C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-08-19.md
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
---

# 受控重试与人工接管（Bounded Retry and Human Handoff）

## 一句话

受控重试（bounded retry）是：客户端只对**明确可恢复**的失败，在调用预算内追加有限次数的真实尝试；当精确的恢复机会已经耗尽时，Agent 停止自治，把事实和证据缺口整理成人工接管结果，而不是无限重试、伪造成功或吞掉其他程序错误。

> [!important] 本卡的边界
> 本卡总结的是“自动恢复耗尽后停止并交接”。它不等于完整的 HITL（Human-in-the-Loop）确认门：危险动作执行前的 allow / deny 仍是另一条控制流。

> [!note] 当前项目证据边界
> `A4-Gate-C4a-2a / C4a-2b1 / C4a-2b2 / C4b-1` 的教学、实现与决定性验证已经闭合，但父任务 `A4-Gate` 仍为 `DOING`。尚未完成的是候选摘要、Reflection 与最终 validator 失败恢复、危险动作 HITL、14 条 eval、Gate 五个必答题和整关正式复核。

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

这两个合同服务于不同层。如果把普通成功和人工接管塞进一个没有判别标签的 `dict`，调用方无法安全区分“继续进入 Reflection”还是“立即结束”。当前实现按失败职责使用三个窄内部异常：

- `AutoRecoveryExhaustedError`：全局 step 硬上限或一次工具重试额度耗尽；
- `ActionCorrectionBudgetError`：Action correction 局部额度耗尽，或剩余 step 不足以完成修正后的可信结果链；
- `ToolRetryCompletionBudgetError`：第一次真实工具可重试失败后，剩余 step 不足以容纳“第二次工具 + 完整下游链”。

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
3. 最后一个已经安全化的校验或工具错误是什么；
4. 为什么当前证据不足以继续生成可信结论；
5. Agent 已停止自治，并把下一步交给人工决定。

没有真实可引用证据时必须使用 `sources=[]`。安全化的 `last_error` 可以被整理进说明，但 raw arguments、原始请求值、prompt/messages、日志、request ID、密钥、异常整串和内部运行上下文不得泄漏，也不应扩展为新的公开字段。

## 四条决定性端到端轨迹

这里用 `M` 表示一次真实模型调用，用 `T` 表示一次真实工具后端调用：

| 场景 | 轨迹 | 真实工具次数 | 最终行为 |
|---|---|---:|---|
| 非法 Action → 修正合法 → 工具与下游成功 | `M,M,T,M,M,M`，step/log `6/6` | 1 | 严格三字段 `success` |
| 非法 Action → 修正仍非法 | `M,M`，step/log `2/2` | 0 | `needs_manual`；Action 修正局部上限；无第三次模型 |
| 初始合法 → 首次工具可重试失败 → 第二次成功 | `M,T,T,M,M,M`，step/log `6/6` | 2 | 严格三字段 `success`；只把第二次成功结果写入真实 Tool Observation |
| 修正合法 → 首次真实工具可重试失败 | `M,M,T`，step/log `3/3` | 1 | `needs_manual`；完整链预算不足；第二次工具零副作用 |

第一次失败仍应进入内部调用账本，但不能作为成功的 Tool Observation 写入模型消息历史。失败证据“可审计”不等于失败结果“可作为下一模型的正常工具内容”。

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
- [ ] 不同请求的 step、request ID 和日志相互隔离。

## 来源与证据

- [A4-Gate Problem Contract](file:///C:/Users/26823/Desktop/AI-Agent-Learning/code/stage4/problem-contract.md)
- [A4-Gate 当前实现](file:///C:/Users/26823/Desktop/AI-Agent-Learning/code/stage4/a4_gate_research_summary_agent.py)
- [2026-08-17：同参数重试成功与 C4a-2b1 启动](file:///C:/Users/26823/Desktop/AI-Agent-Learning/daily/2026-08-17.md)
- [2026-08-18：专用信号、窄映射、15/15 与用户审核](file:///C:/Users/26823/Desktop/AI-Agent-Learning/daily/2026-08-18.md)
- [2026-08-19：Action correction、完整链预算、公开映射与用户审核](file:///C:/Users/26823/Desktop/AI-Agent-Learning/daily/2026-08-19.md)
- [实现提交 `1434adc`](https://github.com/humbleded/AI-Agent-Learning/commit/1434adcdd6af3ab14c55dff547c08baea9059340)
- [C4a-2b2 / C4b-1 实现提交 `da7751f`](https://github.com/humbleded/AI-Agent-Learning/commit/da7751f2525c5de3a2ecb7a9da9d94bed7d7f7d3)

## 相关链接

- [[智能体(Agent)|智能体]]
- [[工具调用与动作(Tool Calling and Action)|工具调用与动作]]
- [[工具定义与执行协议(Tool Definition)|工具定义与执行协议]]
- [[外部 API 工具(External API Tool)|外部 API 工具]]
- [[ReAct推理与行动循环(ReAct)|ReAct 推理与行动循环]]
- [[反思机制(Reflection)|反思机制]]
- [[../LLM/结构化输出(Structured Output)|结构化输出]]
- [[../../04-Projects/Agent/AI-Agent-Learning/a4-gate-research-summary-agent|A4-Gate 研究摘要 Agent]]
