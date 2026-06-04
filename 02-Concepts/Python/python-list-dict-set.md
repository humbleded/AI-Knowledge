---
type: concept
topic: Python
status: seed
created: 2026-06-02
tags:
  - Python
  - 编程基础
---

# Python list、dict、set

`list`、`dict`、`set` 都可以保存一组数据，但它们解决的问题不同。

## 核心区别

| 容器 | 适合保存 | 典型访问方式 | 是否强调顺序 | 是否允许重复 |
|---|---|---|---|---|
| `list` | 有顺序的一组值 | 下标、遍历 | 是 | 是 |
| `dict` | key 到 value 的映射 | 通过 key 查询 | 当前 Python 会保留插入顺序，但核心用途是映射 | key 不允许重复 |
| `set` | 不重复的一组值 | 成员判断、集合运算 | 不强调业务顺序 | 不允许重复 |

## 在任务管理中的选择

- 用 `list` 保存任务列表，因为任务可以按顺序展示。
- 用 `dict` 保存任务状态，因为任务名到状态是天然映射，例如 `task_status["task1"] = "pending"`。
- 用 `set` 保存标签或去重结果，因为标签通常只关心有没有，不关心重复出现几次。

## 常见操作

```python
tasks = ["task1", "task2"]
task_status = {"task1": "pending", "task2": "done"}

tasks.append("task3")
tasks.remove("task1")
tasks[0] = "task2-updated"

status = task_status.get("task2")
task_status["task3"] = "pending"
task_status.pop("task1", None)

tags = {"python", "agent", "python"}
```

`remove(value)` 按值删除，`pop(index)` 按位置删除并返回被删除的元素。

## set 去重的代价

`set` 的查找和去重通常很快，但代价是：

- 丢失重复次数。
- 不适合表达稳定的业务顺序。
- 元素必须可哈希。
- 会占用额外内存。

## 相关

- [[python-basic-data-types]]
- [[python-conditionals-and-loops]]
