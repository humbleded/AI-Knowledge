---
type: project-note
topic: AI-Agent-Learning P0-08 progress file
status: pass
created: 2026-06-13
updated: 2026-06-13
tags:
  - Python
  - AI-Agent-Learning
  - Stage0
  - P0-08
  - JSON
---

# P0-08 文件、JSON、CSV

## 任务

执行区产物：

- `C:\Users\26823\Desktop\AI-Agent-Learning\code\stage0\p0_08_progress_file.py`
- `C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-06-13.md`
- `C:\Users\26823\Desktop\AI-Agent-Learning\resources\stage0_tasks.txt`
- `C:\Users\26823\Desktop\AI-Agent-Learning\resources\stage0_progress.json`

目标：

- 从 `resources/stage0_tasks.txt` 读取任务文本。
- 把任务转换成包含 `name` 和 `status` 的字典列表。
- 写入 `resources/stage0_progress.json`。
- 再读取 JSON，确认 Python 能重新解析。

## 验证结果

2026-06-13 复查时已运行：

```powershell
python -m py_compile code\stage0\p0_08_progress_file.py
python code\stage0\p0_08_progress_file.py
```

关键输出：

```text
['学习文件读写', '学习 JSON', '练习异常处理']
任务数量： 3
jsonpath: C:\Users\26823\Desktop\AI-Agent-Learning\resources\stage0_progress.json
```

另用 Python 验证：

```text
list 3 True
```

含义：

- JSON 文件能被 `json.loads()` 重新解析为 Python `list`。
- 列表长度为 `3`。
- 每个元素都有 `name` 和 `status` 字段。

## 通过理由

- 能读文本文件。
- 能构造结构化任务列表。
- 能写入 JSON 文件。
- JSON 能被 Python 重新解析。
- 第二轮检查题能说明 `json.dumps()` / `json.loads()`、路径排查、`ensure_ascii=False` 和完整流程。

## 保留问题

- 当前代码用的是绝对路径，能在本机运行，但后续更推荐用 `Path(__file__).resolve().parents[2]` 拼项目路径。
- 当前脚本还会打印 `D:/` 文件列表和 `D:\` 绝对路径，这是额外练习输出；建议后续清理，让脚本只输出任务数量和 JSON 文件位置。
- `read_json(json_path)` 当前没有把返回值保存成 `loaded`，后续可改成 `loaded = read_json(json_path)` 再打印 `len(loaded)`。

## 相关概念

- [[../../../02-Concepts/Python/python-file-json-serialization|Python 文件读写与 JSON 序列化]]
- [[../../../02-Concepts/Python/python-exceptions-debugging-testing|Python 异常、调试与单元测试]]

复盘：[[../../../07-Reviews/AI-Agent-Learning/2026-06-13-stage0-p0-08-pass-review|2026-06-13 阶段 0 复盘：P0-08]]
