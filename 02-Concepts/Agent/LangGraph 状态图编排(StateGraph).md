---
type: concept
topic: LangGraph StateGraph
status: usable
created: 2026-09-05
updated: 2026-09-05
source:
  - https://docs.langchain.com/oss/python/langgraph/graph-api
  - https://docs.langchain.com/oss/python/langgraph/streaming
  - https://docs.langchain.com/oss/python/langgraph/persistence
  - C:\Users\26823\Desktop\AI-Agent-Learning\code\stage8\incident_change_review_agent\incident_graph.py
  - C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-08-25.md
  - C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-09-05.md
tags:
  - AI/Agent
  - LangGraph
  - StateGraph
  - Workflow
  - AI-Agent-Learning
---

# LangGraph 状态图编排（StateGraph）

## 一句话

`StateGraph` 像一张写清“现在掌握什么、下一站去哪、何时必须停”的流程地图：`State` 保存当前快照，`Node` 做一步工作并返回局部更新，`Edge` 决定下一步；有限、安全、可枚举的控制规则由代码掌握，LLM 只处理真正需要语言理解和开放推理的部分。

## 什么时候值得用

适合 LangGraph 的任务通常同时具有几项特征：

- 多步处理，共享状态会逐步变化；
- 存在条件分支、回环和多个明确终点；
- 必须限制工具调用、模型调用或业务步数；
- 需要观察每个 Node 的更新；
- 后续还可能加入 checkpoint、暂停恢复或人工确认。

若任务只是改变大小写、两数相加、校验 JSON 必填字段等单步确定性操作，普通函数或短循环更直接。不要只因为一个 `if/elif` 看起来复杂就引入 Graph；关键是整个工作流是否需要显式状态、回环和停止边界。

## 三个核心部件

| 部件 | 白话作用 | 在故障诊断 v1 中的例子 |
| --- | --- | --- |
| `State` | 流程共同携带的工作单 | alerts、logs、evidence、step_count、stop_reason、conclusion |
| `Node` | 领取当前工作单，完成一步并交回变更 | `review_evidence()`、`run_readonly_diagnostic()` |
| `Edge` | 指定固定下一站，或按当前状态选下一站 | 诊断后固定回 review；review 后走五路条件分支 |

官方 Graph API 把它们分别定义为共享快照、处理逻辑和决定后续执行的连接。Graph 先定义 State，再注册 Node/Edge，最后 `compile()`；编译主要检查图的基础结构，不能替代运行时输入校验、Node 返回校验或业务分支测试。

## State schema 不等于运行时校验

```python
class IncidentState(TypedDict):
    evidence: Annotated[list[str], add]
    step_count: int
    stop_reason: str | None
```

`TypedDict` 主要帮助编辑器、类型检查器和读代码的人理解字段；普通 Python 运行时不会因为一个 dict 类型不符就自动拒绝它。真实输入边界仍要由应用代码或 Pydantic 等运行时校验工具守住。

State 字段要区分两种更新规则：

- 没有 reducer：默认用本次返回值替换旧值；
- 声明 reducer：Graph 用 reducer 合并旧值和本次增量。

例如：

```python
evidence: Annotated[list[str], add]
```

若当前是 `['timeout-log']`，Node 只应返回本次新增的 `['db-pool-log']`，Graph 合并后得到：

```python
['timeout-log', 'db-pool-log']
```

若 Node 自己把旧列表也重复带回，reducer 会再次相加，产生重复证据。

## Node 优先返回局部更新

```python
def summarize_logs(state: IncidentState) -> dict:
    return {
        "summary": " | ".join(state["logs"]),
        "step_count": state["step_count"] + 1,
    }
```

这个 Node 读取 `logs` 和 `step_count`，只更新 `summary` 和 `step_count`。没有修改的字段不用重复返回。这样从返回值就能看出这一步拥有哪部分写权限，也降低误覆盖其他字段的风险。

一个函数是否算业务 Node，取决于它是否通过 `add_node()` 注册。挂在条件边上的纯路由函数会读取 State 并返回目的地，但不是业务 Node，也不产生自己的 `updates` chunk。

## Edge：固定路线与条件路线

固定下一站用普通边：

```python
builder.add_edge("run_readonly_diagnostic", "review_evidence")
```

运行时按 State 选择下一站，用条件边：

```python
builder.add_conditional_edges(
    "review_evidence",
    route_after_review,
)
```

同一 Node 连出多条普通边不是 `if/elif`；官方 Graph API 说明，这些目标会在下一次 super-step 中并行调度。互斥业务分支应由一个有完整返回范围的条件路由明确选择。

故障诊断 v1 的路由优先级是：

```text
工具已失败
→ 工具失败停止

否则已经达到或超过业务步数上限
→ 最大步数停止

否则证据不足且无需再查
→ 证据不足停止

否则证据足够
→ 构造结论

否则
→ 执行一次获批只读诊断
```

使用 `>=` 而不是只用 `==`，可以让越界状态也稳定停住。每个可能状态都应有清楚去向，不能把停止责任交给模型临场发挥。

`START` 是入口标记，`END` 是终止标记。它们不返回 State 更新，因此没有业务 Node 的 `updates` chunk。

## 代码与 LLM 怎样分工

```text
多样日志、告警文本
        │
        ▼
LLM：理解、归纳、生成开放式结论

有限工具规则、批准表、预算、失败、停止
        │
        ▼
应用代码：确定性判断并执行
```

在规则已经有限且明确的场景中，代码应控制：

