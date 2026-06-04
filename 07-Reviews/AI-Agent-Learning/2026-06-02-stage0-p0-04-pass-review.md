---
type: review
topic: AI-Agent-Learning Stage0 P0-04
status: pass
created: 2026-06-02
date: 2026-06-02
tags:
  - AI-Agent-Learning
  - Python
  - 复盘
  - PASS
---

# 2026-06-02 阶段 0 复盘：P0-04

## 当日完成

- P0-04 list、tuple、dict、set：PASS

原始每日记录：

- [2026-06-02.md](file:///C:/Users/26823/Desktop/AI-Agent-Learning/daily/2026-06-02.md)

## 已掌握

- 能用 `list` 保存任务列表。
- 能用 `dict` 保存任务状态。
- 能用 `set` 做去重。
- 能区分 `remove(value)` 和 `pop(index)`。
- 能说明 set 去重的主要代价：丢失重复信息、不强调顺序、元素必须可哈希、占用额外内存。

## 验证摘要

实际运行 `code/stage0/p0_04_tasks.py`，脚本能输出任务列表、任务状态和去重结果。代码已经展示新增、删除、修改、查询相关操作，满足 P0-04 当前通过标准。

## 主要问题

1. `tags` 当前从任务名生成，更像任务名去重，不是真正的标签去重。
2. `task_status.get(...)` 查询没有打印结果，验证感不强。
3. 修改任务名后，`task_status` 里还保留旧任务名，后续应练习让数据结构保持一致。

这些问题不影响 P0-04 通过，但适合作为后续代码整洁度练习。

## 下一步

进入 P0-05：函数、参数、返回值。

下一份代码应关注：

- 把重复逻辑封装成函数。
- 区分 `return` 和 `print`。
- 能说明函数的输入、处理、输出。

## 相关

- [[../../02-Concepts/Python/python-list-dict-set]]
- [[../../03-Courses/Python/AI-Agent-Learning/stage0-python-basics]]
- [[../../04-Projects/Python/AI-Agent-Learning/p0-04-tasks]]
