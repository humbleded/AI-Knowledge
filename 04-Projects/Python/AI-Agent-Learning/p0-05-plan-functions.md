---
type: project-note
topic: AI-Agent-Learning P0-05
status: pass
created: 2026-06-09
tags:
  - Python
  - AI-Agent-Learning
  - PASS
---

# P0-05 函数、参数、返回值

## 任务

写 `code/stage0/p0_05_plan_functions.py`：

- 实现 `make_plan(goal, days)`，根据学习目标和天数返回计划列表。
- 实现 `score_answer(answer)`，根据回答长度和关键词返回练习分。
- 在 `main()` 中调用两个函数，并打印返回值。

源代码位置：

- [p0_05_plan_functions.py](file:///C:/Users/26823/Desktop/AI-Agent-Learning/code/stage0/p0_05_plan_functions.py)

## 验证结果

已执行：

```powershell
python -m py_compile .\code\stage0\p0_05_plan_functions.py
python .\code\stage0\p0_05_plan_functions.py
```

额外用函数级断言验证：

- `make_plan("functions", 3)` 返回 3 条计划。
- `make_plan("函数", 2)` 能保留学习目标文本。
- `score_answer("")` 和空白字符串返回 `0`。
- 更完整、包含关键词的答案分数高于普通短答案，且不超过 `100`。
- 非整数天数输入 `abc` 会提示 `天数必须是整数。`

## 通过结论

P0-05 已 PASS。

通过原因：

- 代码可以运行并完成交互流程。
- 至少两个函数被 `main()` 调用。
- `make_plan()` 使用参数作为输入，并用 `return` 返回列表。
- `score_answer()` 使用参数作为输入，并用 `return` 返回分数。
- 问答能说明函数封装、`return`/`print` 区别和函数职责边界。

## 可改进点

- `days <= 0` 当前会返回空列表，后续可以加正整数校验或重新输入提示。
- 完成正整数校验后，可以删除代码中的对应 TODO 注释。

## 相关

- [[../../../02-Concepts/Python/python-functions]]
- [[../../../03-Courses/Python/AI-Agent-Learning/stage0-python-basics]]
- [[../../../07-Reviews/AI-Agent-Learning/2026-06-09-stage0-p0-05-pass-review]]
