---
type: project
topic: AI-Agent-Learning W4-04 存在相近的重复元素
status: pass
created: 2026-08-08
updated: 2026-08-08
source:
  - C:\Users\26823\Desktop\AI-Agent-Learning\code\algorithms\w4_04_contains_nearby_duplicate.py
  - C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-08-08.md
tags:
  - Python
  - Algorithms
  - 数组
  - 哈希表
  - AI-Agent-Learning
---

# W4-04 存在相近的重复元素

## 任务与结果

给定整数列表 `nums` 和非负整数 `k`；如果存在两个不同下标 `i`、`j`，同时满足 `nums[i] == nums[j]` 且 `abs(i - j) <= k`，返回 `True`，否则返回 `False`。

- 产物：`C:\Users\26823\Desktop\AI-Agent-Learning\code\algorithms\w4_04_contains_nearby_duplicate.py`
- 正式判定：**PASS（2026-08-08）**。
- W4 状态：新题正式 PASS `4/4`，内容块由 `DEBT 1` 收口为 `PASS`，结转债务为 0。

## 解法

字典保存“值 → 最近一次出现的下标”：

1. 从左到右遍历 `(i, num)`。
2. `num` 已出现时，检查 `i - last_seen[num] <= k`；满足就立即返回 `True`。
3. 无论这个重复距离是否太远，未返回时都把 `num` 的最近下标更新为 `i`。
4. 遍历结束仍未命中，返回 `False`。

固定当前下标后，最近的历史下标产生最小距离，因此只保存最近一次就足够；更早的同值下标不可能提供更小距离。

## 正式验证

- `.venv\Scripts\python.exe -m py_compile code\algorithms\w4_04_contains_nearby_duplicate.py`：通过。
- `.venv\Scripts\python.exe code\algorithms\w4_04_contains_nearby_duplicate.py`：8 条规定断言全部通过，输出 `All test cases passed.`。
- 性质检查：长度 0～6、元素值 -2～2、`k=0～6` 的 136717 组输入，与双重遍历基准逐例一致。
- 所有返回值均为真正的 `bool`；每次调用前后 `nums` 保持不变。

## 独立性与订正轨迹

- 首答已经想到保存“元素和下标”，但只说比较下标是否不同，并计划循环结束后再计算距离。
- 通过 `[1, 2, 1, 1]`、`k=1` 的反例追踪，学习者自行发现：下标 `2` 的重复虽然太远，仍必须把值 `1` 的记录更新为 `2`，才能在下标 `3` 命中更近的一对。
- 思路订正后独立完成代码；未展示参考实现。规定断言和隐藏性质检查全部通过。

## 复杂度

- 平均时间：`O(n)`。循环最多处理 `n` 个元素，每项执行常数次平均 `O(1)` 的字典查询、读取和写入。
- 额外空间：`O(n)`。全部值互不相同时，字典最多保存 `n` 个键。
- 不需要 `abs()`：保存的历史下标一定小于当前下标，所以 `i - last_seen[num]` 已经非负。

## 相关链接

- [[../../../02-Concepts/Python/list·dict·set 容器|Python list、dict、set：在线维护最近下标]]
- [[../../../07-Reviews/AI-Agent-Learning/2026-08-08-w4-alg-f4-contains-nearby-duplicate-review|W4-ALG-F4 PASS 复盘]]
