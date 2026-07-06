---
type: review
topic: AI-Agent-Learning PR2-Gate
status: done
created: 2026-07-06
tags:
  - AI-Agent-Learning
  - PR2-Gate
  - structured-output
  - JSON
  - PASS
  - 复盘
---

# 2026-07-06 PR2-Gate 邮件处理器 PASS 复盘

## 判定

**PR2-Gate → PASS**。

通过标准达成：

- 完成 `code/stage2/pr2_gate_email_processor.py`。
- 输入邮件文本后，输出分类、摘要、待办 JSON。
- 保存到 `resources/stage2_email_result.json`。
- 三个必答题均能回答：JSON 可解析、分类稳定性、哪些场景不能只靠 prompt。

## 跑码核验

运行：

```powershell
.\.venv\Scripts\python.exe .\code\stage2\pr2_gate_email_processor.py
```

验证结果：

- 成功输出 `category/points/summary/todo`。
- `resources/stage2_email_result.json` 可被 `json.loads` 解析。
- `todo` 五字段齐全：`sender/task/deadline/priority/need_reply`。
- `points` 为 3 条。
- 缺 `deadline` 时，`validate_payload` 抛 `ValueError: 缺失字段: deadline`。
- `classify("我要投诉，你们怎么还不退款？")` 返回 `投诉`，符合 RULES 顺序。
- `simple_summarize` 对按行邮件和普通长文都能取 3 条要点。

## 今日练习判定

14 题全部闭环：

- A 快速回忆 4 题
- B 解释比较 3 题
- C 代码/操作 3 题
- D 应用迁移 4 题

判定分布：

- 直接 PASS：10 题
- 订正后 PASS：4 题（A1、C2、C3、D2）

## 三个必答问题

### 1. 如何保证 JSON 可解析？

最终答案达标：

- 不手拼 JSON 字符串。
- 先组装 Python `dict`。
- 用 `validate_payload(todo)` 检查字段齐全和可序列化。
- 用 `json.dump(result, f, ensure_ascii=False, indent=2)` 让标准库写合法 JSON。
- 抽取坏结果时 raise，不继续保存坏文件。

### 2. 如何测试分类稳定性？

最终答案达标：

- 每个固定标签准备多条样例，覆盖包含/不包含关键词。
- 准备空文本、无关文本、多个关键词同时命中的撞类样例。
- 准备相似语义、不同说法的样例。
- 逐条记录预测标签和期望标签，统计正确率。
- 分析错误类型：漏判、撞类、误命中。

### 3. 哪些场景不能只靠 prompt 解决？

最终答案达标：

- 模型输出可能不是标准 JSON，需要代码解析和校验。
- 模型可能漏字段、编造字段，需要 `validate_payload` 或类似 schema 校验。
- 分类稳定性不能靠一句 prompt 保证，要靠测试样例和错误分析。

## 主要订正点

### A1：`dict` / `json.dumps` / `json.dump`

第一轮把 `json.dump` 说成“打印给用户看”。

订正：

- `dict`：Python 内部数据结构。
- `json.dumps`：把 Python 对象转成 JSON 字符串，常配合 `print`。
- `json.dump`：把 Python 对象写入 JSON 文件。

### C2：三引号缩进 vs 摘要切分

第一轮把“三引号前导空格导致字段匹配失败”和“按句号切不出多条 points”混在一起。

订正：

- 三引号里的前导空格是真实字符，会让 key 变成 `"    事项"`，`LABEL_MAP` 精确匹配失败。
- 按句号切不出多条 points 是 `simple_summarize` 的另一个问题。

### C3：漏看点名子项

第一轮只写了判断切分方式，漏了过滤空行、取 3 条、拼摘要、return。

订正后补全：

```python
if "\n" in text.strip():
    parts = text.strip().split("\n")
else:
    parts = text.strip().split("。")

list_of_sentences = [s.strip() for s in parts if s.strip()]
points = list_of_sentences[:3]
summary = "；".join(points)
return points, summary
```

### D2：模型 JSON 字符串不能直接塞进结果

第一轮只说要 `validate_payload(todo)`，漏了 `json.loads`。

订正：

```python
todo_dict = json.loads(todo)
validate_payload(todo_dict)
```

`json.loads` 负责把合法 JSON 字符串解析成 Python dict；`validate_payload` 负责字段齐全和可序列化。

## 今天最虚 / 下次重点复习

**JSON 字符串、Python dict、文件 JSON 三层边界**还需要继续巩固。

重点链路：

```python
todo_dict = json.loads(model_json_string)
validate_payload(todo_dict)
json.dump(result, f, ensure_ascii=False, indent=2)
```

同时继续回炉 **WP-01 漏看点名子项**：写代码题先把题目要求逐条勾掉，别只完成第一半。

## 错题本更新

- WP-01：C3 重现漏点名子项，打回 🔴。
- WP-04：规则版 vs 模型版分类，复测通过，进入 ✅ 回炉池。
- WP-12：代码兜底 ≠ 约束模型，复测通过，进入 ✅ 回炉池。
- WP-14：模型自编 Observation 代码实景识别，复测通过，🔴 降为 🟡。
- WP-15：JSONDecodeError vs TypeError，复测通过，进入 ✅ 回炉池。
- 新增 WP-16：JSON 字符串 / Python dict / 文件 JSON 三层边界。

## 沉淀

- 概念卡：[[../../02-Concepts/LLM/结构化输出(Structured Output)|结构化输出]]
- 概念卡：[[../../02-Concepts/Python/文件读写与 JSON 序列化|Python 文件读写与 JSON 序列化]]
- 项目页：[[../../04-Projects/LLM/AI-Agent-Learning/pr2-gate-email-processor|PR2-Gate 邮件处理器]]

## 下一步

阶段 2 已收尾。下一步进入：

```text
T3-02 计算器工具
```

重点从“让模型输出结构化 JSON”转向“让模型选择工具参数，由程序真实执行工具”。

