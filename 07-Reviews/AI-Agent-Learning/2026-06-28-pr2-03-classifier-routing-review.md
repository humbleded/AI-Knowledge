---
type: review
topic: AI-Agent-Learning PR2-03
status: done
created: 2026-06-28
tags:
  - AI-Agent-Learning
  - PR2-03
  - 分类
  - 路由
  - PASS
  - 复盘
---

# 2026-06-28 PR2-03 分类与路由 PASS 复盘

## 判定

**PR2-03 → PASS**（通过标准「≥15 样例 + 错误分析」超额达成，含模型版真实对比）。

## 跑码核验

`code/stage2/pr2_03_classifier.py` 实跑（`PYTHONUTF8=1 .venv/Scripts/python.exe`）：

- **规则版** `run_tests`：15 条样例正确率 **73%**，4 错 = 3 漏判 + 1 撞类，错误**自动归因**（`all_hits` + `len(hits)`）输出正确。
- **模型版** `classify_llm` + `compare_hard_cases`：真实调用 DeepSeek 跑通；4 条规则版判错的难样例，规则版 0/4、**模型版 2/4**（救回「你好，今天聊什么？」撞类 + 「我们来闲聊一下」漏判）。
- 规则版纯代码确定可复现；模型版真实联网调用成功。

## 练习 15 题判定

全 PASS。两处经订正：

- **A2** 规则版/模型版对应「四种路由」：一度把「机械版」配给「基于 LLM 路由」（配反），澄清「机械版=不调模型纯代码=基于规则路由」后 RETRY→PASS。
- **D1** 邮件分类迁移：①标签带尾随空格 bug → ②订正时 strip 误用（`[list].strip()` 会崩）→ ③干净版，PARTIAL→RETRY→PASS。

读码/debug/写码/迁移/为什么/真实场景题全覆盖；B3「规则版列举不完」、D2 语义投诉错误分析有洞察。

## 两个错误理解 → 已纠正（最值钱）

1. **规则版到底调不调模型**：误以为「两个都调模型、规则版用 prompt 限制、模型版反而不控制」。
   - ✅ 正解：**规则版 = 纯代码零模型调用**（手写关键词 `if-else`）；模型版 = 调大模型且**更**需 prompt 约束（只有模型自由发挥才需要管）。
2. **`strip()` 误用**：当成「万能去空格咒语」到处贴，甚至 `[list].strip()`（`AttributeError` 崩）。
   - ✅ 正解：strip 是 **str 的方法**、只洗「运行时拿到、你控制不了的脏数据」；自写常量打错改字面量，不用 strip。

两者都属「概念/工具的边界没划清」，但均当场追问纠正、能复述正确版。

## 今天最虚 / 下次重点复习

- **最虚**：`strip()` 的作用对象（str vs list）与使用时机（脏数据 vs 自写常量）——D1 绕两圈才透。
- **下次写代码先问**：「这串是我手写的常量，还是运行时拿来的脏数据？」前者改字面量，后者才 strip。
- **同源弱点延续**：`LABEL=` 大小写写错致兜底失效、`s.strip()` 不赋值——都是「看起来做了、其实没改到目标」的假动作 bug，回头确认一眼改的是不是后面真正用的那个名字。

## 亮点

- 主体超额：规则版 + `all_hits` 诊断 + 自动归因 + 模型版 + 真实对比，远超「≥15 样例 + 错误分析」。
- 「规则 vs 模型」真实对比（0/4 → 2/4）是面试能直接讲的料：模型版更强但非银弹，边界靠 prompt 定义。
- `dict` 分发 `route` = ADP `RunnableBranch` 本质，已打通「分类→路由」。

## 沉淀

- 概念卡：[[../../02-Concepts/LLM/classification-and-routing|分类与路由]]、[[../../02-Concepts/Python/python-strip-and-cleaning-runtime-data|Python strip 与洗运行时脏数据]]
- 项目页：[[../../04-Projects/LLM/AI-Agent-Learning/pr2-03-classifier-routing|PR2-03 动手]]

## 下一步

队列：**S-03 上下文工程**（笔记 + 全量 vs 裁剪上下文小实验）→ **PR2-04 JSON/Schema** → **PR2-Gate 邮件处理器**（周末，把分类+摘要+JSON 串起来）。
PR2-03 模型版没做的「prompt 加每类标签定义」可在 PR2-Gate 一并优化。
