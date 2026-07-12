---
type: review
topic: AI-Agent-Learning T3-Gate
status: pass
created: 2026-07-12
updated: 2026-07-12
source:
  - C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-07-11.md
  - C:\Users\26823\Desktop\AI-Agent-Learning\code\stage3\t3_gate_tool_assistant.py
  - C:\Users\26823\Desktop\AI-Agent-Learning\code\stage3\eval_cases.json
tags:
  - AI-Agent-Learning
  - Agent
  - Tool-Calling
  - Security
  - PASS
---

# 2026-07-12 T3-Gate Tool Calling PASS 复盘

## 判定

**T3-Gate PASS**。

阶段 3 的 T3-01～T3-Gate 已全部通过。当前证据证明能把三个真实工具接入原生 Tool Calling 循环，处理直接回答、多调用、参数失败、安全拒绝、工具异常和最大轮数，并能解释模型与客户端的责任边界。

本结论是课程 PASS，不自动等同 `JOB_EVIDENCE` 或求职就绪等级升级。

## 验证依据

- 数据集：`t3-gate-v2`
- SHA-256：`76664937408435087A48691EE6EBE6287F0127E154CFB51671823950C67C042F`
- normal：10/10
- failure：3/3
- danger：1/1
- holdout：3/3
- failed IDs：`[]`
- 真实 DeepSeek 请求：19
- 两个独立 evaluator 对同一冻结数据集均为 14/14 PASS

关键组件：工具选择与参数 10/10、禁用工具 10/10、工具结果 21/21、轨迹 59/59、最终回答 13/13、安全断言 9/9。

## 真实闭环证据

- `calculator_tool`、`read_sandbox_file`、`public_api_tool` 均由客户端真实执行。
- 模型返回 `assistant.tool_calls`，没有用关键词 `if/elif` 假装模型选择工具。
- 客户端先保存完整 assistant 消息，再为每个调用按原 `tool_call_id` 回填 JSON 字符串结果。
- 没有工具调用时直接返回模型最终文本。
- DeepSeek Thinking Mode 在本关显式关闭；后续开启时需保留完整 `reasoning_content`。

## D01 复合事故闭环

| 调用 | 拦截位置 | 结果 |
|---|---|---|
| 未知工具 | 真实函数执行前 | 不在 `TOOLS` 白名单 |
| SSRF URL | 真实函数执行前 | host 不在 allowlist |
| 302 重定向 | 进入 API 工具后 | 调用一次 mock `requests.get`，禁止跟随并稳定拒绝 |
| timeout | 进入 API 工具后 | mock 抛出 Timeout，工具捕获后返回稳定错误 |

D01 正式 fixture 通过 `tool_call_batch` 直接注入 4 个调用，不经过 `run_agent()`，因此该用例 `model_calls=0`。实际证据为：4 个带原调用 ID 的 dispatcher 结果、Python 工具执行 2 次、mock `requests.get` 调用 2 次、真实外网请求 0 次、重定向跟随 0 次。

若同一批调用由真实 assistant 响应进入 `run_agent()`，协议上会形成 1 个工具轮和 4 条 `role="tool"` 回填；这是回填协议推演，不是 D01 evaluator 的实际外层轨迹。

## F03 最大轮数

当 `max_tool_rounds=3` 且模型连续四次请求工具：

- 脚本客户端 `create/model_calls` 4 次，不是真实 DeepSeek 网络请求；
- `tool_call` 数 4；
- Python 工具执行 3 次；
- `role="tool"` 回填 3 条；
- `tool_rounds` 最终为 3；
- `round_4_call` 未执行；
- `run_agent()` 直接向调用者返回“已达到最大工具调用轮数 3，停止执行。”，不再请求模型。

## 高价值订正

| 初始误区 | 正确理解 |
|---|---|
| 模型从 `TOOLS` 注册表找并执行函数 | 模型只看小写 `tools` schema；客户端查大写 `TOOLS` 并执行 |
| 一轮只有一个工具调用 ID | 一条 assistant 响应可含多个调用，每个调用有独立 ID |
| 工具轮数等于执行数或回填数 | 模型次数、工具轮、调用数、Python 执行数和工具回填数必须分开计 |
| Python 外层单引号说明内部不是 JSON | 外层引号只界定 Python 字符串；应检查字符串内容能否被 `json.loads()` 解析 |
| `.port is None` 表示空端口会自动当 443 | 显式空端口仍需用 `netloc.endswith(":")` 单独拒绝 |
| 执行前拒绝就不需要回填 | 拒绝结果也要按原 `tool_call_id` 回填，模型才能对应失败调用 |
| 达到三轮上限时模型只调用三次 | 当前控制流要先收到第 4 次仍含工具请求的响应，再在执行前停止 |

## 已知边界

- 禁止所有重定向会拒绝合法 3xx；未来若开放必须逐跳重新校验。
- DNS rebinding、解析 IP 与连接目标一致性尚未完整覆盖，留给后续安全任务。
- 五种计数仍是当前最需要脱离原题复测的弱点。
- W4 算法 4 道新题仍为显式 DEBT，课程 Gate PASS 不会把该欠账抹掉。

## 知识库同步

- 更新 [[../../02-Concepts/LLM/函数调用(Function Calling)|函数调用 / Tool Calling]]。
- 更新 [[../../02-Concepts/Agent/工具定义与执行协议(Tool Definition)]]。
- 更新 [[../../02-Concepts/Agent/外部 API 工具(External API Tool)]]。
- 新增项目页 [[../../04-Projects/Agent/AI-Agent-Learning/t3-gate-tool-assistant|T3-Gate 三工具助手]]。

## 下一步

主线进入 A4-02 LLM 与 Agent 基础，随后是 A4-03 ReAct；同时优先补 W4 算法 DEBT，并在后续多步 Agent 中扩展 Thinking Mode 的 `reasoning_content` 回传。
