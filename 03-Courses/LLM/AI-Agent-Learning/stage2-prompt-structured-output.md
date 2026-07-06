---
type: course-note
topic: AI-Agent-Learning Stage 2
status: active
created: 2026-06-25
updated: 2026-07-06
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
- Hello-Agents 第 3 章 3.2.1 提示工程（PR2-01 主资料）；第 9 章 上下文工程（S-03 主资料）。
- OpenAI Structured Outputs / DeepSeek JSON Output 官方文档（PR2-04 主资料）。

## 当前进度

| 编号 | 任务 | 状态 | 产物 | 关键结论 |
|---|---|---|---|---|
| PR2-01 | Prompt 基础 | **PASS** (2026-06-27) | [[../../../02-Concepts/LLM/提示工程基础(Prompt Engineering)]] | 概念+笔记+练习(17 题全 PASS)；四技巧各控一维、指令调优 vs few-shot、技巧≠role、锁 JSON 三件套。**动手完成**：3 个递进 prompt 真跑 DeepSeek（`pr2_01_prompt_cases.md`）——② 清晰具体可 loads、③ few-shot 与 ② 零增益，坐实「prompt 不是越长越好」；坑 f-string 撞 JSON 花括号 |
| PR2-02 | 摘要与改写 | **PASS** (2026-06-27) | [[../../../02-Concepts/LLM/摘要与改写(Summarize & Transform)]] | 概念+笔记+练习(15 题全 PASS)；摘要 vs 改写、控长度软约束、概括 vs 提取、判断漏重点、转换四类。**动手完成** `pr2_02_summarizer.py`：机械版 vs 模型版对比，模型版锁 JSON 正好 3 条、≤20/≤60 字稳定；澄清「代码兜底=事后硬保证 ≠ 约束模型」 |
| PR2-03 | 分类与路由 | **PASS** (2026-06-28) | [[../../../02-Concepts/LLM/分类与路由(Classification & Routing)]] | 概念+练习(15 题全 PASS)+**动手** `pr2_03_classifier.py`：规则版(dict 遍历)+`all_hits` 诊断+15 样例+自动归因(漏判/撞类)+模型版(只输出标签词+strip+白名单)。真跑规则版 73%、4 难样例规则版 0/4→模型版 2/4。分类是路由前半步、规则版 vs 模型版、分类质量=标签定义清晰度 |
| S-03 | 上下文工程（补充项） | **PASS** (2026-06-29) | [[../../../02-Concepts/LLM/上下文工程(Context Engineering)]] | 带读 HA 第9章(9.1~9.2.3/9.7)+练习 15 题全 PASS+**动手** `s03_context_experiment.py` token 对比真跑通(① 100 > ③ 50 > ② 25，程序验证 ②丢名字/③保名字)。context rot/注意力预算/最小≠最短、五手段分层、`trim_history`=truncation 属上下文工程非提示工程、与 Compaction 平级 |
| PR2-04 | JSON 与 Schema | **PASS** (2026-06-30) | [[../../../02-Concepts/LLM/结构化输出(Structured Output)]] | 带做全链路(预读→规则版→模型版→边界验证)+真跑 `pr2_04_extract_json.py`：规则版 `partition` 解析「标签：值」/ 模型版 `json_object`+schema prompt+`validate`。自由文本语义抽出(「比较急」→priority 高)、规则版抽不到；缺优先级→`priority:null` 不编造。🔑 `json_object`≠dict(仍需 `json.loads`)；真调不可复现(截断/空 content)靠 `except`+`if not content` 兜底 |
| PR2-Gate | 结构化输出闯关 | **PASS** (2026-07-06) | [[../../../04-Projects/LLM/AI-Agent-Learning/pr2-gate-email-processor]] | **阶段 2 收尾**：邮件 → 分类 + 摘要 + 待办 JSON 并保存文件。实跑输出可解析 JSON；`todo` 五字段齐全；缺字段由 `validate_payload` 拦截；补强 `simple_summarize` 兼容按行邮件和普通长文。三问与 14 题练习闭环 |

> 阶段 2 的两个概念预习（PR2-01/02）安排在工作日做；它们的**动手产物**与 PR2-03 起的动手任务，统一排在 **L1-Gate（阶段 1 收尾关）之后**，因为 Gate 要整块周末时间。S-03 上下文工程是挂在「阶段 2 后 / 4 前」的补充项，工作日概念/阅读型穿插完成。PR2-04 预读当天带做完成动手交付。

## 已掌握概念

- [[../../../02-Concepts/LLM/提示工程基础(Prompt Engineering)|Prompt 基础：zero/few-shot、角色扮演、上下文示例、CoT]]
- [[../../../02-Concepts/LLM/摘要与改写(Summarize & Transform)|摘要与改写：Summarizing vs Transforming]]
- [[../../../02-Concepts/LLM/分类与路由(Classification & Routing)|分类与路由：Classification vs Routing]]
- [[../../../02-Concepts/LLM/上下文工程(Context Engineering)|上下文工程：策划进窗口的整组 token]]
- [[../../../02-Concepts/LLM/结构化输出(Structured Output)|结构化输出：让模型吐出程序能吃的 JSON]]

## 下一步

**PR2-Gate 已 PASS（2026-07-06）**。阶段 2 概念、动手任务和收尾关全部完成；下一步进入阶段 3 动手：**T3-02 计算器工具**。

```text
[已过] PR2-01 动手 -> [已过] PR2-02 summarizer -> [已过] PR2-03 分类与路由 -> [已过] S-03 上下文工程 -> [已过] PR2-04 JSON/Schema -> [已过] PR2-Gate 邮件处理器 -> T3-02 计算器工具
```

PR2-Gate「邮件处理器」已经把阶段 2 技巧串起来：摘要、分类、结构化抽取、`dict`/JSON 序列化、`validate` 校验和文件保存。核心复盘见 [[../../../07-Reviews/AI-Agent-Learning/2026-07-06-pr2-gate-email-processor-review|2026-07-06 PR2-Gate PASS 复盘]]。

## 阶段 1 到阶段 2 的衔接

阶段 1 解决「**怎么调模型**」（`call_model` 封装、多轮、流式、参数与成本）；阶段 2 解决「**怎么让模型稳定产出**」（prompt 设计 + 结构化输出）。两者的成本意识一脉相承：阶段 1 的 [[../../../02-Concepts/LLM/采样参数与成本(Sampling)|token 计费]] 直接解释了阶段 2「prompt 长 ≠ 好」「摘要历史省 token」；S-03 [[../../../02-Concepts/LLM/上下文工程(Context Engineering)|上下文工程]] 进一步把它系统化为「会进窗口的整组 token 是有限资源」；PR2-04 [[../../../02-Concepts/LLM/结构化输出(Structured Output)|结构化输出]] 把「让模型稳定产出」推到「产出程序能直接吃的 JSON」。

## 阶段 2 到阶段 3 的衔接

阶段 2 练的是“模型输出能被程序吃”：固定标签、JSON 字段、代码校验。阶段 3 会进一步变成“模型输出工具调用请求，程序真实执行工具”：模型只负责选择工具名和参数，客户端程序负责解析、执行和把 Observation 拼回上下文。也就是说，PR2-Gate 的 `json.loads` / `validate_payload` / `dict` 组装能力，会直接迁移到 T3 的工具调用分发器。
