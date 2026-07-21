---
type: project
topic: AI-Agent-Learning A4-03 ReAct
status: pass
created: 2026-07-22
updated: 2026-07-22
source:
  - C:\Users\26823\Desktop\AI-Agent-Learning\code\stage4\a4_03_react_agent.py
  - C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-07-21.md
  - C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-07-22.md
tags:
  - Agent
  - ReAct
  - Python
  - AI-Agent-Learning
---

# A4-03 ReAct Agent

## 目标与产物

- 产物：`C:\Users\26823\Desktop\AI-Agent-Learning\code\stage4\a4_03_react_agent.py`
- 目标：实现可运行的最小 ReAct 循环，展示完整轨迹，并用 `max_steps` 防止无限循环。
- 正式结果：**PASS（2026-07-22）**。

## 结构

| 部分 | 作用 |
|---|---|
| `weather_tool()` | 返回可重复的本地天气数据，避免把网络波动混入控制循环练习 |
| `TOOLS_DESCRIPTION` | 给模型看的工具菜单 |
| `TOOLS` | 客户端持有的名称 → Python 函数注册表 |
| `parse_llm_output()` | 从原始文本提取 Thought / Action |
| `parse_action()` | 用 `re.fullmatch` 解析 `Tool[input]` |
| `build_prompt()` | 把 tools、question、history 拼成每轮完整输入 |
| `run_react()` | 调模型、解析、分发工具、回填 Observation、Finish/限步停止 |
| `demo_llm()` | 根据 prompt 中是否已有天气 Observation 返回两段固定响应 |

## 实际轨迹

```text
--- 第 1 步 ---
Thought: 我需要查询实时天气。
Action: Weather[Singapore]
Observation: 34°C, AQI=160

--- 第 2 步 ---
Thought: 我已经得到了天气信息。
Final Answer: 新加坡的实时天气是 34°C，空气质量指数为 160。
```

第一轮工具结果被客户端追加为 `Observation`；第二轮 `demo_llm` 从完整 prompt 中读到该结果，再返回非空 Finish。

## 关键停止边界

```python
if not action:
    return None

if tool_name == "Finish" and tool_input:
    return tool_input

for step in range(1, max_steps + 1):
    ...
return None
```

- 缺失 Action：安全停止；
- `Finish[]`：不能作为成功答案，会形成无效 Action Observation 并继续；
- 非空 Finish：成功返回；
- 循环耗尽：稳定返回 `None`，没有越界的下一次模型调用。

## 正式验证

- 真实脚本直接运行：退出码 0，完整两轮轨迹通过。
- 内存断言：15/15 通过。
- 覆盖：语法、普通/多行 parser、正文内字面 Action、缩进标签、缺失/坏 Action、空/非空 history、完整 demo、精确 max_steps、空 Finish、未知工具、非空 Finish、安全停止。
- `git diff --check`：通过。
- 未创建一次性持久 runner；决定性命令与结果保存在执行区 `daily/2026-07-22.md`。

## 缺陷与订正

1. 空 `Finish[]` 曾可能被误当成结束意图；最终用 `tool_name == "Finish" and tool_input` 做客户端硬校验。
2. Thought 正文中的字面 `Action:` 曾干扰解析；最终把字段边界绑定到行首，并用多行/跨行 flags。
3. 独立复测时曾把 `(.*?)` 错写为 `(.\**?)`，误把量词星号转义；在新的 `Reasoning/Decision` 场景中无提示迁移通过。
4. 精确返回元组多次漏写 Python 字符串引号；最终能输出合法字符串与 `\n`。

## 证据边界与后续缺口

- 当前 demo 证明客户端 ReAct 控制循环，不证明真实 DeepSeek 的格式遵守率或工具选择质量。
- 当前 Weather 是确定性本地工具，不是生产外部 API。
- 当前是手写文本协议，不等于原生 API Function Calling。
- 工作场景 WS-03 本次新增可执行回归，但不替代 T3-Gate 已有的更强诊断修复证据。
- W4 算法仍为 `DEBT`（0/4）；普通课程 PASS 不升级岗位就绪等级。

## 相关链接

- [[../../../02-Concepts/Agent/ReAct推理与行动循环(ReAct)|ReAct 推理与行动循环]]
- [[../../../02-Concepts/Agent/工具定义与执行协议(Tool Definition)|工具定义与执行协议]]
- [[../../../03-Courses/Agent/AI-Agent-Learning/stage4-agent-basics|阶段 4：Agent 基础原理]]
- [[../../../07-Reviews/AI-Agent-Learning/2026-07-22-a4-03-react-review|A4-03 PASS 复盘]]
