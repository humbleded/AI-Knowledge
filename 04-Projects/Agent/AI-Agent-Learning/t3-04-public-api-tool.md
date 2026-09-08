---
type: project-note
topic: T3-04 Public API Tool
status: pass
created: 2026-07-08
updated: 2026-09-08
source:
  - C:\Users\26823\Desktop\AI-Agent-Learning\code\stage3\t3_04_public_api_tool.py
  - C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-07-08.md
tags:
  - Agent
  - Tool-Calling
  - API
  - HTTP
  - AI-Agent-Learning
---

# T3-04 外部 API 工具

## 目标

实现一个最小外部 API 工具，把 Agent 工具能力从本地函数扩展到真实网络服务：

1. 调用公开 API。
2. 设置 `timeout`。
3. 只返回必要字段，不把巨大原始 JSON 全塞给模型。
4. 对超时、非法 URL、请求异常返回稳定错误结构。

## 产物

- 执行区代码：`C:\Users\26823\Desktop\AI-Agent-Learning\code\stage3\t3_04_public_api_tool.py`
- 默认 API：`https://api.github.com`

核心返回结构：

```python
{
    "ok": response.ok,
    "status_code": response.status_code,
    "server": response.headers.get("Server"),
    "rate_limit_limit": response.headers.get("X-RateLimit-Limit"),
    "rate_limit_remaining": response.headers.get("X-RateLimit-Remaining"),
}
```

失败返回：

```python
{"ok": False, "error": "请求超时"}
{"ok": False, "error": "请求失败：..."}
```

## 验证结果

2026-07-08 实跑通过：

| 用例 | 结果 |
|---|---|
| 语法检查 | `python -m py_compile code/stage3/t3_04_public_api_tool.py` 通过 |
| 默认 `https://api.github.com` | `ok=True`、`status_code=200`、`server="github.com"` |
| `https://api.github.com/not-found-for-t3-04` | `ok=False`、`status_code=404`，不进异常分支 |
| `not-a-valid-url` | `ok=False`、`error="请求失败：..."` |
| 模拟 `requests.Timeout` | `ok=False`、`error="请求超时"` |
| 模拟 `requests.RequestException` | `ok=False`、`error="请求失败：simulated request failure"` |

## 关键结论

- 外部 API 工具补的是 LLM 不能真实访问外部服务的短板。
- `response` 是响应对象，后续要用它读取 `ok/status_code/headers`。
- 404 是服务器正常返回的 HTTP 状态码，不是网络异常。
- 异常分支里可能没有 `response`，不能用 `response.ok`。
- 工具返回稳定的 Python 字典；在当前 Chat Completions 调用链中，客户端先用 `json.dumps(..., ensure_ascii=False)` 转成 JSON 字符串，再写入带原 `tool_call_id` 的工具消息 `content`，供模型读取。
- `requests.get(..., timeout=5)` 分别限制连接与读取等待，不是从开始到结束最多五秒。对方持续慢速发送数据时，整个请求可能超过五秒；任务总时限需要单独控制。见 [Requests 超时说明](https://requests.readthedocs.io/en/latest/user/quickstart/#timeouts)。

上述说明于 2026-09-08 根据 [项目笔记订正](https://github.com/humbleded/AI-Agent-Learning/blob/main/notes/stage3/t3_04_public_api_tool.md)与官方文档核对后同步；上面的 2026-07-08 实跑结果保持历史记录，不代表本次重跑了真实网络工具。

## 今日易错点

- 把 `response` 说成“响应体”。
- 把 `server` 字段误认为 URL 主机名；实际来自响应头 `Server`。
- 把 `RequestException` 说成“捕获并抛出”；正确是捕获后返回稳定错误结构。
- `rate_limit_remaining` 只剩很少时，模型应提醒当前限流窗口额度快用完。

## 相关

- [[../../../../02-Concepts/Agent/外部 API 工具(External API Tool)]]
- [[../../../../02-Concepts/Agent/工具定义与执行协议(Tool Definition)]]
- [[../../../../02-Concepts/Engineering/HTTP 请求全链路与错误处理]]
- [[../../../../07-Reviews/AI-Agent-Learning/2026-07-08-t3-04-public-api-tool-review]]
