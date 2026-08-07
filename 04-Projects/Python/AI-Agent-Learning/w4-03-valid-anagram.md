---
type: project
topic: AI-Agent-Learning W4-03 有效的字母异位词
status: pass
created: 2026-08-06
updated: 2026-08-06
source:
  - C:\Users\26823\Desktop\AI-Agent-Learning\code\algorithms\w4_03_valid_anagram.py
  - C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-08-06.md
tags:
  - Python
  - Algorithms
  - 字符串
  - 哈希表
  - AI-Agent-Learning
---

# W4-03 有效的字母异位词

## 任务与结果

两个字符串只包含小写英文字母；当且仅当二者包含的字符及每个字符的出现次数完全相同时返回 `True`。

- 产物：`C:\Users\26823\Desktop\AI-Agent-Learning\code\algorithms\w4_03_valid_anagram.py`
- 正式判定：**PASS（2026-08-06）**。
- W4 状态：正式 PASS `2/4`，仍为 `DEBT`，剩余 2 道。

## 解法

1. 长度不同直接返回 `False`。
2. 分别遍历两个字符串，用两张字典统计“字符 → 出现次数”。
3. 比较两张字典；键和值都相同才返回 `True`。

当前实现还保留了排序对照函数 `is_anagram_sort()`，但规定接口和全部断言都直接使用计数字典版本 `is_anagram()`。

## 正式验证

- `.venv\Scripts\python.exe -W error -m py_compile code\algorithms\w4_03_valid_anagram.py`：通过。
- `.venv\Scripts\python.exe code\algorithms\w4_03_valid_anagram.py`：8 条显式断言全部通过，输出 `All tests passed.`。
- 性质检查：对字母表 `abc`、长度 0～4 的全部 121 个字符串做 14,641 组有序对照，结果与 `sorted(s) == sorted(t)` 完全一致。
- 返回类型全部为 `bool`；两个 1 万字符真假用例均通过。

## 独立性与订正轨迹

- 学习者先独立提出“逐字符统计次数，再比较两份计数”，随后自行完成双字典实现；没有展示参考答案。
- 首次代码把可用逻辑写在辅助函数中，规定接口 `is_anagram()` 没有实现；断言又只调用辅助函数，形成脚本全绿但交付接口返回 `None` 的假绿灯。
- 订正后 8 条断言全部调用规定接口，并加入“字符种类相同但次数不同”和长度不同的反例。
- 复杂度曾把空间误判为 `O(n²)`，又把固定 26 种字符误套到扫描时间；最后能分别计算输入扫描量和字典键数。

## 复杂度

- 当前小写字母合同：平均时间 `O(n)`，额外空间 `O(1)`。
- 一般字符集：平均时间 `O(n)`，额外空间 `O(k)`；`k` 是不同字符数且 `k <= n`，所以最坏空间为 `O(n)`。
- 单次字典操作平均 `O(1)`，但循环执行 `n` 次，因此循环整体仍是 `O(n)`；字典相等比较为 `O(k)`，不改变总体线性时间。

## 相关链接

- [[../../../02-Concepts/Python/list·dict·set 容器|Python list、dict、set：字符频次计数]]
- [[../../../02-Concepts/Python/异常·调试·测试(Exceptions)|Python 测试：避免交付接口假绿]]
- [[../../../07-Reviews/AI-Agent-Learning/2026-08-06-w4-alg-f3-valid-anagram-review|W4-ALG-F3 PASS 复盘]]
