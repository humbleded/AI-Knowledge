---
type: project
topic: G8-00 Incident Change Review Agent v1
status: pass
created: 2026-09-05
updated: 2026-09-05
source:
  - C:\Users\26823\Desktop\AI-Agent-Learning\code\stage8\incident_change_review_agent\incident_graph.py
  - C:\Users\26823\Desktop\AI-Agent-Learning\code\stage8\incident_change_review_agent\test_incident_graph.py
  - C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-09-03.md
  - C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-09-04.md
  - C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-09-05.md
tags:
  - AI/Agent
  - AI-Agent-Learning
  - LangGraph
  - StateGraph
  - Project
  - PASS
---

# G8-00 故障诊断与变更评审 Agent v1

## 项目结果

这是一个用 LangGraph 显式表达“整理事实 → 审查证据 → 执行一次获批只读诊断 → 再审查 → 构造结论或稳定停止”的最小工作流。

2026-09-05 正式判定：`G8-00 = PASS`。

## 运行图

```text
START
  → organize_facts
  → review_evidence
      ├─ tool_failed ─────────────→ tool_failure_stop ───────→ END
      ├─ step_count >= max_steps ─→ max_steps_stop ─────────→ END
      ├─ insufficient ────────────→ evidence_insufficient_stop → END
      ├─ enough ──────────────────→ build_conclusion ────────→ END
      └─ unknown ─────────────────→ run_readonly_diagnostic
                                      └────────→ review_evidence
```

编译图共有 7 个业务 Node；连同 `START / END` 是 9 个图节点、12 条边。`route_after_review` 是条件路由函数，不是业务 Node。

## State 与 Node

`IncidentState` 有 15 个字段，分为：

- 输入事实：service、alerts、logs、config_changes；
- 过程状态：facts_summary、evidence、evidence_status、requested_tool；
- 控制状态：tool_failed、tool_error、step_count、max_steps、stop_reason；
- 输出：conclusion。

`evidence` 使用 `Annotated[list[str], add]`。诊断 Node 只返回本次新证据，不复制旧 evidence；Graph 负责累积。

业务 Node：

1. `organize_facts`：整理脱敏事实；
2. `review_evidence`：判断证据状态并按有限规则选择工具；
3. `run_readonly_diagnostic`：执行一个获批工具、校验 `list[str]`、归一化失败并增加业务步数；
4. `build_conclusion`：通过可注入生成函数构造结论；
5. 三个停止 Node：分别写入稳定 stop reason。

## 工具与安全边界

批准表只有：

```text
get_recent_errors
get_latency_summary
```

职责分层：

```text
review_evidence
→ 决定当前业务需要哪个工具

APPROVED_READONLY_TOOLS
→ 判断名字是否获批，并映射到真实函数

run_readonly_diagnostic
→ 执行、校验、归一化失败、写回局部 State
```

未批准工具返回 `unapproved_tool`，不会执行任何批准工具；timeout 或非法返回统一成 `diagnostic_unavailable`。工具失败在路由中优先于步数和证据状态，避免模型或后续业务继续推进。

## F1：批准不等于可达

修改前，`review_evidence` 只要 alerts 或 logs 任一非空，就固定请求 recent errors。于是 alerts-only 场景虽然批准了 latency 工具，却永远到不了它：

```text
recent=2
latency=0
model=0
stop_reason=max_steps_reached
```

用户独立定位根因，并提出四个互斥分支：

```text
已有 evidence       → enough / 不请求工具
alerts、logs 都为空 → insufficient / 不请求工具
有 logs             → unknown / get_recent_errors
只有 alerts         → unknown / get_latency_summary
```

助手按用户方案机械落盘并补 maintained regression。修复后：

```text
alerts-only → recent 0 / latency 1 / model 1
logs-only   → recent 1 / latency 0 / model 1
```

这次演进还证明：测试预期要从输入和产品规则推出，不能因为当前错误实现稳定返回 `max_steps_reached` 就把错误行为写进预期。

## `invoke` 与 `stream`

