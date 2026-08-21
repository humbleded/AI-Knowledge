---
aliases:
  - api-params-vs-sdk-client-params
type: concept
topic: LLM
status: usable
created: 2026-06-27
updated: 2026-08-21
source:
  - AI-Agent-Learning L1-Gate
  - C:\Users\26823\Desktop\AI-Agent-Learning\code\stage4\a4_gate_research_summary_agent.py
  - C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-08-21.md
  - https://github.com/openai/openai-python#retries
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

- `OpenAI(..., max_retries=2)`：对 SDK 白名单内的失败，首次物理请求后最多再自动重试 2 次，所以一次 SDK 逻辑调用最多包含 3 次物理 HTTP 尝试。
- OpenAI Python SDK 当前公开文档列出的默认自动重试范围包括连接错误、HTTP 408、409、429 和 500 以上状态；timeout 也会按默认重试设置处理。这个列表是版本敏感事实，使用前要核对实际依赖版本与官方文档。
- 同样是 SDK 参数、不在 DeepSeek API 文档里。调试超时时把它设 `0` 能让超时立刻可见。

### 逻辑调用与物理尝试不要混为一谈

```text
应用代码调用一次 client.chat.completions.create(...)
  = 1 次 SDK 逻辑调用
  = 首次 HTTP + 最多 max_retries 次 SDK 内部 HTTP 重试
```

例如 `max_retries=2` 时：

- 逻辑调用成功或第一次就遇到不重试错误：可能只有 1 次物理请求；
- 持续遇到 SDK 重试白名单错误：最多有 3 次物理请求；
- Agent 在 SDK 最终失败后又额外发起一次 Provider recovery：一共是 2 次逻辑调用，极端最多 `2 × 3 = 6` 次物理请求。

Agent 的 step / 应用日志应该按**逻辑调用**记账，SDK 内部物理尝试则由 transport 日志、spy transport 或服务端计数验证。不能从“Agent 有两个 step”直接推断“只有两个 HTTP 请求”。

### fake client、真实 factory 与 `_request_id` 分别能证明什么

| 证据 | 能证明 | 不能证明 |
|---|---|---|
| fake / scripted client | Agent 成功、异常、恢复和停止编排是否符合合同 | 真实 `OpenAI(...)` factory 是否传入了 `max_retries` / `timeout`，SDK transport 是否真的重试 |
| `client = create_deepseek_client(); client.max_retries` / `client.timeout` | 当前真实 factory 返回对象上的生效配置 | 实际某次调用究竟发生了几次物理 HTTP 尝试 |
| response 的 `_request_id`，或失败 `APIStatusError.request_id` | 从 `x-request-id` 取得请求标识，便于日志定位和支持排查 | client 的重试配置、重试次数；连接失败 / timeout 甚至可能没有服务端 response ID |
| transport / 服务端请求计数 | 某次实验真实发送了几次物理请求 | Agent 的业务阶段是否允许再次发起新的逻辑调用 |

因此，验证真实 factory 的最小探针是：

```python
client = create_deepseek_client()
try:
    assert client.max_retries == 2
    assert client.timeout == 60.0
finally:
    client.close()
```

它证明配置值，不声称已经触发了两次自动重试。要证明物理尝试次数，必须换成可计数 transport / 测试服务器等专门证据。

## timeout 要根据代表性延迟分布调，不凭一次感觉

timeout 是“单次物理请求最多等多久”的止损参数，不是越小越好或越大越稳定：

- 代表性正常请求长期在 5～18 秒完成，当前 60 秒没有正常超时：保持，单次成功不足以支持继续调小；
- 20 次代表性请求有 6 次在 60 秒前超时，改为 90 秒后这些请求能在 65～78 秒稳定成功且质量合格：有调大证据；
- 包含高峰期的长期样本最慢也只有 16 秒，并且业务更重视快速止损：可以逐步调小，再做回归与观测；
- 偶发一次 `APITimeoutError`：先分清网络、Provider 高峰、输入规模和 SDK 自动重试聚合耗时，不能单凭一个点立刻改合同。

修改 timeout 时要同步检查 `max_retries`：每次物理请求的 timeout 乘上最多尝试次数，再加退避时间，才接近一次逻辑调用的最坏等待上界。

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
- 把 `max_retries=2` 理解成“总共两次请求”——它表示首次请求之外最多再重试两次，总物理尝试上限是 3。
- 用 fake client 的成功/异常断言证明真实 SDK 配置——fake 绕过了真实 constructor、transport 与 SDK 内部重试。
- 用 `_request_id` 证明重试配置或物理次数——它是排障关联 ID，不是 retry counter。
- 只看单次正常 smoke 就调小 timeout，或只看一次 timeout 就调大——都缺代表性延迟分布和调整后的成功/质量证据。

## 关联

- [[调用 chat.completions|调用 LLM：chat.completions 与取回复]]：API 参数（messages/取回复）的那一层。
- [[API Key 与 SDK|API Key 与 SDK]]：SDK 是「门禁卡 + 快递柜台」，timeout/max_retries 属柜台这边的规矩。
- [[流式输出(Streaming)|流式输出]]：`stream` 是 API 参数（改服务端返回形态），`timeout` 是 SDK 参数（改本机等待）。
- [[../Engineering/HTTP 请求全链路与错误处理|HTTP 与网络基础]]：timeout 保护客户端、防止干等，是网络层的工程意识。
- [[../Agent/受控重试与人工接管(Bounded Retry and Human Handoff)|受控重试与人工接管]]：SDK 自动重试与 Agent Provider recovery 的分层账本、完整链预算和停止边界。
- [[../../04-Projects/Agent/AI-Agent-Learning/a4-gate-research-summary-agent|A4-Gate 研究摘要 Agent]]：`max_retries=2`、单请求 timeout 60 秒与 Candidate Provider recovery 的可执行证据。

## 来源

- AI-Agent-Learning L1-Gate：`C:\Users\26823\Desktop\AI-Agent-Learning\code\stage1\l1_gate_cli_chatbot.py`、`l1_03_chat.py`、`l1_04_stream_chat.py`
- 每日记录：`C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-06-27.md`
- AI-Agent-Learning A4-Gate Candidate Provider：`C:\Users\26823\Desktop\AI-Agent-Learning\code\stage4\a4_gate_research_summary_agent.py`、`daily\2026-08-21.md`
- [A4-Gate Candidate Provider/API 实现与证据提交 `5fac2ba`](https://github.com/humbleded/AI-Agent-Learning/commit/5fac2bab123ed31232ca9d96a05d2dca51509d96)
- [OpenAI Python SDK README：Request IDs、Retries、Timeouts](https://github.com/openai/openai-python#request-ids)（检查日期：2026-08-21；本项目环境 `openai==2.41.1`）
