---
type: concept
topic: LLM
status: usable
created: 2026-06-27
source:
  - AI-Agent-Learning L1-Gate
tags:
  - LLM
  - SDK
  - API
  - timeout
  - DeepSeek
---

# API 参数 vs SDK 客户端参数

## 一句话解释

调一次模型时传的参数分两层：**API 参数**会被打包进请求体发给服务器、由模型/服务端处理（如 `model`、`messages`、`temperature`、`stream`）；**SDK 客户端参数**只在你本机这边起作用、不进请求体、不发给服务器（如 `timeout`、`max_retries`）。两者文档归属不同，混在同一个 `create()` 调用里很容易以为是同一类。

## 判断法（一句话定位它在哪层）

> **会发给服务器、影响模型怎么生成 → API 参数（查 DeepSeek API 文档）；只在本机管「怎么发、等多久、重试几次」→ SDK 客户端参数（查 OpenAI SDK 文档/源码）。**

| | API 参数 | SDK 客户端参数 |
|---|---|---|
| 例子 | `model` / `messages` / `temperature` / `top_p` / `stream` | `timeout` / `max_retries` |
| 进请求体吗 | 进，发给服务器 | 不进，本机生效 |
| 谁处理 | DeepSeek 服务端 / 模型 | OpenAI SDK + 底层 httpx |
| 文档在哪 | **DeepSeek API 文档** | **OpenAI SDK 文档 / 源码** |
| 查不到时 | 八成是 SDK 参数，别在 API 文档里找 | —— |

**典型困惑**：在 DeepSeek 官方 API 文档里搜 `timeout` 搜不到，却确实能用——因为它根本不是 API 参数，是 SDK 参数。

## timeout：两种写法，作用域不同

```python
# 写法一：客户端级——这个 client 发的所有请求都带 30s 超时
client = OpenAI(api_key=key, base_url="https://api.deepseek.com", timeout=30)

# 写法二：单次请求级——只管这一次调用（覆盖客户端默认）
resp = client.chat.completions.create(model="...", messages=msgs, timeout=60)
```

- **client 级**：省事，全局兜底（L1-Gate 里两个文件用的就是这个）。
- **create 级**：针对性强，「只给某一次超大请求放宽超时」就写这里。
- 不设 `timeout`：SDK 默认要等很久（约 10 分钟）才放弃，用户会以为程序卡死。设 30s → 超时即 `APITimeoutError`，被 `except` 接住返回友好提示。

SDK 的 `create()` 签名里确有这个参数：

```python
timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
```

## max_retries：另一个同层参数

- `OpenAI(..., max_retries=2)`：SDK 默认超时/网络错后**自动重试 2 次**再放弃——所以一次超时可能拖更久。
- 同样是 SDK 参数、不在 DeepSeek API 文档里。调试超时时把它设 `0` 能让超时立刻可见。

## 本机验证（不靠外网也能证明 timeout 真触发）

起一个「只接受连接、永不回应」的本地假服务器，把 `base_url` 指向它、设 `timeout=2`、`max_retries=0`：

```text
[create(..., timeout=2)]  ~2s 后抛出 → APITimeoutError
[OpenAI(timeout=2)]       ~2s 后抛出 → APITimeoutError
```

两种写法都在 ~2 秒触发，且抛的 `APITimeoutError` 是 `Exception` 子类 → 被 `except Exception` 稳稳接住。**timeout（本机掐表）+ except（兜底）合起来才是完整的超时保护。**

## 常见坑

- 在 DeepSeek API 文档里找 `timeout`/`max_retries` 找不到就以为「不支持」——它们是 SDK 参数，去 OpenAI SDK 文档/源码查。
- 以为 `timeout` 只能写在 `create()`——也能写在 `OpenAI()`，作用域是「这个 client 的所有请求」。
- 只加 `timeout` 不加 `except`，或只加 `except` 不加 `timeout`——前者超时仍抛异常崩、后者干等很久。两个一起才完整。

## 关联

- [[chat-completions-call|调用 LLM：chat.completions 与取回复]]：API 参数（messages/取回复）的那一层。
- [[api-key-and-sdk|API Key 与 SDK]]：SDK 是「门禁卡 + 快递柜台」，timeout/max_retries 属柜台这边的规矩。
- [[streaming-output|流式输出]]：`stream` 是 API 参数（改服务端返回形态），`timeout` 是 SDK 参数（改本机等待）。
- [[../Engineering/http-and-network-basics|HTTP 与网络基础]]：timeout 保护客户端、防止干等，是网络层的工程意识。

## 来源

- AI-Agent-Learning L1-Gate：`C:\Users\26823\Desktop\AI-Agent-Learning\code\stage1\l1_gate_cli_chatbot.py`、`l1_03_chat.py`、`l1_04_stream_chat.py`
- 每日记录：`C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-06-27.md`