- `invoke_incident()` 返回整次执行完成后的最终 State；
- `stream_incident_updates()` 使用 `stream_mode="updates", version="v2"`，把每个业务 Node 的局部更新逐 part 交给调用方；
- START、END 和纯路由函数没有自己的 State update；
- 每次调用 `stream()` 都是新运行，不是对前一次 `invoke()` 的回放。

正常 stream 的 Node 顺序：

```text
organize_facts
→ review_evidence
→ run_readonly_diagnostic
→ review_evidence
→ build_conclusion
```

## 正式验证

```powershell
.venv\Scripts\python.exe -m py_compile code/stage8/incident_change_review_agent/incident_graph.py code/stage8/incident_change_review_agent/test_incident_graph.py
.venv\Scripts\python.exe -m pytest -q code/stage8/incident_change_review_agent/test_incident_graph.py
.venv\Scripts\python.exe -m pip check
```

```text
PY_COMPILE_PASS
12 passed in 0.74s
No broken requirements found.
```

12 个测试覆盖 normal、惰性 updates、两种信号工具选择、证据不足、工具 timeout/非法结果、零步数和未批准工具。

一次历史真实 DeepSeek Node 链结果：

```text
REAL_DEEPSEEK status=PASS
model=deepseek-v4-pro
timeout_seconds=60.0
sdk_max_retries=0
conclusion_char_count=934
requested_sections_present=True
input_state_unchanged=True
```

真实调用证明 Provider Node 可用；Graph 的 route/loop/stream/stop 由可重复的离线整图测试证明。

## 证据归属

- 用户独立：G1～G11、F1 的语义回答和订正；I1～I8b 的生产实现；F1 四分支设计。
- 助手实现：I9 具体 pytest、F1-C 新增测试、F1 方案的机械落盘。
- 助手整理：A4 手写循环 ↔ Graph 映射表和正式执行报告。

所以测试文件是有效项目产物，但不证明用户已经独立掌握 pytest 工程化；该能力仍留给 BE5-01。

## 当前指纹与 Git 边界

| 文件 | 大小 | SHA256 |
| --- | ---: | --- |
| `incident_graph.py` | 24781 bytes | `1E3F950551B5841462457DEA4346EA84A55B6A73675C442FA5F42E22C50F102A` |
| `test_incident_graph.py` | 20118 bytes | `0698BF3A05E182D2B1B6738862F76ADA0FF90B87D2A5583A913D2B341C72DBC1` |
| `requirements.txt` | 68 bytes | `7E20F5167C5BED9AD2FBFD5D3EAACA8736ACCC79A580AE50B63561DA249FC985` |

正式核验时，执行区基线为 `HEAD = 0db733f8bef176e4ea93a4f94b04fad253f22a82`，stage8 目录尚未被 Git 跟踪；这是上表初次核验的历史边界。提交前只清理了源码中的过期验收说明和行尾空格，没有改变程序行为，并重新通过 `py_compile`、`pytest 12/12` 与 `pip check`。最终项目产物和学习台账已由提交 [`0fe4332`](https://github.com/humbleded/AI-Agent-Learning/commit/0fe4332) 推送到 `main`，上表指纹已更新为该提交完成后的本地文件版本。

## v1 明确不证明什么

- 无 checkpointer / thread 隔离；
- 无进程重启恢复；
- 无 interrupt/resume 或 HITL；
- 无 replay 幂等副作用；
- 无 FastAPI/SSE、认证、部署、CI、负载和产品观测；
- 无单 Agent / 多 Agent 收益对照。

工作场景 `WS-11` 因此只升级当前无持久化切片到 `EXECUTED`，不能写成 `DIAGNOSED_AND_FIXED` 或 `RECOVERED_UNDER_FAULT`；项目仍只是课程证据，不是 `JOB_EVIDENCE`。

## 相关链接

- [[../../../02-Concepts/Agent/LangGraph 状态图编排(StateGraph)|LangGraph 状态图编排]]
- [[../../../03-Courses/Agent/AI-Agent-Learning/stage4_5-langgraph-basics|阶段 4.5：LangGraph 基础工作流]]
- [[../../../07-Reviews/AI-Agent-Learning/2026-09-05-g8-00-langgraph-v1-review|G8-00 正式 PASS 复盘]]
