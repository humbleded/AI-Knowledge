---
type: review
topic: AI-Agent-Learning A4-02
status: pass
created: 2026-07-15
updated: 2026-07-15
tags:
  - AI-Agent-Learning
  - LLM
  - Agent
  - PASS
---

# 2026-07-15 A4-02 LLM 与 Agent 基础 PASS 复盘

## 判定

**A4-02 PASS**。

两天记录中共有 12 个去重后的有效证据位：LLM/Token/架构与提示训练基础、消息边界与 Chat Template、LLM/客户端/工具/Observation 职责、无状态会话、幻觉风险与分层防线，以及三条换场景迁移。正式练习又独立补齐了 `Instruction Data / Instruction Tuning / Few-shot Prompting` 的对象、参数变化和持久性边界。

## PASS 标准与证据

| PASS 标准 | 决定性证据 |
|---|---|
| LLM 不是执行器 | 能完整说明“模型生成 Tool Call → 客户端解析/校验/执行 → 工具返回真实结果 → 客户端回填 Observation → 第二次 LLM 总结” |
| 消息边界 / Chat Template 会影响理解 | 能诊断历史缺失和目标模型模板错配，并说明 messages → Prompt → Token IDs |
| 幻觉会在 Agent 中放大，且需分层防线 | 能把失败 Observation 被说成成功追踪到错误扣款/发货，并用工具权威事实、客户端硬校验、有限重试/未知状态和人工确认收口 |
| 独立迁移 | 在 6000 条 Tool Call 样本场景中正确区分训练数据、训练过程与请求内 Few-shot 示例 |

## 关键订正闭环

| 原始理解 | 订正后的稳定结论 |
|---|---|
| 参数多就一定更强 | 参数量只是容量因素；数据、训练方法、算力和结构共同影响能力 |
| 模型把输入和“相似 Token”比较 | 模型结合上下文为词表中的候选下一个 Token 打分 |
| Chat Template 控制输出 | Chat Template 首先负责序列化输入角色、顺序和边界 |
| 模型可以自己获取工具结果 | 不在当前上下文中的结果无法被 Attention 读取；客户端必须回填 |
| 生成删除/工具请求可能已经执行 | Tool Call 只是请求；客户端与工具决定真实副作用 |
| `timeout` 可以推断订单失败 | 超时只证明本次查询未得到状态，底层订单状态仍为未知 |
| 微调效果可用于“所有后续请求” | 效果保存在新模型权重中；后续请求必须实际调用该模型 |

## 验证边界

- A4-02 是概念/阅读任务，没有代码产物要求，未创建一次性测试脚本。
- 复核来源：Hello-Agents 2.4.3、2.4.4、3.1.3、3.2.2、3.3.2；Hugging Face Agents Course `what-are-llms.mdx`、`messages-and-special-tokens.mdx`。
- 证据：`daily/2026-07-14.md`、`daily/2026-07-15.md`、`notes/stage4/a4_02_llm_agent_basics.md`。
- 本次仅形成安全原理的解释级证据，不升级工作场景的可执行证据等级，也不升级岗位就绪状态。
- W4 算法仍为 `DEBT`（0/4），继续在 W5 的独立时段结转。

## 复习路由

- `CD-001`：Instruction Data / Instruction Tuning / Prompting / Few-shot 边界。
- `CD-002`：messages → Chat Template → Prompt → Token IDs 与消息边界。
- `CD-003`：幻觉在 Agent 中的风险放大及工具、代码、人工防线。
- `WP-17`：新的文件工具轨迹已订正通过，移入稳定错题池。
- 上述四项首轮回炉均为 2026-07-29；完整排期只维护在项目 `tracker/weak-points.md`。

## 知识库同步

- 更新 [[../../02-Concepts/LLM/提示工程基础(Prompt Engineering)|提示工程基础]]：补 Instruction Data / Tuning / Prompting / Few-shot 和“必须调用微调模型”的持久性边界。
- 更新 [[../../02-Concepts/LLM/特殊Token(Special Tokens)|特殊 Token]]：补 Chat Template、模板错配与 `apply_chat_template()`。
- 更新 [[../../02-Concepts/LLM/LLM 本质与幻觉(Hallucination)|LLM 本质与幻觉]]：补幻觉分类、Agent 风险放大、权威事实与分层防线。
- [[../../02-Concepts/LLM/多轮对话与无状态记忆(Stateless Memory)|无状态记忆]]、[[../../02-Concepts/Agent/工具调用与动作(Tool Calling and Action)|工具调用与动作]]、[[../../02-Concepts/Agent/智能体(Agent)|智能体]] 已准确覆盖本次职责边界，去重检查后保持不改。
- 同步后严格健康检查：`OK: True`，Markdown 189，links 1505，broken links 0，missing frontmatter 0。

## 下一步

进入 A4-03 ReAct：学习并实现多轮 Thought / Action / Observation 循环，重点加入停止条件、最大步数和失败时安全停止。
