---
type: course-note
topic: AI-Agent-Learning Stage 0.5
status: active
created: 2026-06-10
updated: 2026-06-23
tags:
  - AI-Agent-Learning
  - 工程基础
  - 学习路线
---

# 阶段 0.5：工程基础随用随补

## 核心结论

工程基础需要学，但不应该作为进入 Agent 前必须整块学完的前置课程。

当前路线采用“边学 Agent，边补工程基础”的方式：

- Python 后半段先补齐：模块/venv、异常、文件/JSON、HTTP。
- `P0-Gate` 通过后，直接进入 L1：大模型 API 入门。
- Linux、网络、数据库、Docker 按项目触发点补。
- `B0-Gate` 改为后续本地栈整合关卡，不阻塞 L1/API。

## 当前最短路径

```text
P0-06 模块/venv
-> P0-07 异常/调试/测试
-> P0-08 文件/JSON/CSV
-> P0-09 HTTP 请求
-> P0-Gate Python 基础闯关
-> L1 大模型 API 入门
-> PR2 Prompt 与结构化输出
-> T3 Tool Calling
-> A4 最小 Agent
```

## 触发式补课表

| 触发场景 | 补哪部分工程基础 | 对应执行区任务 |
|---|---|---|
| 环境变量、API Key、包安装、路径问题 | venv、pip、`.env`、命令行 | `P0-06`、`L1-01`、`B0-01` |
| API 调不通、超时、状态码不懂 | HTTP、DNS、headers、status code、timeout | `P0-09`、`L1`、`B0-02`、`T3-04` |
| 需要保存学习记录、聊天历史、Memory | SQL、SQLite/PostgreSQL、CRUD、事务 | `B0-03`、RAG/Memory 阶段 |
| 需要本地多服务或数据库容器 | Dockerfile、Compose、volume、network、logs | `B0-04`、`B0-Gate` |
| 需要做可展示项目 | FastAPI、日志、测试、部署 | 综合项目阶段按需补 |

## 已补课记录（PASS）

- **B0-02 网络基础与 HTTP**（2026-06-23 PASS）：搞懂 `requests.get()` 全链路（DNS/IP/端口/TCP/报文/状态码）、三类错误 + 三层防护（timeout / try-except / 主动 check status_code）、`requests` 不对 4xx/5xx 抛异常、timeout 保护客户端、`except` 子类在前基类兜底、`/` vs `//`。产物 `code/stage0_5/b0_02_http_probe.py` 实测四场景（正常 2xx / 404 非 2xx / DNS 失败 / 超时）通过。概念卡 → [[../../../02-Concepts/Engineering/http-and-network-basics|HTTP 全链路与三类错误处理]]。

## B0-Gate 的新定位

`B0-Gate` 不再是 L1 前置闯关。它更适合在下面任一情况发生时完成：

- 已完成 L1-Gate，准备让 Agent 有持久化能力。
- 已完成基础 Tool Calling，准备接数据库或外部服务。
- 准备做 RAG、Memory、MCP 或本地多容器项目。
- 准备把 Agent 做成可运行、可排错、可复盘的小项目。

## 执行区链接

- [AI-Agent-Learning 执行区](file:///C:/Users/26823/Desktop/AI-Agent-Learning/)
- [总 tracker](file:///C:/Users/26823/Desktop/AI-Agent-Learning/tracker/ai-agent-learning-tracker.md)
- [进度表](file:///C:/Users/26823/Desktop/AI-Agent-Learning/tracker/progress.md)
- [stage0_5 code](file:///C:/Users/26823/Desktop/AI-Agent-Learning/code/stage0_5/)
- [stage0_5 notes](file:///C:/Users/26823/Desktop/AI-Agent-Learning/notes/stage0_5/)
- [stage0_5 resources](file:///C:/Users/26823/Desktop/AI-Agent-Learning/resources/stage0_5/)

## 相关链接

- [[README|AI-Agent-Learning]]
- [[../../../02-Concepts/Engineering/http-and-network-basics|一次 HTTP 请求的全链路与三类错误处理（B0-02）]]
- [[../../Python/AI-Agent-Learning/stage0-python-basics|阶段 0：Python 与开发环境]]
- [[../../../01-Maps/AI 开发学习路线]]
- [[../../../08-Memory/AI 学习原则]]
