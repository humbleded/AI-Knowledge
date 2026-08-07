---
type: project
topic: AI-Agent-Learning W4-01 两数之和
status: pass
created: 2026-08-07
updated: 2026-08-07
source:
  - C:\Users\26823\Desktop\AI-Agent-Learning\code\algorithms\w4_01_two_sum.py
  - C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-08-04.md
  - C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-08-05.md
  - C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-08-07.md
tags:
  - Python
  - Algorithms
  - 哈希表
  - AI-Agent-Learning
---

# W4-01 两数之和

## 任务与结果

给定整数列表 `nums` 和目标值 `target`，返回两个不同元素的下标 `[i, j]`；要求 `i < j` 且两数之和等于目标。扩展边界规定无解时返回 `[]`。

- 产物：`C:\Users\26823\Desktop\AI-Agent-Learning\code\algorithms\w4_01_two_sum.py`
- 首次正式结果：`RETRY（2026-08-05）`。代码正确，但思路和复杂度在直接讲解后才闭合。
- 独立复测：**PASS（2026-08-07）**。
- W4 状态：正式 PASS 3/4，仍为 `DEBT`，只剩第 4 道新题。

## 解法

维护 `lookup: dict[int, int]`，保存“已经遍历的数字 → 下标”。遍历当前 `num` 时先查询 `target - num`；命中就返回旧下标和当前下标，未命中才保存 `num → i`。

先查后存避免当前元素与自身匹配。同一个数值可以出现在两个不同下标上并组成合法答案，例如 `[4, 4] → [0, 1]`。

## 正式验证

- 项目文件编译通过，文件内规定案例 3/3。
- 复测时从空白提交的函数首次通过隐藏边界 5/5。
- 最终自设计顶层测试 6/6，覆盖非相邻答案、重复值、零参与有效数对、单元素不得自用和无解。
- 穷举长度 0～5、元素 `-2..2`、目标 `-4..4`，性质检查 35154/35154；输入列表未被修改。

## 独立性与订正边界

- 首次实现虽然运行正确，但用户当时主动求助解题思路与复杂度，因此历史 `RETRY` 保留。
- 2026-08-07 在规定窗口内未查看旧实现，独立说出字典保存对象、补数查询、先查后存和两个复杂度结论，并从空白重写函数。
- “先查后存”的原因最初说成“防止重复保存”，经定向补答后准确落到“防止同一下标自用”。
- 测试最初位于函数内 `return` 之后，移出后又留下顶层空格；最终修正作用域和缩进并真实执行通过。

## 复杂度

- 平均时间：`O(n)`。最多遍历 `n` 个元素，每次字典查询/写入平均 `O(1)`。
- 额外空间：`O(n)`。最坏保存 `n` 个“数字 → 下标”映射。

## 相关链接

- [[../../../02-Concepts/Python/list·dict·set 容器|Python list、dict、set]]
- [[../../../02-Concepts/Python/异常·调试·测试(Exceptions)|Python 异常、调试与测试]]
- [[../../../07-Reviews/AI-Agent-Learning/2026-08-07-w4-alg-f1-two-sum-review|W4-ALG-F1 PASS 复盘]]
