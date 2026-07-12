---
type: concept-index
topic: Engineering
status: active
created: 2026-06-14
updated: 2026-07-12
tags:
  - Engineering
  - 概念卡
---

# Engineering 概念卡

通用软件工程方法论（跨语言、跨技术），区别于 Python / LLM / MCP 这类具体技术卡。

## 调试与质量

- [[调试与错误恢复(Triage)|调试与错误恢复：系统化 triage]]：usable，停线规则 + 复现 / 定位 / 缩小 / 修根因 / 防复发 / 验证 六步。

## 网络与 HTTP

- [[HTTP 请求全链路与错误处理|一次 HTTP 请求的全链路与三类错误处理]]：usable，`requests.get` 背后 7 步（DNS/IP/端口/TCP/报文/状态码）+ 三类错误三层防护 + 「requests 不对 4xx/5xx 抛异常」+ timeout 保护客户端 + except 顺序。来自 B0-02。
- [[服务端请求伪造(SSRF)|服务端请求伪造（SSRF）]]：usable，服务器代替攻击者访问 localhost、私网或云 metadata；覆盖 hostname 伪装、重定向绕过与分层防护。

## 下一批可新增（按需，等用到再写）

- test-driven-development（RED-GREEN-REFACTOR，Python / pytest 版）—— 到 stage 3 写有逻辑的代码时
- code-review 五维评审（正确性 / 可读性 / 架构 / 安全 / 性能）
- git-workflow 与版本管理
