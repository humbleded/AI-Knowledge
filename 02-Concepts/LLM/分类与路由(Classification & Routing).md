---
aliases:
  - classification-and-routing
type: concept
topic: LLM
status: usable
created: 2026-06-28
source:
  - AI-Agent-Learning PR2-03
  - Agentic Design Patterns 第 2 章 Routing
  - Datawhale llm-cookbook《面向开发者的提示工程》Inferring（推断）
tags:
  - LLM
  - prompt
  - classification
  - 分类
  - routing
  - 路由
  - Agent
---

# 分类与路由：Classification（给标签）与 Routing（按标签分流）

## 一句话解释

- **分类 Classification**：把一段输入归到**固定标签**之一（如「问题/投诉/建议/闲聊/其他」）。
- **路由 Routing**：**拿到标签后**，决定把流程导向哪个分支/工具/子流程。
- 🔑 **分类是路由的前半步**：先 `classify()` 出标签，再 `route()` 按标签 `if`/`dict` 分发。分类给「标签」，路由用标签决定「调哪个函数」。

> 口诀：**分类是「这是什么」，路由是「那该交给谁」。**

## 路由的四种实现（ADP 第 2 章）

| 实现 | 靠什么判断 | 调大模型吗 | 特点 |
|---|---|---|---|
| **基于规则** Rule-based | 关键词 / 正则 / 提取的结构化字段（`if-else`、`switch`） | ❌ 否 | 快、确定、可离线；但灵活性差 |
| **基于 LLM** LLM-based | 让模型读输入、输出标签 | ✅ 是 | 懂语义、灵活；但要钱、偶尔不稳 |
| **基于嵌入** Embedding-based | 输入向量与各路由向量的相似度 | （用 embedding 模型） | 语义路由，按含义而非关键词（见 [[嵌入(Embedding)]]） |
| **基于 ML 模型** | 专门微调的判别式分类器 | ❌（推理时不调生成模型） | 路由逻辑编码在微调权重里 |

> PR2-03 只动手前两种：**规则版（基于规则）** 与 **模型版（基于 LLM）**——正好对应 [[摘要与改写(Summarize & Transform)|PR2-02]] 的「机械版 vs 模型版」。后两种属阶段 6 RAG / 后续。

## 规则版 vs 模型版（一张表 + 真实数据）

| | 规则版（关键词 `if-else`） | 模型版（调 LLM） |
|---|---|---|
| **本质** | **纯代码、零模型调用** | 调大模型 + prompt 约束 |
| **判断依据** | 程序员手写的关键词 | 模型读语义 |
| **优点** | 快、免费、确定可复现、可离线 | 懂言外之意、不用穷举关键词 |
| **缺点** | 字面匹配、**关键词列不全**、撞类 | 要钱、偶尔不稳、边界靠 prompt |
| **适合** | 标签明确、特征硬、不常变 | 表达多样、边界模糊、规则列不完 |

🔑 **「规则版也调模型」是高频误区**——规则版**一次模型都不调**，它是 `if "退款" in text: return "投诉"` 这种纯 Python。「约束/控制输出」只存在于模型版（因为只有模型会自由发挥才需要管）。

### 实证：PR2-03 真跑（4 条规则版判错的难样例）

| 样例 | 期望 | 规则版 | 模型版 |
|---|---|---|---|
| 我有一些意见想反馈 | 建议 | 其他 ❌ | 其他 ❌ |
| 我们来闲聊一下 | 闲聊 | 其他 ❌ | 闲聊 ✅ |
| 遇到一个疑问，求解答 | 问题 | 其他 ❌ | 其他 ❌ |
| 你好，今天聊什么？ | 闲聊 | 问题 ❌ | 闲聊 ✅ |

🔑 **规则版 0/4 → 模型版 2/4**：模型版确实更强（救回撞类那条「你好，今天聊什么？」），**但不是银弹**——还错 2 条。两种错**性质不同**：规则版错在「字面没匹配上」（机械），模型版错在「语义边界判断」（需要更好的 prompt）。

## 两类分类错误：漏判 vs 撞类（能用代码自动归因）

| 错误 | 成因 | 信号 |
|---|---|---|
| **漏判** | 一个关键词都没命中 → 落兜底「其他」 | 命中 **0** 个类 |
| **撞类** | 命中**多个**类的关键词 → 被排在前面的类抢走 | 命中 **≥2** 个类 |
| **误命中** | 只命中 1 个类但配错了关键词 | 命中 1 个但 ≠ 期望 |

代码怎么自动区分？`classify()` 只返回**第一个**命中的，丢了「命中几个」的信息 → 加个**诊断函数** `all_hits()` 返回**所有**命中的类，再数 `len(hits)`：

```python
def all_hits(text):                       # classify 的「收集版」：不 return，收集全部命中
    hits = []
    for category, keywords in RULES.items():
        if any(kw in text for kw in keywords):
            hits.append(category)
    return hits

hits = all_hits(text)
if   len(hits) == 0: reason = "漏判"
elif len(hits) >= 2: reason = f"撞类（{hits} 被 {hits[0]} 抢走）"
else:                reason = "误命中（关键词配错）"
```

