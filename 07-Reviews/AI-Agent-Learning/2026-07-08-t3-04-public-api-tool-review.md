---
type: review
topic: AI-Agent-Learning T3-04
status: pass
created: 2026-07-08
tags:
  - AI-Agent-Learning
  - Agent
  - Tool-Calling
  - HTTP
  - PASS
---

# 2026-07-08 T3-04 外部 API 工具 PASS 复盘

## 判定

**T3-04 PASS**

## 验证

- `python -m py_compile code/stage3/t3_04_public_api_tool.py`：通过。
- 默认请求 `https://api.github.com`：返回 `ok=True`、`status_code=200`、`server="github.com"`。
- 函数级测试覆盖：
  - 404 路径返回 `ok=False/status_code=404`，不进入异常分支。
  - 非法 URL 返回 `ok=False/error`。
  - 模拟 `requests.Timeout` 返回“请求超时”。
  - 模拟 `requests.RequestException` 返回“请求失败：...”

## 学到的稳定概念

- [[../../02-Concepts/Agent/外部 API 工具(External API Tool)|外部 API 工具]]
- [[../../02-Concepts/Agent/工具定义与执行协议(Tool Definition)|工具定义与执行协议]]
- [[../../02-Concepts/Engineering/HTTP 请求全链路与错误处理|HTTP 请求全链路与错误处理]]
- [[../../02-Concepts/LLM/函数调用(Function Calling)|函数调用 / Tool Calling]]

## 关键问题闭环

1. 为什么外部 API 工具需要 `timeout`？
   - 防止外部服务卡住整条 Agent 链路，让工具能在超时后返回稳定错误结果。
2. 为什么不直接返回完整 `response.json()`？
   - 原始 JSON 太大，会浪费上下文并分散模型注意力。工具应只返回回答当前问题所需字段。
3. 为什么 404 不进 `except RequestException`？
   - 404 是服务器正常返回的 HTTP 响应状态码，只是资源不存在；请求异常是超时、连接失败、非法 URL 等没有正常拿到响应的情况。
4. 为什么异常分支里不能用 `response.ok`？
   - 请求异常时可能根本没有 `response` 对象，应该返回 `{"ok": False, "error": ...}`。

## 今日易错点

- 把 `response` 说成“响应体”，经订正后改成“响应对象”。
- 把 `server` 误认为 URL 主机名，经订正后能说明来自响应头。
- 把 `RequestException` / timeout 说成“捕获并抛出/返回异常”，经订正后能说成“捕获后返回稳定 dict”。
- 看到 `status_code=404` 时，不能说“网络连接失败”，应解释为路径资源不存在。

## 下一步

进入 `T3-Gate Tool Calling 闯关`：注册计算器、读文件、外部 API 三个工具，设计工具注册表和客户端分发流程，并准备正常、失败、危险输入的评估用例。
