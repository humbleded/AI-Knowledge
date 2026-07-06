---
aliases:
  - python-file-json-serialization
type: concept
topic: Python file IO JSON serialization
status: usable
created: 2026-06-13
updated: 2026-07-06
tags:
  - Python
  - 文件读写
  - JSON
  - 序列化
---

# Python 文件读写与 JSON 序列化

## 核心结论

文件读写解决“数据如何落到磁盘上”，JSON 序列化解决“Python 数据结构如何变成可保存、可交换的文本格式”。

- 文本文件适合保存给人阅读的普通文字、日志、逐行任务清单。
- JSON 适合保存结构化数据，例如 `list`、`dict`、字符串、数字、布尔值和 `null`。
- Python 读写中文文件时应显式写 `encoding="utf-8"`，避免换机器、换终端或换系统后出现乱码或 `UnicodeDecodeError`。

## 文本文件和 JSON 的边界

文本文件偏“人读”：

```text
学习文件读写
学习 JSON
练习异常处理
```

JSON 偏“程序读”和“结构化交换”：

```json
[
  {
    "name": "学习文件读写",
    "status": "todo"
  }
]
```

如果只需要一行一条记录，文本文件很轻量；如果每条记录还要带状态、分数、日期、标签，就应该用 JSON 或数据库。

## `json.dumps()` 与 `json.loads()`

`json.dumps()` 把 Python 数据变成 JSON 字符串：

```python
json_text = json.dumps(data, ensure_ascii=False, indent=2)
```

`json.loads()` 把 JSON 字符串变回 Python 数据：

```python
data = json.loads(json_text)
```

常见方向：

- `dict` / `list` -> JSON 字符串：`json.dumps()`
- JSON 字符串 -> `dict` / `list`：`json.loads()`
- Python 数据 -> JSON 文件：`json.dump(data, file)`
- JSON 文件 -> Python 数据：`json.load(file)`

记忆口诀：**`dump` 是存（写出去）、`load` 是读（读回来）**；带 `s` 的 `dumps`/`loads` 对**字符串**，不带 `s` 的 `dump`/`load` 配**文件对象**。

## 三层边界：dict、JSON 字符串、JSON 文件

PR2-Gate 暴露出一个高频混淆点：**Python `dict`、JSON 字符串、JSON 文件不是一回事**。

| 层 | 形态 | 常用 API | 用途 |
|---|---|---|---|
| Python 内部数据 | `dict` / `list` | 直接用 key/index 访问 | 程序内部处理，例如 `result["todo"]["deadline"]` |
| JSON 字符串 | `str` | `json.dumps` / `json.loads` | 在内存里把 Python 对象和 JSON 文本互转 |
| JSON 文件 | `.json` 文件 | `json.dump` / `json.load` | 保存到磁盘或从磁盘读回 |

稳定链路：

```python
# 模型或外部系统给的是 JSON 字符串
todo_dict = json.loads(model_json_string)

# 程序内部用 dict 做校验和组装
validate_payload(todo_dict)
result = {"todo": todo_dict}

# 最后写成文件 JSON
with open(path, "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)
```

常见错误：

```python
result = {"todo": model_json_string}
```

这样 `todo` 会变成字符串字段，而不是可继续取 key 的 dict；外层文件也许是合法 JSON，但结构不是下游程序想要的。

## 序列化会改变类型：tuple 读回变 list

JSON 的类型系统比 Python 小：**它没有 `tuple`**。把 tuple 存进 JSON 会被写成数组，读回来变成 `list`——类型在「存盘 → 读回」后悄悄变了。

```python
import json

msgs = [("user", "你好"), ("assistant", "你好呀")]   # 每条是 tuple
back = json.loads(json.dumps(msgs))

print(back == msgs)        # False！tuple 已变成 list
print(type(back[0]))       # <class 'list'>
```

