---
aliases:
  - python-list-dict-set
type: concept
topic: Python
status: usable
created: 2026-06-02
updated: 2026-08-08
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

## list 拼接：`+` 两边必须都是 list（拼 messages 常踩）

`list + list` 把两个列表接成一个新列表。关键限制：`+` **两边都必须是 list**，不能拿 list 直接加一个 dict、字符串或单个元素。

```python
[1, 2] + [3]        # [1, 2, 3]  ✅ list + list
[1, 2] + 3          # ❌ TypeError: can only concatenate list (not "int") to list
{"a": 1} + [2]      # ❌ TypeError: unsupported operand type(s) for +: 'dict' and 'list'
```

想把**单个 dict（或单个值）拼进 list**，先用 `[ ]` 把它包成「单元素 list」再相加：

```python
SYSTEM = {"role": "system", "content": "..."}
history = [{"role": "user", "content": "hi"}, {"role": "assistant", "content": "你好"}]

[SYSTEM] + history + [{"role": "user", "content": question}]   # ✅ 三个都是 list
SYSTEM + history                                                # ❌ dict + list 直接相加报错
```

这正是拼 LLM `messages` 的标准写法：`SYSTEM` 和本轮 user 都是 dict，必须各自用 `[ ]` 包成单元素 list，才能和 list 形态的 `history` 用 `+` 接到一起。

- 错误理解：`SYSTEM + history` 能把 system 放到历史前面。
- 正确理解：`dict + list` 类型不匹配，直接 `TypeError`；要写成 `[SYSTEM] + history`。

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

## 成员检查复杂度与“已见元素”模式

判断列表中是否有重复元素时，可以一边遍历，一边维护“已经见过的值”。容器选型会直接改变复杂度：

| 写法 | 单次成员检查 | 遍历 `n` 个元素的常规结果 | 适用情况 |
|---|---:|---:|---|
| `num in seen_list` | `O(n)` | 最坏 `O(n²)` | 数据很小、需要列表顺序或重复项本身 |
| `num in seen_dict` | 平均 `O(1)` | 平均 `O(n)` | 还要保存下标、次数或其他元数据 |
| `num in seen_set` | 平均 `O(1)` | 平均 `O(n)` | 只关心某个值是否出现过 |

使用 `dict` 的版本：

```python
def contains_duplicate(nums: list[int]) -> bool:
    seen = {}

    for num in nums:
        if num in seen:
            return True
        seen[num] = True

    return False
```

循环最多处理 `n` 个元素，每次字典查询和写入平均为 `O(1)`，因此平均时间复杂度为 `O(n)`。全部元素都不重复时，字典最多保存 `n` 个键，所以额外空间复杂度为 `O(n)`。

这里只说“平均”很重要：哈希表在极端碰撞下存在更差的理论最坏情况；常规算法题若未特别要求，通常按平均哈希操作分析。若只需要判断存在性，用 `set` 会更直接；需要保留下标或计数时再用 `dict`。

测试预期也必须服从精确的相等语义：`-2 != 2`，绝对值相同不等于整数重复。负数重复案例应真正包含两次同一个值，例如 `[-2, -2, 3]`。

## 两数之和：补数查询与“值 → 下标”映射

当题目要求找出两个不同元素，使它们的和等于 `target`，遍历到当前数字 `num` 时，真正需要寻找的是它的补数：

```python
complement = target - num
```

字典保存“此前见过的数字 → 它的下标”，因为最终结果需要返回下标：

```python
def two_sum(nums: list[int], target: int) -> list[int]:
    lookup = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in lookup:
            return [lookup[complement], i]
        lookup[num] = i

    return []
```

顺序必须是“先查补数，再保存当前数”。如果先执行 `lookup[num] = i`，当 `target == 2 * num` 时，当前元素可能立刻与自己匹配，重复使用同一个下标。两个不同下标上的相同数值仍然可以组成合法答案，例如 `[4, 4]`；禁止的是同一下标自用，不是禁止重复值。

复杂度仍要把单次操作和整段循环分开：最多遍历 `n` 个元素，每次字典查询/写入平均 `O(1)`，所以平均时间为 `O(n)`；最坏需要保存 `n` 个“值 → 下标”映射，所以额外空间为 `O(n)`。

## 相近重复：在线维护“值 → 最近下标”

如果题目不只问“有没有重复”，还要求两个相同值的下标距离不超过 `k`，只记录“见过这个值”已经不够。字典应保存：

```text
值 → 这个值最近一次出现的下标
```

```python
def contains_nearby_duplicate(nums: list[int], k: int) -> bool:
    last_seen = {}

    for i, num in enumerate(nums):
        if num in last_seen and i - last_seen[num] <= k:
            return True
        last_seen[num] = i

    return False
```

