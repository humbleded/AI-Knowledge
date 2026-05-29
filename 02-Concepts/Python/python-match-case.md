---
type: concept
topic: Python match case
status: active
created: 2026-05-29
tags:
  - Python
  - match-case
  - 条件判断
  - AI-Agent-Learning
---

# Python match/case

`match/case` 适合把同一个值和多个固定模式进行匹配。它常用于命令、状态码、菜单选项、类型标签等场景。

```python
command = input("请输入命令：")

match command:
    case "start":
        print("开始学习")
    case "pause":
        print("暂停学习")
    case "exit":
        print("退出")
    case _:
        print("未知命令")
```

和多层 `elif` 相比，`match/case` 的优势是结构更整齐：每个 `case` 都是在描述同一个变量可能出现的模式。

不过，不是所有条件判断都必须改成 `match/case`。如果判断条件是范围比较，例如学习时长小于 2、2 到 4、大于等于 4，用 `if/elif/else` 更自然。

## 什么时候用

- 同一个变量有多个明确取值。
- 分支像菜单、命令、状态码一样清晰。
- 想让代码读起来更接近“按模式分发”。

## 什么时候不用

- 主要逻辑是大小比较、范围判断。
- 条件来自多个变量的组合。
- 简单两三个分支，用 `if/else` 已经足够清楚。

## 关联

- [[python-conditionals-and-loops]]
- [[../../04-Projects/Python/AI-Agent-Learning/p0-03-scheduler]]
