---
type: concept
topic: LLM
status: usable
created: 2026-06-30
source:
  - AI-Agent-Learning PR2-04
  - OpenAI Structured Outputs 官方文档
  - DeepSeek JSON Output 官方文档
tags:
  - LLM
  - structured-output
  - json-mode
  - schema
  - json_object
  - DeepSeek
---

# 结构化输出（Structured Outputs）：让模型吐出程序能吃的 JSON

## 一句话解释

结构化输出 ＝ 让模型的输出**不是一段话，而是字段固定、类型固定、能 `json.loads()` 解析、缺信息不乱编的 JSON**——把「模型」接到「下游程序」的关键一环。是 [[prompt-engineering-basics|prompt 工程]]「锁 JSON」的系统化。

## 两档强度：JSON 模式 vs 严格 Schema

| 档 | 名字 | 保证什么 | 不保证什么 |
|---|---|---|---|
| 弱档 | **JSON 模式**（`json_object`） | 输出是**合法 JSON** | 字段对不对（可能缺 / 多 / 类型错 / 值乱编） |
| 强档 | **严格 Schema**（`json_schema` + `strict`） | 还保证：字段齐 / 类型对 / 不许多余字段 / 枚举不乱编 / 拒答可检测 | —— |

> 原文：**only Structured Outputs ensure schema adherence**（只有严格 Schema 保证贴合结构；JSON 模式只保证是合法 JSON）。

## schema 锁的 4 件事

1. **必填字段（required）**
2. **字段类型（types）**
3. **不许多余字段（`additionalProperties: false`）**
4. **枚举值（enum）**——只能从固定集合选，防乱编（如 priority 只能 `高/中/低`）

> enum 在严格模式下是**硬约束**（约束解码 constrained decoding：生成时把非法 token 概率**归零**，物理上选不到「特急」）——不是「提高概率」。对比：**enum / top-k ＝ 硬归零；temperature ＝ 软压低（仍 >0）**。见 [[sampling-params-and-cost]]。

## 处理异常输出：查 3 处

1. `finish_reason == "length"` → 被 `max_tokens` **截断**（JSON 没写完）
2. `message.refusal` → **拒答**
3. `message.content` → 正常，拿去 `json.loads`

## DeepSeek 落地（只有弱档 json_object）

开关 `response_format={'type': 'json_object'}`。三条硬要求：
1. prompt 里必须出现 `"json"` 这个词
2. prompt 里给一段 JSON 格式样例（**双引号**！单引号不是合法 JSON）
3. 设 `max_tokens` 防截断

坑：偶尔返回**空 content** → `loads` 前 `if not content` 兜底。

> DeepSeek 没有严格 Schema 档 → 用「**prompt 写清 schema（点名字段 + 双引号样例 + 枚举 + 缺失 null）+ Python 端 `validate` 校验**」两头夹，凑出强档效果。

## 🔑 最大的坑：`response_format=json_object` ≠ 返回 dict

`response.choices[0].message.content` **永远是字符串**。`json_object` 只保证「这个字符串的内容是合法 JSON」，**仍要 `json.loads(content)` 才得到 dict**。直接把 content 当 dict 用，下游 `key in payload` 会变成查子串、行为全错。

## 实证：PR2-04 邮件抽取（真跑 DeepSeek）

规则版 `extract_email`（`partition` 解析「标签：值」）vs 模型版 `extract_email_llm`（`json_object` + schema prompt）：

| 输入 | 规则版 | 模型版 |
|---|---|---|
| 结构化邮件（有「标签：」）| ✅ | ✅ |
| 自由文本「张三说下周五前交报告、比较急、记得回复」| ❌ 抽不到 | ✅ 语义抽出（"比较急"→priority 高、"记得回复"→need_reply 是）|
| 缺优先级邮件 | —— | ✅ `priority: null`（**不编造**）|

🔑 模型版价值：**读懂语义再结构化**，规则版对自由文本（没有「标签：」）一个字段都抽不到。

## 常见坑 / 错误理解 → 正确理解

- ❌ 开了 `json_object` 拿到的就是 dict → ✅ content 永远是 **str**，仍需 `json.loads`。
- ❌ prompt 里 JSON 样例用**单引号** → ✅ 必须**双引号**，单引号 `json.loads` 抛 `JSONDecodeError`（模型会照样例学）。
- ⚠️ 真调模型**不可复现**：同一封缺字段邮件两次跑出「**截断**（Unterminated string）」和「**空 content**（None）」两种失败 → `except` + `if not content` 兜住不崩（兜底价值实锤）。
- ⚠️ `str.split("：", 1)` 遇无冒号行解包崩 → 用 `str.partition("：")`（总返回 3 段、不崩）。
- ⚠️ 函数体缩进 **4 / 8 空格混用** → `IndentationError: unexpected indent`。

## 关联

- [[prompt-engineering-basics]]：schema 靠 prompt 写清（点名字段 + 样例 + 锁 JSON）。
- [[classification-and-routing]]：同为「规则版 vs 模型版」；模型版懂语义、规则版认字面。
- [[summarizing-and-transforming]]：都靠 prompt 锁 JSON + 代码兜底。
- [[context-engineering]]：真调模型不可复现、兜底必要性同源。
- [[sampling-params-and-cost]]：enum 硬归零 vs temperature 软压低；真实计费看 `usage`。

## 来源

- AI-Agent-Learning PR2-04：产物 `code/stage2/pr2_04_extract_json.py`；预读 `notes/stage2/pr2_04_structured_output_preview.md`；带做与坑 `daily/2026-06-30.md`。
- OpenAI《Structured Outputs》、DeepSeek《JSON Output》官方文档（2026-06-30 抓取）。
