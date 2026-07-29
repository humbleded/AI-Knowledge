---
type: concept
topic: Plan-and-Solve
status: usable
created: 2026-07-30
updated: 2026-07-30
source:
  - C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-07-22.md
  - C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-07-23.md
  - C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-07-29.md
  - C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-07-30.md
  - C:\Users\26823\Desktop\AI-Agent-Learning\code\stage4\a4_04_plan_solve_demo.py
tags:
  - AI/Agent
  - Planning
  - Plan-and-Solve
  - AI-Agent-Learning
aliases:
  - Plan-and-Solve
  - Plan and Solve
  - Planning Agent
---

# 计划与求解（Plan-and-Solve）

## 一句话

`Plan-and-Solve` 先让 Planner 把原始目标拆成有序、可执行的步骤，再让 Executor 按顺序执行；后续步骤必须同时看到原始目标、完整计划和之前步骤的真实结果。

```text
原始目标 q
   -> Planner：生成计划 P
   -> Executor：执行 P[0]
   -> history：保存 (step, result)
   -> Executor：带着 q + P + history 执行 P[1] ...
   -> 事实性复盘：记录计划、执行、异常与最终状态
```

## Planner：设计路线，不提前完成任务

Planner 的产物是“怎样做”的步骤列表，不是最终答案。

例如，目标是“安排三天旅行”时：

```python
[
    "查询三天的天气",
    "根据天气和预算筛选活动",
    "生成每日行程",
]
```

Planner 不应在尚未查询时直接声称某天是晴天。天气属于执行阶段取得的事实，计划只描述如何取得和使用它。

一个合格的步骤通常包含：

- 明确动作：查询、选择、预订、计算、汇总；
- 必须满足的约束：预算、时间、排除项；
- 可供后续使用的产出；
- 与前后步骤的顺序或数据依赖。

## Executor 为什么需要四类上下文

| 上下文 | 作用 |
|---|---|
| 原始目标 `question` | 防止局部步骤做着做着偏离最终目标 |
| 完整计划 `plan` | 知道当前步骤处于整体路线的哪个位置 |
| 当前步骤 `step` | 明确本轮只执行什么 |
| 历史结果 `history` | 让后一步使用前一步真实取得的数据 |

历史最好把步骤名和结果绑定保存：

```python
StepResult = tuple[str, str]
history: list[StepResult] = [
    ("查询天气", "晴天"),
]
```

只保存 `["晴天"]` 会丢失结果来源；后续步骤和复盘都更难追溯。

## 状态边界：非法结果不能先污染 history

类型别名：

```python
LLMCall = Callable[[str], str]
StepResult = tuple[str, str]
```

表达了预期的数据形状，但 Python 不会仅凭类型提示自动阻止运行时的 `None`。

如果模型适配器异常返回 Python 值 `None`，旧执行器先把它写入 history：

```text
[("s1", "r1"), ("s2", None)]
```

那么第 3 步 prompt 会携带脏状态，最终还可能在 `result.strip()` 处崩溃。只让最后的 `.strip()` “接受 None”不能撤销已经发生的上下文污染。

最小降级策略是在状态写入前恢复 `str` 契约：

```python
result = llm_call(context)
if result is None:
    result = ""

results.append((step, result))
history.append((step, result))
```

空字符串在当前实现中表示该步骤没有有效结果；事实复盘会把任务标记为未完成。

> [!important] 分层契约
> `execute_plan` 的内部步骤结果必须是 `(step, str)`，因为它会进入 history。外层编排函数可以按自己的 `str | None` 契约，在空计划时向调用方返回 `None`；这两个边界不能混为一谈。

## 静态 Planning 与 Replanning

最小静态 Executor 会继续执行原计划。即使某一步错误，它也可能把错误结果带给下一步；它不会自动校验、回滚或重规划。

当执行中出现新约束时，Replanning 应更新的是“剩余路线”，不是把原计划从头再跑一次：

