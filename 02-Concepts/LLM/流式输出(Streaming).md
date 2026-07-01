---
aliases:
  - streaming-output
type: concept
topic: LLM
status: usable
created: 2026-06-17
source:
  - AI-Agent-Learning L1-04
tags:
  - LLM
  - 流式输出
  - streaming
  - 推理模型
  - DeepSeek
---

# 流式输出：stream=True 与逐 chunk 处理

## 一句话解释

流式输出 = 让模型**边生成边一小块一小块（chunk）地把文字传回来**，客户端逐字打印（打字机效果）。它不缩短「总生成时间」，缩短的是**「首字等待时间」（TTFT, time-to-first-token）**——优化的是体验/感知，不是吞吐。

## 底层传输：SSE（Server-Sent Events）

`stream=True` 底层走的是 **SSE（服务器发送事件）**——一种 Web 技术：

- **普通请求-响应**：一问一答、一锤子买卖，服务器把完整结果一次性塞回来、连接就断（对应 `call_messages` 非流式）。
- **SSE**：服务器把那条 HTTP 连接**一直攥着不挂**，然后分很多次、一点点往客户端**单向**推文本，推完才关。模型每生成几个字就推一小段过来，`for chunk in response` 每次收到的就是这么一块。
- 对比 **WebSocket**：WebSocket 是**双向**实时互推（聊天室、协同编辑）；SSE 只有服务器→客户端单向，够流式输出用。

SDK 把每个 SSE 数据片解析成 Python 的 `chunk` 对象喂给你的 `for` 循环，所以你不用自己解析 SSE 协议——这是 SDK（客户端层）的活，与 `stream`（API 参数、改服务端返回形态）分属两层，见 [[API 参数与 SDK 客户端参数|API 参数 vs SDK 客户端参数]]。

## 流式三件套

```python
response = client.chat.completions.create(
    model="...", messages=messages,
    stream=True,                       # ① 开关：边生成边发，别等整段
)
answer = ""
for chunk in response:                 # ② 非流式 response 是整段；流式变成可逐块循环
    if not chunk.choices:              #   防御：choices 为空列表时跳过（见下「两个守卫」）
        continue
    content = chunk.choices[0].delta.content or ""   # ③ 取增量 + None 兜底（关键！）
    answer += content                  #   边打印边收集，拼回完整文本
    print(content, end="", flush=True) #   end="" 不换行；flush=True 立刻刷屏
print()
return answer                          #   把完整字符串交出去（多轮要存进 history）
```

- 非流式取整段：`response.choices[0].message.content`。
- 流式取增量：`chunk.choices[0].delta.content`（`delta` = 这一小块**新增**文字）。
- `flush=True`：默认 `print` 会把字攒在缓冲区不立即显示；加它让每块立刻刷到屏幕，才有打字机效果。

## `delta.content` 为 None 的两种场景（必须 `or ""` 兜底）

`delta.content` 在以下时刻是 `None`，不兜底会出事：

1. **推理模型的「思考阶段」**——思考文字走的是另一个字段（见下），此时 `content` 是 None。
2. **最后一个 chunk**（带 `finish_reason` 的收尾块）通常 `content` 也是 None。

不加 `or ""` 的两种翻车：
- `print(None)` 会把 None 转成字符串 **`"None"`** 打到屏幕上（实测开 thinking 时真答案前糊了约 37 个 `None`）。
- `answer += None` 会直接 **`TypeError`**（`str + NoneType`）。

`None or ""` → 返回 `""`（None 是假值，`or` 返回后者）→ `print("")` 不显示、`answer += ""` 不崩。

## 推理模型「两条流」：reasoning_content vs content

开了 thinking（推理模型）后，流式返回的文字**分装在两个字段**（这不是「流式 vs 一次性」，是两个内容字段）：

