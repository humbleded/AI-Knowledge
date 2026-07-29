---
type: concept
topic: Reflection
status: usable
created: 2026-07-23
updated: 2026-07-30
source:
  - C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-07-23.md
tags:
  - AI/Agent
  - Reflection
  - Planning
  - AI-Agent-Learning
aliases:
  - Reflection
  - Agent 反思
  - Agent 反思机制
---

# 反思机制（Reflection）

## 一句话

`Reflection` 是 Agent 对执行过程或结果进行质量评价的机制：它对照原始目标或评价标准识别不足，分析原因，提出改进，并把结论用于重试、重规划、重写或后续记忆。

> [!important] 术语边界
> `Reflection` 有时也会被宽泛地翻译成“反思”或“复盘”，没有脱离上下文的唯一译法。本文所说的“复盘”，特指 A4-04 Plan-and-Solve 验收中的**运行事实总结**；它和 A4-05 的 `Reflection` 不是同一层职责。

## Reflection 与运行复盘的区别

| 判断维度 | 运行复盘（事实总结） | Reflection（评价与改进） |
|---|---|---|
| 核心问题 | 发生了什么？ | 做得是否足够好？为什么？怎样改？ |
| 主要输入 | 计划、执行步骤、异常、调整、最终状态 | 原始目标、评价标准、完整轨迹、当前结果 |
| 主要输出 | 可审计的执行摘要 | 质量判断、问题原因、改进建议 |
| 是否必须改变后续行为 | 不一定，可以只用于记录 | 要形成闭环，应指导重试、重规划、重写或后续记忆 |

### 运行复盘示例

```text
原计划 4 步，第 3 步失败后通过重规划的替代步骤完成，
最终任务完成。
```

这段话交代了计划规模、失败位置、调整方式和最终状态，回答的是“发生了什么”，没有评价答案质量。

### Reflection 示例

```text
最终答案虽然完成了任务，但论据不足，无法支撑结论。
下一轮应先补充可靠数据，再根据数据重写答案。
```

这段话对照质量要求指出了缺口，并提出下一步改进，因此属于 `Reflection`。

## 不能只用“发生时间”判断

`Reflection` 可以出现在执行中，也可以在一轮任务结束后发生；人或团队的完整复盘也可能包含评价和改进。因此，两者真正的分界不是“一个在过程中、一个在结束后”，而是：

> [!tip] 共同判断标准
> 只还原执行事实，是运行复盘；对照目标评价过程或结果，并产出改进方向，是 `Reflection`。

如果 `Reflection` 只生成一段点评，却既不影响当前任务，也不进入后续记忆，那么它只有“反思文本”，还没有形成完整的反思闭环。

## 与 Observation、Planning 的关系

```text
Action
  -> Observation（工具或环境返回的事实）
  -> 记录进执行轨迹
       |-> 运行复盘：总结发生了什么
       `-> Reflection：评价哪里不足、为什么、怎样改
                              |
                              `-> 重试 / 重写 / 触发重新 Planning / 写入 Memory
```

- `Observation` 提供外部反馈，是证据。
- `Reflection` 解释和评价证据，形成改进意见。
- `Planning` 负责制定或调整行动路线；重新规划可能由 Reflection 触发，但二者不是同一个动作。

## 常见误区

| 错误理解 | 正确理解 |
|---|---|
| 只要任务结束后写了一段总结，就是 Reflection | 只记录步骤和结果属于事实复盘；还要有质量评价与改进 |
| 发生重新规划，就一定做了 Reflection | 重新规划属于 Planning；它可以由外部新约束、执行失败或 Reflection 触发 |
| Reflection 必须在每一步后立即执行 | 可以按步、按阶段或整轮触发，取决于任务成本与质量要求 |
| Reflection 写得越多越好 | 它会增加模型调用、延迟和 token 成本，应只在结果可评价且改进有价值时使用 |

## 相关链接

- [[ReAct推理与行动循环(ReAct)|ReAct 推理与行动循环]]
- [[计划与求解(Plan-and-Solve)|计划与求解]]
- [[智能体(Agent)|智能体]]
- [[工具调用与动作(Tool Calling and Action)|工具调用与动作]]

## 来源与证据

- `C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-07-23.md`：A4-04-G6 对“运行事实复盘”和 A4-05 `Reflection` 的拆分考察与订正证据。
