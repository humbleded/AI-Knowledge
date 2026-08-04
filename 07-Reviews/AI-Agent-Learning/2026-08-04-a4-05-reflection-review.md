---
type: review
topic: AI-Agent-Learning A4-05
status: pass
created: 2026-08-04
updated: 2026-08-04
tags:
  - AI-Agent-Learning
  - Agent
  - Reflection
  - PASS
---

# 2026-08-04 A4-05 Reflection PASS 复盘

## 判定

**A4-05 PASS**。

真实产物可以执行“初稿 → Reflection → 可选 Refinement → 同标准比较 → 最终选择”。39 项确定性断言、真实 2 调用提前停止和受控坏初稿后的真实修正路径均通过；10 个任务级语义证据覆盖全部必答问题与换场景迁移。

## PASS 标准与决定性证据

| PASS 标准 | 决定性证据 |
|---|---|
| 有初稿 | 正常主程序由真实 DeepSeek 生成长度 39 的全约束公告 |
| 有反思 | 正常路径返回“无需改进”；故障路径逐项指出缺日期、地点和行动指引 |
| 有改进稿 | 受控坏初稿后，真实 Refinement 生成长度 41 的合格候选稿 |
| 有对比 | 初稿和候选稿使用同一 `evaluate_draft()`；失败回退，合格候选才接受 |
| 适用场景 | 能根据风险、实时性、评价标准和改进价值判断是否值得加入 Reflection |
| 成本 | 能从额外模型调用与串行依赖解释 API/计算成本和总延迟 |
| 防止越改越差 | 能区分 prompt 软评审、客户端硬门槛和未编码语义质量的外部证据 |
| 迁移 | 能设计只注入首稿、后两步真实调用的故障验证，并如实声明证据边界 |

## 关键订正闭环

| 原始理解或错误 | 订正后的稳定结论 |
|---|---|
| Reflection 输入漏掉原始任务 | `Task` 必须进入 Reflection 与 Refinement，作为评审和保留约束的共同基准 |
| 把 `add_record()` 当完整历史读取 | 写入用 `add_record()`；完整历史用 `get_trajectory()`；最近执行稿用 `get_last_execution()` |
| prompt 注释写了标准就算传给模型 | 只有实际 prompt 文本会进入上下文，标准和输出协议都必须出现在返回字符串中 |
| 漏掉停止前已经写入的反馈 | 轨迹按真实执行顺序记录；第二轮“无需改进”先写入再停止 |
| 更快但只过 4/5 测试的候选可当最佳稿 | 硬约束回退时保留唯一 5/5 的旧稿，失败候选只留审计证据 |
| 当前检查器会拒绝缺行动指引的候选 | 当前代码只查日期、地点、长度；候选可能通过但语义质量退化 |
| Reflection prompt 只规定输出格式 | 它还规定评审标准和反馈协议，但模型仍可能不遵守，因此只是软约束 |
| 改停止条件来强制覆盖 Refinement | 在验证边界注入确定性坏初稿，生产停止语义保持不变 |

## 工程验证

- `.venv\Scripts\python.exe -m py_compile code/stage4/a4_05_reflection_writer.py`：退出码 0。
- 聚焦内存断言：39/39。
- 真实正常路径：初稿三项硬约束通过，Reflection 为“无需改进”，2 次调用后 `no_improvement`。
- 真实故障路径：注入首稿缺日期/地点，后 2 次为真实 DeepSeek；12/12 断言通过，候选稿三项硬约束通过并被接受。
- fake SDK 请求契约：用户订正前 12/15，订正后 15/15；正式复核再次覆盖固定模型、单条 user message、非流式、thinking 关闭和 `None → ""`。
- `git diff --check` 与敏感字面量扫描通过。

## 复习、场景与岗位边界

- 到期 `CD-003` 首答未独立闭合，因此从核心定义间隔池移除并合并回活跃 `WP-12`；不生成新的到期日期。
- `WS-03` 维持 `DIAGNOSED_AND_FIXED`，新增请求契约与 39/39 回归证据。
- `WS-05` 在“模型首稿缺硬约束”子场景达到 `RECOVERED_UNDER_FAULT`；429/fallback 仍待后续任务。
- W4 算法继续 `DEBT`（0/4），下一合适计划安排一个 30～45 分钟回收位。
- 普通课程 PASS 不更新 `job-readiness.md`。

## 知识库同步

- 扩写 [[../../02-Concepts/Agent/反思机制(Reflection)|反思机制]]：新增三阶段数据依赖、停止轨迹、成本、质量回退、软/硬证据分层与故障注入边界。
- 新增 [[../../04-Projects/Agent/AI-Agent-Learning/a4-05-reflection-writer|A4-05 Reflection Writer 项目页]]。
- 更新阶段 4 课程页、课程/项目/概念索引、跳转索引、全局索引和维护日志。
- 未新增同义 Reflection 概念卡；总地图已经存在正确入口，本次保持不变。
- 严格知识库检查：Markdown 202、链接 1728、断链 0、缺 frontmatter 0。

## 下一步

先在一个独立 30～45 分钟时段推进 W4 算法欠账中的 1 题；下一主任务进入 A4-Gate problem contract 与最小 Agent 闯关。
