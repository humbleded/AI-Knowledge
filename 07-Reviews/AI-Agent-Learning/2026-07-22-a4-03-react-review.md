---
type: review
topic: AI-Agent-Learning A4-03
status: pass
created: 2026-07-22
updated: 2026-07-22
tags:
  - AI-Agent-Learning
  - Agent
  - ReAct
  - PASS
---

# 2026-07-22 A4-03 ReAct PASS 复盘

## 判定

**A4-03 PASS**。

提交的 ReAct demo 能直接运行并展示完整两轮轨迹；正式复核的 15 项内存断言全部通过。学习证据共 10 个合格检查点，覆盖 Thought / Action / Observation 职责、停止条件、防无限循环、工具定义/分发、prompt/history、解析器调试、Tool Use 边界及确定性 demo 的证据边界。

## PASS 标准与决定性证据

| PASS 标准 | 决定性证据 |
|---|---|
| 跑通或改写 ReAct 代码 | `code/stage4/a4_03_react_agent.py` 退出码 0 |
| 展示完整执行轨迹 | 第 1 轮 Weather → Observation；第 2 轮读取历史并返回非空 Finish |
| 有最大步数 | `max_steps=2` 的连续 Weather 和空 Finish 场景均恰好调用 LLM 2 次后返回 `None` |
| 解释三个槽位 | 能分清 LLM 生成 Action、客户端执行/回填、工具返回真实结果、下一轮 LLM 读取 |
| 解释何时停止 | 能区分目标完成后的成功停止与解析失败/步数耗尽等安全停止 |
| 独立迁移 | 在新 `Reasoning/Decision` 字段上无提示写出完整 regex、flags、精确元组和原因 |

## 关键订正闭环

| 原始理解或错误 | 订正后的稳定结论 |
|---|---|
| Thought 把 Observation 写回 history | 客户端写回；下一轮 LLM 读取 |
| `get_weather` 就是外部天气 API | 它是本地工具函数，内部可以再调用外部 API |
| 正常停止就代表任务质量足够 | 控制流停止与目标是否真正满足要分开判断 |
| `Finish[]` 可以直接收口 | 只有非空 Finish 才进入最终返回分支 |
| Prompt 写了格式就足够 | Prompt 是软请求，客户端 parser/validator 是硬边界 |
| `(.*?)` 写成 `(.\**?)` | `*?` 必须修饰前面的 `.`；转义后会变成字面星号 |
| fake LLM 证明真实模型可靠 | 只证明固定响应下的客户端代码路径可运行 |

原 F2 与首次独立复测的 `RETRY` 均保留；后续新字段名无提示迁移构成新的独立 PASS，因此当前掌握链路记为 `RETRY → PASS`。

## 工程验证

- 直接运行真实文件：完整两轮轨迹，退出码 0。
- 聚焦断言：15/15。
- 关键故障再注入：正文内 Action、缩进 Action、缺失/坏 Action、空 Finish、未知工具、连续 Weather。
- `git diff --check`：通过。
- 未持久化一次性测试 runner；命令与决定性结果保存在 `daily/2026-07-22.md`。

## 复习、场景与岗位边界

- 新增 `CD-004`：ReAct 成功停止与安全停止，首轮回炉 2026-08-05。
- 新增稳定错题 `WP-24`：正则量词/转义与精确 Python 字符串，首轮回炉 2026-08-05。
- `WP-12` 到期复测通过，进入 `+1月` 档，下次 2026-08-21。
- WS-03 本次新增可执行回归证据，但不升级既有更强等级；A4-03 不要求复合事故。
- W4 算法仍为 `DEBT`（0/4），继续结转到 W5 独立时段。
- 普通课程 PASS 不更新 `job-readiness.md`；Agent 控制循环仍需 A4-Gate 和后续工程化产物形成岗位证据。

## 知识库同步

- 新增 [[../../02-Concepts/Agent/ReAct推理与行动循环(ReAct)|ReAct 推理与行动循环]]：职责链、成功/安全停止、max_steps、硬校验和 fake LLM 证据边界。
- 新增 [[../../04-Projects/Agent/AI-Agent-Learning/a4-03-react-agent|A4-03 ReAct Agent 项目页]]：实现结构、轨迹、正式验证与缺陷闭环。
- 更新 [[../../03-Courses/Agent/AI-Agent-Learning/stage4-agent-basics|阶段 4 课程页]] 与相关索引；下一项切换为 A4-04 Plan-and-Solve。
- [[../../02-Concepts/Agent/智能体(Agent)|智能体]]、[[../../02-Concepts/Agent/工具定义与执行协议(Tool Definition)|工具定义与执行协议]] 已准确覆盖通用职责边界，保留原内容，只补 ReAct 关联入口。

## 下一步

进入 A4-04 Plan-and-Solve；另在独立算法时段补 W4 的 4 道新题债务。