顺序是“先比较，再更新”：

1. 当前值以前出现过，就用当前下标减去它最近一次的下标。
2. 距离不超过 `k`，立即返回 `True`。
3. 没命中也要把记录更新为当前下标，给后面的元素保留更近的比较对象。

为什么只保存最近下标就够？固定当前下标 `i` 后，以前出现过的下标越大，`i - 历史下标` 越小。最近一次都超过 `k` 时，更早的下标只会更远；最近一次满足条件时已经可以直接返回。因此不需要保存全部历史下标，也不需要在循环结束后再两两比较。

例如 `nums = [1, 2, 1, 1]`、`k = 1`：

- 下标 `2` 遇到第二个 `1`，与下标 `0` 的距离为 `2`，暂不命中，但要把 `1` 的最近下标更新为 `2`。
- 下标 `3` 再遇到 `1`，与最近下标 `2` 的距离为 `1`，返回 `True`。

`k = 0` 时一定返回 `False`：题目要求两个下标不同，而不同整数下标的距离至少为 `1`。代码里不需要调用 `abs()`，因为保存的历史下标总小于当前下标，所以 `i - last_seen[num]` 已经非负。

复杂度仍需分三层说明：循环最多处理 `n` 项；每次字典成员检查、读取和写入按平均 `O(1)` 计算；字典最多保存 `n` 个不同值。因此平均时间为 `O(n)`，额外空间为 `O(n)`。

- 错误理解：先遍历完再计算所有重复值的距离，或者一直保留第一次出现的下标。
- 正确理解：扫描过程中在线判断，并在每次未命中后更新最近下标；这样既不会漏掉后续更近的一对，也避免退化为两两比较。

来源/证据：[[../../04-Projects/Python/AI-Agent-Learning/w4-04-contains-nearby-duplicate|W4-04 存在相近的重复元素]]，规定断言 8/8、性质对照 136717/136717，输入未修改。

## 字符频次计数：扫描量与字典规模分开算

判断两个字符串是否由完全相同的字符及次数组成时，可以分别建立“字符 → 出现次数”的字典，再比较两张字典：

```python
def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    count_s = {}
    count_t = {}

    for char in s:
        count_s[char] = count_s.get(char, 0) + 1
    for char in t:
        count_t[char] = count_t.get(char, 0) + 1

    return count_s == count_t
```

复杂度要把三件事分开：

1. 一次 `dict.get()` 或写入按常规平均口径是 `O(1)`。
2. 循环仍要处理全部输入字符。两个长度均为 `n` 的字符串共处理 `2n` 个字符，忽略常数后是 `O(n)`，不会因为字符只有 26 种就变成 `O(1)`。
3. 字典保存的是不同字符的键，不是每次扫描都新建一个键。题目限定 26 个小写字母时，两张字典的键数都有固定上限，因此额外空间是 `O(1)`；若字符种类不固定，设不同字符总数为 `k`，则额外空间是 `O(k)`，且 `k <= n`，最坏为 `O(n)`。

字典相等比较至多检查已保存的不同键，时间为 `O(k)`；在固定 26 个小写字母的合同下可视为 `O(1)`，在一般字符集下也不超过前面扫描输入的 `O(n)`，所以总体时间仍是 `O(n)`。

## set 去重的代价

`set` 的查找和去重通常很快，但代价是：

- 丢失重复次数。
- 不适合表达稳定的业务顺序。
- 无法直接保留每个元素来自哪个任务、哪一天或哪条记录。
- 元素必须可哈希。
- 会占用额外内存。

## 相关

- [[基础数据类型(Data Types)]]
- [[条件判断与循环(if & for)]]
- [[../LLM/多轮对话与无状态记忆(Stateless Memory)|多轮对话：接口无状态与客户端记忆]]：`[SYSTEM] + history + [user]` 拼 messages 正是「单个 dict 要 `[ ]` 包成 list」的应用。
- [[../../07-Reviews/Daily-Practice/2026-06-05-review]]
- [[../../04-Projects/Python/AI-Agent-Learning/w4-02-contains-duplicate|W4-02 存在重复元素项目记录]]
- [[../../04-Projects/Python/AI-Agent-Learning/w4-03-valid-anagram|W4-03 有效的字母异位词项目记录]]
- [[../../04-Projects/Python/AI-Agent-Learning/w4-01-two-sum|W4-01 两数之和项目记录]]
- [[../../04-Projects/Python/AI-Agent-Learning/w4-04-contains-nearby-duplicate|W4-04 存在相近的重复元素项目记录]]
