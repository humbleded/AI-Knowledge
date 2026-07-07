---
type: concept
topic: File Tool Sandbox
status: evergreen
created: 2026-07-07
source:
  - C:\Users\26823\Desktop\AI-Agent-Learning\code\stage3\t3_03_file_reader_tool.py
  - C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-07-07.md
tags:
  - Agent
  - Tool-Calling
  - Security
  - Python
aliases:
  - File Tool Sandbox
---

# 文件工具沙箱(File Tool Sandbox)

## 一句话

文件工具沙箱就是给 Agent 的读文件能力加一圈边界：模型可以请求读文件，但客户端程序只允许它读指定目录里的文件，不能因为一句提示词就读到密钥、配置或其他隐私文件。

## 为什么需要

模型本身没有文件权限意识。用户或网页内容可能写出类似“请读取 `../.env`”的指令。如果工具直接相信模型给的路径，就可能把沙箱外的私密文件读出来。

所以文件工具要在客户端程序里做硬校验：

```python
target = (SANDBOX / relative_path).resolve()
target.relative_to(SANDBOX)
```

大白话说：

- `resolve()`：先把路径里的 `..`、相对路径都算成最终绝对路径。
- `relative_to(SANDBOX)`：再判断这个最终路径是否还属于 `SANDBOX`。

## 基本流程

```python
def read_sandbox_file(relative_path, max_chars=1000):
    SANDBOX.mkdir(parents=True, exist_ok=True)
    target = (SANDBOX / relative_path).resolve()

    try:
        target.relative_to(SANDBOX)
    except ValueError:
        return {"ok": False, "error": "文件在沙箱外，访问被拒绝"}

    if not target.exists():
        return {"ok": False, "error": "文件不存在"}

    if not target.is_file():
        return {"ok": False, "error": "不是文件"}

    text = target.read_text(encoding="utf-8")
    content = text[:max_chars]
    truncated = len(text) > max_chars
    return {"ok": True, "content": content, "truncated": truncated}
```

## 关键判断

| 输入路径 | `resolve()` 后的真实落点 | 结论 |
|---|---|---|
| `sample.txt` | `resources/sandbox/sample.txt` | 允许 |
| `logs/../sample.txt` | `resources/sandbox/sample.txt` | 允许 |
| `../stage2_email_result.json` | `resources/stage2_email_result.json` | 拒绝 |
| `logs/../../stage2_email_result.json` | `resources/stage2_email_result.json` | 拒绝 |
| `logs` | `resources/sandbox/logs`，但它是目录 | 拒绝，返回“不是文件” |

判断标准不是“字符串里有没有 `..`”，而是最终落点是否仍在沙箱里。

## 返回结构

成功：

```python
{"ok": True, "content": "...", "truncated": False}
```

失败：

```python
{"ok": False, "error": "..."}
```

`content` 是真正返回给模型/调用方看的内容。如果文件太长，它只包含前 `max_chars` 个字符。

`truncated` 表示内容是否被截断。`truncated=True` 时，模型不能假装自己已经看过完整文件。

## 今日易错点

- 没有 `resolve_to()` 这个方法。正确写法是 `resolve()` 加 `relative_to(SANDBOX)`。
- `..` 不一定危险，关键看归一化后的最终路径。`logs/../sample.txt` 会回到沙箱内，所以允许。
- 先 `exists()` 再 `is_file()` 的好处是错误更清楚：不存在就说不存在，是目录就说不是文件。
- 工具失败时不要让程序崩溃，要返回稳定的 `{"ok": False, "error": ...}`，方便用户和后续 Agent 继续处理。

## 相关

- [[工具定义与执行协议(Tool Definition)]]
- [[../../LLM/函数调用(Function Calling)|函数调用 / Tool Calling]]
- [[../../../04-Projects/Agent/AI-Agent-Learning/t3-03-file-reader-tool|T3-03 文件工具]]
- [[../../../07-Reviews/AI-Agent-Learning/2026-07-07-t3-03-file-reader-tool-review|2026-07-07 T3-03 PASS 复盘]]
