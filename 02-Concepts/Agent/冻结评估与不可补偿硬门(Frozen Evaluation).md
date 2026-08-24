---
type: concept
topic: Agent Frozen Evaluation and Non-Compensable Gates
status: usable
created: 2026-08-24
updated: 2026-08-24
source:
  - C:\Users\26823\Desktop\AI-Agent-Learning\code\stage4\eval_cases.json
  - C:\Users\26823\Desktop\AI-Agent-Learning\code\stage4\problem-contract.md
  - C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-08-24.md
tags:
  - AI/Agent
  - Evaluation
  - Holdout
  - Regression
  - Data-Integrity
  - AI-Agent-Learning
aliases:
  - Frozen Evaluation
  - 评估冻结
  - 不可补偿硬门
  - Score-Bearing Run
---

# 冻结评估与不可补偿硬门（Frozen Evaluation）

## 一句话

冻结评估是：在看见计分输出之前，先固定案例、证据锚点、指标、阈值、运行顺序和被测文件指纹；正式运行后既不挑选重跑，也不换 holdout 或降低门槛，让结果真正回答“这个事先定义的版本是否通过”。

## 为什么“跑了很多测试”仍可能不可信

下面几种做法都可能让分数看起来很好，却无法证明系统可靠：

- 看见失败后只重跑失败样本；
- 换掉表现差的 holdout；
- 运行多次后只保留最好一次；
- 在结果出来后新增或删除指标；
- 用总通过率补偿一个安全硬门失败；
- 修改代码或数据后仍沿用旧运行报告；
- ground truth 明显错误，却为了维持分数拒绝修正；
- 改正 ground truth 后反过来重判旧运行。

冻结评估的核心不是“永远不能修改”，而是：

> 修改必须透明升版、重新冻结，并保留旧版本的失败历史。

## 运行前必须冻结的六类东西

| 类别 | 要冻结什么 |
|---|---|
| 数据 | active case ID、顺序、normal/failure/danger 分组、regression/holdout 身份 |
| 证据 | 每例允许的工具结果、主 anchor、ground truth / keypoints |
| 行为合同 | 输入、输出、路由、step、日志、恢复和安全确认规则 |
| 指标 | exact、supportedness、semantic、latency、token、调用次数等计算方式 |
| 阈值 | 每个指标的最小/最大值，以及哪些失败不可补偿 |
| 指纹 | 被测源码、eval、合同、fixture 的 bytes 与 SHA-256 |

只有独立冻结审计确认这些内容互相一致，才允许计分运行。

## 硬门与质量指标必须分开

A4-Gate 的最终例子：

| 层 | 观察点 | 阈值 | 能否互相补偿 |
|---|---|---:|---|
| exact approved summary | 公开 `summary` 是否逐码点等于客户端 `approved_summary` | normal 10/10 | 不能 |
| supportedness | 每个公开事实是否由允许证据直接支持 | normal 10/10 | 不能 |
| semantic keypoints | 预先冻结的关键点是否覆盖 | 至少 9/10 case | 独立报告，不能补硬门 |
| holdout | 未提前看模型输出的样本是否通过 | 至少 3 条且 100% | 不能 |
| failure | 三类复合失败是否安全停止 | 3/3 | 不能 |
| danger | HITL 所有 A～K 子分支是否满足副作用边界 | 1/1，11/11 子分支 | 不能 |

“不可补偿”意味着：一个越权执行、一个错误 success 或一个来源硬门突破，就足以让对应分组 FAIL；不能拿其他 13 条成功抵消。

## exact 与 semantic 为什么不是同一件事

`validate_success_result` 的 exact gate 只证明：

```text
模型最终输出
==
客户端已经批准的正文和来源
```

它不证明客户端批准的工具证据在现实世界一定真实、安全或相关。因此还需要：

- supportedness：批准正文是否真的来自允许证据；
- semantic keypoints：证据和结果是否覆盖任务所需关键点；
- source / tool audit：工具是否返回了正确来源；
- 人工或独立评估器：检查 ground truth 本身是否可靠。

同样，Candidate 中间态的无据添加率也不能在看完结果后临时加入当前计分门。若未来要把它变成指标，必须在下一版本运行前冻结定义、分母和阈值。

## holdout 的独立性

holdout 不只是“文件里写了 holdout 标签”。它还要求：

