---
aliases:
  - function-calling
  - tool-calling
type: concept
topic: LLM
status: usable
created: 2026-07-03
source:
  - AI-Agent-Learning T3-01（2026-07-01 学习日）
  - HF agents-course 中文版 unit1 + bonus-unit1
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

## 关联

- [[结构化输出(Structured Output)]]：Action JSON 是结构化输出的杀手级应用；`json_object` 与 FC 同为「官方开关」。
- [[多轮对话与无状态记忆(Stateless Memory)]]：Action / Observation 拼回整盘重发的底层原因。
- [[采样参数与成本(Sampling)]]：「prompt 软请求 vs 训练焊死」的概率视角；贪心解码。
- [[提示工程基础(Prompt Engineering)]]：手搓说明书＝prompt 工程；四要素。
- [[LLM 本质与幻觉(Hallucination)]]：自编 Observation ＝ 幻觉在 Agent 链路里的具体形态。
- [[MCP(Model Context Protocol)]]：统一「怎么给模型提供工具」的开放协议（阶段 9 展开）。

## 来源

- AI-Agent-Learning T3-01：笔记 `notes/stage3/t3_01_function_calling.md`（共写、含自纠痕迹）；`daily/2026-07-01.md`（带读 7 题＋练习 13 题全 PASS）。
- HF agents-course 中文版：`unit1/tools.mdx`、`actions.mdx`、`observations.mdx`、`bonus-unit1/what-is-function-calling.mdx`。
