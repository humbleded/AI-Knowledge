---
type: course-note
topic: AI-Agent-Learning Stage 2
status: active
created: 2026-06-25
updated: 2026-06-28
tags:
  - LLM
  - prompt
  - 结构化输出
  - AI-Agent-Learning
  - Stage2
---

# 阶段 2：Prompt 与结构化输出

## 阶段目标

能**设计稳定 prompt**，让模型输出**摘要、分类、JSON**。重点从「会调模型」（阶段 1）转向「让模型**稳定、可控、结构化**地产出」——这是后续工具调用、Agent、RAG 都依赖的底座。

## 主资料

- Datawhale **llm-cookbook**《面向开发者的提示工程》（DeepLearning.AI 官方中文版）：第 2 章 提示原则、第 3 章 迭代优化、第 4 章 文本概括、第 6 章 文本转换。
- DeepLearning.AI《Prompt Engineering for Developers》Guidelines（两原则：写清晰具体指令 / 给模型思考时间）。
- Hello-Agents 第 3 章 3.2.1 提示工程（PR2-01 主资料）。

## 当前进度

| 编号 | 任务 | 状态 | 产物 | 关键结论 |
|---|---|---|---|---|
| PR2-01 | Prompt 基础 | **PASS** (2026-06-27) | [[../../../02-Concepts/LLM/prompt-engineering-basics]] | 概念+笔记+练习(17 题全 PASS)；四技巧各控一维、指令调优 vs few-shot、技巧≠role、锁 JSON 三件套。**动手完成**：3 个递进 prompt 真跑 DeepSeek（`pr2_01_prompt_cases.md`）——② 清晰具体可 loads、③ few-shot 与 ② 零增益，坐实「prompt 不是越长越好」；坑 f-string 撞 JSON 花括号 |
| PR2-02 | 摘要与改写 | **PASS** (2026-06-27) | [[../../../02-Concepts/LLM/summarizing-and-transforming]] | 概念+笔记+练习(15 题全 PASS)；摘要 vs 改写、控长度软约束、概括 vs 提取、判断漏重点、转换四类。**动手完成** `pr2_02_summarizer.py`：机械版 vs 模型版对比，模型版锁 JSON 正好 3 条、≤20/≤60 字稳定；澄清「代码兜底=事后硬保证 ≠ 约束模型」 |
| PR2-03 | 分类与路由 | **PASS** (2026-06-28) | [[../../../02-Concepts/LLM/classification-and-routing]] | 概念+练习(15 题全 PASS)+**动手** `pr2_03_classifier.py`：规则版(dict 遍历)+`all_hits` 诊断+15 样例+自动归因(漏判/撞类)+模型版(只输出标签词+strip+白名单)。真跑规则版 73%、4 难样例规则版 0/4→模型版 2/4。分类是路由前半步、规则版 vs 模型版、分类质量=标签定义清晰度 |
| PR2-04 | JSON 与 Schema | TODO | — | 资料：OpenAI Structured Outputs |
| PR2-Gate | 结构化输出闯关 | TODO | `code/stage2/pr2_gate_email_processor.py` | 邮件 → 分类 + 摘要 + 待办 JSON 并存文件（周末做） |

> 阶段 2 的两个概念预习（PR2-01/02）安排在工作日做；它们的**动手产物**与 PR2-03 起的动手任务，统一排在 **L1-Gate（阶段 1 收尾关）之后**，因为 Gate 要整块周末时间。

## 已掌握概念

- [[../../../02-Concepts/LLM/prompt-engineering-basics|Prompt 基础：zero/few-shot、角色扮演、上下文示例、CoT]]
- [[../../../02-Concepts/LLM/summarizing-and-transforming|摘要与改写：Summarizing vs Transforming]]
- [[../../../02-Concepts/LLM/classification-and-routing|分类与路由：Classification vs Routing]]

## 下一步

**PR2-03 分类与路由已 PASS（2026-06-28）**。队列里下一个是 **S-03 上下文工程**（笔记 + 全量 vs 裁剪上下文小实验），再到 PR2-04 JSON/Schema：

```text
[已过] PR2-01 动手 -> [已过] PR2-02 summarizer -> [已过] PR2-03 分类与路由 -> S-03 上下文工程 -> PR2-04 JSON/Schema -> PR2-Gate 邮件处理器
```

PR2-Gate「邮件处理器」会把阶段 2 全部技巧串起来（角色 + 清晰指令 + few-shot + 摘要 + 分类 + 锁 JSON）——本阶段所有概念都为它铺路。PR2-03 模型版没做的「prompt 加每类标签定义」可在 PR2-Gate 一并优化。

## 阶段 1 到阶段 2 的衔接

阶段 1 解决「**怎么调模型**」（`call_model` 封装、多轮、流式、参数与成本）；阶段 2 解决「**怎么让模型稳定产出**」（prompt 设计 + 结构化输出）。两者的成本意识一脉相承：阶段 1 的 [[../../../02-Concepts/LLM/sampling-params-and-cost|token 计费]] 直接解释了阶段 2「prompt 长 ≠ 好」「摘要历史省 token」。
