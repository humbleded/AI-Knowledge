---
aliases:
  - function-calling
  - tool-calling
type: concept
topic: LLM
status: usable
created: 2026-07-03
updated: 2026-07-12
source:
  - AI-Agent-Learning T3-01（2026-07-01 学习日）
  - AI-Agent-Learning T3-Gate（2026-07-11 ChatCompletionMessage 回填辨析）
  - AI-Agent-Learning T3-Gate 正式复核（2026-07-12）
  - HF agents-course 中文版 unit1 + bonus-unit1
  - DeepSeek API Docs：Tool Calls / Thinking Mode
tags:
  - LLM
  - Agent
  - function-calling
  - tool-calling
  - Action
  - Observation
---

# 函数调用（Function Calling / Tool Calling）：模型点菜，程序炒菜

## 一句话解释

函数调用 ＝ 让 LLM 能「点名要用哪个工具、传什么参数」、由**你的程序**真正执行、结果再喂回模型的整套机制。**模型从不执行任何工具**——它只产出「调用请求」。Tool Calling 与 Function Calling 是**同一机制的两个名字**（OpenAI 早期参数叫 `functions`，后改 `tools`/`tool_calls`，叫法随之泛化）。

## 为什么需要工具：补两个洞

1. **「不知道」**：训练截止后的事、此刻的实时状态（天气、订单物流、用户位置）——硬问就幻觉。
2. **「不会算 / 做不了」**：精确算术等模型天生不擅长的活 → 计算器工具。

工具既能**感知（查）**也能**行动（做）**。对模型来说，工具＝一段文字说明书（四要素：**名称 / 功能 / 每个参数名+类型+含义 / 输出**）——模型「看菜单点菜」，说明书是它认识工具的**唯一窗口**（写烂了→不用或乱传参，锅在说明书）。

## 整条链（7 步，「谁干的」最重要）

```text
第 1 步：【程序】把用户问题 + 工具说明书发给模型
第 2 步：【模型】选工具+定参数，生成调用请求 JSON（= Action），吐完立刻停 ←「停」
第 3 步：【程序】解析 Action：认出函数、抽出参数 ←「解析」
第 4 步：【程序】真正执行工具，拿到真实结果
第 5 步：【程序】结果当 Observation（role:"tool"）拼回 messages，整盘重发
第 6 步：【模型】看 Observation：够 → 人话收尾；不够 → 吐新 Action 回第 3 步（可循环多轮）
第 7 步：【程序】把回答显示给用户
```

- **Action** ＝ 模型吐出的调用请求 JSON 本身（工具名+参数）——「模型唯一的行动方式是说话」。
- **Observation** ＝ 工具**真实执行结果**（成功数据 / 报错信息 / 状态码都算）——报错也是情报，模型看到才能重试、换参数或如实告知。
- 接口无状态：Action 与 Observation 都要 append 进 messages **整盘重发**，模型才「看得见」自己刚干了什么（见 [[多轮对话与无状态记忆(Stateless Memory)]]）。
- 「中间人」永远是模型之外的**客户端程序**——自己写的脚本，或 Claude Code / Codex 这类别人写好的 harness（跑在本机，不是「平台」）。

## assistant 消息对象为什么可以直接 append

```python
message = response.choices[0].message
print(message)
```

打印出来通常是 `ChatCompletionMessage(...)`，而不是 `{...}`。这是因为 `message` 是 SDK 返回的**消息模型对象**，不是普通 `dict`。但 `list.append()` 本来就能保存任意 Python 对象；更关键的是，DeepSeek 使用的 OpenAI 兼容 SDK 能在下一次请求时把这个消息对象序列化成 API 所需的 JSON。

因此，工具调用后应优先完整保存模型刚返回的 assistant 消息：

```python
messages.append(message)
```

它会保留 `role`、`content`、`tool_calls` 等字段；Thinking Mode 下还会保留后续请求必须回传的 `reasoning_content`。这也是 DeepSeek 官方 Tool Calls 示例采用的写法。

如果确实需要普通字典，例如调试、持久化或自行组装请求，可以完整转换：

```python
assistant_message = message.model_dump(exclude_none=True)
messages.append(assistant_message)
```

下面这种“外层手写 dict、内层仍放 SDK 对象”的混合写法不一定立刻报错，但容易漏字段，不作为默认写法：

```python
messages.append({
    "role": "assistant",
    "content": message.content,
    "tool_calls": message.tool_calls,
})
```

