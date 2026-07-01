---
type: project-note
topic: AI-Agent-Learning L1-01 first model call
status: pass
created: 2026-06-14
updated: 2026-06-14
tags:
  - LLM
  - API
  - SDK
  - DeepSeek
  - AI-Agent-Learning
---

# L1-01 API Key 与 SDK

## 任务

执行区产物：

- `C:\Users\26823\Desktop\AI-Agent-Learning\code\stage1\l1_01_first_call.py`
- `C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-06-14.md`

目标：

- 从环境变量读取 API Key。
- 调一次模型并打印结果。
- 不把真实密钥写死在代码里。

## 验证结果

2026-06-14 批改时运行：

```powershell
.\.venv\Scripts\python.exe -X utf8 -m py_compile code\stage1\l1_01_first_call.py
.\.venv\Scripts\python.exe -X utf8 code\stage1\l1_01_first_call.py
```

真实运行结果：

```text
模型回复： API Key 是用于身份验证和授权的一串唯一标识符，允许应用程序或用户安全地访问 API 服务。
```

代码检查结果：

- 使用 `os.environ.get("DEEPSEEK_API_KEY")` 读取 key。
- 使用 `OpenAI(api_key=api_key, base_url="https://api.deepseek.com")` 指向 DeepSeek。
- 未发现明文 `sk-` 类型密钥。
- 多余的无参数 `client = OpenAI()` 已不存在。

## 通过理由

- 当前环境变量中存在可用 `DEEPSEEK_API_KEY`，模型调用成功。
- 代码没有把 key 硬编码到脚本中。
- 能说明 API Key 是身份和权限凭证，不是模型本身。
- 能说明 SDK 省掉了拼 URL、加鉴权头、序列化 JSON、发送 POST、解析响应等重复工作。

## 保留问题

- 当前 `.env` 文件里只看到 `TEST_VARIABLE`，`DEEPSEEK_API_KEY` 来自当前 PowerShell 环境；换终端时可能需要重新配置。
- 后续可把 `model="deepseek-v4-pro"` 抽成环境变量，例如 `DEEPSEEK_MODEL`。
- 发布到 GitHub 前必须确认 `.env`、虚拟环境、缓存文件不被提交。

## 相关概念

- [[../../../02-Concepts/LLM/API Key 与 SDK|API Key 与 SDK：调用模型的门禁卡和快递柜台]]
- [[../../../02-Concepts/LLM/调用 chat.completions|调用 LLM：chat.completions 与取回复]]

复盘：[[../../../07-Reviews/AI-Agent-Learning/2026-06-14-stage0-p0-gate-l1-01-pass-review|2026-06-14 阶段 0 / 阶段 1 复盘]]