- 计分运行前没有看过该输入的模型 Action/Candidate/Reflection/Refinement；
- 没有保存该样本的 latency、token、step/log 或最终判定；
- model-0 工具 anchor 可以在运行前取得，用于冻结真实证据，但不能调用模型；
- 新 ID 不能掩盖与历史样本相同的实际输入；
- 一旦模型输出已揭示，该样本不能在下一行为版本继续冒充未揭示 holdout。

A4-Gate 中，N16 虽是新 ID，但与历史 N04 输入重复，因此在任何模型调用前淘汰；随后用新的 N19 替换并重新冻结 V5。

## transparent versioning：失败不能被擦掉

A4-Gate 的评估演进可作为模板：

```text
RUN-1 / V1
→ 暴露评估或行为缺口
→ 修复后升 V2，不覆盖旧记录

RUN-2 / V2
→ 新缺口
→ V3

RUN-3 / V3
→ 句级支持性仍不足
→ V4

唯一 RUN-4 / V4
→ RETRY，保留全部逐例证据
→ R5a 把最终正文所有权收紧到客户端 approved_summary
→ 替换已揭示 / 污染 holdout
→ V5 独立冻结审计
→ 唯一 RUN-5 / V5
→ PASS
```

RUN-5 PASS 不会改写 RUN-4 的 RETRY。不同版本回答的是不同问题：

- RUN-4：旧行为版本是否通过旧冻结评估？否。
- RUN-5：新行为和新冻结 holdout 是否通过 V5？是。

## score-bearing run 的执行纪律

正式计分运行应：

1. 重新计算所有冻结文件指纹；
2. 按 JSON 固定顺序执行全部案例；
3. 每例使用 fresh module/client/context；
4. 失败也只记录后继续，不重跑；
5. 只保存合同允许的指标，不倾倒 prompt、原始响应或异常正文；
6. 运行后再次计算指纹；
7. 由独立只读审计复算聚合值和 keypoints；
8. 最后才写正式 PASS / RETRY / FAIL。

如果启动器在第一个案例、client、模型、工具和网络之前因语法或环境错误退出，它不是案例重跑；但必须透明记录 attempted case 和副作用均为 0，再修复运行器后启动唯一计分执行。

## 指纹为什么重要

同一份报告必须绑定同一份被测对象：

```text
源码 SHA
+ eval SHA
+ 合同 SHA
+ fixtures SHA
→ 一次可复查的评估快照
```

运行后只修改“状态措辞”的合同也会产生新 SHA。正确写法是同时记录：

- 运行前计分绑定指纹；
- 运行后文档状态指纹；
- 明确后者不倒写成计分输入。

任何生产行为、数据、ground truth 或阈值的实质变化都必须重新升版和冻结。

## A4-Gate 的最终证据

唯一 V5 RUN-5：

- normal `10/10`；
- exact approved summary `10/10`；
- supportedness `10/10`；
- semantic `10/10 cases / 20/20 keypoints`；
- holdout N17/N18/N19 `3/3`；
- failure F01～F03 `3/3`；
- danger D01 `1/1`，A～K `11/11`；
- 完整固定集 `14/14`；
- selective rerun / resampling / best-of / 失败替换均为 0。

这些数字只绑定冻结的 V5 文件指纹，不能自动外推到未来模型、工具、数据或生产代码版本。

## 常见误区

| 错误理解 | 正确理解 |
|---|---|
| 测试越多，评估一定越完整 | 案例数量不能替代覆盖定义、ground truth 质量和不可补偿硬门 |
| holdout 只要换一个新 ID 就重新独立 | 实际输入、历史模型输出和调参暴露也必须独立 |
| 失败后修复再重跑同一版本即可 | 行为或数据实质变化必须升版、重新冻结，并保留旧失败 |
| exact validator 通过就证明事实真实 | 它只证明输出与客户端批准值一致 |
| 总分 13/14 已经足够好 | 安全、路由、来源等硬门的单例失败不可由平均分抵消 |
| 结果出来后加一个新指标更严格 | 这是 data peeking；新指标应进入未来版本 |
| ground truth 错了也不能改 | 应透明修正、升版；但不能反向改判旧运行 |

## 相关链接

- [[动作绑定人工确认(Action-Bound Confirmation)|动作绑定人工确认]]
- [[受控重试与人工接管(Bounded Retry and Human Handoff)|受控重试与人工接管]]
- [[反思机制(Reflection)|反思机制]]
- [[../../04-Projects/Agent/AI-Agent-Learning/a4-gate-research-summary-agent|A4-Gate 研究摘要 Agent]]
- [[../../04-Projects/Agent/AI-Agent-Learning/a4-gate-function-call-reference|A4-Gate 函数调用参考]]
