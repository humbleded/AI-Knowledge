---
type: review
topic: AI-Agent-Learning A4-Gate
status: pass
created: 2026-08-24
updated: 2026-08-24
source:
  - C:\Users\26823\Desktop\AI-Agent-Learning\tracker\progress.md
  - C:\Users\26823\Desktop\AI-Agent-Learning\code\stage4\problem-contract.md
  - C:\Users\26823\Desktop\AI-Agent-Learning\code\stage4\a4_gate_research_summary_agent.py
  - C:\Users\26823\Desktop\AI-Agent-Learning\code\stage4\eval_cases.json
  - C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-08-24.md
tags:
  - AI-Agent-Learning
  - AI/Agent
  - Tool-Calling
  - Reflection
  - HITL
  - Evaluation
  - PASS
---

# 2026-08-24 A4-Gate 研究摘要 Agent PASS 复盘

## 正式判定

**A4-Gate = PASS。**

这次通过证明用户能设计、实现、运行并解释一套最小但完整的 Agent 控制器：

```text
输入硬校验
→ 模型提出 Tool Action
→ 客户端校验并执行真实工具
→ Tool Observation 回填
→ Candidate
→ Reflection
→ Refinement
→ 客户端 exact validator
→ 公开三字段结果
```

它同时具备请求级 step / 七字段日志、受控恢复、完整尾链预算、action-bound HITL、固定 eval、holdout 和失败注入。最终状态是 `COURSE_PASS`，不是 `JOB_EVIDENCE`：仍缺面向他人的 README/架构说明、长期自动测试、服务化、依赖锁定、CI、lint/type-check 和公开可复现部署。

## 最终产物与指纹

| 产物 | 最终用途 | 指纹 |
|---|---|---|
| `code/stage4/a4_gate_research_summary_agent.py` | 生产 Agent、工具、恢复、HITL 与 validator | `243712 bytes / A6190964BFC7B70EED6F929C2495AC291CEBA441B1BFE5001B6A4EFC6D6F5DC6` |
| `code/stage4/eval_cases.json` | 唯一长期固定评估数据 | `102737 bytes / 1802BAF7BF1ABF883E087CF6B9510C3043F394038E4609C90E1F595ECA0AFEDE` |
| `code/stage4/problem-contract.md` | FINAL / PASS 行为合同 | post-review `54902 bytes / 8DE95E6B8CEFA0C8261287CAD23516B970E888ADC33740BB25F9D732632C2C9E` |
| `resources/sandbox/sample.txt` | 正常 file fixture | `105 bytes / 60C21EBB6EE52C8D100B5D527BFFC4F7788F9A25AE11D843AE7DBF1E7DE7F9FF` |
| `resources/sandbox/long.txt` | 截断状态 fixture | `27 bytes / 1010A7E761610980AC591359C871F724DE150F23440EBB5959AC4C0724C91D91` |

唯一 RUN-5 实际绑定运行前 Contract `54211 bytes / 25BB32E132521B1DEB9C84FFF8870FD8BF000D390A75155F09744D83018ED604`。正式判定后的 Contract 只写回状态与证据时态，因此新指纹不能倒写成计分输入。

## PASS 标准与决定性证据

| PASS 标准 | 决定性证据 | 判定 |
|---|---|---|
| 完整 Problem Contract | 输入、输出、工具、循环、停止、恢复、日志、HITL、eval、非目标均冻结；状态 FINAL / PASS | PASS |
| 可运行主链 | topic/path 两路；4 次模型 + 1 次真实工具；`step/log=5/5`；本地 validator 放行 | PASS |
| 受控恢复 | 工具、Action、Candidate、Reflection、Refinement 均有局部额度 + `MAX_STEPS=6` + 完整链预算 | PASS |
| 最终正文硬门 | `summary == approved_summary` 逐码点；`sources == allowed_sources` 精确列表 | PASS |
| HITL | D01 allow/deny/missing/invalid/mismatch/replay/timeout A～K `11/11`；未授权副作用 0 | PASS |
| 固定评估 | `14 = 10 normal + 3 failure + 1 danger`；3 条未揭示 holdout | PASS |
| 五道必答题 | GQ1 guided restatement；GQ2/GQ4/GQ5 订正后 PASS；GQ3 PASS | PASS |

## 唯一 V5 RUN-5

| 指标 | 冻结阈值 | 实际 |
|---|---:|---:|
| normal mechanical | 10/10 | 10/10 |
| exact approved summary | 10/10 | 10/10 |
| supportedness | 10/10 | 10/10 |
| semantic keypoints | 至少 9/10 case | 10/10 case，20/20 keypoints |
| holdout | 至少 3 条且 100% | N17/N18/N19 = 3/3 |
| failure | F01～F03 = 3/3 | 3/3 |
| danger | D01 = 1/1 | 1/1，A～K = 11/11 |
| 完整固定集 | 所有分组独立达标 | 14/14 |

性能与成本：

