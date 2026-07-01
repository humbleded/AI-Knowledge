---
type: review
topic: AI-Agent-Learning L1-Gate PASS 复盘
status: done
created: 2026-06-27
tags:
  - AI-Agent-Learning
  - Stage1
  - L1-Gate
  - 复盘
  - PASS
---

# 2026-06-27 阶段 1 L1-Gate PASS 复盘

## 判定

| 任务 | 状态 | 产物 |
|---|---|---|
| L1-Gate API 入门闯关 | **PASS** | [[../../04-Projects/LLM/AI-Agent-Learning/l1-gate-cli-chatbot|L1-Gate CLI Chatbot]] |

**阶段 1（大模型 API 入门）至此全部通过**，解锁阶段 2 的动手交付与 PR2-Gate。

## 验证

- 流式真实 5 轮跑通：第 2 轮准确答出「三玖」、第 4 轮数出「聊了 3 轮」并复述每轮 → 客户端记忆完整带上。
- 非网络冒烟：空输入提示、API 出错 `except` 兜成友好字符串不崩、`exit` 退出码 0。
- 代码核对：`build_prompt` 拼 `[SYSTEM]+history+question`；非流式用 `call_messages`（非 `call_model`）；先成对 append 再 `trim_history`；`create`/client 加 `timeout=30`；key 走 `.env` 且 `git check-ignore .env` 命中。
- 4 必答 + 完整调用链路口头全过。

## 5 个整合坑（整合关的价值所在）

1. 失效 import：`build_prompt` 当时不存在 → 先补进 l1_03。
2. **非流式误用 `call_model`（列表当字符串 + 丢历史）→ 改 `call_messages`**（今日最值钱的新坑）。
3. 历史限长顺序：先成对 append 再 trim，否则限长晚一轮、history 越界。
4. 错误兜底返回友好字符串、非 None（防毒化 history）。
5. `timeout=30` 超时保护（SDK 参数，不在 DeepSeek API 文档里）。

## 配套练习

15 题全 PASS。RETRY/订正：

- **C1 漏 [SYSTEM]**：写 `build_prompt` 拼出的 messages 时漏掉开头 system，4 条答成 3 条。
- **C2 限长后果方向反**：把「先 trim 再 append」答成「信息变少」，逐条数后订正为「history 变多、限长失效」。
- B2 ③：先想到 apikey，订正为 max_retries。

## 今天最虚 / 下次重点复习

- **最虚 = 对「列表/消息的逐条精确追踪」**：C1 漏 SYSTEM、C2 数错方向，都没把 messages 逐条列出来数 —— 与 2026-06-26「Python 类型/运算要逐行跑」是同一类弱点的延续。
- **下次**：读码/写码先在脑子里把 `messages` 逐条列清（system→user→assistant→…）再下结论。
- **亮点**：L1-Gate 一次闯通；整合链路、超时闭环、API vs SDK 参数、SSE、`or` 兜底迁移全部站得住；`call_model` 整合坑彻底吃透；few-shot≠schema 老弱点已翻篇。

## 沉淀到知识库

- 新增概念卡：[[../../02-Concepts/LLM/API 参数与 SDK 客户端参数|API 参数 vs SDK 客户端参数]]
- 更新概念卡：[[../../02-Concepts/LLM/流式输出(Streaming)|流式输出]]（补 SSE 底层传输）
- 新增项目页：[[../../04-Projects/LLM/AI-Agent-Learning/l1-gate-cli-chatbot|L1-Gate CLI Chatbot]]
- 更新课程页：[[../../03-Courses/LLM/AI-Agent-Learning/stage1-llm-api-basics|阶段 1：大模型 API 入门]]

## 下一步

- 进阶段 2 动手：PR2-01 三个 prompt 对比、PR2-02 `summarizer.py`（概念+练习早已完成，动手产物排在 L1-Gate 后，现已解锁）。
- 队列：PR2-01 → PR2-02 → PR2-03 分类 → S-03 上下文工程 → PR2-04 JSON/Schema →（周末）PR2-Gate 邮件处理器。

## 来源

- 每日记录：`C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-06-27.md`
- 设计稿：`C:\Users\26823\Desktop\AI-Agent-Learning\notes\stage1\l1_gate_design_draft.md`
