---
type: concept
topic: Agent
status: usable
created: 2026-07-10
updated: 2026-07-21
source:
  - AI-Agent-Learning 对话：Tool / Tool Calling / Action / Fine-tuning 辨析（2026-07-10）
  - AI-Agent-Learning 对话：Action / Tool Call / Tool Execution 边界订正（2026-07-11）
  - AI-Agent-Learning T3-Gate 正式复核（2026-07-12）
  - AI-Agent-Learning 对话：Function Calling / Tool Calling 范围与调用格式辨析（2026-07-21）
tags:
  - Agent
  - Tool-Calling
  - Action
  - Fine-tuning
  - AI-Agent-Learning
aliases:
  - Tool Calling 与 Action
  - Tool Calling and Action
  - 工具调用
  - tools 参数
---

# 工具调用与动作(Tool Calling and Action)

## 一句话

**Action 是 Agent 对“下一步做什么”的决策；Tool Call 是模型发给客户端的结构化调用请求；Tool Execution 才是客户端真正执行工具。**

因此，模型生成工具名和参数 JSON，并不等于工具已经执行。Tool Calling 可以看作 Action 的一种实现形式，但二者不是在所有语境下都完全同义。

再补一层边界：Tool Calling 能力通常由模型厂商训练好，但你在 API 里传 `tools` 参数，只是在提供工具说明书，不是在微调模型。

## Tool Calling 与 Function Calling

**Tool Calling 是上位概念，Function Calling 是其中常见的函数型实现。**

| 比较项 | Tool Calling | Function Calling |
|---|---|---|
| 范围 | 更宽，泛指模型请求使用外部工具 | 更窄，工具以函数名和参数 schema 暴露 |
| 工具形态 | 函数、API、数据库、浏览器、代码执行器等 | `get_weather(city)` 这类函数接口 |
| 常见表达 | API 的 `tool_calls`，或 ReAct / 自定义协议里的 Action | 函数名 + `arguments`，常放在 API 的 `tool_calls` 中 |

不同平台可能近似混用这两个名字。例如，API 顶层字段叫 `tools` / `tool_calls`，其中一个具体调用的类型仍可能叫 `function`。术语判断要分两层：

- **概念层**：Tool Calling 更宽，Function Calling 是其子集；
- **平台实现层**：以当前 API 文档规定的字段和 schema 为准。

手写 ReAct 文本 `Action: Weather[Singapore]` 属于广义 Tool Calling；如果它只是靠 prompt 生成、再由客户端自行解析，就不等于 API 原生 Function Calling。详见 [[../../LLM/函数调用(Function Calling)|函数调用（Function Calling）]]。

## 六个词的关系

| 概念 | 人话解释 | 例子 |
|---|---|---|
| `Tool` | 一个可用能力，通常包含工具说明和真实执行函数 | `get_weather(city)`、`calculator(expression)` |
| `Tool Calling` | 模型说“我要用哪个工具、参数是什么”的请求 | 调用 `calculator`，参数是 `{"expression": "128 * 37"}` |
| `Function Calling` | Tool Calling 的函数型具体形式 | 请求 `get_weather(city="Singapore")` |
| `Action` | Agent 决定要采取的下一步动作 | 调工具、查资料、写文件、点击按钮、最终回答等 |
| `Tool Execution` | 客户端读取 Tool Call 后，真正运行函数或请求外部 API | 执行 `calculator(expression="128 * 37")` |
| `Tool Result` | 工具真实执行后产生的结果；回填给模型时常叫 `Observation` | `4736`，或结构化成功/错误信息 |

所以关系是：

```text
Action
  -> Tool Calling
       -> 调用 search_web(query)
       -> 调用 calculator(expression)
       -> 调用 get_weather(city)
  -> 其他动作
       -> 点击按钮
       -> 写文件
       -> 最终回答用户
```

更严格地说：模型输出的 `tool_call` 是“动作请求”，真正执行工具的是客户端程序。

## 四层流程：不要把请求当成执行

```text
Action（模型决定：下一步调用 calculator）
  -> Tool Call（模型生成：工具名 + 参数）
  -> Tool Execution（客户端真正运行 calculator）
  -> Tool Result / Observation（结果返回并回填给模型）
```

关键分界：

- **Action 是决策层**：决定下一步做什么；它不一定调用工具，也可能直接回答或结束任务。
- **Tool Call 是请求层**：模型生成客户端可解析的工具名和参数；常通过专用 `tool_calls` 字段表达，也可能在手写 ReAct 协议中表现为 JSON 文本。
- **Tool Execution 是执行层**：客户端或 Agent Runtime 才真正调用函数、数据库、浏览器或外部 API。
- **Tool Result 是结果层**：真实执行结果返回客户端，再作为工具消息或 `Observation` 交给模型。

> [!warning] 生成 JSON ≠ 执行工具
> 模型生成 `{"name": "get_weather", "arguments": {"city": "北京"}}`，只表示“请求调用”。只有客户端读取它并运行 `get_weather(city="北京")` 后，工具才真正被执行。
>
> 这还是一种**简化表示**，不是跨厂商统一的完整响应格式。若它只是出现在普通正文中，也不能仅凭外形认定为 API 原生 Function Calling。

## 为什么有些资料直接说 Action 就是 JSON

`Action` 有两种常见用法，必须看上下文：

