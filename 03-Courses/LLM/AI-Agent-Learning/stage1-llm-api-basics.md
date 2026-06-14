---
type: course-note
topic: AI-Agent-Learning Stage 1
status: active
created: 2026-06-14
updated: 2026-06-14
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
| L1-01 | API Key 与 SDK | PASS | [[../../../04-Projects/LLM/AI-Agent-Learning/l1-01-first-call]] | 能从环境变量读取 DeepSeek key，用 OpenAI 兼容 SDK 调用模型并打印回复 |

## 已掌握概念

- [[../../../02-Concepts/LLM/api-key-and-sdk]]
- [[../../../02-Concepts/LLM/chat-completions-call]]
- [[../../../02-Concepts/Python/python-venv-pip-env]]
- [[../../../02-Concepts/Python/python-http-requests]]

## 下一步

下一项是 `L1-02 单轮问答`。

建议关注：

- 如何把用户输入传给 `call_model(prompt)`。
- 如何让错误提示短、清楚、可操作。
- 如何避免把 key、base_url、model 分散写在多个文件里。

## 阶段 0 到阶段 1 的衔接

`P0-Gate` 已证明你能写最小 Python CLI、读写 JSON、做输入校验；`L1-01` 则开始把这个能力接到真实模型服务上。

后续路线是：

```text
Python CLI 基础 -> 环境变量 / SDK -> 单轮问答 -> 多轮聊天 -> 流式输出 -> API 入门闯关
```

复盘：[[../../../07-Reviews/AI-Agent-Learning/2026-06-14-stage0-p0-gate-l1-01-pass-review|2026-06-14 阶段 0 / 阶段 1 复盘]]
