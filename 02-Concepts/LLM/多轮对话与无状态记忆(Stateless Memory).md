---
aliases:
  - multi-turn-stateless-memory
type: concept
topic: LLM
status: usable
created: 2026-06-17
updated: 2026-06-27
source:
  - AI-Agent-Learning L1-03
  - AI-Agent-Learning L1-Gate 设计准备
tags:
  - LLM
  - 多轮对话
  - 记忆
  - DeepSeek
---

# 多轮对话：接口无状态与客户端记忆

## 一句话解释

`chat.completions` 接口是**无状态**的：服务端在两次请求之间什么都不记。所谓「多轮记忆」不是模型记住了你，而是**客户端代码每一轮都把历史对话重新发一遍**。

## 核心：记忆落在客户端

- 服务端不保存上一轮。你这次不发，模型就看不到。
- 「记住对话」是你代码的责任：维护一个 `history`，每轮把它一起发出去。
- 每轮发出去的 `messages` = `[SYSTEM] + history + [本轮 user]`，**SYSTEM 也要每轮重发**（不是只发一次）。

```python
history = []                      # 记忆存这里，直接用 messages 格式
while True:
    question = input("你：")
    messages = [SYSTEM] + history + [{"role": "user", "content": question}]
    answer = call_messages(messages)          # 整盘对话一起发
    history.append({"role": "user", "content": question})
    history.append({"role": "assistant", "content": answer})
    history = trim_history(history)            # 只留最近 N 轮
```

## history 直接存成 messages 格式

每条消息就存成 API 要的 `{"role": ..., "content": ...}`，发送时零转换：

- `role` 只能是 `system` / `user` / `assistant`（不是 `model`）。
- 一轮对话 = 2 条消息（一条 user + 一条 assistant）。

## append 和 trim 各管什么

- `history.append(...)`：决定**记不记**——把本轮问答累积进 history。删掉 append → history 永远为空 → 每轮只发 `[SYSTEM, 本轮 user]` → 退化成单轮。
- `trim_history(...)`：决定**记多久**——只留最近 `MAX_TURNS` 轮。1 轮 = 2 条，所以切 `history[-MAX_TURNS*2:]`，`*2` 保证不从半轮切断（奇数切片会留下以 assistant 开头的残缺历史）。

## SYSTEM 记忆 vs 多轮 history 记忆

想让助手「永远记得用户叫三玖」，可以放进 SYSTEM：`{"role":"system","content":"用户叫三玖"}`。它和多轮 history 的区别：

| | SYSTEM 固定事实 | 多轮 history |
|---|---|---|
| 谁来发 | 每轮都重发（无状态，两者都得重发） | 每轮都重发 |
| 会不会被裁 | **不进 trim，永远带着** | 动态增长，**超长会被 trim 砍旧的** |
| 能装新信息吗 | 写死的，模型没法聊天中往里「学」新事实 | 能接住用户中途说的新信息 |

一句话：**SYSTEM = 写死、不裁的固定事实；history = 会裁的动态对话累积**。两者都因为「无状态」而每轮重发。

## 常见坑

- 以为「SYSTEM 只发一次、之后模型就记住了」——错。无状态 = 每轮都要把 SYSTEM 连同 history 重发。
- 删了 `append` 还按「N 轮上限 / 切片」去想——此时 history 恒为空，trim 无东西可砍。
- 忘记历史（没喂够上下文）≠ 幻觉（无依据编造）。trim 丢历史属于前者。
- **顺序坑：trim 砍在 append 之前（先砍后存）**——砍的是「还没算上本轮」的旧 history，于是每轮实际发出去的历史比 `MAX_TURNS` 多一轮，限长滞后、形同失效。顺序必须「**先存（成对 append user+assistant）后砍**」，trim 放在循环末尾。
- 把 `[SYSTEM] + history` 写成 `SYSTEM + history`——`dict + list` 直接相加报 `TypeError`，单个 dict 要 `[ ]` 包成 list（见 [[../Python/list·dict·set 容器|Python list、dict、set]]）。

## 关联

- [[调用 chat.completions|调用 LLM：chat.completions 与取回复]]：怎么发 `messages`、怎么取回复。
- [[消息角色与指令优先级(Instruction Hierarchy)|消息角色与指令优先级]]：system/user/assistant 的角色分工。
- [[流式输出(Streaming)|流式输出：stream=True 与逐 chunk 处理]]：把这套多轮接成流式版（L1-04）；流式函数要 return 完整 answer 才能进 history。
- [[自回归生成(Autoregressive)|Autoregressive Generation]]：`stream=True` 逐 token 返回的底层原因。
- [[文件读写与 JSON 序列化|Python 文件读写与 JSON 序列化]]：把 history 存盘续聊（dict 不丢类型，tuple 会变 list）。

## 来源

- AI-Agent-Learning L1-03：`C:\Users\26823\Desktop\AI-Agent-Learning\code\stage1\l1_03_chat.py`
- 每日记录：`C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-06-16.md`