- `back == msgs` 是 `False`，因为 `["user","你好"]`（list）≠ `("user","你好")`（tuple）。
- 启示：**别依赖「存盘读回后还是原来的类型」**；需要严格类型/不可变时，JSON 序列化不是可靠手段。
- 反过来，用 `dict` / `list` 存（如多轮对话的 `history = [{"role":..,"content":..}, ...]`）就没这个坑——dict 读回还是 dict、list 还是 list，`for m in history`、`m["role"]` 照常用。

> 辨析：tuple「不可变」指不能改 tuple **内部**的元素，**不是**不能往外层 `list` 里 `append`。所以「用 tuple 存就没法加历史」是误解——能加，只是存盘读回会丢类型。

## 为什么要写 `ensure_ascii=False`

`json.dumps()` 默认会把中文转成 `\uXXXX` 形式。这样程序仍能读，但人看起来不直观。

写中文 JSON 时常用：

```python
json.dumps(data, ensure_ascii=False, indent=2)
```

这样输出文件能直接看到中文，例如 `"学习 JSON"`。

## 路径错误怎么排查

遇到 `FileNotFoundError` 或路径不对，按这个顺序排查：

1. 看报错里的完整路径，确认程序到底在找哪个文件。
2. 确认当前工作目录是否正确，例如 PowerShell 里运行 `pwd`。
3. 确认目标文件是否真的存在，例如 `Test-Path resources/stage0_tasks.txt`。
4. 检查代码里的路径拼接，是相对路径、绝对路径，还是从 `__file__` 推出来的项目路径。

## P0-08 最小流程

1. 准备输入文本路径和输出 JSON 路径。
2. 如果任务文本不存在，创建示例文本。
3. 读取文本，每行变成一个任务名。
4. 把任务名转换成结构化字典列表。
5. 写入 JSON，再读回 JSON，确认能被 Python 重新解析。

## 常见坑

- 代码能跑不等于真正掌握；至少要能说清楚“读文本 -> 建结构 -> 写 JSON -> 读回验证”这条链路。
- `json.dumps` 是转 JSON 字符串，常配合 `print`；`json.dump` 是写文件。别把 `json.dump` 说成“打印给用户看”。
- 模型返回的 JSON 字符串先 `json.loads`，再做字段校验；不要拿字符串直接喂给期待 dict 的校验函数。
- 写死绝对路径能在当前机器运行，但换目录或换机器容易失效；项目练习更推荐从项目根目录拼路径。
- `read_json(path)` 只是调用但不保存返回值时，虽然能证明 JSON 可解析，但不方便后续使用；更清楚的写法是 `loaded = read_json(path)`。
- 调试时可以打印目录列表，但最终脚本应减少无关输出，让结果聚焦在任务本身。

## 来源

- AI-Agent-Learning P0-08：`C:\Users\26823\Desktop\AI-Agent-Learning\code\stage0\p0_08_progress_file.py`
- AI-Agent-Learning PR2-Gate：`C:\Users\26823\Desktop\AI-Agent-Learning\code\stage2\pr2_gate_email_processor.py`
- 每日记录：`C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-06-13.md`
- 每日记录：`C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-07-06.md`
- 阅读材料：廖雪峰 Python 教程 `文件读写`、`操作文件和目录`、`序列化`

## 相关链接

- [[README|Python 概念卡]]
- [[异常·调试·测试(Exceptions)|Python 异常、调试与单元测试]]
- [[../../03-Courses/Python/AI-Agent-Learning/stage0-python-basics|阶段 0：Python 与开发环境]]
- [[../../04-Projects/Python/AI-Agent-Learning/p0-08-progress-file|P0-08 文件、JSON、CSV]]
- [[../../04-Projects/LLM/AI-Agent-Learning/pr2-gate-email-processor|PR2-Gate 邮件处理器]]
- [[../../07-Reviews/AI-Agent-Learning/2026-06-13-stage0-p0-08-pass-review|2026-06-13 阶段 0 复盘：P0-08]]
- [[../../07-Reviews/AI-Agent-Learning/2026-07-06-pr2-gate-email-processor-review|2026-07-06 PR2-Gate PASS 复盘]]
