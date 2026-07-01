---
type: concept
topic: Python string methods
status: usable
created: 2026-06-28
source:
  - AI-Agent-Learning PR2-03
tags:
  - Python
  - string
  - strip
  - 数据清洗
  - AI-Agent-Learning
aliases:
  - python-strip-and-cleaning-runtime-data
  - Python strip 使用时机
  - strip 洗脏数据
---

# Python `strip()`：作用对象与「何时该用」

## 一句话

`strip()` 去掉**字符串首尾**的空白（空格、`\n`、`\t` 等）。但今天真正要记的不是「怎么用」，而是 **「何时用」与「对谁用」**：

> 🔑 **`strip()` 只用来洗「运行时才拿到、你控制不了的脏数据」；你自己手写的常量打错了，改字面量本身，不该用 strip。**

## 基础行为

```python
"  投诉\n".strip()    # "投诉"   去首尾空白/换行
"a b".strip()         # "a b"    只去【首尾】，不动中间
"投诉".strip()         # "投诉"   本来就干净，strip 是空操作（多余）
```

- 字符串**不可变**：`strip()` **返回新字符串**，不改原值。`s.strip()` 单独一行不赋值 = 白做，要 `s = s.strip()`。

## ⚠️ 作用对象：只能用于字符串，对 list 会**直接崩**

```python
"账单 ".strip()                 # ✅ str 有 strip
["工作", "账单"].strip()        # ❌ AttributeError: 'list' object has no attribute 'strip'
```

🔑 **`strip()` 是 str 的方法，list/dict 等没有**。想「给整个列表去空格」是误区——要逐个元素处理：`[x.strip() for x in lst]`。把 `.strip()` 贴到 list 上，程序**起都起不来**。

## 决策表：何时该 strip，何时不该

| 数据来源 | 你能控制吗 | 怎么办 |
|---|---|---|
| **自己手写的常量**（标签、关键词字面量） | ✅ 能 | **改字面量本身**，删掉空格，**不用 strip** |
| 模型返回 `call_model(...)` | ❌ 不能 | `.strip()` 洗（常带 `"投诉\n"`） |
| 用户输入 `input()` | ❌ 不能 | `.strip()` 洗（首尾空格） |
| 文件 / 配置读出来的行 | ❌ 不能 | `.strip()` 洗（常带 `\n`） |

> 判断口诀：写代码时问一句——**「这串是我手写的常量，还是运行时拿来的脏数据？」** 前者改字面量，后者才 strip。

## 配合白名单兜底（治不同的病）

洗完还不够稳。模型版分类里两层一起上：

```python
label = call_model(prompt).strip()    # strip 治「格式脏」(投诉\n)
if label not in LABELS:               # 白名单治「答了列表外的词」(负面反馈)
    label = "其他"
```

- `strip` 解决「值对但首尾有脏字符」；白名单解决「值本身不在允许集合」。两者**不能互相替代**。

## 常见坑 / 错误理解 → 正确理解（PR2-03 实录）

- ❌ 把 `strip()` 当「万能去空格咒语」到处贴，甚至 `[list].strip()` → ✅ 它**只是 str 的方法**，对 list 会 `AttributeError` 崩。
- ❌ 给**自己手写的干净常量** `"工作".strip()` 贴 strip → ✅ 多余；常量打错就**改字面量**。
- ❌ 定义标签时手抖带尾随空格 `"账单 "` 再想用 strip 补救 → ✅ 源头删空格即可，下游 `== "账单"` 才不会因 `"账单 " != "账单"` 失败。
- ❌ 以为 `s.strip()` 会就地修改 `s` → ✅ 字符串不可变，strip **返回新值**，要 `s = s.strip()` 才生效（同类隐患：「看起来做了，其实没改到目标变量」——和 `LABEL=` 大小写写错、兜底没生效是同一种「假动作」bug）。

## 关联

- [[分类与路由(Classification & Routing)|分类与路由]]：模型版三件套之一，洗 `call_model` 返回。
- [[and-or 短路求值|Python and/or 短路]]：`delta.content or ""`、`x or 默认值` 是另一种「洗运行时脏值（None/空）」的手法。
- [[流式输出(Streaming)|流式输出]]：`delta.content or ""` 兜 None 与 strip 洗脏同属「对模型返回做防御」。
- [[基础数据类型(Data Types)|Python 基础数据类型]]：str 不可变、方法返回新对象。

## 来源

- AI-Agent-Learning PR2-03：`code/stage2/pr2_03_classifier.py` 模型版 `classify_llm`；练习与动手过程 `daily/2026-06-28.md`（D1 标签空格 → strip 误用 → 干净版，绕两圈才彻底踩透）。
