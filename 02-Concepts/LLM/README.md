---
type: concept-index
topic: LLM
status: active
created: 2026-05-28
updated: 2026-06-17
tags:
  - LLM
  - 概念卡
---

# LLM 概念卡

## 训练基础

- [[backpropagation|Backpropagation]]：usable，理解计算图和梯度传播。
- [[gradient-descent|Gradient Descent]]：usable，理解如何用梯度更新参数。

## 语言建模基础

- [[tokenization|Tokenization]]：usable，理解文本如何变成 token ID。
- [[embedding|Embedding]]：usable，理解 token/position 如何变成向量表示。
- [[autoregressive-generation|Autoregressive Generation]]：usable，理解下一个 token 预测和生成循环。
- [[llm-essence-and-hallucination|LLM 本质与幻觉]]：usable，LLM=预测下一个最可能 token；幻觉是"只求像、不求真"的天生副作用(最可能≠最真实)，靠 RAG 等缓解。

## Transformer 基础

- [[attention|Attention]]：usable，理解 Q/K/V、causal mask 和上下文读取。
- [[transformer|Transformer]]：usable，理解 GPT 类模型的基本 block。

## 调用与工程

- [[api-key-and-sdk|API Key 与 SDK：调用模型的门禁卡和快递柜台]]：usable，理解 key、模型名、SDK 和环境变量的分工。
- [[chat-completions-call|调用 LLM：chat.completions 与取回复]]：usable，传 `messages`、取 `response.choices[0].message.content`，含 key/`load_dotenv`、错误提示、封装复用等易错点。
- [[message-roles-and-instruction-hierarchy|消息角色与指令优先级（chain of command）]]：usable，system/developer/user/assistant 四角色何时进 messages、system=developer 新旧叫名、优先级链（平台>system/developer>user>tool）、规则放 system 的两点理由、上下文窗口≠幻觉。
- [[multi-turn-stateless-memory|多轮对话：接口无状态与客户端记忆]]：usable，服务端不记上一轮，记忆=客户端每轮重发 `[SYSTEM]+history+本轮`（SYSTEM 也每轮发）；append=记不记 / trim=记多久；SYSTEM 固定不裁 vs history 动态会裁。
- [[streaming-output|流式输出：stream=True 与逐 chunk 处理]]：usable，`stream=True`+`for chunk`+`delta.content or ""` 三件套；None 两场景（思考阶段/末块）；推理模型两条流 `reasoning_content`/`content`；拼回完整文本才能进 history；错误 return 字符串而非 None 防毒化。

## 对应课程

- [[../../03-Courses/LLM/Karpathy-Zero-to-Hero/README|Karpathy Zero to Hero]]
- [[../../03-Courses/LLM/Karpathy-Zero-to-Hero/01-micrograd]]
- [[../../03-Courses/LLM/Karpathy-Zero-to-Hero/02-makemore]]
- [[../../03-Courses/LLM/Karpathy-Zero-to-Hero/05-gpt-from-scratch]]

## 下一批可新增概念

- cross entropy
- logits
- softmax
- train/validation split
- overfitting
- layer normalization
- residual connection