```text
失败或新约束
  -> 停止依赖旧状态的未执行步骤
  -> 保存 current_state 与 history
  -> 保留已经成功且不可重复的副作用
  -> replanner(question, current_state, history)
  -> 只执行新的 remaining_plan
  -> 用 max_replans 限制重规划次数
```

例如火车票订单 `T100` 已支付且不可退、酒店 A 满房时：

- 不得再次买票；
- 不得继续使用酒店 A；
- 先搜索并实际预订满足位置和预算约束的替代酒店；
- 路线步骤必须引用该预订步骤真实返回的酒店位置；
- 最后才能汇总票、酒店和路线。

只写“不得买票、不得用酒店 A”仍是约束集合，不是 Executor 可逐项调用的剩余计划；提前写死“酒店 B”则是在执行前虚构结果。

## 什么时候用固定工作流

“任务有多个步骤”不是必须使用动态 Planning 的充分条件。

- how 已知、规则稳定、流程可重复：优先固定工作流，行为更可预测，成本更低；
- how 需要现场发现，或执行中经常遇到新约束：Planning / Replanning 更合适；
- 规划会增加模型调用、延迟、token 成本和不确定性，不应给简单任务机械套 Planner。

## 事实性复盘不是 Reflection

A4-04 的运行复盘回答“发生了什么”：

- 原计划规模；
- 实际完成步骤；
- 失败或未执行步骤；
- 是否重规划；
- 最终结果与状态。

它不评价答案质量，也不提出改进方案。后者属于 [[反思机制(Reflection)|Reflection]]。

## 确定性 demo 的证据边界

确定性 `demo_llm` 可以稳定证明：

- Planner 文本能被解析为结构化计划；
- Executor 按顺序调用并携带 history；
- 计划、逐步结果、复盘和最终返回值能形成完整轨迹；
- 空计划与异常结果分支按客户端代码工作。

它不能证明真实模型总会生成好计划、遵守格式或正确使用前序结果。真实模型质量仍需要后续数据集、指标和评估。

## 常见错误 → 正确理解

| 错误理解 | 正确理解 |
|---|---|
| Planner 应直接给出天气和行程答案 | Planner 先规划“查询并使用天气”的步骤，事实由 Executor 获取 |
| 后一步只需要看当前步骤 | 还需要原始目标、完整计划和前序真实结果 |
| `list[str]` / `Callable[[str], str]` 会自动校验运行时类型 | 类型提示主要服务阅读和静态检查，运行时边界仍需代码与测试 |
| 最后 `.strip()` 不崩就算修好 `None` | 必须在非法值进入 results/history 前处理 |
| 约束集合就是新计划 | 新计划必须是可执行动作链，并明确真实产出与数据依赖 |
| Replanning 要把所有步骤重做 | 保留已完成且不可重复的动作，只重写并执行剩余路线 |
| 运行复盘就是 Reflection | 前者记录事实，后者评价质量并提出改进 |

## 相关链接

- [[智能体(Agent)]]
- [[ReAct推理与行动循环(ReAct)|ReAct 推理与行动循环]]
- [[反思机制(Reflection)|反思机制]]
- [[../LLM/结构化输出(Structured Output)|结构化输出]]
- [[../../04-Projects/Agent/AI-Agent-Learning/a4-04-plan-and-solve|A4-04 Plan-and-Solve 代码实践]]
- [[../../07-Reviews/AI-Agent-Learning/2026-07-30-a4-04-plan-and-solve-review|2026-07-30 A4-04 PASS 复盘]]

## 来源与证据

- `C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-07-22.md`～`2026-07-30.md`：带读、实现、正式题目、订正和任务级验收。
- `C:\Users\26823\Desktop\AI-Agent-Learning\code\stage4\a4_04_plan_solve_demo.py`：当前通过 39 项聚焦边界断言的可运行实现。
- Hello-Agents 第 4 章 `4.3 Plan-and-Solve` 与 Agentic Design Patterns Chapter 6 Planning：具体版本与本地 commit 记录在上述 daily。
