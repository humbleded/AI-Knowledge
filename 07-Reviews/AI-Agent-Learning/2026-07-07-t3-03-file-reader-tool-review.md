---
type: review
topic: AI-Agent-Learning T3-03
status: pass
created: 2026-07-07
tags:
  - AI-Agent-Learning
  - Agent
  - Tool-Calling
  - PASS
---

# 2026-07-07 T3-03 文件工具 PASS 复盘

## 判定

**T3-03 PASS**

## 验证

- `python -m py_compile code/stage3/t3_03_file_reader_tool.py`：通过。
- CLI 读取 `sample.txt`：返回 `ok=True`、完整 `content`、`truncated=False`。
- 函数级测试覆盖：
  - 正常读取沙箱内文件。
  - 长文件按 `max_chars` 截断，`truncated=True`。
  - 不存在文件返回“文件不存在”。
  - 目录路径返回“不是文件”。
  - `../stage2_email_result.json` 拒绝。
  - `logs/../sample.txt` 允许。
  - `logs/../../stage2_email_result.json` 拒绝。

## 学到的稳定概念

- [[../../02-Concepts/Agent/文件工具沙箱(File Tool Sandbox)|文件工具沙箱]]
- [[../../02-Concepts/Agent/工具定义与执行协议(Tool Definition)|工具定义与执行协议]]
- [[../../02-Concepts/LLM/函数调用(Function Calling)|函数调用 / Tool Calling]]

## 关键问题闭环

1. 为什么文件工具必须限制在沙箱内？
   - 因为模型可能被用户或外部文本诱导去读隐私文件。客户端程序要用硬校验挡住沙箱外路径。
2. `resolve()` 和 `relative_to(SANDBOX)` 各做什么？
   - `resolve()` 把路径算成最终绝对路径；`relative_to(SANDBOX)` 判断最终路径是否仍属于沙箱。
3. 为什么要区分 `exists()` 和 `is_file()`？
   - 不存在就返回“文件不存在”；存在但不是文件就返回“不是文件”。错误更清楚，后续 Agent 也更容易继续处理。
4. `content` 和 `truncated` 表示什么？
   - `content` 是实际返回的内容；`truncated=True` 表示原文件比返回内容更长。

## 今日易错点

- 一开始容易按 `..` 字面判断路径。正确做法是看 `resolve()` 后的最终落点。
- 一度写成不存在的 `target.resolve_to(SANDBOX)`。正确方法是 `target.relative_to(SANDBOX)`。
- 返回结构要按真实代码字段说清楚：成功是 `ok/content/truncated`，失败是 `ok/error`。

## 下一步

进入 `T3-04 外部 API 工具`：把工具调用从本地纯函数扩展到外部 API，继续练习参数校验、错误兜底、稳定返回和 Observation 回填。
