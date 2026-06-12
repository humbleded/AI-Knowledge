---
type: project-note
topic: AI-Agent-Learning P0-07 safe divide
status: pass
created: 2026-06-11
updated: 2026-06-11
tags:
  - Python
  - AI-Agent-Learning
  - Stage0
  - P0-07
---

# P0-07 异常、调试、单元测试

## 任务

执行区产物：

- `C:\Users\26823\Desktop\AI-Agent-Learning\code\stage0\p0_07_safe_divide.py`
- `C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-06-11.md`

目标：

- 实现 `safe_divide(a_text, b_text)`。
- 处理除零和非数字输入。
- 保留至少 3 个测试样例：正常、除零、非数字。

## 验证结果

2026-06-11 批改时已运行：

```powershell
.\.venv\Scripts\python.exe -m py_compile code\stage0\p0_07_safe_divide.py
```

聚焦检查覆盖：

- `safe_divide("10", "2") -> 5.0`
- `safe_divide("10", "0") -> "错误：除数不能为 0。"`
- `safe_divide("abc", "2") -> "错误：请输入数字。"`
- `safe_divide("3.5", "0.5") -> 7.0`
- `safe_divide("", "2") -> "错误：请输入数字。"`

入口脚本在设置 `PYTHONIOENCODING=utf-8` 后，通过 `subprocess.run(input=...)` 验证了正常输入、除零和非数字输入，返回码均为 `0`。

## 通过理由

- 错误输入不会让程序崩溃。
- 测试样例覆盖了正常和异常场景。
- 问答能说明 `try/except` 捕获异常、不应吞掉所有异常、单元测试的价值。

## 后续提醒

PowerShell 管道给 Python 喂输入时，第一行可能带 UTF-8 BOM，导致 `float()` 失败。复查交互脚本时优先使用干净输入流或设置 `PYTHONIOENCODING=utf-8`。

相关概念：[[../../../02-Concepts/Python/python-exceptions-debugging-testing|Python 异常、调试与单元测试]]

复盘：[[../../../07-Reviews/AI-Agent-Learning/2026-06-11-stage0-p0-07-pass-review|2026-06-11 阶段 0 复盘：P0-07]]
