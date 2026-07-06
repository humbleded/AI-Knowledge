---
type: project
topic: LLM
status: done
created: 2026-07-05
source:
  - AI-Agent-Learning PR2-Gate
tags:
  - LLM
  - structured-output
  - JSON
  - prompt
  - AI-Agent-Learning
  - Stage2
---

# PR2-Gate 动手：邮件处理器（分类 + 摘要 + 待办 JSON）

> 阶段 2 收尾关，2026-07-05 PASS。概念见 [[../../../02-Concepts/LLM/结构化输出(Structured Output)]]、[[../../../02-Concepts/Python/文件读写与 JSON 序列化]]。

## 任务

输入一封邮件文本，输出：

- `category`：分类标签
- `points`：最多 3 条要点
- `summary`：摘要
- `todo`：待办 JSON（`sender/task/deadline/priority/need_reply`）

并保存到 `resources/stage2_email_result.json`。

## 核心实现

产物：`C:\Users\26823\Desktop\AI-Agent-Learning\code\stage2\pr2_gate_email_processor.py`

```python
def process_email(text):
    points, summary = simple_summarize(text)
    todo = extract_email(text)
    validate_payload(todo)
    category = classify(text)
    return {
        "category": category,
        "points": points,
        "summary": summary,
        "todo": todo,
    }
```

`process_email` 只负责整合旧模块，不复制旧函数：

- `simple_summarize` 来自 PR2-02。
- `classify` 来自 PR2-03。
- `extract_email` / `validate_payload` 来自 PR2-04。

`main()` 负责准备邮件文本、调用 `process_email`、`json.dump` 保存文件、`json.dumps` 打印结果。

## 实跑结果

运行：

```powershell
.\.venv\Scripts\python.exe .\code\stage2\pr2_gate_email_processor.py
```

输出文件：

```text
C:\Users\26823\Desktop\AI-Agent-Learning\resources\stage2_email_result.json
```

结果结构：

```json
{
  "category": "其他",
  "points": [
    "发件人：王五",
    "事项：确认本周项目周报",
    "截止时间：2026-07-06"
  ],
  "summary": "发件人：王五；事项：确认本周项目周报；截止时间：2026-07-06",
  "todo": {
    "sender": "王五",
    "task": "确认本周项目周报",
    "deadline": "2026-07-06",
    "priority": "中",
    "need_reply": "是"
  }
}
```

额外断言：

- 结果文件可被 `json.loads` 解析。
- `todo` 五字段齐全。
- 缺 `deadline` 会被 `validate_payload` 拦住，抛 `ValueError: 缺失字段: deadline`。
- `classify("我要投诉，你们怎么还不退款？")` 返回 `投诉`，因为撞类时 `RULES` 先命中投诉。

## 本次改动

`simple_summarize` 原本只按中文句号 `。` 切，邮件没有句号时只能得到 1 条 `points`。本次补强为：

```python
if "\n" in text.strip():
    parts = text.strip().split("\n")
else:
    parts = text.strip().split("。")
list_of_sentences = [s.strip() for s in parts if s.strip()]
points = list_of_sentences[:3]
```

这样同时兼容：

- 按行写的结构化邮件。
- 普通段落长文。

## 关键学习点

### 1. 先 dict，后 JSON

程序内部用 Python `dict` 处理字段，最后才用 `json.dump` 写文件。

不要手拼 JSON 字符串，也不要把模型返回的 JSON 字符串直接塞进最终结果：

```python
todo_dict = json.loads(model_json_string)
validate_payload(todo_dict)
json.dump(result, f, ensure_ascii=False, indent=2)
```

### 2. prompt 是软约束，代码是硬闸门

prompt 可以写“必须输出 JSON、字段缺失填 null、不许编造”，但模型仍可能漏字段、空 content、截断或输出坏 JSON。

代码里的 `validate_payload` 才是最终拦截坏数据的闸门。

### 3. 分类稳定性靠测试集

分类稳定性不能只靠 prompt 或感觉判断。要准备：

- 每个标签多条样例。
- 空文本、无关文本、多个关键词同时命中的边界样例。
- 预测标签 vs 期望标签。
- 错误归因：漏判、撞类、误命中。

## 踩的坑

- `json.dump` 误说成“打印给用户看” → 正确：写入文件；`json.dumps` 才是转字符串常配合 `print`。
- `extract_email` 返回 `dict`，不是 JSON 字符串；`validate_payload` 返回 JSON 字符串，但在 Gate 里主要借它做检查。
- 三引号文本缩进会变成真实空格，导致 `LABEL_MAP` 精确匹配失败。
- `{{...}}` 不是合法 JSON，也不是 Python `dict`；外面一层 `{}` 就够。
- 在 Gate 文件里重复定义 `simple_summarize` 会遮住导入函数；整合关应复用旧模块。

## 关联

- [[../../../02-Concepts/LLM/提示工程基础(Prompt Engineering)|Prompt 基础]]
- [[../../../02-Concepts/LLM/摘要与改写(Summarize & Transform)|摘要与改写]]
- [[../../../02-Concepts/LLM/分类与路由(Classification & Routing)|分类与路由]]
- [[../../../02-Concepts/LLM/结构化输出(Structured Output)|结构化输出]]
- [[../../../02-Concepts/Python/文件读写与 JSON 序列化|Python 文件读写与 JSON 序列化]]
- [[../../../07-Reviews/AI-Agent-Learning/2026-07-05-pr2-gate-email-processor-review|PR2-Gate PASS 复盘]]

## 来源

- AI-Agent-Learning：`daily/2026-07-05.md`
- AI-Agent-Learning：`code/stage2/pr2_gate_email_processor.py`
- AI-Agent-Learning：`notes/stage2/pr2_gate_email_processor_notes.md`

