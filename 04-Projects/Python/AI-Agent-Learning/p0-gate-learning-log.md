---
type: project-note
topic: AI-Agent-Learning P0-Gate learning log
status: pass
created: 2026-06-14
updated: 2026-06-14
tags:
  - Python
  - AI-Agent-Learning
  - Stage0
  - P0-Gate
  - JSON
  - CLI
---

# P0-Gate Python 基础闯关

## 任务

执行区产物：

- `C:\Users\26823\Desktop\AI-Agent-Learning\code\stage0\p0_gate_learning_log.py`
- `C:\Users\26823\Desktop\AI-Agent-Learning\resources\p0_gate_learning_log.json`
- `C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-06-14.md`

目标：

- 输入今日学习记录，保存到 JSON。
- 支持查看最近 7 条记录。
- 有错误处理。
- 有 3 条以上测试记录。

## 验证结果

2026-06-14 批改时运行/验证：

```powershell
.\.venv\Scripts\python.exe -X utf8 -m py_compile code\stage0\p0_gate_learning_log.py
```

并用临时 JSON 文件测试：

- 文件不存在时 `load_logs()` 返回空列表。
- JSON 损坏时返回空列表并给出提示。
- 有效输入能新增、保存、重新读取。
- 非整数分钟数被拒绝。
- 负数分钟数被拒绝。
- `show_recent(logs)` 只展示最近 7 条。

当前执行区 JSON 中共有 4 条记录，其中 3 条为有效非负记录，满足闯关要求；另有一条旧脏数据 `minutes: -5`，后续建议清理。

## 通过理由

- 代码可运行并能通过语法检查。
- 数据结构能解释：`list` 存多条记录，`dict` 存单条记录字段。
- 能解释文件不存在时从空列表开始。
- 能说明该脚本后续可扩展为学习追踪系统的记录层。

## 保留问题

- `resources/p0_gate_learning_log.json` 里仍有一条历史负数分钟记录；脚本已阻止新增负数，但旧数据需要单独清理。
- 发布到 GitHub 前应确认 `.env`、虚拟环境和缓存文件不被提交。
- 后续如要统计、更新、删除、按主题筛选，应考虑迁移到 SQLite。

## 相关概念

- [[../../../02-Concepts/Python/python-json-learning-log-cli|Python JSON 学习日志 CLI：list[dict] 与输入校验]]
- [[../../../02-Concepts/Python/python-file-json-serialization|Python 文件读写与 JSON 序列化]]
- [[../../../02-Concepts/Python/python-list-dict-set|Python list、dict、set]]

复盘：[[../../../07-Reviews/AI-Agent-Learning/2026-06-14-stage0-p0-gate-l1-01-pass-review|2026-06-14 阶段 0 / 阶段 1 复盘]]