> 🔑 `classify` **做决策**（只要一个答案，命中即 `return`）；`all_hits` **做诊断**（要全部信息）。同一套 `RULES`，`classify` 返回的永远是 `all_hits()[0]`——所以 `label != hits[0]` 是死代码。

## 为什么标签必须固定、有限

下游路由长 `if label == "投诉": escalate()` ——**标签固定且有限，这些分支才写得全、匹配得上**。若让模型自由发挥，同一个意思今天回「投诉」、明天「客户不满」、后天「负面反馈」，`if label == "投诉"` 全部失败，**路由直接断掉**。固定标签还利于**统计/测试**（数 N 条对几条）和**逼模型收敛**（封闭选项比开放回答稳）。

## 模型版三件套（缺一不稳）

```python
label = call_model(prompt).strip()        # ① prompt 只输出标签词 ② strip 洗换行
if label not in LABELS:                    # ③ 白名单兜底
    label = "其他"
return label
```

1. **prompt 死命令「只输出一个标签词，前后不带别的字」**——否则模型回「这条属于投诉类。」，`== "投诉"` 失败（同 [[摘要与改写(Summarize & Transform)|锁 JSON]] 心法）。
2. **`.strip()`**：模型常返回 `"投诉\n"`，不洗则白名单/比较全失效（见 [[strip() 与数据清洗]]）。
3. **白名单兜底**：模型答了列表外的词（如「负面反馈」）→ 强制纠回「其他」。这是 **代码事后把关**，与 prompt 的**事前软请求**两层配合。

## 分类质量 = 标签定义在 prompt 里说得多清楚

PR2-03 模型版错的 2 条（「意见反馈」该归建议、「疑问求解答」该归问题），根因是 prompt **只点名标签、没定义每类含义**，模型只能猜。改进：给**每类一句话定义** + 覆盖边界的 few-shot：

```text
问题=咨询/求助/有疑问；投诉=不满/抱怨；建议=意见/希望改进；闲聊=寒暄无明确诉求
```

> 🔑 这是 PR2 的精髓：**分类质量取决于标签语义在 prompt 里的清晰度**，不是模型不行。

## 真实场景应用

- **客服分流**：消息 → `classify` 判类 → 投诉 `escalate()`（转人工）、问题 `answer()`（自动答疑）、闲聊 `chat()`。下游用 **`dict` 分发**最干净（加新类只改 dict、不动 route 逻辑，即 ADP 里 LangChain `RunnableBranch` / ADK 工具分发的本质）：
  ```python
  HANDLERS = {"问题": answer, "投诉": escalate, "建议": log_idea, "闲聊": chat, "其他": fallback}
  def route(text):
      return HANDLERS.get(classify(text), fallback)(text)   # 函数当值存进 dict + .get 兜底
  ```
- **邮件处理器（PR2-Gate）**：邮件按内容分类 → 路由到不同处理（呼应阶段 2 收尾关）。
- **实战常两者结合**：规则版快速兜「明显的」+ 模型版兜「模糊的」，省钱又灵活。

## 常见坑 / 错误理解 → 正确理解

- ❌ 以为「规则版也调模型、模型版反而不控制」→ ✅ **规则版=纯代码零模型调用**；模型版才调，且**更**需 prompt 约束。
- ❌ 标签定义时手抖带尾随空格 `"账单 "` → ✅ 下游 `== "账单"` 因 `"账单 " != "账单"` 失败；**标签首尾永不留空格**（见 [[strip() 与数据清洗]]）。
- ❌ 模型版 prompt 混入「先概要、再判断」→ ✅ 和「只输出标签词」自相矛盾；**任务要纯**。
- ❌ 以为模型版万能 → ✅ 边界模糊的照样错，**靠 prompt 里写清标签定义**才救得回。
- ❌ 错误分析只报告「分错了 X→Y」→ ✅ 要写**为什么**（漏判/撞类），用 `all_hits` + `len` 自动归因。

## 关联

- [[摘要与改写(Summarize & Transform)|摘要与改写]]：同 PR2 系列，「机械版 vs 模型版」「锁格式只输出目标、别夹带人话」一脉相承。
- [[提示工程基础(Prompt Engineering)|Prompt 基础]]：分类 prompt 同样靠角色 + 清晰指令 + few-shot；few-shot 给边界例子才有价值。
- [[strip() 与数据清洗|Python strip 与洗运行时脏数据]]：模型版 `.strip()` 洗 `"投诉\n"` 的依据。
- [[list·dict·set 容器|Python list、dict、set]]：`RULES` 字典、`HANDLERS` 函数分发。
- [[消息角色与指令优先级(Instruction Hierarchy)|消息角色与指令优先级]]：分类指令放 `system`、待分类文本放 `user`。

## 来源

- AI-Agent-Learning PR2-03：产物 `code/stage2/pr2_03_classifier.py`（规则版 + `all_hits` + 15 样例 + 自动归因 + 模型版 + 真实对比）；练习 `daily/2026-06-28.md`（15 题全 PASS）。
- 资料：Agentic Design Patterns 第 2 章 Routing（`repos/agentic-design-patterns/bilingual/Chapter 2_ Routing.md`）；DeepLearning.AI《Prompt Engineering for Developers》Inferring 节。
