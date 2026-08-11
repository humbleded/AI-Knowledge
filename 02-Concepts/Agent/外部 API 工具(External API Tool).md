---
type: concept
topic: External API Tool
status: evergreen
created: 2026-07-08
updated: 2026-07-12
source:
  - C:\Users\26823\Desktop\AI-Agent-Learning\code\stage3\t3_04_public_api_tool.py
  - C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-07-08.md
  - C:\Users\26823\Desktop\AI-Agent-Learning\code\stage3\t3_gate_tool_assistant.py
  - C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-07-11.md
tags:
  - Agent
  - Tool-Calling
  - HTTP
  - API
  - Python
aliases:
  - External API Tool
---

# 外部 API 工具(External API Tool)

## 一句话

外部 API 工具就是让 Agent 通过客户端程序访问真实外部服务：模型负责提出“要查哪个 API”，客户端程序负责发 HTTP 请求，工具函数把结果整理成模型能读懂的稳定结构。

## 为什么需要

LLM 本身不能真正联网，也不知道“此刻”某个 API 是否能访问、剩余额度是多少、服务器返回什么状态码。遇到当前外部状态、实时数据或第三方服务结果时，模型不能靠训练记忆猜，要通过工具获取真实结果。

典型分工：

```text
LLM -> 选择工具和参数
客户端程序 -> 解析工具调用并执行函数
public_api_tool -> 发 HTTP 请求并返回结构化 dict
客户端程序 -> 把 dict 作为 Observation/tool message 放回上下文
LLM -> 根据 Observation 整理最终回答
```

## 最小实现

```python
def public_api_tool(url=API_URL):
    try:
        import requests
    except ImportError:
        return {"ok": False, "error": "请先安装 requests：pip install requests"}

    try:
        response = requests.get(url, timeout=5, allow_redirects=False)
    except requests.Timeout:
        return {"ok": False, "error": "请求超时"}
    except requests.RequestException as exc:
        return {"ok": False, "error": f"请求失败：{exc}"}

    if 300 <= response.status_code < 400:
        return {
            "ok": False,
            "error": "拒绝重定向",
            "status_code": response.status_code,
        }

    return {
        "ok": response.ok,
        "status_code": response.status_code,
        "server": response.headers.get("Server"),
        "rate_limit_limit": response.headers.get("X-RateLimit-Limit"),
        "rate_limit_remaining": response.headers.get("X-RateLimit-Remaining"),
    }
```

## 设计要点

### 1. 必须设置 timeout

`timeout=5` 表示最多等 5 秒。没有 timeout 时，外部 API 卡住会拖死整条 Agent 链路，后续 Observation 回填和模型回答都无法继续。

### 2. 失败时返回稳定 dict

工具失败不要把异常直接甩出去。更适合 Agent 的返回是：

```python
{"ok": False, "error": "请求超时"}
{"ok": False, "error": "请求失败：..."}
```

这样客户端还能把失败结果作为 Observation 回填给模型，让模型解释失败、提示用户稍后重试，或选择其他工具。

### 3. 只返回必要字段

外部 API 的原始 JSON 往往很大。工具输出应该是“给模型看的摘要结果”，不是把完整 `response.json()` 搬进上下文。

今天的必要字段：

```python
{
    "ok": response.ok,
    "status_code": response.status_code,
    "server": response.headers.get("Server"),
    "rate_limit_limit": response.headers.get("X-RateLimit-Limit"),
    "rate_limit_remaining": response.headers.get("X-RateLimit-Remaining"),
}
```

`rate_limit_limit` 是当前限流窗口总额度；`rate_limit_remaining` 是剩余调用次数。

### 4. 404 不是请求异常

`requests.get()` 拿到 404 时，说明服务器已经正常返回响应，只是路径资源不存在。它不会进入 `except requests.RequestException`。

判断方式：

```python
response.ok          # 404 时 False
response.status_code # 404
```

只有超时、连接失败、非法 URL 等请求过程中没有正常拿到响应的情况，才走异常分支。

## Agent 工具的 URL 安全边界

仅仅“能请求 URL”还不够。模型参数和用户输入都不可信，客户端应在真正发请求前限制：

