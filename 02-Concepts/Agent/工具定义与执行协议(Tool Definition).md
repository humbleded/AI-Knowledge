---
type: concept
topic: Agent Tool Definition
status: active
created: 2026-07-06
updated: 2026-07-21
source:
  - C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-07-06.md
  - C:\Users\26823\Desktop\AI-Agent-Learning\code\stage3\t3_02_calculator_tool.py
  - C:\Users\26823\Desktop\AI-Agent-Learning\repos\hello-agents\docs\chapter4\第四章 智能体经典范式构建.md
  - C:\Users\26823\Desktop\AI-Agent-Learning\code\stage3\t3_gate_tool_assistant.py
  - C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-07-11.md
  - C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-07-21.md
tags:
  - Agent
  - Tool-Calling
  - ReAct
  - AI-Agent-Learning
---

# 工具定义与执行协议（Tool Definition）

## 一句话

一个 Agent 工具不是“随便一个函数”，而是由 **Name（叫什么）+ Description（什么时候用）+ Execution Logic（真实怎么做）** 组成的可调用能力。

## 三个核心要素

| 要素 | 人话解释 | 解决的问题 |
|---|---|---|
| `Name` | 工具的唯一名字 | 让模型和程序都能点名同一个工具 |
| `Description` | 写给模型看的用途说明 | 帮模型判断什么时候该用哪个工具 |
| `Execution Logic` | 客户端里真正执行任务的函数或方法 | 把模型的 Action 变成真实结果 |

以 `T3-02 calculator_tool` 为例：

```text
Name: calculator_tool
Description: 用于精确执行基础数学计算，支持 add/sub/mul/div
Execution Logic: 校验 operation/a/b，然后调用 operator.add/sub/mul/truediv
```

## ReAct 链路里的职责

```text
用户问题
  -> 客户端把问题 + 工具菜单发给模型
  -> 模型生成 Action：要调哪个工具、传什么参数
  -> 客户端解析 Action 并真实执行工具
  -> 工具返回 Observation
  -> 客户端把 Observation 拼回上下文
  -> 模型基于 Observation 生成最终回答
```

关键边界：

- 模型不“查自己有没有工具”；工具菜单由客户端提供。
- 模型不执行工具；它只生成工具调用请求。
- 模型不把工具结果放进上下文；客户端把 Observation 拼回去。

## `tools` schema 与 `TOOLS` 注册表

同一个工具在系统里有两种表示，服务于不同对象：

| 名称         | 使用者 | 内容                         |
| ---------- | --- | -------------------------- |
| 小写 `tools` | 模型  | JSON Schema 菜单：工具名、描述、参数结构 |
| 大写 `TOOLS` | 客户端 | Python 注册表：工具名到真实函数的映射     |

```python
TOOLS = {
    "calculator_tool": calculator_tool,
    "read_sandbox_file": read_sandbox_file,
    "public_api_tool": public_api_tool,
}
```

模型不会访问 `TOOLS`。它只根据 `tools` 生成调用请求；客户端校验通过后才执行：

```python
result = TOOLS[tool_name](**arguments)
```

原生 API 的 function schema 至少要包含：

```python
{
    "type": "function",
    "function": {
        "name": "calculator_tool",
        "description": "...",
        "parameters": {
            "type": "object",
            "properties": {...},
            "required": ["operation", "a", "b"],
            "additionalProperties": False,
        },
    },
}
```

其中 `required` 限制必填字段，`additionalProperties: false` 拒绝 schema 之外的多余字段；schema 负责告诉模型约束，客户端仍要再次硬校验。

## 客户端校验顺序

`tool_call.function.arguments` 是 JSON 字符串。不要使用会执行 Python 代码的 `eval()`；安全顺序是：

```text
工具名在 TOOLS 白名单
-> arguments 是字符串
-> json.loads()
-> 结果必须是 dict / JSON object
-> required 字段齐全
-> 没有多余字段
-> 类型、枚举、范围、业务规则和安全边界合法
-> TOOLS[name](**arguments)
```

未知工具、坏 JSON、缺字段和多余字段都应在真实函数执行前返回稳定错误。同一 assistant 消息里的多个调用要彼此独立处理，不能因为一个失败就混淆其他调用的结果。

## 稳定错误返回

工具失败时，不应该把一大串异常直接甩给用户或让程序中断。学习阶段的稳定返回结构是：

```python
{"ok": True, "result": 15.0}
{"ok": False, "error": "除数不能为 0"}
```

这样后续程序可以根据 `ok` 判断：

```python
if result["ok"]:
    # 读取 result
else:
    # 读取 error
```

## 常见坑

- 把 `Action` 当成工具结果：Action 只是模型生成的调用请求。
- 把 `Observation` 当成模型编出来的话：Observation 应来自工具真实执行。
- `Description` 写得太泛：模型会不知道该不该调用，或在多个工具之间选错。
- 回答工具错误协议时改字段名：真实代码里是 `ok/result/error`，不要临时说成 `code/result/error`。
- 把小写 `tools` 和大写 `TOOLS` 当成同一个对象：前者给模型看 schema，后者给客户端查真实函数。
- 用 `eval(arguments)` 解析模型参数：这会把不可信字符串当 Python 代码；应使用 `json.loads()` 并继续验证解析结果。

## 相关链接

- [[ReAct推理与行动循环(ReAct)|ReAct 推理与行动循环]]
- [[../LLM/函数调用(Function Calling)|函数调用（Function Calling）：Tool Calling 的函数型形式]]
- [[../../04-Projects/Agent/AI-Agent-Learning/t3-02-calculator-tool|T3-02 计算器工具]]
- [[../../07-Reviews/AI-Agent-Learning/2026-07-06-t3-02-calculator-tool-review|2026-07-06 T3-02 PASS 复盘]]
- [[../../04-Projects/Agent/AI-Agent-Learning/t3-gate-tool-assistant|T3-Gate 三工具助手]]
- [[../../07-Reviews/AI-Agent-Learning/2026-07-12-t3-gate-tool-calling-review|2026-07-12 T3-Gate PASS 复盘]]
