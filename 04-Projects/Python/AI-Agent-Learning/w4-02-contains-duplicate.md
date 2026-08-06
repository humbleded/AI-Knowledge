---
type: project
topic: AI-Agent-Learning W4-02 存在重复元素
status: pass
created: 2026-08-06
updated: 2026-08-06
source:
  - C:\Users\26823\Desktop\AI-Agent-Learning\code\algorithms\w4_02_contains_duplicate.py
  - C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-08-06.md
tags:
  - Python
  - Algorithms
  - 哈希表
  - AI-Agent-Learning
---

# W4-02 存在重复元素

## 任务与结果

给定整数列表；任意数值至少出现两次就返回 `True`，否则返回 `False`。空列表允许输入。

- 产物：`C:\Users\26823\Desktop\AI-Agent-Learning\code\algorithms\w4_02_contains_duplicate.py`
- 正式判定：**PASS（2026-08-06）**。
- W4 状态：正式 PASS `1/4`，仍为 `DEBT`，剩余 3 道。

## 解法

维护一个记录“已见元素”的 `dict`：

1. 从左到右遍历 `nums`。
2. 当前数已经是字典键时，立即返回 `True`。
3. 未出现时把当前数写入字典。
4. 遍历结束仍未命中，返回 `False`。

本题只需要判断是否出现过，使用 `set` 也可以更简洁；当前实现选择 `dict` 并保存下标，不影响正确性。

## 正式验证

- `.venv\Scripts\python.exe -W error -m py_compile code\algorithms\w4_02_contains_duplicate.py`：通过。
- `.venv\Scripts\python.exe code\algorithms\w4_02_contains_duplicate.py`：8 条显式断言全部通过，输出 `All test cases passed.`。
- 9 条隐藏边界全部通过：空列表、单元素、重复零、负数唯一/重复、末尾重复、全相同、1 万个唯一值、末尾追加重复值。
- 返回类型为 `bool`；调用前后输入列表不变。

## 独立性与订正边界

- 最初用 `list` 保存已见元素，控制流正确，但循环里的列表成员检查会让最坏时间达到 `O(n²)`。
- 在只指出性能问题后，学习者自行选择 `dict`、完成函数、补齐测试并解释复杂度；没有展示或复制参考实现。
- 测试阶段一度把 `[-2, 2, ...]` 判为存在重复；订正为重复同一个负整数后，8 条显式测试共同通过。
- 这道题不替代“两数之和”的独立复测；两个题的查询对象不同。

## 复杂度

- 平均时间：`O(n)`。最多遍历 `n` 次，每次字典查询/写入平均 `O(1)`。
- 额外空间：`O(n)`。全部唯一时字典最多保存 `n` 个键。
- “平均”来自哈希表的常规操作口径，不应误写成无条件理论最坏 `O(1)`。

## 相关链接

- [[../../../02-Concepts/Python/list·dict·set 容器|Python list、dict、set]]
- [[../../../07-Reviews/AI-Agent-Learning/2026-08-06-w4-alg-f2-contains-duplicate-review|W4-ALG-F2 PASS 复盘]]
