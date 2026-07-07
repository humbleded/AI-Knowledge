---
type: project-note
topic: T3-03 File Reader Tool
status: pass
created: 2026-07-07
source:
  - C:\Users\26823\Desktop\AI-Agent-Learning\code\stage3\t3_03_file_reader_tool.py
  - C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-07-07.md
tags:
  - Agent
  - Tool-Calling
  - AI-Agent-Learning
  - Security
---

# T3-03 文件工具

## 目标

实现一个安全的文件读取工具，用来练习 Agent 工具的三个要点：

1. 只允许读取 `resources/sandbox/` 里的文件。
2. 对不存在、目录、沙箱外路径返回稳定错误。
3. 长文件只返回前 `max_chars` 个字符，并用 `truncated` 标记是否截断。

## 产物

- 执行区代码：`C:\Users\26823\Desktop\AI-Agent-Learning\code\stage3\t3_03_file_reader_tool.py`
- 沙箱测试文件：
  - `C:\Users\26823\Desktop\AI-Agent-Learning\resources\sandbox\sample.txt`
  - `C:\Users\26823\Desktop\AI-Agent-Learning\resources\sandbox\long.txt`
  - `C:\Users\26823\Desktop\AI-Agent-Learning\resources\sandbox\logs\`

核心结构：

```python
target = (SANDBOX / relative_path).resolve()
try:
    target.relative_to(SANDBOX)
except ValueError:
    return {"ok": False, "error": "文件在沙箱外，访问被拒绝"}
```

## 验证结果

2026-07-07 实跑通过：

| 用例 | 结果 |
|---|---|
| `sample.txt` | `{"ok": True, "content": "...", "truncated": False}` |
| `long.txt`, `max_chars=5` | `{"ok": True, "content": "abcde", "truncated": True}` |
| `missing.txt` | `{"ok": False, "error": "文件不存在"}` |
| `logs` | `{"ok": False, "error": "不是文件"}` |
| `../stage2_email_result.json` | `{"ok": False, "error": "文件在沙箱外，访问被拒绝"}` |
| `logs/../sample.txt` | 允许，最终仍在沙箱内 |
| `logs/../../stage2_email_result.json` | 拒绝，最终逃逸到沙箱外 |

语法检查也通过：

```text
python -m py_compile code/stage3/t3_03_file_reader_tool.py
```

## 关键结论

- 文件工具的安全边界必须由客户端程序保证，不能靠模型“自觉不乱读”。
- 路径判断要看 `resolve()` 后的最终绝对路径，再用 `relative_to(SANDBOX)` 判断是否仍在沙箱内。
- `truncated=True` 表示只读到部分内容，模型不能基于未读部分下结论。
- 稳定返回结构能让用户看懂错误，也让后续 Agent 流程继续执行。

## 相关

- [[../../../../02-Concepts/Agent/文件工具沙箱(File Tool Sandbox)]]
- [[../../../../02-Concepts/Agent/工具定义与执行协议(Tool Definition)]]
- [[../../../../07-Reviews/AI-Agent-Learning/2026-07-07-t3-03-file-reader-tool-review]]