> [!important] assistant 消息与 tool 消息不是同一种东西
> assistant 的工具调用请求可以完整追加 `message`；客户端执行函数后生成的工具结果，要转成字符串再追加 `role: "tool"` 消息，并带回匹配的 `tool_call_id`。

```python
result_json = json.dumps(tool_result, ensure_ascii=False)
messages.append({
    "role": "tool",
    "tool_call_id": tool_call.id,
    "content": result_json,
})
```

还要区分两个动作：

- `messages.append(message)`：把当前消息保存进对话历史。
- `message = response.choices[0].message`：让变量指向最新一次模型响应。

只 append 不重新赋值，后面检查的仍可能是旧 `message`；只重新赋值不 append，模型下一轮又看不到前一轮的工具调用请求。

## 一次响应可以有多个 tool_call

一个 assistant 响应不等于一次工具调用。模型可以在同一条消息里返回多个 `tool_call`，每个调用都有独立的 `tool_call.id`：

```text
assistant.tool_calls = [call_calc, call_file]
  -> role="tool", tool_call_id=call_calc.id
  -> role="tool", tool_call_id=call_file.id
```

客户端必须先保存完整 assistant 消息，再逐个处理并按原 ID 回填。即使某个调用因为未知工具、坏参数或安全策略在执行前被拒绝，也要回填一条稳定错误结果；这样模型才能把结果和具体调用对应起来。

```python
messages.append(message)

for tool_call in message.tool_calls:
    result = execute_tool_call(tool_call)
    messages.append({
        "role": "tool",
        "tool_call_id": tool_call.id,
        "content": json.dumps(result, ensure_ascii=False),
    })
```

## 五种数量与最大轮数

不要把下面五个数字混成“调用次数”：

| 数量 | 计数单位 |
|---|---|
| 模型 API 调用数 | 每次 `chat.completions.create()` |
| 工具轮数 | 一条含 `tool_calls` 的 assistant 响应被整批处理一次 |
| `tool_call` 数 | 调用请求的条数；一轮可以有多条 |
| Python 工具执行数 | 真正进入注册表函数的次数；执行前拒绝不计 |
| `role="tool"` 回填数 | 每个已处理调用各一条；执行前拒绝也要回填 |

直接回答分支没有 `tool_calls`，客户端应直接返回 `message.content`，不执行工具。

最大轮数限制的是**已完成的工具轮数**。以 `max_tool_rounds=3` 为例，客户端可能先收到第 4 次模型响应，看到它仍要求调用工具后才判断到达上限；第 4 个调用不执行，稳定停止文本直接返回 Agent 调用者，不再发回模型。

## 停止并解析（stop and parse）

**停 ＝ 模型侧**（Action 吐完立刻闭嘴）；**解析 ＝ 程序侧**（读 JSON → 认函数 → 抽参数），发生在调用工具**之前**。

「停」防的事故：不停的话，模型顺着训练里见过的剧本把 **Observation 槽位自己编出来**（假天气、假订单），再基于假数据写出自信的最终回答——格式全对、文本上肉眼不可辨，**最隐蔽的失败**。唯一判别法：**看代码有没有真执行**（有没有 TOOLS 注册表 / 分发器 / 真调用）。本质＝把「填 Observation 的权力」锁死在程序手里。

## Function Calling（官方版）vs 手搓 prompt 教学法

| | 手搓（HF unit1 教法） | Function Calling |
|---|---|---|
| 工具怎么告诉模型 | system prompt 手写说明书 | SDK `tools=[...]` 参数 |
| 模型怎么表达调用 | 正文文本里吐 JSON，程序去抠 | 专用字段 `tool_calls` |
| 结果怎么回 | 当普通文本塞回 | 专用 `role:"tool"` 消息 |
| 能力哪来 | prompt 临场教（软请求） | **训练焊进权重**（肌肉记忆） |

手搓不稳的根因＝**概率采样**：prompt 只把「守格式」的概率推高，低概率的歪格式永远抽得中——prompt 是**事前软请求**，「读到 ≠ 必须照做」（模型不是「忘记」，说明书每轮都在上下文里）→ 所以要 `json.loads` try/except + validate 代码兜底。FC 稳＝训练把行为焊进权重＋底层特殊词元（`[TOOL_CALLS]` 类，SDK 包掉）。与 [[结构化输出(Structured Output)]] 的 `json_object` 同族：都是「官方开关」替代「口头求」。

## 最小分发器（实证可跑，2026-07-03 脚本验证）

```python
action = json.loads(model_output)            # 解析 Action（对象是模型吐的 JSON 文本）
tool_name = action["action"]
args = action["action_input"]
result = TOOLS[tool_name](**args)            # 注册表取函数 + 关键字解包执行（任意工具签名通吃）
messages.append({"role": "tool", "content": result})   # Observation 拼回
```

