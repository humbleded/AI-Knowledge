---
type: concept
topic: Reflection
status: usable
created: 2026-07-23
updated: 2026-08-22
source:
  - C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-07-23.md
  - C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-07-30.md
  - C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-08-03.md
  - C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-08-04.md
  - C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-08-10.md
  - C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-08-20.md
  - C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-08-21.md
  - C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-08-22.md
  - C:\Users\26823\Desktop\AI-Agent-Learning\code\stage4\problem-contract.md
  - C:\Users\26823\Desktop\AI-Agent-Learning\code\stage4\a4_05_reflection_writer.py
  - C:\Users\26823\Desktop\AI-Agent-Learning\code\stage4\a4_gate_research_summary_agent.py
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

## 最小闭环与数据依赖

一个可执行的 Reflection 闭环至少包含三个不同职责：

```text
Execution(Task)
  -> initial_draft

Reflection(Task, initial_draft, evaluation_criteria)
  -> feedback

Refinement(Task, initial_draft, feedback)
  -> refined_draft
```

- `Execution` 根据原始任务生成初稿。
- `Reflection` 必须同时看到原始任务、待评审稿和评价标准；它输出的是反馈，不是改进稿。
- `Refinement` 必须同时看到原始任务、上一版草稿和反馈；它才负责生成候选改进稿。

原始任务必须贯穿三阶段。如果 Reflection 只看到初稿，它不知道用什么标准判断；如果 Refinement 只看到反馈，它可能修复一个问题却丢掉原任务中的其他约束。

## 停止条件与可观察轨迹

A4-05 的最小实现只允许一轮改进：

```text
execution(initial_draft)
  -> reflection(feedback)
       |-> feedback == "无需改进"：停止
       `-> 其他反馈：execution(refined_draft) 后停止
```

- “无需改进”必须先记录进轨迹，再执行停止判断。
- 精确停止分支只有 2 次模型调用：初稿 + Reflection。
- 完整改进分支有 3 次模型调用：初稿 + Reflection + Refinement。
- 轨迹和最终选择要分开保存：失败候选可以留在审计记录中，但不能因此成为最终稿。

实现 Memory 时也要区分读取目的：完整审计需要全部轨迹，下一轮只需要最近执行稿时应逆序寻找最近一条 `execution`，不能把列表末尾的 Reflection 反馈误当成稿件。

## 如何证明没有越改越差

模型说“无需改进”或“已经更好”只是模型反馈，不能单独证明质量。可靠的选择至少需要：

1. 初稿和候选稿使用同一套评估标准。
2. 任一硬约束失败时拒绝候选稿，保留上一版已验证最佳稿。
3. 未编码的语义质量必须有额外证据，例如领域测试、事实来源、rubric evaluator 或人工确认。
4. 同时保存候选稿、检查结果、接受标记、决策原因和最终稿，保证决定可审计。

```text
candidate
  -> deterministic checks
       |-> fail：保留候选轨迹，但 final = previous_best
       `-> pass：只证明已编码维度通过，再检查其余质量证据
```

> [!warning] 接受标记的边界
> `accepted_refinement=True` 只说明候选稿通过了当前代码已经实现的门槛。若代码只检查日期、地点和长度，它不能证明行动指引、事实正确性或表达质量也得到改善。

## Prompt 软评审与客户端硬门槛

- Reflection prompt 负责告诉模型“按哪些标准评审”和“反馈采用什么协议”。
- 模型仍可能漏项、误判或不遵守格式，因此 prompt 是软约束。
- 客户端 validator 负责对已编码条件作可重复执行的硬判定，并决定接受或回退。
- 工具结果、外部测试和权威事实源提供独立证据；高风险动作还需要人工确认，失败或超时必须保持未知。

代码硬校验不是“让模型一定守规矩”，而是在模型返回之后限制系统能接受什么、拒绝什么。它也不能自动覆盖没有编码进去的质量维度。

### 来源白名单只是引用边界，不是内容证明

研究摘要类 Agent 还要把“来源是谁”和“内容是否受证据支持”分成两层。`allowed_sources`（允许来源集合）必须由**本轮真实 Observation** 派生，不能从模型生成的摘要或反馈里反推：

```text
本轮真实 Observation
  |-> read_material：只允许这次实际读取的规范化相对路径
  `-> search_web：只允许这次 results[*].url 中出现的 URL
          |
          `-> allowed_sources

候选摘要 + 完整 content/results + allowed_sources
  -> Reflection 软评审
  -> Refinement 结构化候选
  -> JSON 解析
  -> 客户端硬校验 sources ⊆ allowed_sources
```

