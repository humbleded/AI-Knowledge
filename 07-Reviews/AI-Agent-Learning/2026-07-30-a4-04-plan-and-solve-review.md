---
type: review
topic: AI-Agent-Learning A4-04
status: pass
created: 2026-07-30
updated: 2026-07-30
tags:
  - AI-Agent-Learning
  - Agent
  - Planning
  - PASS
---

# 2026-07-30 A4-04 Plan-and-Solve PASS 复盘

## 判定

**A4-04 PASS**。

真实产物可直接输出结构化计划、3 个步骤结果、事实性复盘和最终答案；语法编译、直接 demo 与 39 项聚焦边界断言全部通过。G1–G7 与 F1–F3 共 10 个任务级语义目标已经闭合。

## PASS 标准与决定性证据

| PASS 标准 | 决定性证据 |
|---|---|
| 输出计划 | Planner 只拆解步骤；有效围栏列表被解析为 3 步计划 |
| 输出执行结果 | Executor 按顺序执行，每轮携带原目标、完整计划、当前步骤与 `(step, result)` history |
| 输出事实性复盘 | 完整、空计划、部分执行和不一致状态均返回字段清楚的事实总结 |
| 解释 Planning 解决什么 | 能说明从目标发现 how，并区分计划步骤与执行阶段事实 |
| 解释计划错了怎么办 | 能保存当前状态、保留不可重复动作、重写并只执行剩余计划 |
| 解释简单任务为何不规划 | 稳定、已知、可重复的 how 优先固定工作流，减少成本和不确定性 |
| 独立迁移 | 完成 `None` 级联故障、编排返回契约和酒店满房 Replanning 三个换表面检查 |

## 关键订正闭环

| 原始理解或错误 | 订正后的稳定结论 |
|---|---|
| 把 Python 值 `None` 说成字符串 `"None"` | 两者类型不同；`"None".strip()` 不会触发本事故 |
| 只修最后的 `.strip()` | 非法值必须在进入 results/history 前处理，否则后续 prompt 已被污染 |
| 把空计划外部返回 `None` 当成 history 污染 | 内部步骤结果和外部编排返回是不同契约 |
| 成功分支返回 `results[-1]` | 它是 `(step, result)` 元组；外层需要 `results[-1][1]` |
| prompts、return 和 stdout 混用 | 三者分别验证模型输入、调用方返回值和屏幕轨迹 |
| 只复述“不买票、不用酒店 A” | 约束必须落成可执行动作，并声明产出与后续数据依赖 |
| 提前写死酒店 B | 未执行出的事实不能进入后续计划；必须引用实际返回酒店 |

所有原始 `RETRY/PARTIAL` 均保留；最终通过可执行测试和换表面迁移形成 `RETRY → PASS`，没有倒改历史。

## 工程验证

- `python -m py_compile`：退出码 0。
- 真实脚本：3 步计划、3 个不同结果、完整执行复盘、最终答案全部输出。
- 聚焦内存断言：39/39。
- 关键故障：有效计划、`r1`、Python `None`、`r3`。
- 修复后结果：`[("s1", "r1"), ("s2", ""), ("s3", "r3")]`；第 3 步 prompt 无 `None`；复盘最终状态未完成。
- 正常编排：一次 Planner + 每个计划步骤一次 Executor；空计划只有一次 Planner 调用。
- `git diff --check`：退出码 0，无空白错误。

## 复习、场景与岗位边界

- `WP-08` 回炉通过，转入稳定错题间隔池，首轮回炉 2026-08-13。
- 新增 `WP-25`：内部步骤结果 vs 外部编排返回契约。
- 新增 `WP-26`：约束集合 vs 可执行剩余计划。
- 新增 `CD-005`：Plan-and-Solve 两阶段职责与执行上下文，首轮回炉 2026-08-13。
- WS-02 与 WS-05 形成复现、定位、修复和回归证据，达到 `DIAGNOSED_AND_FIXED`；A4-Gate 仍需补结构化日志、真实 provider 故障和安全停止。
- W4 算法继续 `DEBT`（0/4），不被课程 PASS 覆盖。
- 普通课程 PASS 不更新 `job-readiness.md`。

## 知识库同步

- 新增 [[../../02-Concepts/Agent/计划与求解(Plan-and-Solve)|计划与求解]]：两阶段职责、Executor 上下文、history 合同、静态/动态规划边界、事实复盘和 fake LLM 证据边界。
- 新增 [[../../04-Projects/Agent/AI-Agent-Learning/a4-04-plan-and-solve|A4-04 Plan-and-Solve 项目页]]：函数结构、可观察轨迹、`None` 事故与 39/39 正式验证。
- 更新 [[../../03-Courses/Agent/AI-Agent-Learning/stage4-agent-basics|阶段 4 课程页]]、课程/项目/概念索引、跳转索引、总地图和全局索引。
- [[../../02-Concepts/Agent/反思机制(Reflection)|反思机制]] 已准确覆盖 Reflection 与事实复盘边界，本次只补 Plan-and-Solve 反向链接，没有复制同义解释。

## 下一步

进入 A4-05 Reflection；另在独立算法时段逐题偿还 W4 的 4 道新题债务。
