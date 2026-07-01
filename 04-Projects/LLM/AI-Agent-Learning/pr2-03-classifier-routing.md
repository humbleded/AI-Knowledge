---
type: project
topic: LLM
status: done
created: 2026-06-28
source:
  - AI-Agent-Learning PR2-03
tags:
  - LLM
  - prompt
  - classification
  - 分类
  - routing
  - AI-Agent-Learning
  - Stage2
---

# PR2-03 动手：分类与路由（规则版 + 模型版 + 真实对比）

> 阶段 2 第三个动手交付，2026-06-28 PASS。概念见 [[../../../02-Concepts/LLM/分类与路由(Classification & Routing)]]。
> 本页记录**动手代码与真跑结果**。

## 任务

把客服消息分到固定标签「问题/投诉/建议/闲聊/其他」，≥15 条测试样例 + 错误分析。产物 `code/stage2/pr2_03_classifier.py`。

## 实现（5 块，超出通过标准）

1. **`RULES`**：`dict` 标签→关键词列表（投诉/建议/问题/闲聊，「其他」是兜底无关键词）。
2. **`classify(text)`** 规则版：遍历 `RULES`，`any(kw in text)` 命中即 `return`，全不中 `return "其他"`。
3. **`all_hits(text)`** 诊断：`classify` 的「收集版」，返回**所有**命中类，用于区分漏判/撞类。
4. **`run_tests()`**：15 条 `(文本, 期望)` 成对样例（含 4 条故意刺头）→ 逐条判对错 → 错误**自动归因**（`len(hits)==0` 漏判 / `>=2` 撞类 / 否则误命中）→ 统计正确率。
5. **`classify_llm(text)`** 模型版：`call_model` + prompt 只输出标签词 + `.strip()` + 白名单兜底 + `compare_hard_cases()` 对比。

## 真跑结果

**规则版** `run_tests`：15 条正确率 **73%**，4 错 = **3 漏判 + 1 撞类**：

| 样例 | 预测 | 期望 | 自动归因 |
|---|---|---|---|
| 我有一些意见想反馈 | 其他 | 建议 | 漏判（"意见/反馈"不在 RULES） |
| 我们来闲聊一下 | 其他 | 闲聊 | 漏判（"闲聊"不在 RULES["闲聊"]） |
| 遇到一个疑问，求解答 | 其他 | 问题 | 漏判（无"怎么/如何/？"） |
| 你好，今天聊什么？ | 问题 | 闲聊 | 撞类（命中 ['问题','闲聊']，问题排前抢走） |

**模型版** `compare_hard_cases`（真实调用 DeepSeek，4 条难样例）：

| 样例 | 期望 | 规则版 | 模型版 |
|---|---|---|---|
| 我有一些意见想反馈 | 建议 | 其他 ❌ | 其他 ❌ |
| 我们来闲聊一下 | 闲聊 | 其他 ❌ | 闲聊 ✅ |
| 遇到一个疑问，求解答 | 问题 | 其他 ❌ | 其他 ❌ |
| 你好，今天聊什么？ | 闲聊 | 问题 ❌ | 闲聊 ✅ |

🔑 **规则版 0/4 → 模型版 2/4**：模型版救回撞类那条（懂"你好…"是闲聊），但边界模糊的（"意见反馈"/"疑问求解答"）也错——因为 prompt 只点名标签、没定义每类含义。**分类质量 = 标签定义在 prompt 里的清晰度。**

## 踩的坑（动手过程，绕两圈才透）

1. **规则版 vs 模型版一度搞反**：以为「两个都调模型、规则版用 prompt 限制」→ 纠正：**规则版=纯代码零模型调用**，模型版才调且更需约束。
2. **`strip()` 误用**（最值钱）：把 strip 当万能去空格贴到 `[list].strip()` → `AttributeError` 崩；还给自写常量 `"工作".strip()` 贴。纠正：strip 只洗运行时脏数据，自写常量改字面量。详见 [[../../../02-Concepts/Python/strip() 与数据清洗]]。
3. **标签定义带尾随空格** `"账单 "` → 下游 `==` 失败（自己跑不报错、接下游才炸）。
4. **`LABEL=`（大写）兜底没生效**：写了白名单但赋值到空气变量，`label`（小写）没改——「看起来做了，其实没做到目标上」。
5. **单引号跨多行 → SyntaxError**：多行 prompt 用三引号 `"""`。
6. **死代码** `if label != hits[0]`：`classify` 返回的永远是 `all_hits()[0]`，恒不成立。

## 运行

```text
PYTHONUTF8=1 .venv/Scripts/python.exe code/stage2/pr2_03_classifier.py
```

（规则版纯本地；模型版 `compare_hard_cases` 需外网调用 DeepSeek，读系统环境变量 `DEEPSEEK_API_KEY`。）

## 关联

- [[../../../02-Concepts/LLM/分类与路由(Classification & Routing)|分类与路由（概念卡）]]
- [[../../../02-Concepts/Python/strip() 与数据清洗|Python strip 与洗运行时脏数据]]
- [[pr2-01-02-handson|PR2-01/02 动手]]
- [[../../../07-Reviews/AI-Agent-Learning/2026-06-28-pr2-03-classifier-routing-review|本次 PASS 复盘]]

## 来源

- AI-Agent-Learning PR2-03 动手；`daily/2026-06-28.md`（15 题全 PASS + 动手补完记录）。
