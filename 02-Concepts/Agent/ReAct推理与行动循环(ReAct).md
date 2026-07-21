---
type: concept
topic: ReAct
status: usable
created: 2026-07-22
updated: 2026-07-22
source:
  - C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-07-21.md
  - C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-07-22.md
  - C:\Users\26823\Desktop\AI-Agent-Learning\code\stage4\a4_03_react_agent.py
  - C:\Users\26823\Desktop\AI-Agent-Learning\repos\hello-agents\docs\chapter4\第四章 智能体经典范式构建.md
tags:
  - Agent
  - ReAct
  - Tool-Calling
  - AI-Agent-Learning
aliases:
  - ReAct
  - Reasoning and Acting
---

# ReAct 推理与行动循环（ReAct）

## 一句话

ReAct（Reasoning and Acting）让模型在“判断下一步”和“通过工具获取真实反馈”之间循环：模型提出 `Action`，客户端执行工具并回填 `Observation`，下一轮模型再决定继续还是结束。

```text
Question
  -> Thought
  -> Action
  -> 客户端解析、校验并执行工具
  -> Observation
  -> 下一轮 Thought
  -> 继续 Action 或 Finish
```

## 三个槽位分别做什么

| 槽位 | 作用 | 不是什么 |
|---|---|---|
| `Thought` | 当前轮展示出来的判断/决策文本，帮助形成下一步 Action | 不能据此证明模型存在可验证的内部思考过程 |
| `Action` | 模型提出的调用意图，例如 `Weather[Singapore]` | Action 出现时，工具尚未执行 |
| `Observation` | 工具真实执行后的结果或失败反馈，供下一轮读取 | 不是执行者，也不应由模型自行编造 |

职责链要按主语拆开：

```text
LLM：读取 prompt/history，生成 Thought 和 Action
客户端：解析并硬校验 Action，从 TOOLS 注册表分发真实函数
工具：执行具体能力并返回结果
客户端：把结果写成 Observation，追加到 history
下一轮 LLM：读取带 Observation 的完整输入，再判断目标是否满足
```

## 成功停止与安全停止

ReAct 不只有一种“停”。

### 成功停止

模型已经拿到足够证据，输出非空最终答案，例如：

```text
Action: Finish[新加坡的实时天气是 34°C，AQI 为 160。]
```

但“格式正确的 Finish”只表示控制流愿意结束，不自动证明任务质量足够。模型仍可能过早结束，因此客户端至少要做非空、格式和安全校验；更复杂系统还需要目标充分性检查或评估。

### 安全停止

系统无法继续或触及保护边界时停止，例如：

- 没有解析到 `Action`；
- Action 格式无效；
- 达到 `max_steps`；
- 后续生产系统中的超时、取消或人工确认拒绝。

安全停止的目标不是“回答一定完成”，而是“不让循环失控或副作用继续扩大”。

## `max_steps` 为什么必要

模型可能连续请求工具、反复收到无用结果，或者不断输出空 `Finish[]`。如果只相信模型自己收口，循环可能一直运行。

```python
for step in range(1, max_steps + 1):
    response_text = llm_call(prompt)
    ...

print("已达到最大步数，流程结束。")
return None
```

在这个实现中，每轮循环只调用一次 `llm_call`，所以 `max_steps=N` 同时把循环轮数和 LLM 调用次数限制在最多 N 次。其他实现若一轮含多次模型调用，必须按真实控制流重新定义这个计数器。

## Prompt 是软请求，客户端做硬校验

提示词可以要求：

```text
Thought: 当前判断
Action: ToolName[input] 或 Finish[最终答案]
```

但模型仍可能漏字段、加缩进、输出空 Finish 或把正文里的 `Action:` 当普通文本。Prompt 只能提高守格式的概率，不能代替客户端解析与校验。

一个严格的文本协议解析示例：

```python
thought_pattern = r"^Thought:\s*(.*?)\s*(?=^Action:|\Z)"
action_pattern = r"^Action:\s*(.*)"
flags = re.MULTILINE | re.DOTALL
```

- `^` 配合 `re.MULTILINE`：字段标签只在行首生效；
- `re.DOTALL`：Thought 可以跨多行；
- 非贪婪 `(.*?)`：尽量少取；
- `(?=^Action:|\Z)`：在真正的行首 Action 或全文末尾前停止。

这是一种有意严格的协议：`  Action:` 不会被识别为字段，而会留在 Thought 正文里。是否允许缩进必须由协议明确决定，不能靠猜。

## 工具注册与 Observation 回填

模型看到的是工具说明，客户端持有的是真实函数注册表：

```python
TOOLS_DESCRIPTION = "- Weather: 查询指定城市的实时天气和空气质量，输入为城市名。"
TOOLS = {"Weather": weather_tool}
```

- `Description` 帮模型判断该不该选 Weather；
- `Name` 让客户端从 `TOOLS` 找到 `weather_tool`；
- `Execution Logic` 是客户端真正执行的函数；它内部还可以访问外部 API、数据库或其他服务；
- 函数返回值由客户端追加为 `Observation`。

## 确定性 fake LLM 能证明什么

把 `llm_call` 注入 `run_react`，可用固定函数稳定验证客户端循环：

```python
def deepseek_llm(prompt: str) -> str:
    response = client.chat.completions.create(...)
    return response.choices[0].message.content

run_react(question="...", llm_call=deepseek_llm, max_steps=3)
```

最小接口契约是 `Callable[[str], str]`：输入完整 prompt 字符串，输出模型原始文本字符串。

确定性 demo 可以证明：

- 客户端能解析格式正确的 Action；
- 能执行注册工具并获得真实本地结果；
- 能把 Observation 写入 history，供下一轮读取；
- 非空 Finish 和 `max_steps` 分支能按代码工作。

它不能证明：

- 真实 LLM 总会遵守 Thought/Action 格式；
- 真实 LLM 总会选择正确工具和参数；
- `Thought:` 文本就是可验证的模型内部思考；
- 当前玩具 demo 已具备生产级安全、恢复或质量保证。

## 常见错误 → 正确理解

| 错误理解 | 正确理解 |
|---|---|
| 出现 Action 就代表天气 API 已执行 | Action 只是请求；客户端随后才解析和执行 |
| Thought 把 Observation 写回历史 | 客户端写回，下一轮 LLM 读取 |
| 工具函数就是外部 API | 工具函数是客户端执行入口，内部可以再调用外部 API |
| 正常退出就代表目标完成 | 控制流停止与任务质量要分开判断 |
| Prompt 写了格式就一定守格式 | Prompt 是软约束，解析器和校验分支才是硬边界 |
| fake LLM 跑通证明真实模型可靠 | 只证明固定输入下的客户端代码路径可运行 |

## 相关链接

- [[智能体(Agent)]]
- [[工具调用与动作(Tool Calling and Action)]]
- [[工具定义与执行协议(Tool Definition)]]
- [[../LLM/多轮对话与无状态记忆(Stateless Memory)|多轮对话与无状态记忆]]
- [[../../04-Projects/Agent/AI-Agent-Learning/a4-03-react-agent|A4-03 ReAct Agent 代码实践]]
- [[../../07-Reviews/AI-Agent-Learning/2026-07-22-a4-03-react-review|2026-07-22 A4-03 PASS 复盘]]