- 当前允许请求哪一个工具；
- 工具名和参数是否在批准范围；
- 真实工具函数怎样执行；
- 工具返回值是否符合要求；
- 失败写成哪个稳定错误码；
- 是否达到业务上限、是否终止。

原因不是“LLM 永远不能提出工具”，而是安全和停止不能只靠模型自觉。工具失败时模型可能仍继续；达到停止条件后模型也可能继续请求。开放语义场景可以让 LLM 提议工具，但应用代码仍须拥有批准、参数、预算、执行、失败和停止边界。

### 工具选择、批准和执行是三层

```text
业务决策 Node
→ 这一次需要哪个工具

APPROVED_READONLY_TOOLS
→ 这个名字是否获批，并映射到哪个真实函数

执行 Node
→ 真正调用、校验结果、归一化失败、更新 State
```

某个工具存在于白名单，只说明“允许调用”，不说明它在当前业务规则下必然可达，更不说明它已经执行。G8-00 的一次真实错误正是：latency 工具已在批准表里，但旧选择规则永远不会请求它。

## 两种不同的上限

| 上限 | 负责什么 | 触发后怎样表现 |
| --- | --- | --- |
| `max_steps` | 当前业务允许处理多少次诊断请求 | 路由进入 `max_steps_stop`，写稳定 `stop_reason`，正常到 `END` |
| `recursion_limit` | 一次 Graph 最多允许多少个调度 super-step | 超过时抛 `GraphRecursionError`，属于运行保护错误 |

一个工具请求可能要经过 review、diagnostic、再次 review 等多个 Node 调度轮次，因此两者不能互相替代。`max_steps_stop` 也不是“设置最大次数”的 Node；它只在路由已经判断达到上限后写入停止原因。

## `invoke()` 与 `stream()`

```python
result = compiled_graph.invoke(initial_state)
```

`invoke()` 等整次 Graph 结束后，把最终 State 交给调用方。普通 `.py` 文件若既不保存也不 `print()`，终端不会自动显示这个 dict。

```python
for part in compiled_graph.stream(
    initial_state,
    stream_mode="updates",
    version="v2",
):
    if part["type"] == "updates":
        print(part["data"])
```

`updates` 给出各 Node 本次返回的局部更新，不是完整 State，也不是模型逐 token 文本；逐 token 对应 `messages`。每次调用 `stream()` 都会从传入的输入启动一次新运行，不会回放前一次 `invoke()`。

当前官方 Streaming 文档说明统一的 v2 `StreamPart` 结构需要 LangGraph 1.1+；G8-00 实际锁定并验证的是 `langgraph==1.2.11`，检查日期 2026-09-05。版本升级后应重新核对字段和默认行为。

## 没有 checkpointer 就不会跨调用续接

仅写：

```python
StateGraph(IncidentState)
```

不会让下一次独立调用自动带回上次 evidence。后续若要让同一条工作流跨调用续接，需要：

1. 编译时配置 checkpointer；
2. 调用时使用同一个 `thread_id` 定位这条流程；
3. 若要求进程重启后仍能恢复，使用持久化类型的 checkpointer。

这是 thread 范围的工作流状态保存，不是跨 thread 的长期 Memory。长期 Memory 的 CRUD、TTL、来源、冲突、删除、租户隔离、PII 和 poisoning 是另一套能力。

## 分层测试

| 层级 | 主要证明什么 |
| --- | --- |
| Node 单测 | 精确局部更新和稳定错误码 |
| route 单测 | 各 State 组合返回哪个目的地，优先级是否正确 |
| 整图测试 | 实际 Node 顺序、回环、最终 State 和停止原因 |
| 整图 + spy/tripwire | 工具/模型是否被多调、危险分支是否真的零外部调用 |

只看最终 State 可能看不出多余读取、费用和延迟已经发生。Graph 测试应联合检查最终 State、`updates` Node 顺序、工具/模型调用次数、Provider 零调用门和 fresh State 隔离。

测试预期必须从精确输入与产品规则推出，不能为了绿灯追随当前错误实现。例如 alerts-only 已规定应查 latency 时，旧实现即使稳定停在 `max_steps_reached`，也不能把这个错误结果改成测试预期。

## 来源与版本

- [LangGraph Graph API](https://docs.langchain.com/oss/python/langgraph/graph-api)，检查日期 2026-09-05。
- [LangGraph Streaming](https://docs.langchain.com/oss/python/langgraph/streaming)，检查日期 2026-09-05。
- [LangGraph Persistence](https://docs.langchain.com/oss/python/langgraph/persistence)，检查日期 2026-09-05。
- 本项目验证版本：`langgraph==1.2.11`。

## 相关链接

- [[智能体(Agent)|智能体：模型、工具与客户端调度]]
- [[ReAct推理与行动循环(ReAct)|ReAct 循环与停止]]
- [[工具定义与执行协议(Tool Definition)|工具定义、批准与执行边界]]
- [[受控重试与人工接管(Bounded Retry and Human Handoff)|受控重试与人工接管]]
- [[../../04-Projects/Agent/AI-Agent-Learning/g8-00-incident-change-review-agent-v1|G8-00 故障诊断与变更评审 Agent v1]]
- [[../../03-Courses/Agent/AI-Agent-Learning/stage4_5-langgraph-basics|阶段 4.5：LangGraph 基础工作流]]
- [[../../07-Reviews/AI-Agent-Learning/2026-09-05-g8-00-langgraph-v1-review|G8-00 正式 PASS 复盘]]
