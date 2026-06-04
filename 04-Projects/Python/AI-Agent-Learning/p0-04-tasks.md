---
type: project-note
topic: AI-Agent-Learning P0-04
status: pass
created: 2026-06-02
tags:
  - Python
  - AI-Agent-Learning
  - PASS
---

# P0-04 list、tuple、dict、set

## 任务

写 `code/stage0/p0_04_tasks.py`：

- 用 list 保存任务。
- 用 dict 保存任务状态。
- 用 set 去重标签。
- 展示任务的新增、删除、修改、查询。

源代码位置：

- [p0_04_tasks.py](file:///C:/Users/26823/Desktop/AI-Agent-Learning/code/stage0/p0_04_tasks.py)

## 验证结果

运行命令：

```powershell
python code\stage0\p0_04_tasks.py
```

脚本能正常输出任务列表、任务状态和去重结果，并展示了 `append`、`insert`、`pop`、`remove`、下标修改、`dict.get`、`dict.pop` 等基础操作。

## 通过结论

P0-04 已 PASS。

通过原因：

- 代码可以运行。
- 能用 list 保存和调整任务顺序。
- 能用 dict 保存任务状态。
- 能用 set 做去重。
- 已修正 set 去重代价的理解。

## 可改进点

- `tags` 最好保存真实标签，而不是由任务名生成。
- 查询操作最好打印结果，便于确认输出。
- 修改任务名时，应同步维护 `task_status` 中的 key，避免任务列表和状态字典不一致。

## 相关

- [[../../../02-Concepts/Python/python-list-dict-set]]
- [[../../../03-Courses/Python/AI-Agent-Learning/stage0-python-basics]]
- [[../../../07-Reviews/AI-Agent-Learning/2026-06-02-stage0-p0-04-pass-review]]
