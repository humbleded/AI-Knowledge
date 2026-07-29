---
type: project
topic: AI-Agent-Learning A4-04 Plan-and-Solve
status: pass
created: 2026-07-30
updated: 2026-07-30
source:
  - C:\Users\26823\Desktop\AI-Agent-Learning\code\stage4\a4_04_plan_solve_demo.py
  - C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-07-22.md
  - C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-07-23.md
  - C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-07-24.md
  - C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-07-25.md
  - C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-07-29.md
  - C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-07-30.md
tags:
  - Agent
  - Planning
  - Python
  - AI-Agent-Learning
---

# A4-04 Plan-and-Solve

## 目标与产物

- 产物：`C:\Users\26823\Desktop\AI-Agent-Learning\code\stage4\a4_04_plan_solve_demo.py`
- 目标：实现“生成计划 → 逐步执行 → 事实性复盘 → 返回最终结果”的最小静态 Plan-and-Solve 闭环。
- 正式结果：**PASS（2026-07-30）**。

## 代码结构

| 部分 | 作用 |
|---|---|
| `parse_plan()` | 用 `ast.literal_eval()` 安全解析 Python 代码围栏中的字符串列表 |
| `create_plan()` | 构造 Planner prompt，只拆步骤，不提前回答原问题 |
| `execute_plan()` | 按顺序执行，并把 `(step, result)` 写入 results/history |
| `build_recap()` | 区分空计划、完整执行和部分执行，输出事实性复盘 |
| `run_plan_and_solve()` | 串联计划、逐步输出、复盘与外部返回值 |
| `demo_llm()` | 提供无需网络、结果可重复的本地演示 |

## 可观察轨迹

演示目标是计算周一到周三的平均温度：

```text
生成的计划：
  1. 计算周一的平均温度
  2. 计算周二的平均温度
  3. 计算周三的平均温度

步骤结果：
  20°C -> 21°C -> 22°C

复盘：
  计划规模 3 步
  已完成 3 步
  无异常
  最终状态完成

最终答案：
  22°C
```

## 关键接口契约

```python
LLMCall = Callable[[str], str]
StepResult = tuple[str, str]
```

- Planner 每次只调用一次 `llm_call`，有效文本返回 `list[str]`，无效格式返回 `[]`。
- Executor 每个计划步骤调用一次模型；每轮 prompt 包含原始问题、完整计划、历史结果和当前步骤。
- history 保存 `(step, result)`，不能只保存孤立结果。
- 空计划只调用 Planner，仍打印正式复盘并返回 `None`。
- 成功编排返回最后一个元组中的结果字符串，不返回整个 `StepResult`。

## `None` 级联故障与修复

故障注入依次返回：

```python
["r1", None, "r3"]
```

旧轨迹：

```text
第二步 None
  -> 写入 results/history
  -> 第三步 prompt 出现 ('s2', None)
  -> build_recap 调用 None.strip()
  -> AttributeError
```

最终修复位于最早的状态写入边界：

```python
result = llm_call(context)
if result is None:
    result = ""

results.append((step, result))
history.append((step, result))
```

修复后第三步仍能执行，但收到的是满足字符串契约的空失败结果；复盘不会崩溃，并明确给出最终状态未完成。

## 正式验证

- `py_compile`：退出码 0。
- 真实脚本直接运行：计划、3 步结果、完整复盘与最终答案全部输出。
- 聚焦内存断言：39/39。
- 覆盖解析、Planner、Executor/history、`None` 故障、空/完整/部分复盘、结果不一致、空计划和成功编排、返回类型与确定性重复运行。
- `git diff --check`：退出码 0，无空白错误。
- 没有为一次正式检查新增持久 runner；命令与决定性结果保存在执行区 `daily/2026-07-30.md`。

## 订正闭环

1. 缺少代码围栏时，链式 `split()[1]` 会触发 `IndexError`；最终进入统一的 `[]` 失败路径。
2. Planner prompt 曾只说“生成结构化计划”；最终明确“只拆解步骤，不直接回答”。
3. Executor history 曾只保存结果，丢失步骤来源；最终统一为 `StepResult`。
4. 复盘字段曾把最终结果、异常说明和最终状态串位；最终按结构状态分支生成。
5. 编排函数曾返回 recap、results 列表或完整元组；最终按 `str | None` 返回最后结果。
6. 正式迁移中曾把内部 history 契约和外部函数返回混为一谈；最终能分别验证 prompts、return 与 stdout。

## 能力边界

- 当前代码是静态 Plan-and-Solve，没有实现动态 replanner。
- F3 的 Replanning 伪代码证明概念迁移，不代表当前产物已具备该功能。
- `demo_llm` 证明客户端路径，不证明真实 DeepSeek 的规划质量和格式可靠性。
- A4-04 是课程产物，不单独升级岗位证据；动态恢复、日志、模型韧性和安全仍要在 A4-Gate/后续工程任务继续验证。
- W4 算法仍为 `DEBT`（0/4）。

## 相关链接

- [[../../../02-Concepts/Agent/计划与求解(Plan-and-Solve)|计划与求解]]
- [[../../../02-Concepts/Agent/反思机制(Reflection)|反思机制]]
- [[../../../03-Courses/Agent/AI-Agent-Learning/stage4-agent-basics|阶段 4：Agent 基础原理]]
- [[../../../07-Reviews/AI-Agent-Learning/2026-07-30-a4-04-plan-and-solve-review|A4-04 PASS 复盘]]
