---
aliases:
  - special-tokens
  - eos-token
  - end-of-sequence
type: concept
topic: LLM
status: usable
created: 2026-07-02
updated: 2026-07-15
source:
  - DeepSeek 分享对话：上下文工程、路由与特殊 Token
  - Hugging Face Agents Course：Messages and Special Tokens
  - AI-Agent-Learning A4-02 正式复核（2026-07-15）
tags:
  - LLM
  - token
  - Tokenization
  - special-token
  - EOS
  - API
---

# 特殊Token：模型词表里的控制暗号

## 一句话解释

特殊 token 是模型词表里的“控制暗号”：它们不主要表示普通文字，而是告诉模型或服务层“这里是用户消息”“这里轮到助手”“这里该结束了”等结构信息。

## API 消息格式 vs 模型内部序列

开发时常写：

```python
{"role": "user", "content": "你好"}
```

这不是模型底层真正看到的全部内容，而是 API 提供给开发者的高级协议。服务端会按该模型的 chat template，把它转换成模型专用的 token 序列。这个序列里通常会混入角色边界、轮次边界、结束标记等特殊 token。

所以要分清两层：

| 层次 | 给谁用 | 例子 |
|---|---|---|
| API 消息层 | 开发者和 SDK | `{"role": "user", "content": "..."}` |
| token 序列层 | 模型推理程序 | 普通文本 token + 角色/结束类特殊 token |

## Chat Template：把 messages 变成模型认识的边界

Chat Template 是两层之间的桥梁：它按目标模型训练时使用的格式，把结构化 messages 序列化为带角色、顺序、消息边界和生成起点的 Prompt；Tokenizer 再把 Prompt 转成 Token ID。

```text
messages
  -> Chat Template
带 system/user/assistant 边界的 Prompt 字符串
  -> Tokenizer
Token IDs
  -> LLM
```

不同模型可能使用不同的角色标记、消息结束标记和生成起点。把 SmolLM2 的标记手工套给 Llama，可能让模型把错误标记当成普通文本，或误判谁说了什么、消息在哪里结束、现在该由谁生成。

本地使用 `transformers` 时，可以让目标模型配套的 tokenizer 负责渲染：

```python
rendered_prompt = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
)
```

- `tokenize=False`：先返回格式化后的 Python `str`，不是 Token ID。
- `add_generation_prompt=True`：在模板支持时加入 assistant 开始生成的位置。
- 这一步只格式化输入，没有调用 LLM，也没有修改模型参数。

平时调用 API 不需要手写特殊 token；只有做本地开源模型、tokenizer 调试、chat template 排查时，才需要关心底层格式。

## EOS：让模型停下来的信号

EOS 是 End of Sequence，意思是“这一段序列到此结束”。在自回归生成里，模型每一步都在预测下一个 token；EOS 也是候选 token 之一。

当模型生成 EOS 时，服务层通常会把它当作“可以停止生成”的信号。否则模型理论上会继续预测下一个 token，直到触发外部限制，比如 `max_tokens`、stop sequence、内容安全中断或工具调用协议。

## 文本结束 vs 序列结束

| 对比 | 文本结束 | 序列结束 / EOS |
|---|---|---|
| 面向谁 | 人类读者 | 模型和推理程序 |
| 形式 | 句号、段落结束、语义说完 | 看不见的特殊 token |
| 作用 | 让文字读起来完整 | 让生成循环停止或切换轮次 |
| 是否硬停止 | 不是，后面还可以继续写 | 通常是服务层的停止信号 |

大白话：文本结束像文章最后一个句号；EOS 像对讲机里说“完毕”，它不是内容本身，而是流程控制信号。

## EOT 与多轮对话

有些模型会区分 EOS 和 EOT：

- EOS：一段序列整体结束。
- EOT：End of Turn，一轮对话结束，轮到下一个角色。

不同模型的特殊 token 名称、ID 和含义可能不同。不要把某个模型的 `<|end|>`、`<|eot_id|>` 或其他标记直接套到另一个模型上。

## 为什么它重要

- 它让 API 能把多轮对话切成清楚的角色边界。
- 它让模型知道什么时候应该停止，而不是继续胡乱生成。
- 它是工具调用、结构化输出、多轮消息模板的底层基础之一。
- 它解释了为什么“人类看到的一段文本”和“模型内部处理的一串 token”不是同一个层次。

## 常见坑 / 错误理解 → 正确理解

- ❌ `{"role": "user", "content": "..."}` 就是模型底层 prompt 的全部样子 → ✅ 这是 API 协议层，服务端还会转成模型专用 token 序列。
- ❌ 文本写完句号就等于模型停止 → ✅ 句号只是普通文本 token；真正停止通常靠 EOS、stop sequence 或服务层限制。
- ❌ 所有模型的特殊 token 都一样 → ✅ 特殊 token 属于 tokenizer 和 chat template 的一部分，换模型就可能不同。
- ❌ API 开发必须手写特殊 token → ✅ 常规 API 调用交给 SDK 和服务端处理即可。
- ❌ 套上 ChatML 角色标记就把 Base Model 变成 Instruct Model → ✅ 模板只负责输入边界；指令遵循能力还需要相应训练。
- ❌ Chat Template 会自动保存历史 → ✅ 客户端仍需保存并在下一请求重发必要 messages；模板只负责序列化当前收到的消息。

## 关联

- [[分词(Tokenization)]]：特殊 token 也是 tokenizer 词表的一部分。
- [[自回归生成(Autoregressive)]]：EOS 是生成循环可能输出的下一个 token。
- [[调用 chat.completions]]：API 消息格式是开发者使用的上层协议。
- [[结构化输出(Structured Output)]]：结构化输出依赖模型按约束生成，也受停止信号影响。
- [[多轮对话与无状态记忆(Stateless Memory)]]：为什么历史和 system 指令仍需由客户端重发。
- [[../../07-Reviews/AI-Agent-Learning/2026-07-15-a4-02-llm-agent-basics-review|A4-02 PASS 复盘]]
