---
type: review
topic: AI-Agent-Learning Stage0
status: pass
created: 2026-05-28
date: 2026-05-27
tags:
  - AI-Agent-Learning
  - Python
  - 复盘
  - PASS
---

# 2026-05-27 阶段 0 复盘：P0-01 与 P0-02

## 当日完成

- P0-01 环境与第一个程序：PASS
- P0-02 数据类型与变量：PASS

原始每日记录：

- [2026-05-27.md](file:///C:/Users/26823/Desktop/AI-Agent-Learning/daily/2026-05-27.md)

## 已掌握

- 能写基础交互脚本。
- 能使用 `input()` 接收输入。
- 能使用 `print()` 输出结果。
- 能用 `int()`、`float()` 做基础类型转换。
- 能区分 `str`、`int`、`float`、`bool` 的使用场景。

## 主要问题

1. 问答能说出“是什么”，但解释还偏短，需要逐步补上“为什么”和例子。
2. `input()` 默认返回字符串这一点要反复记住。
3. `bool(input(...))` 容易误判，不能作为可靠的真假输入解析方式。
4. 递归目前属于超前内容，不必在 P0-01/P0-02 阶段强行掌握。

## Codex 判定摘要

P0-01：代码能运行，能输入姓名和学习目标并输出结果；基础问答通过。

P0-02：修正后能运行，已经体现 `str`、`int`、`float`、`bool` 四种数据类型，满足通过标准。

## 下一步

进入 P0-03：条件判断、模式匹配、循环。

下一份代码应关注：

- 判断逻辑是否正确。
- 是否能解释 `if/elif/else`。
- 是否能用循环避免重复写 7 次 `print()`。

## 相关

- [[../../03-Courses/Python/AI-Agent-Learning/stage0-python-basics]]
- [[../../04-Projects/Python/AI-Agent-Learning/p0-01-hello-script]]
- [[../../04-Projects/Python/AI-Agent-Learning/p0-02-profile-script]]
