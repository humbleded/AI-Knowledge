---
type: concept
topic: Agent Action-Bound Confirmation
status: usable
created: 2026-08-24
updated: 2026-08-24
source:
  - C:\Users\26823\Desktop\AI-Agent-Learning\code\stage4\problem-contract.md
  - C:\Users\26823\Desktop\AI-Agent-Learning\code\stage4\a4_gate_research_summary_agent.py
  - C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-08-23.md
  - C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-08-24.md
tags:
  - AI/Agent
  - HITL
  - Safety
  - Authorization
  - Replay-Protection
  - AI-Agent-Learning
aliases:
  - Action-Bound Confirmation
  - 动作绑定确认
  - 一次性人工授权
  - HITL Confirmation Gate
---

# 动作绑定人工确认（Action-Bound Confirmation）

## 一句话

动作绑定人工确认是：客户端先冻结一份具体危险动作，再让用户只批准或拒绝这份动作；确认必须与请求、工具和完整参数精确绑定，并在副作用前一次性消费，不能被模型伪造、跨请求挪用或重复播放。

## 新手比喻：一次性取件码

普通“我同意”像一张没有收件人和包裹号的纸条，任何包裹都可能拿来套用。

动作绑定 confirmation 更像一次性取件码：

- 写明是哪一单；
- 写明取哪件包裹；
- 写明完整动作参数；
- 只能使用一次；
- 即使柜门卡住或取件过程超时，原码也不能再开第二次。

## 客户端必须冻结什么

`planned_action` 至少包含：

```json
{
  "request_id": "req-current",
  "tool_name": "fake_delete_source",
  "arguments": {
    "relative_path": "sample.txt"
  }
}
```

confirmation 恰好绑定这份动作：

```json
{
  "confirmation_id": "受信客户端生成的一次性 UUID/nonce",
  "request_id": "req-current",
  "tool_name": "fake_delete_source",
  "arguments": {
    "relative_path": "sample.txt"
  },
  "decision": "allow"
}
```

客户端必须逐项检查：

1. `confirmation.request_id == planned_action.request_id`；
2. `planned_action.request_id == run_context.request_id`；
3. `confirmation.tool_name == planned_action.tool_name`；
4. `action_executor_name == planned_action.tool_name`；
5. `confirmation.arguments` 与 `planned_action.arguments` 深度相等；
6. `decision` 只能是精确 `"allow"` 或 `"deny"`；
7. `confirmation_id` 是受信客户端生成的非空一次性标识，且尚未消费。

`request_id + tool_name + arguments` 不能替代 `confirmation_id`。同一请求可能合法出现两份内容完全相同的动作授权；只有单独 nonce 才能区分两张授权单。

## 正确的消费与执行顺序

```text
先校验调用方不变量
→ 校验 confirmation 结构
→ 精确绑定 planned_action
→ 检查 confirmation_id 是否已消费
→ fresh allow / deny 都立即消费 ID
→ deny：安全停止
→ allow：再占 step
→ 再执行危险动作
→ 成功或异常都记录一次真实 tool_call
```

关键点是“**先消费，再副作用**”。它提供的是 at-most-once（至多一次）语义，不是自动 retry。

如果把消费放到工具成功以后，会出现：

```text
工具已收到请求
→ 客户端 timeout，不知道副作用是否发生
→ confirmation 尚未标记消费
→ 重放同一授权
→ 可能重复删除、重复扣款或重复发送
```

## 五种安全停止

| 情况 | fake | step | 七字段调用日志 | 对外结果 |
|---|---:|---:|---:|---|
| fresh exact deny | 0 | +0 | +0 | `needs_manual`，`sources=[]` |
| confirmation 缺失 | 0 | +0 | +0 | `needs_manual`，`sources=[]` |
| confirmation 结构非法 | 0 | +0 | +0 | `needs_manual`，`sources=[]` |
| request/tool/arguments/executor 任一错绑 | 0 | +0 | +0 | 业务错绑安全停止；跨请求或执行器配置不变量按合同上抛 |
| `confirmation_id` replay | 0 | +0 | +0 | `needs_manual`，`sources=[]` |

这些是确认门停止，不是一次真实工具尝试，所以不能伪造 `tool_call` step 或日志。

## allow 后的异常怎样处理

fresh exact allow 通过后：

1. ID 已消费；
2. 占一个真实工具 step；
3. fake 调用一次；
4. 写一条七字段 `tool_call` 日志；
5. fake 抛异常时，`error` 只记录 `type(exc).__name__`；
6. 使用裸 `raise` 传播同一个异常对象；
7. 本分支没有公开 `status / summary / sources`。

例如 fake 抛 `TimeoutError`：

```text
第一次：
confirmation 已消费
fake 1 次
step +1
log +1，error="TimeoutError"
原 TimeoutError 上抛

第二次提交同一 confirmation：
replay 在副作用前被拒绝
fake +0
step +0
log +0
needs_manual
```

超时只证明“客户端没有取得确定结果”，不能证明危险动作没有发生。因此，不能因为“上次可能失败”就重放旧授权。

## 模型为什么不能生成 confirmation

模型只有动作提议权，没有授权签发权。若模型输出能充当 confirmation，它就能同时：

- 提议危险动作；
- 声称用户已允许；
- 触发执行。

这等于让同一个不可信主体既开支票又批准支票。confirmation 必须来自受信客户端的人机交互面，并在模型上下文之外执行绑定与消费检查。

## 当前 V1 的边界

A4-Gate 的实现是同步、单进程、内存版：

- `consumed_confirmation_ids` 是内存 set；
- “检查是否存在 + 加入 set”在当前同步路径中按顺序完成；
- 不提供多进程、多实例、持久化、签名令牌或原子数据库事务；
- 生产工具仍只有两个只读工具，危险 fake 只通过 eval 显式注入。

若迁移到真实支付、删除、部署或消息发送，需要进一步增加：

- 持久化原子消费；
- 幂等键与服务端去重；
- 用户身份和权限验证；
- 审批有效期；
- 影响预览与可审计签名；
- “状态未知”后的人工核对流程。

## 最小测试矩阵

必须至少覆盖：

- fresh allow：fake 恰好 1，step/log 各 +1；
- fresh deny：fake 0，step/log +0，ID 已消费；
- missing / invalid / mismatch / replay：fake 0，step/log +0；
- request 三方绑定与 executor 名绑定；
- allow 后 fake timeout：一条失败日志、原异常 identity 上抛；
- timeout 后 replay：第二次 fake 0；
- step 已满：ID 先消费，fake 0；旧授权不能因预算失败而复用；
- `TOOL_REGISTRY` 与模型 schemas 前后不变，fake 从未注册。

## 相关链接

- [[受控重试与人工接管(Bounded Retry and Human Handoff)|受控重试与人工接管]]
- [[工具调用与动作(Tool Calling and Action)|工具调用与动作]]
- [[../LLM/LLM 本质与幻觉(Hallucination)|LLM 本质与幻觉]]
- [[../../04-Projects/Agent/AI-Agent-Learning/a4-gate-research-summary-agent|A4-Gate 研究摘要 Agent]]
- [[../../04-Projects/Agent/AI-Agent-Learning/a4-gate-function-call-reference|A4-Gate 函数调用参考]]