1. **系统设计的宽泛用法**：Action 是 Agent 的下一步决策；Tool Call 是其中一种具体请求。
2. **ReAct / 自定义协议的狭义用法**：`Action` 字段直接记录工具名，`Action Input` 记录参数；两者合起来基本等于一个 Tool Call。有些代码还会把整段调用 JSON 命名为 `action`。

所以，“Action 是模型生成的 JSON”不是在任何情况下都错误，而是**使用了 ReAct 协议里的狭义定义**。当需要严格区分决策、请求和执行时，应使用四层表达：`Action -> Tool Call -> Tool Execution -> Tool Result`。

## 一条完整链路

```text
用户提问
  -> 客户端把问题 + tools 工具说明书发给模型
  -> 模型判断需要工具
  -> 模型输出 tool_call，也就是一个 Tool Calling 类型的 Action
  -> 客户端解析工具名和参数
  -> 客户端真正执行工具函数
  -> 工具结果作为 Observation / tool message 回填给模型
  -> 模型根据真实结果整理最终回答
```

例子：

```json
{
  "name": "calculator",
  "arguments": {
    "expression": "128 * 37"
  }
}
```

这段 JSON 不是计算结果，而是模型发出的调用请求。真正算出结果的是程序里的 `calculator` 函数。

## Tool Calling 和微调的关系

Tool Calling **不是微调本身**。

| 问题                     | 正确理解                                         |
| ---------------------- | -------------------------------------------- |
| Tool Calling 是微调吗？     | 不是。它是模型表现出来的一种能力或 API 机制。                    |
| 这个能力从哪来？               | 通常由模型厂商在训练、指令微调、对齐等阶段做进去。                    |
| 我传 `tools=[...]` 是微调吗？ | 不是。只是告诉模型“有哪些工具、怎么填参数”。                      |
| 什么情况才接近微调？             | 你准备大量样本，如“用户问题 -> 应调用哪个工具 -> 参数怎么填”，再继续训练模型。 |

可以用这个比喻记：

```text
微调 = 驾校训练司机
Tool Calling 能力 = 司机学会看导航、打转向灯、按规则开车
tools 参数 = 你告诉司机这辆车上有哪些按钮
客户端程序 = 真正把按钮按下去、让车动起来的部分
```

## 厂商、开发者、客户端各负责什么

| 角色 | 负责什么 |
|---|---|
| 模型厂商 | 训练模型看懂工具说明、选择工具、按格式写参数、看工具结果继续回答 |
| 开发者 | 提供具体 Tool 的名称、描述、参数结构、真实执行函数 |
| 客户端程序 | 解析模型的 tool call，真实执行工具，把结果回填给模型 |

注意：厂商训练好的是“会用工具说明书”的能力，不是你的具体工具。模型原本不知道你的 `send_email(to, subject, body)`，只有你把说明书传进去后，它才知道这轮对话里可以请求这个工具。

## 常见坑 / 错误理解 -> 正确理解

- 错误理解：Tool Calling 就是 Tool。  
  正确理解：Tool 是工具本身，Tool Calling 是请求使用工具的动作。

- 错误理解：Tool Calling 与 Function Calling 永远是完全相同的两个名字。
  正确理解：概念上 Tool Calling 更宽，Function Calling 是函数型工具调用；具体平台可能近似混用术语。

- 错误理解：Tool Calling 后模型自己执行了工具。  
  正确理解：模型只输出工具名和参数；客户端程序才真正执行工具。

- 错误理解：模型生成调用 JSON，就代表工具已经执行。
  正确理解：JSON 只是 Tool Call；客户端真正运行函数或外部 API 才是 Tool Execution。

- 错误理解：Action 在所有资料里都只表示“抽象决策”，绝不可能指调用 JSON。
  正确理解：系统设计语境里 Action 通常指下一步决策；ReAct 或自定义协议可能把工具名与参数 JSON 直接称为 Action。判断时要看该框架的字段定义。

- 错误理解：只要传了 `tools` 参数，就是在微调模型。  
  正确理解：`tools` 参数只是工具说明书；不会改变模型权重。

- 错误理解：Tool Calling 是所有 Action。  
  正确理解：Tool Calling 是 Action 的一种；Action 还可以是点击、写文件、发消息、最终回答等。

- 错误理解：模型厂商训练好了我的具体业务工具。  
  正确理解：厂商训练好的是通用调用能力；具体工具由开发者提供。

## 复习口诀

```text
Tool = 能力本身
Action = 决定下一步做什么
Tool Call = 模型生成调用请求（工具名 + 参数）
Function Calling = Tool Calling 的函数型具体形式
Tool Execution = 客户端真正执行工具
Tool Result = 真实执行结果，再回填给模型
Tool Calling 属于 Action 的一种实现形式
tools 参数 = 工具说明书
Fine-tuning = 训练或改变模型，不是普通传参
```

## 相关链接

- [[../../LLM/函数调用(Function Calling)|函数调用（Function Calling）：原生调用与手写 JSON 的边界]]
- [[工具定义与执行协议(Tool Definition)]]
- [[外部 API 工具(External API Tool)]]
- [[../../04-Projects/Agent/AI-Agent-Learning/t3-gate-tool-assistant|T3-Gate 三工具助手]]
- [[../../07-Reviews/AI-Agent-Learning/2026-07-12-t3-gate-tool-calling-review|T3-Gate PASS 复盘]]
