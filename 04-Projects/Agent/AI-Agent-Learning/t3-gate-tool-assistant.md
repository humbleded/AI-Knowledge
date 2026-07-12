---
type: project-note
topic: T3-Gate Tool Calling Assistant
status: pass
created: 2026-07-12
updated: 2026-07-12
source:
  - C:\Users\26823\Desktop\AI-Agent-Learning\code\stage3\t3_gate_tool_assistant.py
  - C:\Users\26823\Desktop\AI-Agent-Learning\code\stage3\eval_cases.json
  - C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-07-11.md
tags:
  - Agent
  - Tool-Calling
  - Security
  - Evaluation
  - AI-Agent-Learning
---

# T3-Gate 三工具助手

## 目标

把计算器、沙箱文件读取和公开 API 接入一个真实的 DeepSeek Tool Calling 客户端闭环：模型选择工具与参数，客户端校验并执行真实 Python 函数，再把结果按 `tool_call_id` 回填给模型生成最终回答。

## 执行区产物

- 主程序：`C:\Users\26823\Desktop\AI-Agent-Learning\code\stage3\t3_gate_tool_assistant.py`
- 唯一持久评估数据：`C:\Users\26823\Desktop\AI-Agent-Learning\code\stage3\eval_cases.json`
- 学习笔记：`C:\Users\26823\Desktop\AI-Agent-Learning\notes\stage3\t3_gate_tool_assistant.md`
- 正式记录：`C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-07-11.md`

## 闭环结构

```text
客户端发送 messages + tools schema
  -> DeepSeek 返回最终 content 或 assistant.tool_calls
  -> 客户端保存完整 assistant 消息
  -> 每个调用独立校验并从 TOOLS 注册表执行真实函数
  -> 结果 json.dumps 后以 role="tool" + 原 tool_call_id 回填
  -> 客户端再次请求模型
  -> 最终回答，或进入下一工具轮
```

核心分工：

| 组件 | 作用 |
|---|---|
| 小写 `tools` | 给模型看的三个 function JSON Schema |
| 大写 `TOOLS` | 客户端使用的工具名到 Python 函数注册表 |
| 模型 | 选择工具和参数，或返回最终文本 |
| 客户端 | 解析、校验、执行、回填、控制轮数 |

## 客户端校验

每个 `tool_call.function.arguments` 按以下顺序处理：

```text
工具名白名单
-> JSON 字符串
-> json.loads()
-> dict / JSON object
-> required 与多余字段
-> 类型、枚举、范围、有限数字
-> 路径或 URL 安全策略
-> TOOLS[name](**arguments)
```

不使用 `eval()`。未知工具、坏 JSON、缺字段、多余字段、非法类型和执行异常都会变成稳定的 `ok/error` 结果，而不是让 Agent 主循环崩溃。

## 多调用与回填协议

一个 assistant 响应可同时包含多个 `tool_call`。客户端先追加完整 assistant 消息，再为每个调用追加独立工具结果：

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

执行前被客户端拒绝的调用仍要按原 ID 回填错误；它增加 `tool_call` 和工具消息数量，但不增加真实 Python 函数执行数。

## 安全边界

### 文件

- Gate 分发器先限制相对路径。
- 真实文件工具再用 `resolve() + relative_to(SANDBOX)` 验证最终落点。
- 限制 `max_chars`，避免把长文件全部塞进上下文。

### 外部 API

- 仅允许 HTTPS。
- hostname 必须在 allowlist。
- 只允许默认端口或 `443`；显式空端口通过 `netloc.endswith(":")` 拒绝。
- `requests.get(..., allow_redirects=False)` 禁止自动跳转；3xx 稳定返回“拒绝重定向”。
- 设置 `timeout=5` 并稳定处理超时。

当前重定向策略会同时拒绝合法 API 的 3xx。若未来允许跳转，必须逐跳重新校验 `Location`；DNS rebinding 与解析后 IP 约束留给后续完整安全任务。

## 最大工具轮数

`MAX_TOOL_ROUNDS = 3`。当模型第四次仍请求工具时，客户端已经收到第四次模型响应，但不会执行其中的 `round_4_call`，而是直接向 `run_agent()` 调用者返回：

```text
已达到最大工具调用轮数 3，停止执行。
```

## 正式评估

- 数据集：`t3-gate-v2`
- SHA-256：`76664937408435087A48691EE6EBE6287F0127E154CFB51671823950C67C042F`

| 类别 | 结果 | 阈值 |
|---|---:|---:|
| normal | 10/10 | >= 90% |
| failure | 3/3 | 100% |
| danger | 1/1 | 100% |
| holdout | 3/3 | 100% |

总计 14/14，失败 ID 为空；两个独立 evaluator 直接执行同一冻结数据集，结果一致。真实 DeepSeek 请求 19 次，三工具均真实执行。

组件证据：工具选择与参数 10/10、禁用工具 10/10、工具结果 21/21、轨迹 59/59、最终回答 13/13、安全断言 9/9。

### D01 复合故障

- 未知工具：客户端执行前拒绝。
- SSRF URL：客户端执行前拒绝。
- 302：进入真实 API 工具，调用一次 mock `requests.get`，但不跟随跳转。
- timeout：进入真实 API 工具，由 mock 抛出 `requests.Timeout` 并返回稳定错误。
- 正式 fixture 以 `tool_call_batch` 直接注入 4 个调用，不经过 `run_agent()`：`model_calls=0`、Python 工具执行 2 次、mock `requests.get` 调用 2 次、真实外网请求 0 次、带原 ID 的 dispatcher 结果 4 个、重定向跟随 0 次。

若同一批调用由真实 assistant 响应进入 `run_agent()`，协议上会形成 1 个工具轮和 4 条 `role="tool"` 回填；这是协议推演，不是 D01 evaluator 的实际外层轨迹。

### F03 轮数上限

- 脚本客户端 `create/model_calls` 4 次，不是真实 DeepSeek 网络请求。
- `tool_call` 数 4。
- Python 工具执行 3 次。
- `role="tool"` 回填 3 条。
- `tool_rounds=3`。
- `round_4_call` 未执行。

## 评估产物取舍

项目只长期保留 `eval_cases.json`，正式运行用一次性内存 evaluator，稳定结果写入 daily。没有保存专用 `run_evals.py`、baseline 或逐次原始报告，避免一次性评估产物增加维护和上下文成本。

## 相关

- [[../../../../02-Concepts/LLM/函数调用(Function Calling)|函数调用 / Tool Calling]]
- [[../../../../02-Concepts/Agent/工具定义与执行协议(Tool Definition)]]
- [[../../../../02-Concepts/Agent/文件工具沙箱(File Tool Sandbox)]]
- [[../../../../02-Concepts/Agent/外部 API 工具(External API Tool)]]
- [[../../../../07-Reviews/AI-Agent-Learning/2026-07-12-t3-gate-tool-calling-review|T3-Gate PASS 复盘]]
