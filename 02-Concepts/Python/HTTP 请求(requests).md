---
aliases:
  - python-http-requests
type: concept
topic: Python HTTP requests
status: active
created: 2026-06-13
tags:
  - Python
  - HTTP
  - requests
  - API
  - AI-Agent-Learning
---

# Python HTTP 请求：URL、headers、status code 与 JSON

## 核心结论

一次 HTTP API 调用可以先按这条线理解：

`URL -> requests.get(..., timeout=10) -> response.status_code -> response.headers -> response.json()`

- `URL` 是请求服务器资源的地址。
- `headers` 是请求或响应的元信息，不是资源地址，也不是主要数据内容。
- `status_code` 表示服务器如何处理这次请求。
- `response.json()` 会把响应体里的 JSON 文本解析成 Python 数据结构，通常是 `dict` 或 `list`。
- `timeout` 用来避免程序长期卡住，真实 API 调用应该设置超时并处理失败。

## 最小代码

```python
import requests

url = "https://api.github.com"
response = requests.get(url, timeout=10)

print(response.status_code)
print(dict(list(response.headers.items())[:5]))
print(response.json())
```

## URL、headers、body

`URL` 决定请求哪个服务器、哪个路径、哪个资源。例如：

```text
https://api.github.com
```

`headers` 是附加说明或元信息，常见内容包括：

- `Content-Type`：响应体是什么格式。
- `Date`：响应时间。
- `Cache-Control`：缓存规则。
- `Authorization`：请求方携带的认证信息。
- `Cookie`：客户端和服务端之间保存状态的辅助信息。

`body` 是请求或响应的主体数据。API 常见响应体是 JSON，例如：

```json
{
  "current_user_url": "https://api.github.com/user"
}
```

## 常见状态码

```text
2xx：成功
4xx：客户端这边的问题，比如没登录、地址写错、资源不存在
5xx：服务器这边的问题
```

P0-09 需要优先记住这几个：

| 状态码 | 含义 |
| --- | --- |
| `200` | 请求成功，服务器正常处理并返回响应 |
| `401` | 没有认证、没带 API Key，或 token 错误 |
| `404` | 请求的具体资源不存在 |
| `500` | 服务器内部错误 |

## 易错点

### `200` 不等于一定有想要的数据

`200` 表示服务器正常处理了这次请求，但业务结果可能为空。

例如搜索用户：

```text
/search/users?q=not-exist
```

搜索动作成功执行，只是结果为空，状态码更可能是 `200`。

### 具体资源不存在更可能是 `404`

如果请求的是一个具体资源：

```text
/users/not-exist
```

服务器找不到这个用户资源，更可能返回 `404`。

### `response.json()` 不是“把响应 JSON 化”

更准确的说法是：

`response.json()` 把响应体中的 JSON 文本解析成 Python 数据结构。

如果响应体不是合法 JSON，`response.json()` 可能抛出解析错误，所以代码里要处理异常。

## P0-09 通过判断

能说明下面几件事，就说明已经掌握 P0-09 的核心：

- 请求的 `URL` 是什么。
- 为什么要设置 `timeout`。
- `status_code` 是多少，代表什么。
- `headers` 和 JSON body 分别是什么。
- `response.json()` 做了什么。
- 常见失败状态码大概表示什么。

## 来源

- AI-Agent-Learning P0-09：`code/stage0/p0_09_http_request.py`
- AI-Agent-Learning progress：`tracker/progress.md`
- 廖雪峰 Python 教程：HTTP 协议简介、requests

## 相关

- [[../Engineering/HTTP 请求全链路与错误处理|一次 HTTP 请求的全链路与三类错误处理]]（B0-02 进阶：DNS/IP/端口、报文结构、三类错误、timeout、`requests` 不对 4xx/5xx 抛异常）
- [[环境管理(venv & pip)|Python 项目环境管理：venv、pip 与 .env]]
- [[异常·调试·测试(Exceptions)|Python 异常、调试与单元测试]]
- [[../../07-Reviews/AI-Agent-Learning/2026-06-13-stage0-p0-08-pass-review]]