- Reflection prompt 应同时带上完整的 `content/results` 和 `allowed_sources`：前者用来判断摘要结论有没有正文证据，后者只限定允许引用哪些来源。
- prompt 中要求“只能从白名单选来源”仍是软约束；模型可能虚构、混入或返回空来源，解析后必须由客户端重新校验。
- 客户端应拒绝空来源、非字符串来源、全越界来源，以及“一个合法来源 + 一个虚构来源”的混合结果，不能删除坏项后把剩余部分静默当成成功。
- `source in allowed_sources` 只证明这个来源身份来自本轮 Observation；它**不证明**摘要里的每个事实都由该来源正文支持。内容支持仍要由 Reflection、可执行 evaluator 或人工审核另行判断。

这条边界也解释了为什么“模型说来源真实”不能替代代码检查：模型既是候选内容的生成者，又是软评审参与者；最终可接受集合必须由客户端根据外部执行事实确定。

## Reflection 反馈失败时，恢复的是评审，不是最终答案

Reflection 的输出只是供 Refinement 使用的中间反馈，不是最终摘要。因此，当模型 API 已经返回、但反馈外壳或正文不可用时，一次安全恢复必须保持阶段职责：仍然重新完成同一个 Reflection，只返回纯文本反馈；不能跳过 Refinement，不能直接生成最终三字段结果，也不能把“已有合法 Candidate”误当成成功。

```text
合法 Candidate
  -> step 4 Reflection 响应可恢复失败
  -> step 5 Reflection recovery
  -> step 6 Refinement
  -> JSON 解析与客户端 validator
```

这里有四个关键边界：

