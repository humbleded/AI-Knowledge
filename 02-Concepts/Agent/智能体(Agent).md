---
type: concept
topic: Agent
status: usable
created: 2026-07-10
updated: 2026-07-22
source:
  - C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-07-09.md
  - C:\Users\26823\Desktop\AI-Agent-Learning\notes\stage4\a4_01_what_is_agent.md
tags:
  - Agent
  - ToolCalling
  - Observation
  - AI-Agent-Learning
---

# 智能体（Agent）

## 一句话定义

Agent 是一个为了完成用户目标，使用模型进行推理和计划，并通过工具执行动作、接收 Observation、与外部环境交互的系统。

可以记成：

```text
Agent = LLM + 工具 + 客户端调度程序 + Observation 反馈循环
```

## 四个关键部件

| 部件 | 职责 |
|---|---|
| LLM | 理解目标、推理/计划、选择工具和参数 |
| 客户端调度程序 | 提供工具菜单、解析 Action、执行工具、回填 Observation |
| 工具 | 执行具体能力，例如计算、读文件、请求 API |
| Observation | 工具执行后的真实反馈，供 LLM 判断下一步 |

LLM 不亲自执行工具。它生成工具调用请求；客户端程序真正执行工具；工具结果再作为 Observation 回到上下文。

## Agent 和 Chatbot 的区别

Chatbot 偏回答问题，Agent 偏为了目标采取行动。

```text
Chatbot：
用户输入 -> 模型生成文本 -> 展示给用户

Agent：
用户目标 -> LLM 推理/计划 -> Action -> 客户端执行工具
-> 工具返回结果 -> Observation -> LLM 最终回答或继续行动
```

所以区别不在“Agent 用的模型更聪明”，而在 Agent 是否能通过工具影响程序流程和外部环境。

## Tool / Action / Observation / Final Answer

| 概念 | 解释 | 例子 |
|---|---|---|
| Tool | 系统提供的能力 | `public_api_tool` |
| Action | 一次具体工具调用请求 | `{"tool_name": "public_api_tool", "arguments": {"url": "https://api.github.com"}}` |
| Observation | 工具执行后的真实结果 | `{"ok": false, "status_code": 404}` |
| Final Answer | 模型基于 Observation 写给用户的人话答案 | “请求已到达服务器，但目标资源不存在。” |

Tool 是能力，Action 是一次使用能力的请求。Observation 不是执行者，而是工具结果被回填后的反馈。

## Tool Calling 不等于多步 Agent

Tool Calling 解决的是“模型如何表达要调用哪个工具、传什么参数”。

多步 Agent 还需要循环：

```text
Thought -> Action -> Observation
如果目标完成 -> Final Answer
如果目标未完成 -> 继续下一轮
```

只有当程序把 Observation 回填给模型，并让模型基于结果判断是否继续行动时，才是多步 Agent。

## 什么时候不需要 Agent

稳定概念通常不需要工具：

```text
HTTP 404 是什么意思？
```

当前外部状态、私有数据、精确计算或真实副作用需要工具：

```text
现在 https://api.github.com/not-found-for-t3-04 返回什么状态码？
```

关键判断：

```text
是否依赖外部实时信息、私有数据、精确计算或真实副作用？
```

## 可靠性边界

不能只相信模型。

```text
模型负责判断和生成意图；
程序负责执行、校验、兜底和拦截。
```

常见代码硬校验：

- Action JSON 必须能被 `json.loads` 解析。
- `tool_name` 必须存在于 `TOOLS` 注册表。
- `arguments` 必须是 dict，并符合参数 schema。
- 文件路径必须 `resolve()` 后确认仍在 `SANDBOX` 内。
- 外部 API 必须设置 `timeout`，并捕获异常返回稳定 `ok/error`。
- 结构化输出解析成 Python dict 后必须 `validate_payload`。

## 常见坑

### 把模型自编 Observation 当真

模型输出：

```text
Observation: {"ok": true, "status_code": 200}
```

不代表工具真的执行了。

判别法：

```text
看代码有没有真实解析 Action、调用工具、拿到返回值。
```

### Action JSON 不严格

工具调用请求要能被客户端稳定解析。

正确例子：

```json
{
  "tool_name": "public_api_tool",
  "arguments": {
    "url": "https://api.github.com"
  }
}
```

严格 JSON 不能使用中文弯引号，字符串值必须加双引号，最后一个字段后不能有尾逗号。

## 相关链接

- [[ReAct推理与行动循环(ReAct)]]
- [[工具调用与动作(Tool Calling and Action)]]
- [[工具定义与执行协议(Tool Definition)]]
- [[文件工具沙箱(File Tool Sandbox)]]
- [[外部 API 工具(External API Tool)]]
- [[../LLM/函数调用(Function Calling)|函数调用(Function Calling)]]
