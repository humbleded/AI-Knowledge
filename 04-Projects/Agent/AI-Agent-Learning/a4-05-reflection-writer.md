---
type: project
topic: AI-Agent-Learning A4-05 Reflection Writer
status: pass
created: 2026-08-04
updated: 2026-08-04
source:
  - C:\Users\26823\Desktop\AI-Agent-Learning\code\stage4\a4_05_reflection_writer.py
  - C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-07-23.md
  - C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-07-30.md
  - C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-08-03.md
  - C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-08-04.md
tags:
  - Agent
  - Reflection
  - Python
  - DeepSeek
  - AI-Agent-Learning
---

# A4-05 Reflection Writer

## 目标与产物

- 产物：`C:\Users\26823\Desktop\AI-Agent-Learning\code\stage4\a4_05_reflection_writer.py`
- 目标：实现“生成初稿 → 反思反馈 → 可选改进 → 同标准比较 → 选择最终稿”的最小单轮 Reflection 闭环。
- 正式结果：**PASS（2026-08-04）**。

公告任务要求包含固定日期 `2026年8月8日`、固定地点 `3号会议室`，去除首尾空白后不超过 80 个字符，并明确邀请同事参加。

## 代码结构

| 部分 | 作用 |
|---|---|
| `evaluate_draft()` | 确定性检查日期、地点、长度及总硬约束 |
| `build_initial_prompt()` | 携带原始任务，只要求输出初稿正文 |
| `build_reflection_prompt()` | 携带任务、待评审稿和硬检查；规定评审标准与反馈协议 |
| `build_refinement_prompt()` | 携带任务、上一版与反馈，只输出修订正文 |
| `run_reflection_once()` | 至多执行一轮 Reflection，记录轨迹、调用次数和停止原因 |
| `select_best_draft()` | 用同一个评估器检查候选，接受或回退初稿 |
| `run_reflection_writer()` | 整合生成轨迹与最终选择，返回 11 个审计字段 |
| `create_deepseek_llm_call()` | 创建真实 DeepSeek `str -> str` 适配器 |

## 两条真实运行路径

### 正常提前停止

```text
真实初稿（长度 39，日期/地点/长度均通过）
  -> 真实 Reflection：无需改进
  -> refined_draft = None
  -> model_call_count = 2
  -> stop_reason = no_improvement
  -> final_draft = initial_draft
```

### 受控坏初稿后的真实修复

验证包装器只把第一次 `llm_call` 替换为：

```text
公司将于本周五举办AI Agent学习分享会，诚邀同事参加，具体地点另行通知。
```

该稿缺少固定日期和固定地点。后续两次调用仍委托真实 DeepSeek：

```text
受控坏初稿
  -> 真实 Reflection 指出缺日期/地点
  -> 真实 Refinement 生成长度 41 的候选稿
  -> 候选日期/地点/长度全部通过
  -> accepted_refinement = True
  -> decision_reason = accepted_hard_constraints_pass
```

生产条件 `if feedback == "无需改进"` 没有修改；正常路径再次运行仍然只调用 2 次。

## 选择与审计合同

完整返回值包含：

```text
initial_draft
initial_checks
feedback
refined_draft
refined_checks
final_draft
accepted_refinement
decision_reason
trajectory
model_call_count
stop_reason
```

候选稿即使失败也保留在 `refined_draft` 和 `trajectory` 中，方便审计；`final_draft` 单独表示系统认可的版本。模型反馈不能替代 `evaluate_draft()`，不合格候选必须回退。

## 正式验证

- `py_compile`：退出码 0。
- 确定性内存断言：39/39。
- 覆盖 80/81 字边界、三类 prompt、精确停止、非精确停止文本、候选接受/回退/留痕、十一字段整合、fake SDK 请求契约和 `main()` 输出。
- 真实正常路径：2 次 DeepSeek 调用，提前停止。
- 真实故障分支：首稿为明确标注的夹具，Reflection/Refinement 为 2 次真实 DeepSeek 调用，12/12 断言通过。
- `git diff --check`：退出码 0；敏感字面量与未完成骨架扫描通过。
- 没有为一次正式检查新增持久 runner、原始日志或时间戳报告。

## 关键订正闭环

1. Reflection prompt 的注释列出了标准，但实际文本没有传给模型；最终把日期、地点、长度、清晰度和行动指引写入真实 prompt。
2. DeepSeek 适配器曾使用错误模型和顶层 `thinking=False`；最终使用固定 `deepseek-v4-pro` 与 `extra_body={"thinking": {"type": "disabled"}}`。
3. 一度把模型“无需改进”或三个硬检查当成总体质量证明；最终明确硬检查只证明已编码维度。
4. 为覆盖改进分支，最初尝试用 prompt 诱导模型写错，但模型仍生成合格稿；最终只在验证边界注入确定性坏初稿。
5. 故障路径明确区分夹具与真实 API 输出，不把“后两步真实”冒充“整条路径均真实生成”。

## 能力边界

- `evaluate_draft()` 只确定性检查日期、地点和长度；行动指引、事实质量和表达质量仍需要额外 evaluator、领域测试或人工确认。
- 当前只执行至多一轮 Reflection，没有多轮收敛策略、token/延迟预算控制或完整 tracing。
- 当前只验证坏文本输出恢复；429、Retry-After、fallback 与 context 超限留到 A4-Gate/BE5。
- 这是课程产物，不单独升级岗位证据；W4 算法仍为 `DEBT`（0/4）。

## 相关链接

- [[../../../02-Concepts/Agent/反思机制(Reflection)|反思机制]]
- [[../../../02-Concepts/Agent/计划与求解(Plan-and-Solve)|计划与求解]]
- [[../../../03-Courses/Agent/AI-Agent-Learning/stage4-agent-basics|阶段 4：Agent 基础原理]]
- [[../../../07-Reviews/AI-Agent-Learning/2026-08-04-a4-05-reflection-review|A4-05 PASS 复盘]]
