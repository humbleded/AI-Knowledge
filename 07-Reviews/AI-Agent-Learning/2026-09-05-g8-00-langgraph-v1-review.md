---
type: review
topic: AI-Agent-Learning G8-00 LangGraph v1
status: pass
created: 2026-09-05
updated: 2026-09-05
source:
  - C:\Users\26823\Desktop\AI-Agent-Learning\tracker\progress.md
  - C:\Users\26823\Desktop\AI-Agent-Learning\code\stage8\incident_change_review_agent\incident_graph.py
  - C:\Users\26823\Desktop\AI-Agent-Learning\code\stage8\incident_change_review_agent\test_incident_graph.py
  - C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-09-05.md
tags:
  - AI-Agent-Learning
  - AI/Agent
  - LangGraph
  - StateGraph
  - Review
  - PASS
---

# 2026-09-05 G8-00 LangGraph v1 PASS 复盘

## 正式判定

`G8-00 = PASS`。

用户已经把 A4 手写控制循环迁移成可运行、可观察、可测试的 LangGraph v1：typed State、Node 局部更新、reducer、固定边/条件边、诊断回环、五路选择、四类业务结果、只读工具边界、业务步数和 v2 updates 都已经闭合。

这是阶段 4.5 的课程 PASS，不是完整 LangGraph 旗舰、durable workflow 或求职作品证据。

## 决定性结果

| 项目 | 结果 |
| --- | --- |
| 语法 | `py_compile=PASS` |
| maintained pytest | `12/12 PASS`，0.74s |
| 依赖 | `pip check` 无损坏依赖 |
| Graph | 7 个业务 Node；含 START/END 共 9 个节点、12 条边 |
| route 独立探针 | 6/6 PASS |
| stream | 5 个惰性 v2 updates part，Node 顺序准确 |
| 外部调用边界 | 零预算、证据不足和危险工具均无越界工具/模型调用 |
| 真实模型 | DeepSeek 结论 Node 链 PASS，934 字符、三段齐、输入 State 不变 |
| 学习证据 | G1～G11 + F1 共 12 个合格检查，无遗留 RETRY |

## 用户真正掌握的内容

- State 是当前流程快照，Node 读取 State 并返回局部更新，Edge 决定下一站；
- 路由函数若没有注册为 Node，就不算业务 Node，也没有 updates chunk；
- 多条普通出边不是 `if/else`，互斥分支要用条件边；
- 工具失败、业务上限、证据不足和证据足够都要有显式终点；
- 白名单、真实执行、参数/结果校验、错误码、预算和停止由应用代码控制；
- LLM 适合理解多样日志和生成开放式结论，不应独占安全路由和停止；
- `max_steps` 是业务诊断请求预算，`recursion_limit` 是 Graph super-step 保险丝；
- `updates` 是 Node 局部更新，`messages` 才是模型 token；新的 `stream()` 是新运行；
- checkpointer + 相同 `thread_id` 才能跨调用续接当前 thread，不能冒充跨 thread 长期 Memory；
- 最终 State 不能证明没有多余外部调用，还要检查 Node 顺序和 spy/tripwire 次数。

## 有价值的订正轨迹

### reducer

Node 返回旧 evidence 加新 evidence，会被 `add` reducer 再加一次并产生重复。正确做法是只返回本次增量。

### Graph 装配

曾把路由函数写成业务 Node，又在注册时混淆 `review_evidence` 与 `route_after_review`；订正后明确：review 是更新 State 的 Node，route 是条件 Edge 使用的纯选择函数。

### 业务预算与运行保险丝

曾把 `max_steps_stop` 说成设置上限的 Node；订正后明确：`max_steps` 字段保存上限，route 判断是否达到，stop Node 只写稳定 `stop_reason`。

### F1 调用次数

修改前场景的第一次回答是：

```text
get_recent_errors=2
get_latency_summary=1
model=0
```

订正后是：

```text
get_recent_errors=2
get_latency_summary=0
model=0
```

原因：两次 recent errors 已把 `step_count` 从 0 消耗到 `max_steps=2`，路由会直接进入 `max_steps_stop`，不可能再调用 latency，也不会到结论模型。今后应用“Node 次数 + 计数字段 + 最终 State”三方守恒检查。

## F1：从错误实现返回到产品规则

旧实现让 alerts-only 永远请求 recent errors。用户没有把 `max_steps_reached` 追认成正确测试预期，而是从题目输入和产品规则推出 latency 工具应该被请求，并独立给出四分支修复方案。

这同时让到期稳定错题 `WP-28` 在新场景中复测 PASS：测试预期必须服从输入语义和产品规则，不能为了让测试变绿而迁就当前实现。

## 证据归属

- 用户独立：G1～G11、F1 原始回答/订正、I1～I8b 生产实现、F1 四分支设计。
- 助手实现：I9 pytest、F1-C 新回归、F1 方案的机械落盘。
- 助手整理：A4 Loop ↔ Graph 映射和正式审计材料。

因此，12/12 能证明项目行为被保护，但不能证明用户已经独立完成 pytest 工程化。BE5-01 仍须独立验收这一能力。

## 工作场景等级

`WS-11 = EXECUTED`，范围只包括无持久化 v1 的 State、route/loop/stop、stream、工具边界和真实模型 Node 链。

没有把它写成更高等级，原因是：

- F1 没有保存修复前业务测试的真实执行输出；
- 测试和机械落盘由助手完成；
- 没有 checkpointer、thread 隔离、重启恢复、replay 幂等或 interrupt/resume。

## 回炉、算法和岗位状态

- `WP-28` 从 `+2周` 升为 `+1月`，下次 2026-10-04；
- 新增 `CD-006`：StateGraph 的 State / Node / Edge / 条件路由与应用控制边界，下次 2026-09-19；
- 剩余到期 `WP-27 / WP-29`，最老逾期 15 天，签发 `RECOVERY_BLOCK_PENDING`；
- W5 算法仍是 `DEBT 4`，G8 回炉不冒充一道算法题；
- W6 岗位审计仍是 `RETRY / INCOMPLETE`；
- `job-readiness.md` 不更新，不把课程 PASS 升级为 `JOB_EVIDENCE`。

## 下一步

1. 独立算法恢复 Session：用一个问题复测 `WP-27 / WP-29`；
2. 独立 W6 岗位审计：补齐或替换 6 条 UNKNOWN，得到恰好 10 条 `HARD_ELIGIBLE`；
3. 再进入 `R6-01`。

## 相关链接

- [[../../02-Concepts/Agent/LangGraph 状态图编排(StateGraph)|LangGraph 状态图编排]]
- [[../../03-Courses/Agent/AI-Agent-Learning/stage4_5-langgraph-basics|阶段 4.5：LangGraph 基础工作流]]
- [[../../04-Projects/Agent/AI-Agent-Learning/g8-00-incident-change-review-agent-v1|G8-00 项目记录]]