这类“让服务器替攻击者访问其原本无法直接访问的目标”的风险，叫作 [[02-Concepts/Engineering/服务端请求伪造(SSRF)|服务端请求伪造（SSRF）]]。

- scheme 必须是 `https`；
- hostname 必须在明确 allowlist；
- 只允许未显式写端口或标准 `443`；
- 拒绝 userinfo 绕过、localhost、私网、link-local 和云 metadata 目标；
- 禁止自动跟随重定向，或逐跳重新校验每个 `Location`。

### `urlparse()` 不等于 URL 安全校验器

`urlparse()` 是宽松解析器。对 `https://api.github.com:`，它可能解析出合法 hostname，且 `.port` 为 `None`；这不表示解析器已经把空端口赋值为 443。应额外拒绝：

```python
if parsed_url.netloc.endswith(":"):
    return {"ok": False, "error": "url 字段端口号不合法"}
```

随后只允许：

```python
parsed_url.port in (None, 443)
```

### 为什么默认重定向危险

`requests` 默认跟随 301/302 等跳转。如果客户端只检查初始允许 URL，服务器仍可能把请求重定向到 `127.0.0.1`、私网或 metadata 地址，形成 [[02-Concepts/Engineering/服务端请求伪造(SSRF)|SSRF]] 绕过。

本次 Gate 采用最保守策略：

```python
requests.get(url, timeout=5, allow_redirects=False)
```

收到 3xx 就稳定拒绝。取舍是合法 API 的重定向也会失败；未来若确需允许，必须限制跳转次数，并对每一跳的 `Location` 重新执行 scheme/host/port/IP 校验。

> [!warning] 剩余风险
> 仅校验字符串 hostname 还不能覆盖 DNS rebinding、解析后 IP 变化等问题。完整网络工具需要在后续安全任务中校验解析 IP，并防止连接阶段发生目标漂移。

## 今日易错点

- `response` 是响应对象，不只是响应体；里面有 `ok`、`status_code`、`headers`、正文等。
- 异常分支里可能根本没有 `response`，所以不能写 `response.ok`。
- `server` 字段来自 `response.headers.get("Server")`，不是 URL 主机名。
- 捕获 `RequestException` 不是为了继续抛出异常，而是为了返回稳定 `{"ok": False, "error": ...}`。
- 404/500 不会被 `requests` 自动当异常抛出，需要主动看 `response.ok/status_code`。
- `urlparse().port is None` 不代表显式空端口合法；空 `:` 要单独拒绝。
- 只校验初始 URL 后自动跟随 302，仍可能访问本地或私网目标。

## 迁移模板

如果以后写天气工具 `weather_api_tool(city)`，同样要有：

- 清楚的工具职责边界：只负责查询天气，不负责闲聊。
- `timeout`。
- `requests.Timeout` / `requests.RequestException` 兜底。
- HTTPS、host/port allowlist 与重定向策略。
- 成功时只返回必要字段，例如 `city/weather/temperature/update_time/source`。
- 失败时返回稳定 `ok/error`。

## 相关

- [[02-Concepts/Engineering/服务端请求伪造(SSRF)|服务端请求伪造（SSRF）]]
- [[工具定义与执行协议(Tool Definition)]]
- [[文件工具沙箱(File Tool Sandbox)]]
- [[../../Engineering/HTTP 请求全链路与错误处理|HTTP 请求全链路与错误处理]]
- [[../../LLM/函数调用(Function Calling)|函数调用 / Tool Calling]]
- [[../../../04-Projects/Agent/AI-Agent-Learning/t3-04-public-api-tool|T3-04 外部 API 工具]]
- [[../../../07-Reviews/AI-Agent-Learning/2026-07-08-t3-04-public-api-tool-review|2026-07-08 T3-04 PASS 复盘]]
- [[../../../04-Projects/Agent/AI-Agent-Learning/t3-gate-tool-assistant|T3-Gate 三工具助手]]
- [[../../../07-Reviews/AI-Agent-Learning/2026-07-12-t3-gate-tool-calling-review|2026-07-12 T3-Gate PASS 复盘]]