- 发起 recovery 前一次性检查完整尾链预算。Reflection recovery 后必需还有一个 Refinement 位置，所以至少需要 2 个剩余 step；若首次 Reflection 已到 step 5，只剩 step 6，就应在新调用前停止。
- recovery prompt 复用原始可信 Reflection prompt，因此仍包含真实 Observation、合法 Candidate、`allowed_sources` 和原评审标准；失败响应或失败反馈正文不进入 prompt。
- 同一阶段最多恢复一次。恢复后只有合法反馈能进入 Refinement；terminal 或仍可恢复的响应都安全停止。
- Reflection 协议恢复分支不能顺手吞掉 Provider / HTTP / SDK 异常；Reflection Provider/API 由独立 wrapper、完整链预算和窄停止信号处理。进入 Refinement 后由独立 Refinement 编排接管：Provider、响应、JSON 与模型 candidate 合同的可恢复失败共享一次额外模型调用；新的 candidate 仍须重过最终 validator，非法 `allowed_sources` 与普通程序 / 不变量错误保持原异常上抛。详细共享额度与 prompt 信任边界见 [[受控重试与人工接管(Bounded Retry and Human Handoff)#Refinement 恢复：四个失败域，共用一次机会|Refinement 恢复合同]]。

Reflection Provider recovery 与 protocol recovery 要分成两本账。它们都只统计**因相应原因真正额外发出的逻辑模型调用**，不统计首次 Reflection、SDK 内部物理重试、错误事件、本地分类或只存在但没有使用的恢复额度：

- 前一调用因 Provider/API 错误结束，Agent 真的另发一条请求，才记 Provider recovery；
- API 已返回坏协议 / 坏正文，Agent 真的另发一条请求，才记 protocol recovery；
- 一次 protocol recovery 后来 timeout，它仍是 protocol recovery，因为调用角色由“为什么发起”决定，不由“后来怎样失败”倒改；如果 timeout 后没有再发新请求，Provider recovery 仍是 0；
- Provider recovery 返回合法反馈后的本地校验不是模型请求，因此不会把 protocol recovery 计为 1。

正常链中，step 4 的首次 Reflection 遇 recoverable Provider 错误时，可以在完整链预算允许的前提下执行 step 5 Provider recovery，再由 step 6 Refinement 收尾，计数为 Provider 1 / protocol 0。若前序恢复已把首次 Reflection 推到 step 5，剩余一步无法同时容纳 recovery + Refinement，应在新请求前停止，计数为 0 / 0。若 step 5 本来就是因坏响应发出的 protocol recovery，而该调用以 Provider 错误结束，则计数保持 Provider 0 / protocol 1，并停止而不是发第三次请求。

停止后的 `needs_manual.sources` 仍只表示本轮工具真实取得、供人工复核的证据池。此时已有合法 Candidate，但还没有任何最终摘要完成 Reflection → Refinement → validator；详细的分类、完整链预算、公开信号对账与防篡改边界见 [[受控重试与人工接管(Bounded Retry and Human Handoff)|受控重试与人工接管]]。

## 成本与适用场景

每个完整改进轮都会增加 Reflection 与 Refinement 模型调用；后一阶段依赖前一阶段结果，因此通常串行执行，总延迟也会累加。若保存或发送完整轨迹，还会增加上下文与状态管理成本。

更适合使用 Reflection 的任务通常具有以下特征：

- 错误代价高，质量和可靠性优先于即时响应。
- 存在明确评价标准、测试或事实来源。
- 发现问题后确实有可执行的修复路径。
- 可以容忍额外模型调用和串行延迟。

低风险欢迎语、强实时回复或一次结果已经够用的任务，往往不值得增加 Reflection 循环。

## 如何验证平时走不到的改进分支

真实模型可能每次都直接生成合格初稿，导致正常运行只能证明提前停止路径。为了稳定验证 Refinement，可在**验证边界**只注入一个已知缺陷初稿，然后让 Reflection 与 Refinement 继续调用真实模型：

```text
正常路径：真实初稿 -> 真实 Reflection -> 无需改进 -> 停止
故障路径：受控坏初稿 -> 真实 Reflection -> 真实 Refinement -> 同标准检查
```

这种故障路径不能冒充“全链路每一步都由真实模型生成”；它必须和正常全真实路径组合使用，并明确记录哪些输出是夹具、哪些输出来自真实 API。生产停止条件本身不得为了测试而改成“永远进入 Refinement”。

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
| Reflection prompt 只负责规定输出格式 | 它还负责表达评审标准和反馈协议，但仍不能保证模型遵守 |
| 模型说“无需改进”就证明质量通过 | 模型反馈是软证据；接受决定还需要客户端硬校验、外部证据或人工确认 |
| 候选稿通过三个检查就证明总体更好 | 只证明已编码的三个维度；未编码的语义质量仍可能退化 |
| 为了覆盖改进分支，可以删除生产提前停止 | 测试应在验证边界注入已知缺陷，不能改变生产停止语义 |

## 相关链接

- [[ReAct推理与行动循环(ReAct)|ReAct 推理与行动循环]]
- [[计划与求解(Plan-and-Solve)|计划与求解]]
- [[智能体(Agent)|智能体]]
- [[工具调用与动作(Tool Calling and Action)|工具调用与动作]]
- [[受控重试与人工接管(Bounded Retry and Human Handoff)|受控重试与人工接管]]

## 来源与证据

- `C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-07-23.md`：A4-04-G6 对“运行事实复盘”和 A4-05 `Reflection` 的拆分考察与订正证据。
- `C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-07-30.md`、`daily\2026-08-03.md`：A4-05 带读、三阶段数据依赖、停止条件、成本、适用场景和质量回退证据。
- `C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-08-04.md`：正式练习、真实 DeepSeek 正常/故障分支与任务级 PASS 复核。
- `C:\Users\26823\Desktop\AI-Agent-Learning\code\stage4\a4_05_reflection_writer.py`：可运行的单轮 Reflection Writer、确定性门槛和审计字段。
- `C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-08-10.md`、`code\stage4\a4_gate_research_summary_agent.py`：A4-Gate C3d 的 Observation 来源白名单、Reflection / Refinement prompt 与客户端来源子集硬门；这些子检查点已通过，整个 A4-Gate 仍为 `DOING`。
- `C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-08-20.md`、`code\stage4\problem-contract.md`、`code\stage4\a4_gate_research_summary_agent.py`：A4-Gate C4b-2b-1 的 Reflection 反馈三分法、一次安全恢复、两步完整尾链预算、阶段停止和公开来源对账；坏协议分支由可重复的 fake / spy 故障注入验证，真实 DeepSeek 只证明正常五步链没有回归。该证据只关闭 C4b-2b-1，父 Gate 仍为 `DOING`。
- [C4b-2b-1 Reflection 反馈恢复提交 `e4a5681`](https://github.com/humbleded/AI-Agent-Learning/commit/e4a56813aa6b4e68ffee4ab7b45d5a3a2c1d2a5f)
- `C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-08-21.md`、`code\stage4\problem-contract.md`、`code\stage4\a4_gate_research_summary_agent.py`：A4-Gate C4b-2b-2b 的 Reflection Provider/API 一次恢复、Provider / protocol 独立计数、完整链预算与零第三次请求；真实 DeepSeek 只证明正常链没有回归。该证据只关闭本教学 / 实现子单元，父 Gate 仍为 `DOING`。
- [C4b-2b-2b Reflection Provider/API 恢复提交 `427d60c`](https://github.com/humbleded/AI-Agent-Learning/commit/427d60c)
- `C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-08-22.md`、`code\stage4\problem-contract.md`、`code\stage4\a4_gate_research_summary_agent.py`：A4-Gate C4b-2c 的 Refinement Provider / 响应 / JSON / candidate-contract 共享一次 recovery、新候选重校验、普通程序错误上抛与安全人工接管。该证据只关闭 C4b-2c 子单元，父 Gate 仍为 `DOING`。
