---
type: concept
topic: LLM
status: usable
created: 2026-06-15
updated: 2026-06-21
source:
  - AI-Agent-Learning L1-02
  - OpenAI Text Generation：Message roles and instruction following
  - B站 BV1ptXPYREpe p2（语言模型 / 聊天指令 / tokens）
  - https://developers.openai.com/api/docs/guides/text
  - https://developers.openai.com/api/docs/guides/reasoning-best-practices
  - https://model-spec.openai.com/
tags:
  - LLM
  - API
  - prompt
  - 消息角色
  - 指令优先级
---

# 消息角色与指令优先级（chain of command）

## 一句话解释

`messages` 是一份「对话剧本」，每条 `{"role": ..., "content": ...}` 标明「谁说的」；模型读完整段剧本后只做一件事——续写下一句 `assistant` 台词。不同角色的话**算数程度不一样**，这套优先级叫 instruction following / chain of command。

## 常见角色：装什么、谁产生、何时进 messages

| 角色 | 谁产生 | 装什么 | 何时进 `messages` |
|------|--------|--------|------------------|
| `developer` | 开发者 | 应用规则、业务逻辑、输出约束 | OpenAI 当前文档中的应用级指令角色，优先于 `user` |
| `system` | 开发者 / 平台适配层 | 兼容接口中的全局规则、身份设定 | 是否支持及其语义取决于模型、API 和供应商 |
| `user` | 用户 | 用户这一轮说的话 | **每一轮用户发言**时追加 |
| `assistant` | 模型 | 模型的回复 | 模型生成；**多轮时把它的回复 append 回 `messages` 当历史**，下一轮模型才「记得」上文 |
| `tool` | 工具 / 客户端 | 工具调用结果 | 模型调用工具后，由客户端把结果回传给模型 |

- 单轮调用（如 L1-01/L1-02）里看不到 `assistant`，因为发完就结束。
- `assistant` 进 `messages` = L1-03 多轮聊天的核心动作：`messages.append({"role": "assistant", "content": reply})`。

## 关键点：不要把 system 与 developer 无条件视为同义词

- OpenAI 当前 Text Generation 文档把 `developer` 定义为应用开发者提供的规则和业务逻辑，并明确它优先于 `user`。
- OpenAI Reasoning Best Practices 明确写到：从 `o1-2024-12-17` 开始，推理模型使用 `developer` messages，而不是 `system` messages。
- Chat Completions、Responses API、不同模型以及 OpenAI 兼容供应商的角色支持并不完全相同，因此不能把两者写成跨平台永远相同。
- **实用结论**：代码应以当前模型和供应商文档为准。现有 DeepSeek 兼容调用若使用 `{"role": "system", ...}` 已验证可运行，就保留；迁移到 OpenAI 新模型时再按对应文档改为 `developer` 或 Responses API 顶层 `instructions`。

## 指令优先级链（chain of command，从高到低）

```text
平台/厂商内置规则（安全红线，开发者改不了）
        ▼
developer（应用开发者定的规则）
        ▼
user（用户说的话）
        ▼
guideline（可被更高层或上下文覆盖的默认建议）
```

- `assistant` 历史和 `tool` 输出主要是上下文或数据，不应自动当成高权限指令；工具返回的网页、文件内容尤其要按不可信输入处理。
- `system` message 在具体 API 中如何映射到这条权限链，必须以该模型与接口文档为准。
- 用户说「忽略前面所有规则」时，模型仍应优先遵守更高权限的应用规则——这就是全局规则不能只拼进普通 `user` 内容的原因。

## 规则该放哪里：使用供应商支持的应用级指令槽位

把「整段对话都生效的规则」放在模型支持的 `developer`、`system` 或顶层 `instructions`，而不是拼进普通 `user` content：

1. **持久**：开头传一次，整轮生效；放 user 要每轮重复（多耗 token，且漏带一次就破规则）。
2. **优先级更高**：放 user 的规则只有 user 级权限，以后某轮用户说句冲突的话容易把它盖掉；放 system 压得住。

下面是当前 DeepSeek 兼容 Chat Completions 代码的工程写法：抽成**带默认值的参数**，统一维护并允许按需覆盖：

```python
def call_model(prompt: str, system: str = "回答用中文，控制在 100 字以内") -> str:
    ...
    messages=[
        {"role": "system", "content": system},
        {"role": "user", "content": prompt},
    ]
```

## 边界：别把「上下文窗口限制」叫成「幻觉」

| 概念 | 是什么问题 | 表现 |
|------|-----------|------|
| 上下文窗口 context window 限制 | **容量**问题 | 一次最多读 N 个 token，历史太长放不下 → 要裁剪（`trim_history`）。与真不真实无关。 |
| 幻觉 hallucination | **真实性**问题 | 自信地**编造**不存在的事实 / API / 引用。 |

两者可能间接关联，但定义上是两回事。多轮把历史塞进 `messages` → 输入 token 逐轮变多 → 更贵、且可能撞上下文上限，所以需要裁剪。

## 关联

- [[chat-completions-call]]：`messages` 怎么传、回复怎么取（`response.choices[0].message.content`）。
- [[tokenization]]：`messages` 里所有角色的文本都会被 tokenize；system+user+assistant 全计入 token。
- [[autoregressive-generation]]：模型续写下一句 assistant，就是逐 token 预测。

## 来源与版本边界

- [OpenAI Text generation](https://developers.openai.com/api/docs/guides/text)：`developer` 高于 `user`，并说明常见消息角色。
- [OpenAI Reasoning best practices](https://developers.openai.com/api/docs/guides/reasoning-best-practices)：说明从 `o1-2024-12-17` 起，推理模型使用 `developer` 取代 `system`。
- [OpenAI Model Spec](https://model-spec.openai.com/)：公开的 chain of command（指令权限链）。
- 本页于 2026-06-21 核验。供应商、模型和 API 会变化，移植代码前应重新确认角色支持。
