---
type: project-note
topic: AI-Agent-Learning P0-03
status: pass
created: 2026-05-29
tags:
  - Python
  - AI-Agent-Learning
  - PASS
---

# P0-03 条件判断、模式匹配、循环

## 任务

写一个学习时长判断脚本：输入今天学习时长，判断“不足、合格、优秀”，并用循环打印未来 7 天学习计划。

源代码位置：

- [p0_03_scheduler.py](file:///C:/Users/26823/Desktop/AI-Agent-Learning/code/stage0/p0_03_scheduler.py)

## 代码要点

脚本使用 `if/elif/else` 根据学习时长进入不同分支：

```python
if time < 2:
    print("学习时长不足，请加油！")
elif time < 4:
    print("学习时长合格，继续保持！")
else:
    print("学习时长优秀，太棒了！")
```

脚本使用 `for` 和 `range(1, 8)` 打印 7 天计划，避免重复写 7 次 `print()`。

## 验证结果

P0-03 已 PASS。

验证输入：

| 输入 | 结果 |
|---|---|
| `0` | 不足 |
| `1` | 不足 |
| `2` | 合格 |
| `4` | 优秀 |

每次运行都能打印未来 7 天计划。

## 通过结论

通过原因：

- 判断逻辑正确。
- 能用分支表达不同学习时长的结果。
- 能用循环生成 7 天计划。
- 问答能说明 `if/elif/else`、`match/case`、`for`、`while` 的基本使用场景。

## 可改进点

- 把变量名 `time` 改成 `study_hours`，避免和 Python 常见的 `time` 模块名字混淆。
- 后续学到异常处理时，可以补上非数字输入处理。
- 当前任务暂不要求真正使用 `match/case`，但要知道它适合处理同一个变量的多个固定取值。

## 相关

- [[../../../03-Courses/Python/AI-Agent-Learning/stage0-python-basics]]
- [[../../../07-Reviews/AI-Agent-Learning/2026-05-28-stage0-p0-03-pass-review]]
