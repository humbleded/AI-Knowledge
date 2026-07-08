---
type: concept
topic: External API Tool
status: evergreen
created: 2026-07-08
source:
  - C:\Users\26823\Desktop\AI-Agent-Learning\code\stage3\t3_04_public_api_tool.py
  - C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-07-08.md
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
        response = requests.get(url, timeout=5)
    except requests.Timeout:
        return {"ok": False, "error": "请求超时"}
    except requests.RequestException as exc:
        return {"ok": False, "error": f"请求失败：{exc}"}

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

## 今日易错点

- `response` 是响应对象，不只是响应体；里面有 `ok`、`status_code`、`headers`、正文等。
- 异常分支里可能根本没有 `response`，所以不能写 `response.ok`。
- `server` 字段来自 `response.headers.get("Server")`，不是 URL 主机名。
- 捕获 `RequestException` 不是为了继续抛出异常，而是为了返回稳定 `{"ok": False, "error": ...}`。
- 404/500 不会被 `requests` 自动当异常抛出，需要主动看 `response.ok/status_code`。

## 迁移模板

如果以后写天气工具 `weather_api_tool(city)`，同样要有：

- 清楚的工具职责边界：只负责查询天气，不负责闲聊。
- `timeout`。
- `requests.Timeout` / `requests.RequestException` 兜底。
- 成功时只返回必要字段，例如 `city/weather/temperature/update_time/source`。
- 失败时返回稳定 `ok/error`。

## 相关

- [[工具定义与执行协议(Tool Definition)]]
- [[文件工具沙箱(File Tool Sandbox)]]
- [[../../Engineering/HTTP 请求全链路与错误处理|HTTP 请求全链路与错误处理]]
- [[../../LLM/函数调用(Function Calling)|函数调用 / Tool Calling]]
- [[../../../04-Projects/Agent/AI-Agent-Learning/t3-04-public-api-tool|T3-04 外部 API 工具]]
- [[../../../07-Reviews/AI-Agent-Learning/2026-07-08-t3-04-public-api-tool-review|2026-07-08 T3-04 PASS 复盘]]
