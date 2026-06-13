---
type: review
topic: AI-Agent-Learning P0-08
status: pass
created: 2026-06-13
updated: 2026-06-13
tags:
  - AI-Agent-Learning
  - Python
  - Stage0
  - P0-08
  - JSON
---

# 2026-06-13 阶段 0 复盘：P0-08

## 判定

`P0-08 文件、JSON、CSV`：PASS。

CSV 暂不作为本次硬通过项；本次主线按文件读写和 JSON 判定。

## 验证摘要

- `code/stage0/p0_08_progress_file.py` 通过 `py_compile`。
- 脚本从 `resources/stage0_tasks.txt` 读取任务文本。
- 脚本把任务转换为包含 `name` 和 `status` 的字典列表。
- 脚本写入 `resources/stage0_progress.json`。
- 生成的 JSON 能被 Python 重新解析为 `list`，长度为 `3`，每个元素都有 `name` 和 `status`。

## 当天卡点

- 初版答案只说“路径错误时查看报错信息”，缺少当前工作目录、文件是否存在、路径拼接方式这些排查步骤。
- 初期代码能看懂但不一定能独立写出，说明“能运行”和“能复写”还不是一回事。
- 当前代码仍有额外调试输出，例如打印 `D:/` 目录列表；不影响通过，但后续应清理。

## 稳定结论

- 文本文件适合保存简单文字或逐行任务；JSON 适合保存结构化数据并让程序重新读取。
- `json.dumps()` 把 Python 数据转成 JSON 字符串，`json.loads()` 把 JSON 字符串转回 Python 数据。
- `ensure_ascii=False` 可以让 JSON 中的中文保持可读。
- 路径问题应按“报错完整路径 -> 当前工作目录 -> 文件是否存在 -> 代码路径拼接”的顺序排查。
- 读写中文文件时显式写 `encoding="utf-8"` 更稳。

## 同步内容

- 概念卡：[[../../02-Concepts/Python/python-file-json-serialization|Python 文件读写与 JSON 序列化]]
- 项目记录：[[../../04-Projects/Python/AI-Agent-Learning/p0-08-progress-file|P0-08 文件、JSON、CSV]]
- 阶段页：[[../../03-Courses/Python/AI-Agent-Learning/stage0-python-basics|阶段 0：Python 与开发环境]]

## 下一步

进入 `P0-09 HTTP 请求`。