- latency：平均 `7193.3 ms`，最小 `4431 ms`，最大 `10639 ms`；
- 10/10 均低于 `240000 ms`，也低于单例 `360000 ms` 硬门；
- token：总计 `33303`，每例 `2370..3899`，10/10 低于 `20000`；
- 40 次逻辑模型、10 次逻辑生产工具、8 次物理 GET、50 step、50 条七字段日志；
- normal 中 Action correction、Agent recovery、工具 retry 均为 0；
- selective rerun、resampling、best-of、失败替换均为 0。

## 透明保留的失败历史

V4 唯一 RUN-4 的 `RETRY` 永久保留。它暴露了模型即使经过 Reflection，仍会在最终摘要里加入自证元陈述、扩大主语或改写因果。

R5a 没有降低 supportedness 门槛，而是改变正文所有权：

```text
真实工具结果
→ 客户端确定性构造 approved_summary
→ Refinement 只能逐字符复制
→ validator exact 比较
```

行为发生实质变化后，系统没有重跑 V4 覆盖旧失败，而是：

1. 升级到 V5；
2. 替换已揭示 holdout；
3. 淘汰与历史输入重复的 N16；
4. 修正错误 N01 ground truth 并透明留痕；
5. 独立冻结新 SHA；
6. 只执行一次完整 RUN-5。

## 完整学习演进

| 阶段 | 学到并实现了什么 |
|---|---|
| Contract / C1 | 把模糊需求改成输入、输出、失败状态、阈值和安全边界；非法输入零副作用 |
| C2 | `read_material` 沙箱读取；`search_web` 中文 Wikipedia；区分外部故障、零证据和程序 bug |
| C3a～C3c | function-tool Schema、Action 白名单/JSON/schema/值绑定、真实 Tool Calls + Observation 闭环 |
| C3d | allowlist、Reflection/Refinement prompt、JSON 解析与客户端 validator |
| C4a-1 | 每请求独立 run_context、step、七字段日志、精确 finish_reason 与第 7 次零副作用硬门 |
| C4a-2 | 同参数工具 retry、真实执行 provenance、`tool_failure / insufficient_evidence / needs_manual` 精确映射 |
| C4b-1 | Action correction、安全 validation Observation 与完整尾链预算 |
| C4b-2 | Candidate / Reflection Provider 与 protocol recovery、Refinement 四域共享 recovery |
| HITL | 动作绑定、一次性 confirmation、allow/deny、replay 与 timeout 后不可复用 |
| Eval | V1～V5 透明升版、holdout 独立性、不可补偿硬门、RUN-5 与独立审计 |
| 五问 | 能解释主循环、停止、工具恢复、幻觉风险和可测试验收合同 |

## 最有价值的“错误理解 → 当前结论”

- 模型调用工具 → 模型只提出 Action，客户端才执行工具。
- 工具返回 dict 就能继续 → 必须严格 `ok is True` 且证据充分。
- JSON Mode 等于业务合法 → 仍需 `json.loads` 和客户端 validator。
- allowlist 能证明事实真实 → 只能证明来源属于本轮证据池。
- `MAX_STEPS` 足以管理所有恢复 → 还要局部额度和完整尾链预算。
- 失败类型变化会刷新 recovery → Refinement 四域共享一次额度，跨域不会重置。
- Candidate recovery 可以把坏输出喂回模型 → 只能传固定安全 reason，失败值和异常正文隔离。
- timeout 后可以重放危险授权 → confirmation 在副作用前消费，未知状态下旧授权必须作废。
- exact validator 证明事实真实性 → 只证明最终输出与客户端批准证据一致。
- 测试总分高可以抵消一个安全失败 → 硬门按组不可补偿。
- 新 case ID 就是新 holdout → 输入和历史曝光也必须独立。

## 剩余风险

- Candidate 仍是内部最容易产生无据文字的阶段，只是不能越过 exact gate。
- 工具证据本身可能错误、恶意、受提示注入或与问题无关；exact gate 无法判定现实真实性与内容安全。
- 当前搜索后端只覆盖中文 Wikipedia，不代表全网检索。
- 当前 HITL 是同步单进程内存版，不提供持久化原子消费或多实例一致性。
- 当前 eval 只证明冻结的源码、模型、数据和合同快照，未来变化必须重新评估。

## 相关链接

- [[../../04-Projects/Agent/AI-Agent-Learning/a4-gate-research-summary-agent|A4-Gate 完整学习流程]]
- [[../../04-Projects/Agent/AI-Agent-Learning/a4-gate-function-call-reference|A4-Gate 函数调用参考]]
- [[../../02-Concepts/Agent/受控重试与人工接管(Bounded Retry and Human Handoff)|受控重试与人工接管]]
- [[../../02-Concepts/Agent/动作绑定人工确认(Action-Bound Confirmation)|动作绑定人工确认]]
- [[../../02-Concepts/Agent/冻结评估与不可补偿硬门(Frozen Evaluation)|冻结评估与不可补偿硬门]]
- [[../../02-Concepts/LLM/LLM 本质与幻觉(Hallucination)|LLM 本质与幻觉]]
