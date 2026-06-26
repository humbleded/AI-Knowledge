---
type: course-note
topic: AI-Agent-Learning Stage 1
status: active
created: 2026-06-14
updated: 2026-06-18
tags:
  - LLM
  - API
  - AI-Agent-Learning
  - Stage1
---

# 阶段 1：大模型 API 入门

## 阶段目标

阶段 1 的目标是能调用大模型 API：完成第一次请求、单轮问答、多轮聊天、流式输出、参数实验和基础错误处理。

这一阶段的重点不是“会问模型一句话”本身，而是建立可复用的调用层：环境变量、SDK、模型名、错误提示、成本意识和后续可扩展的 `call_model()` 封装。

## 当前通过项

| 编号 | 任务 | 状态 | 产物 | 关键结论 |
|---|---|---|---|---|
| L1-01 | API Key 与 SDK | PASS | [[../../../04-Projects/LLM/AI-Agent-Learning/l1-01-first-call]] | 从环境变量读 DeepSeek key，用 OpenAI 兼容 SDK + `base_url` 调用并打印回复；区分 SDK / API / 模型 |
| L1-02 | 单轮问答 | PASS | `code/stage1/l1_02_ask.py` | 复用 `call_model`；空输入有提示；`system` 抽成带默认值参数 |
| L1-03 | 多轮聊天 | PASS | [[../../../02-Concepts/LLM/multi-turn-stateless-memory]] | 接口无状态，记忆 = 客户端每轮重发 `[SYSTEM]+history+本轮`；`append`=记不记 / `trim`=记多久 |
| L1-04 | 流式输出 | PASS | [[../../../02-Concepts/LLM/streaming-output]] | `stream=True` + `for chunk` + `delta.content or ""`；拼回完整文本才能进 history；错误 `return` 字符串而非 None 防毒化 |
| L1-05 | 参数实验与成本意识 | PASS | [[../../../02-Concepts/LLM/sampling-params-and-cost]] | temperature = 概率差距悬殊度（低稳高野，`T→0`=贪心）；top-k/p 砍候选名单；DeepSeek 温度表；成本 = 输入(缓存命中/未命中) + 输出，输出最贵 |

## 已掌握概念

- [[../../../02-Concepts/LLM/api-key-and-sdk]]
- [[../../../02-Concepts/LLM/chat-completions-call]]
- [[../../../02-Concepts/LLM/message-roles-and-instruction-hierarchy]]
- [[../../../02-Concepts/LLM/multi-turn-stateless-memory]]
- [[../../../02-Concepts/LLM/streaming-output]]
- [[../../../02-Concepts/LLM/sampling-params-and-cost]]
- [[../../../02-Concepts/Python/python-venv-pip-env]]
- [[../../../02-Concepts/Python/python-http-requests]]

## 下一步

下一项是 `L1-Gate API 入门闯关`（阶段 1 收尾整合关）。

要做 `code/stage1/l1_gate_cli_chatbot.py`，整合：多轮 + 流式 + 退出命令 + 错误提示 + 历史长度限制。

建议关注：

- 把 L1-01 ~ L1-05 的能力（`call_model` 封装、history 管理、流式、错误提示、参数与成本意识）整合成一个完整 CLI。
- 闯关是整块任务，安排在精力好的整段时间（基本 = 周末）做，工作日不碰 Gate。

## 阶段 0 到阶段 1 的衔接

`P0-Gate` 已证明你能写最小 Python CLI、读写 JSON、做输入校验；`L1-01` ~ `L1-05` 则把这个能力接到真实模型服务上，并补齐流式、参数与成本意识。

后续路线是：

```text
Python CLI 基础 -> 环境变量/SDK(L1-01) -> 单轮(L1-02) -> 多轮(L1-03) -> 流式(L1-04) -> 参数与成本(L1-05) -> API 入门闯关(L1-Gate)
```

复盘：[[../../../07-Reviews/AI-Agent-Learning/2026-06-14-stage0-p0-gate-l1-01-pass-review|2026-06-14 阶段 0 / 阶段 1 复盘]]
