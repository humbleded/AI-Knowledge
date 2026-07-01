---
type: project-note
topic: AI-Agent-Learning P0-09 HTTP request
status: pass
created: 2026-06-14
updated: 2026-06-14
tags:
  - Python
  - AI-Agent-Learning
  - Stage0
  - P0-09
  - HTTP
---

# P0-09 HTTP 请求

## 任务

执行区产物：

- `C:\Users\26823\Desktop\AI-Agent-Learning\code\stage0\p0_09_http_request.py`
- `C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-06-13.md`

目标：

- 请求一个公开 API。
- 打印状态码、headers 和 JSON。
- 能解释 URL、headers、body、status code、timeout 和 `response.json()`。

## 验证结果

2026-06-13 批改时用项目虚拟环境运行：

```powershell
.\.venv\Scripts\python.exe code\stage0\p0_09_http_request.py
```

关键结果：

- 成功请求 GitHub API。
- 返回状态码 `200`。
- 能打印响应 headers 和 JSON。

## 通过理由

- 代码能成功发起 HTTP 请求。
- 能说明 `URL` 是请求地址，`headers` 是请求/响应元信息，JSON body 是结构化数据。
- 能说明常见状态码：`200` 成功、`401` 未授权、`404` 找不到、`500` 服务器错误。
- 能说明调用 API 必须设置失败处理和 timeout，避免程序一直等。

## 相关概念

- [[../../../02-Concepts/Python/HTTP 请求(requests)|Python HTTP 请求：URL、headers、status code 与 JSON]]

复盘：[[../../../07-Reviews/AI-Agent-Learning/2026-06-14-stage0-p0-gate-l1-01-pass-review|2026-06-14 阶段 0 / 阶段 1 复盘]]
