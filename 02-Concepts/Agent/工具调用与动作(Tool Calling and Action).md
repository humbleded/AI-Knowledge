---
type: concept
topic: Agent
status: usable
created: 2026-07-10
updated: 2026-07-10
source:
  - AI-Agent-Learning 对话：Tool / Tool Calling / Action / Fine-tuning 辨析（2026-07-10）
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

**Tool 是工具本身；Tool Calling 是模型请求调用工具的动作；在 Agent 循环里，Tool Calling 通常可以看作 Action 的一种。**

再补一层边界：Tool Calling 能力通常由模型厂商训练好，但你在 API 里传 `tools` 参数，只是在提供工具说明书，不是在微调模型。

## 三个词的关系

| 概念 | 人话解释 | 例子 |
|---|---|---|
| `Tool` | 一个可用能力，通常包含工具说明和真实执行函数 | `get_weather(city)`、`calculator(expression)` |
| `Tool Calling` | 模型说“我要用哪个工具、参数是什么”的请求 | 调用 `calculator`，参数是 `{"expression": "128 * 37"}` |
| `Action` | Agent 决定要采取的下一步动作 | 调工具、查资料、写文件、点击按钮、最终回答等 |

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

| 问题 | 正确理解 |
|---|---|
| Tool Calling 是微调吗？ | 不是。它是模型表现出来的一种能力或 API 机制。 |
| 这个能力从哪来？ | 通常由模型厂商在训练、指令微调、对齐等阶段做进去。 |
| 我传 `tools=[...]` 是微调吗？ | 不是。只是告诉模型“有哪些工具、怎么填参数”。 |
| 什么情况才接近微调？ | 你准备大量样本，如“用户问题 -> 应调用哪个工具 -> 参数怎么填”，再继续训练模型。 |

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

- 错误理解：Tool Calling 后模型自己执行了工具。  
  正确理解：模型只输出工具名和参数；客户端程序才真正执行工具。

- 错误理解：只要传了 `tools` 参数，就是在微调模型。  
  正确理解：`tools` 参数只是工具说明书；不会改变模型权重。

- 错误理解：Tool Calling 是所有 Action。  
  正确理解：Tool Calling 是 Action 的一种；Action 还可以是点击、写文件、发消息、最终回答等。

- 错误理解：模型厂商训练好了我的具体业务工具。  
  正确理解：厂商训练好的是通用调用能力；具体工具由开发者提供。

## 复习口诀

```text
Tool = 能力本身
Tool Calling = 请求使用能力
Action = Agent 的下一步动作
Tool Calling 属于 Action
tools 参数 = 工具说明书
Fine-tuning = 训练或改变模型，不是普通传参
```

## 相关链接

- [[../../LLM/函数调用(Function Calling)|函数调用(Function Calling / Tool Calling)]]
- [[工具定义与执行协议(Tool Definition)]]
- [[外部 API 工具(External API Tool)]]
