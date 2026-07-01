---
aliases:
  - chat-completions-call
type: concept
topic: LLM
status: usable
created: 2026-06-14
source:
  - AI-Agent-Learning L1-01 / L1-02
tags:
  - LLM
  - API
  - SDK
  - DeepSeek
---

# 调用 LLM：chat.completions 与取回复

## 一句话解释

用 OpenAI 兼容 SDK 调一次对话模型：传一个带 role 的 `messages` 列表，再从返回对象里取出回复文本。DeepSeek 兼容 OpenAI SDK，只需换 `base_url`、`api_key`、`model`。

## 最小代码

```python
from openai import OpenAI

client = OpenAI(api_key=key, base_url="https://api.deepseek.com")
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},  # 立规矩：设定模型身份/行为，开头设一次
        {"role": "user", "content": "你的问题"},                        # 这一轮用户说的话
    ],
)
text = response.choices[0].message.content
```

## 怎么取回复（接口不同，取法不同）

- `chat.completions` 接口：`response.choices[0].message.content`
  - `choices` 是候选列表（可能多个），`[0]` 取第一个；`.message` 是那条 assistant 消息；`.content` 才是文本。
- OpenAI 新的 `responses` 接口：`response.output_text`
- 记忆点：**先确认你用的是哪个接口，再决定怎么取**——不是所有模型/SDK 写法都一样。

## system / user 消息的作用

- `role="system"`：设定模型「该怎么回答」（身份、规则），一般开头设一次、整轮生效。
- `role="user"`：用户这一轮实际问的内容。
- 多轮聊天时，把历史的 user/assistant 依次放进 `messages`，模型才「记得」上文（不发历史就不记得）。

## 常见坑 / 易错点

1. **key 怎么进来**：用 `os.environ.get("DEEPSEEK_API_KEY")` 读环境变量。
   - `load_dotenv()`（来自 python-dotenv）只是把 `.env` 里的 `KEY=VALUE` 装进环境变量。
   - **如果 key 已配在系统环境变量里，删掉 `load_dotenv()` 也照样取得到**；它只在「key 写在 .env」时才必需。
   - 永远不要把真实 key 硬编码进代码。
2. **错误提示要可读、可操作**：没配 key 或调用失败时，别让程序甩一长串 traceback。
   - 好的错误提示 = **具体原因 + 可操作的下一步**（例：「请在 `.env` 加一行 `DEEPSEEK_API_KEY=...`」）。
   - `except` 要**指定异常类型**（如 `except json.JSONDecodeError:`），别用裸 `except:`（会吞掉 `Ctrl+C` 和其他 bug）；并给个**兜底值**让调用方能继续。
3. **封装复用**：把「怎么调模型」收进一个 `call_model(prompt)` 函数。换模型 / 换 `base_url` 只改这一个函数，调用它的地方（如 `l1_02_ask.py`）一行都不用动。

## 关联

- [[分词(Tokenization)]]：`messages` 里的文本最终会被 tokenize。
- [[自回归生成(Autoregressive)]]：`stream=True` 时逐 token 返回，对应流式输出。
