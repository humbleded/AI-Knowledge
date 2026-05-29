---
type: review
topic: AI-Agent-Learning Stage0 P0-03
status: pass
created: 2026-05-29
date: 2026-05-28
tags:
  - AI-Agent-Learning
  - Python
  - 复盘
  - PASS
---

# 2026-05-28 阶段 0 复盘：P0-03

## 当日完成

- P0-03 条件判断、模式匹配、循环：PASS

原始每日记录：

- [2026-05-28.md](file:///C:/Users/26823/Desktop/AI-Agent-Learning/daily/2026-05-28.md)

## 已掌握

- 能用 `if/elif/else` 表达互斥分支。
- 能用 `int(input(...))` 接收数字输入。
- 能用 `for day in range(1, 8)` 生成固定次数循环。
- 能解释为什么循环比复制多行 `print()` 更容易维护。

## 验证摘要

实际运行 `code/stage0/p0_03_scheduler.py`，输入 `0`、`1`、`2`、`4` 均得到预期分支：

- `0` 和 `1`：不足。
- `2`：合格。
- `4`：优秀。

每次运行都打印了 7 天计划，满足 P0-03 通过标准。

## 主要问题

1. 问答方向正确，但解释偏短，需要继续练习“结论 + 适用场景 + 例子”的回答方式。
2. 变量名 `time` 可以改成 `study_hours`，语义更清楚，也能避免和常见模块名混淆。
3. 非数字输入会触发异常，但这是 P0-07 异常处理阶段再补的内容，不影响 P0-03 通过。

## 下一步

进入 P0-04：list、tuple、dict、set。

下一份代码应关注：

- 是否能用 list 保存任务。
- 是否能用 dict 保存任务状态。
- 是否能用 set 做标签去重。
- 是否能解释不同容器的选择理由。

## 相关

- [[../../03-Courses/Python/AI-Agent-Learning/stage0-python-basics]]
- [[../../04-Projects/Python/AI-Agent-Learning/p0-03-scheduler]]