- `TOOLS` dict ＝ 最小工具注册表；`**args` 解包让分发器对任何工具通用（计算器 `a,b`、订单 `user_id,days` 一个写法接住）。
- 坏 Action（如 JSON 没双引号）→ `json.loads` 抛 **`json.JSONDecodeError`（ValueError 子类）**；兜底进阶：把「Action 不合法，请重新输出」当 Observation 发回，让模型重吐一轮（错误对模型也是情报）。

## 常见坑 / 错误理解 → 正确理解

- ❌ 工具自己执行 / 平台执行 → ✅ 中间人＝**客户端程序**（×2 踩，最顽固）。
- ❌ Agent ＝ 会用工具的聪明模型 → ✅ **Agent ＝ LLM(大脑) + 工具(手脚) + 调度程序(脊髓) 组成的系统**；光有模型＝chatbot，能说「我帮你查」但说完啥也不发生。
- ❌ 「停止」在输出完最终回答之后 → ✅ 在 **Action 吐完瞬间**（×2 踩）；防自编 Observation。
- ❌ 名字坑：叫「函数调用」→ ✅ 模型**不调用**函数，只**生成调用请求**。
- ❌ 「prompt 教的工具模型会忘记」 → ✅ 没有忘（每轮都在上下文里），是**不保证遵守**（概率采样）。
- ⚠️ 自编 Observation 的**代码实景不易识别**：见「一次 call_model 吐出 Action+Observation+答案」的代码，第一眼仍会信结果来自工具（概念背得出≠实景认得出）——判别法＝找有没有真执行。
- ⚠️ 坏 JSON 抛 `JSONDecodeError`（**值**的问题，ValueError 家族），不是 `TypeError`（类型不匹配操作，如 `answer += None`）。
- ❌ `message` 打印出来不是 dict，所以不能 append → ✅ `ChatCompletionMessage` 是 SDK 消息对象；Python 列表可以保存它，SDK 会在请求时序列化。需要显式 dict 时用 `message.model_dump(exclude_none=True)`。
- ❌ 手动只复制 `role/content/tool_calls` 就一定等价 → ✅ 可能漏掉 `reasoning_content` 等字段；优先追加完整 `message`，尤其是 Thinking Mode。
- ❌ 一条 assistant 响应只会有一个工具调用 → ✅ `tool_calls` 是列表；每个调用有独立 ID 和独立工具结果。
- ❌ 工具轮数就是 Python 函数执行次数 → ✅ 一轮可含多个调用，且客户端拒绝的调用会回填错误但不进入真实函数。

## 关联

- [[结构化输出(Structured Output)]]：Action JSON 是结构化输出的杀手级应用；`json_object` 与 FC 同为「官方开关」。
- [[多轮对话与无状态记忆(Stateless Memory)]]：Action / Observation 拼回整盘重发的底层原因。
- [[采样参数与成本(Sampling)]]：「prompt 软请求 vs 训练焊死」的概率视角；贪心解码。
- [[提示工程基础(Prompt Engineering)]]：手搓说明书＝prompt 工程；四要素。
- [[LLM 本质与幻觉(Hallucination)]]：自编 Observation ＝ 幻觉在 Agent 链路里的具体形态。
- [[MCP(Model Context Protocol)]]：统一「怎么给模型提供工具」的开放协议（阶段 9 展开）。
- [[../Agent/工具定义与执行协议(Tool Definition)|工具定义与执行协议]]：`tools` schema、`TOOLS` 注册表与客户端校验顺序。
- [[../../04-Projects/Agent/AI-Agent-Learning/t3-gate-tool-assistant|T3-Gate 三工具助手]]：原生三工具闭环与 14 条评估用例。
- [[../../07-Reviews/AI-Agent-Learning/2026-07-12-t3-gate-tool-calling-review|T3-Gate PASS 复盘]]。

## 来源

- AI-Agent-Learning T3-01：笔记 `notes/stage3/t3_01_function_calling.md`（共写、含自纠痕迹）；`daily/2026-07-01.md`（带读 7 题＋练习 13 题全 PASS）。
- HF agents-course 中文版：`unit1/tools.mdx`、`actions.mdx`、`observations.mdx`、`bonus-unit1/what-is-function-calling.mdx`。
- DeepSeek API Docs：[Tool Calls](https://api-docs.deepseek.com/guides/tool_calls)、[Thinking Mode](https://api-docs.deepseek.com/guides/thinking_mode)。