| 阶段 | `delta.content` | `delta.reasoning_content` |
|---|---|---|
| 🤔 思考中 | **None** | 有值（思考草稿） |
| 💬 正式回答 | 有值 | None / 空 |

- 普通模型只有一条流（`content`）；推理模型把「想」和「答」分到两个字段，所以叫两条流。
- 只取 `content` → 思考阶段全是 None（这就是那串 None 的根源）。
- 想显示思考：循环里再取 `reasoning_content`，哪个有值就打哪个：

```python
content = chunk.choices[0].delta.content or ""
reasoning = chunk.choices[0].delta.reasoning_content or ""
if reasoning:
    print(reasoning, end="", flush=True)   # 思考阶段
print(content, end="", flush=True)         # 回答阶段
```

- 决策：若**开了 thinking 却不显示** reasoning，等于白花时间/token——要么不开（删 `reasoning_effort`/`thinking`），要么开了就把 reasoning 显示出来。

## 两个守卫别混（同是「防 None」也分两层）

| 守卫 | 防什么 |
|---|---|
| `if not chunk.choices: continue` | `chunk.choices` 是**空列表 `[]`** 时，`chunk.choices[0]` 越界 `IndexError`。 |
| `chunk.choices[0].delta.content or ""` | `delta.content` 是 **None** 时，防 `print` 出 "None" + `answer += None` 崩溃。 |

- 「防 None」还分两层：**打印循环层**（防打出 None / 累加崩溃）vs **发 API 层**（messages 里 `content` 必须是字符串）。别用一个理由套两个场景。

## 流式接回多轮：必须 return 完整字符串

单轮只 `print` 就够；多轮记忆靠 `history.append({"role":"assistant","content": answer})`，而 `print` 把字送屏幕后程序**不留副本**。所以流式函数必须把循环里拼好的 `answer` **`return`** 出去，`main` 才有字符串可 append。

## 错误处理：返回字符串，不要返回 None

`except` 里若只 `print` 不 `return`（或 `return` 不跟值），函数返回 **`None`**（不是空字符串）。多轮里这会：

```
出错 → return None → history.append({"content": None})
     → 下一轮把 content=None 发给 API（content 必须是字符串）→ 报错 → 毒化后续所有轮
```

修法：`except Exception as exc: return f"流式输出失败：{exc}"`（让任何路径都交出一个字符串，和 L1-03 的 `call_messages` 一致）。

## 常见坑

- `stream` 拼成 `strem`：报「意外关键字参数」或被忽略，流式不生效。
- 漏 `or ""`：开 thinking 时屏幕糊一串 `"None"`；累加时 `TypeError`。
- 把「`choices` 空列表守卫」当成「None 兜底」的解药——两者管不同的事。
- 以为「函数没 return 值返回空字符串」——其实返回 **`None`**（`None ≠ ""`，`None` 是全局单例，判断用 `is None`）。
- 以为「推理模型两条流 = 流式 vs 一次性」——其实是 `reasoning_content` / `content` 两个字段，与流式无关。
- 开了 thinking 却不显示 reasoning = 白花时间/token。

## 关联

- [[多轮对话与无状态记忆(Stateless Memory)|多轮对话：接口无状态与客户端记忆]]：流式接回多轮，return 的 answer 才能进 history。
- [[调用 chat.completions|调用 LLM：chat.completions 与取回复]]：非流式取 `message.content`，对照流式取 `delta.content`。
- [[自回归生成(Autoregressive)|Autoregressive Generation]]：模型逐 token 生成，正是流式逐 chunk 返回的底层原因。
- [[消息角色与指令优先级(Instruction Hierarchy)|消息角色与指令优先级]]：messages 里 `content` 必须是字符串（毒化 history 的根因）。

## 来源

- AI-Agent-Learning L1-04：`C:\Users\26823\Desktop\AI-Agent-Learning\code\stage1\l1_04_stream_chat.py`
- 每日记录：`C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-06-17.md`
