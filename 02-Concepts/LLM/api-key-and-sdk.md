---
type: concept
topic: LLM API Key SDK
status: usable
created: 2026-06-14
source:
  - AI-Agent-Learning L1-01
tags:
  - LLM
  - API
  - SDK
  - API-Key
  - DeepSeek
---

# API Key 与 SDK：调用模型的门禁卡和快递柜台

## 一句话解释

`API Key` 是调用模型服务的身份和权限凭证，不是模型本身；`SDK` 是一层封装，帮你少写重复的 HTTP 请求细节。

## 比喻

调用大模型像去一栋办公楼办事：

- `API Key` 是门禁卡：证明你是谁、有没有权限进去。
- `model` 是你要找的办公室：不同模型能力、速度、价格可能不同。
- `SDK` 是前台/快递柜台：帮你把地址、授权、请求格式和返回结果包装好。

没有 API Key，服务不知道你是谁；模型名写错，等于走错办公室。

## SDK 帮你省掉了什么

对比手写 `curl`，SDK 通常帮你处理：

- 拼接请求 URL。
- 添加 `Authorization: Bearer ...` 鉴权头。
- 设置 `Content-Type: application/json`。
- 把 `messages` 序列化成 JSON body。
- 发起 POST 请求。
- 把返回 JSON 解析成 Python 对象。

但 SDK 不是魔法，底层仍然是在发 HTTP 请求。

## 最小安全习惯

真实 key 不应该写进代码，而应该来自环境变量：

```python
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.environ.get("DEEPSEEK_API_KEY")
client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")
```

如果换一个终端后突然取不到 key，要先区分：

- `.env` 文件里是否真的写了 `DEEPSEEK_API_KEY=...`。
- 当前终端的系统环境变量里是否有 `DEEPSEEK_API_KEY`。
- 程序有没有在读取环境变量前调用 `load_dotenv()`。

## 模型名为什么要作为参数

模型名决定本次请求用哪个模型。后续最好把它做成配置，例如：

```python
model = os.environ.get("DEEPSEEK_MODEL", "deepseek-chat")
```

这样换模型时不用改业务代码，只改配置。

## 常见坑

- 把 key 写死在代码里，容易被提交到 GitHub。
- 错把 API Key 当模型名，或错把模型名当 API Key。
- 只测试了当前 PowerShell 能运行，却没有确认 `.env` / `.gitignore` 是否适合长期保存和发布。
- 直接打印完整异常可以排错，但给用户看的错误提示应该更短、更可操作。

## 相关链接

- [[chat-completions-call|调用 LLM：chat.completions 与取回复]]
- [[../../04-Projects/LLM/AI-Agent-Learning/l1-01-first-call|L1-01 API Key 与 SDK]]
- [[../../07-Reviews/AI-Agent-Learning/2026-06-14-stage0-p0-gate-l1-01-pass-review|2026-06-14 PASS 复盘]]
