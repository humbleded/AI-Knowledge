---
type: concept
topic: Python JSON learning log CLI
status: usable
created: 2026-06-14
source:
  - AI-Agent-Learning P0-Gate
tags:
  - Python
  - JSON
  - CLI
  - 输入校验
---

# Python JSON 学习日志 CLI：list[dict] 与输入校验

## 一句话解释

一个简单的学习日志 CLI 可以先用 `list[dict]` 存数据：外层列表表示一条条记录，内层字典表示每条记录的字段，例如日期、主题、分钟数和备注。

## 最小数据结构

```python
logs = [
    {
        "date": "2026-06-14",
        "topic": "学习 JSON",
        "minutes": 30,
        "note": "练习读写学习记录",
    }
]
```

这样设计的好处：

- `list` 适合按时间追加记录。
- `dict` 适合保存一条记录里的多个字段。
- 最近 7 条可以直接用 `logs[-7:]` 取出。
- 以后要统计总时长、按主题筛选、生成周报时，也有清晰字段可用。

## 一个小比喻

可以把 JSON 文件看成一个“账本”：

- 整个 JSON 文件是账本。
- 外层列表是一页页流水。
- 每个字典是一条流水记录。
- `minutes`、`topic`、`note` 是这一条流水的列。

刚开始用 JSON 足够轻；等记录很多、要复杂查询时，再升级到 SQLite。

## CLI 要先守住输入边界

用户输入永远可能不规整，所以最小 CLI 至少要处理：

- 文件不存在：返回空列表，让程序从空账本开始。
- JSON 损坏：给可读提示，不要直接崩溃。
- 分钟数不是整数：提示“分钟数必须是整数”。
- 分钟数为负数：拒绝保存，因为学习时长不能是负数。

```python
try:
    minutes = int(minutes_text)
    if minutes < 0:
        print("分钟数不能为负数。")
        return logs
except ValueError:
    print("分钟数必须是整数。")
    return logs
```

## 常见坑

- 脚本现在能拒绝新输入的负数，不代表旧 JSON 里一定没有脏数据；发布或统计前要检查历史文件。
- 每次新增后要保存，再重新读取验证，才算确认“写入磁盘”这一步真的成功。
- JSON 适合当前阶段的小数据练习；如果后续要按主题统计、更新、删除、分页，就应该迁移到 SQLite。

## 来源

- 代码：`C:\Users\26823\Desktop\AI-Agent-Learning\code\stage0\p0_gate_learning_log.py`
- 数据：`C:\Users\26823\Desktop\AI-Agent-Learning\resources\p0_gate_learning_log.json`
- 每日记录：`C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-06-14.md`

## 相关链接

- [[python-file-json-serialization|Python 文件读写与 JSON 序列化]]
- [[python-list-dict-set|Python list、dict、set]]
- [[python-exceptions-debugging-testing|Python 异常、调试与单元测试]]
- [[../../04-Projects/Python/AI-Agent-Learning/p0-gate-learning-log|P0-Gate Python 基础闯关]]
- [[../../07-Reviews/AI-Agent-Learning/2026-06-14-stage0-p0-gate-l1-01-pass-review|2026-06-14 PASS 复盘]]
