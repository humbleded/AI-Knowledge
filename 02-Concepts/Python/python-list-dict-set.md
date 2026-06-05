---
type: concept
topic: Python
status: usable
created: 2026-06-02
updated: 2026-06-06
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

## 访问方式不要混用

```python
tasks = ["read", "code", "review"]
task_status = {"read": "done", "code": "todo", "review": "todo"}
tags = {"Python", "function", "Agent"}

print(tasks[0])              # 正确：list 用整数下标
print(task_status["read"])   # 正确：dict 用 key
print("Python" in tags)      # 正确：set 用 in 判断是否存在
```

下面两种写法是错的：

```python
print(tasks["read"])    # 错：list 不能用字符串 key 访问
print(tags["Python"])   # 错：set 不能像 dict 一样按 key 取值
```

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

## 修改任务名时同步迁移状态

如果任务名同时存在于 `tasks` 列表和 `task_status` 字典里，改名时必须同步迁移状态。否则列表里的任务名和字典里的 key 会断开。

```python
tasks = ["task1", "task2"]
task_status = {"task1": "todo", "task2": "done"}

old_name = tasks[0]
new_name = "task4"

tasks[0] = new_name
old_status = task_status[old_name]
task_status[new_name] = old_status
del task_status[old_name]
```

最终结果是：

```python
tasks == ["task4", "task2"]
task_status == {"task2": "done", "task4": "todo"}
```

## set 去重的代价

`set` 的查找和去重通常很快，但代价是：

- 丢失重复次数。
- 不适合表达稳定的业务顺序。
- 无法直接保留每个元素来自哪个任务、哪一天或哪条记录。
- 元素必须可哈希。
- 会占用额外内存。

## 相关

- [[python-basic-data-types]]
- [[python-conditionals-and-loops]]
- [[../../07-Reviews/Daily-Practice/2026-06-05-review]]
