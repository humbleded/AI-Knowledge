---
type: concept
topic: LLM
status: usable
created: 2026-06-24
source:
  - AI-Agent-Learning PR2-01
  - Hello-Agents 第3章 3.2.1 提示工程 (2)-(5)
  - DeepLearning.AI《Prompt Engineering for Developers》Guidelines
tags:
  - LLM
  - prompt
  - few-shot
  - 角色扮演
  - 思维链
  - CoT
  - 指令调优
---

# Prompt 基础：zero/few-shot、角色扮演、上下文示例、CoT

## 一句话解释

写 prompt 就是「**用最少的话，把任务、格式、边界、思考方式都交代清楚**」。四个基础技巧各管一块：**角色扮演**定身份、**上下文示例**锁格式、**few-shot** 划边界、**CoT** 给思考时间。判据不是「长短」而是「**相关 + 清晰**」。

## 四个技巧，各控什么维度（最重要的一张表）

| 技巧 | 怎么用 | 主控维度（一句话） |
|---|---|---|
| **角色扮演** role-playing | 开头给模型安身份「你是资深 Python 专家」 | **怎么说**——风格 / 语气 / 知识深浅 |
| **上下文示例** in-context example | 给「输入 → 输出」样例（尤其锁 JSON） | **长啥样**——输出格式 |
| **few-shot** 少样本 | 给多个、且覆盖不同情况的样例 | **划边界 + 锁格式**——摸清任务边界和细微差别 |
| **CoT** 思维链 | 加一句「请一步一步思考」 | **多步推理**——复杂题别一步蹦答案 |

> 上下文示例 = few-shot 的应用，两者同源：few-shot 强调「划边界」，上下文示例强调「锁格式」，本质一回事。
> 口诀：**角色扮演管「怎么说」，上下文示例/few-shot 管「长啥样 + 边界」，CoT 管「怎么想」。**

## zero / one / few-shot：唯一区别 = 给几个样例

| | 给几个样例 | 主要作用 |
|---|---|---|
| zero-shot | 0 个 | 直接下命令、靠模型泛化；边界全凭它自己猜 |
| one-shot | 1 个 | 照葫芦画瓢，主要教**格式** |
| few-shot | 多个、覆盖不同情况 | 摸清任务**边界和细微差别** → 答得更准 |

⚠️ **区别 ≠ 效果**：三者唯一的【区别】是「给几个样例」；「划清边界」是 few-shot 带来的【效果】，别把效果当区别答。

## 指令调优 vs few-shot：改「模型」还是改「这次的 prompt」

| | 指令调优 Instruction Tuning | few-shot |
|---|---|---|
| 改模型本身？ | **改**（动模型权重） | **不改** |
| 发生在 | **训练阶段**（出厂前练好） | **推理时**（你用的时候） |
| 持久性 | 永久焊进，人人受益 | 这次性，下次不带就忘 |
| 代价 | 一次性训练投入 | 每次都带例子 → 占 `prompt_tokens` |

- 老 GPT-3 = 只会「文本补全」，得靠 few-shot 示范才会干活。
- ChatGPT / DeepSeek / Qwen = 指令调优过 → 一句命令就照做（也是 zero-shot 能成立的原因）。

## 技巧 ≠ role（system / user / assistant）

两个独立维度，别叠混：

- **维度一·技巧**（内容「怎么写」）：角色扮演 / 上下文示例 / CoT。
- **维度二·role**（内容「放进哪个格子」）：`system` / `user` / `assistant`。

技巧不「是」role，但**技巧的内容可以放进某个 role**：

- **角色扮演**（人设 = 全局规则）→ 放 `system`：优先级最高、一次设置整段生效；放 `user` 优先级低且要每轮重复，放 `assistant` = 替模型伪造发言（逻辑不通）。详见 [[message-roles-and-instruction-hierarchy]]。
- **few-shot 示例**两种合法摆法：**甲** 直接塞 `system`（紧凑省事）；**乙** 伪造成 `user`/`assistant` 对话轮（更像真实聊天格式，有时模型更照学）。两种都只在开头设一次。

## 实战模板：锁 JSON 输出的 few-shot prompt

```text
你是一个情感分类器。给定评论，输出 JSON {"label":"正面/负面/中性","reason":"一句话理由"}，只输出 JSON，不要多余文字。
评论：物流很快，包装精美 -> {"label":"正面","reason":"包装好物流快"}
评论：客服态度太差了 -> {"label":"负面","reason":"客服体验差"}
评论：这个商品还行 ->
```

三件套叠用：**角色扮演（定身份）+ 清晰指令（schema + 只输出 JSON）+ few-shot（示例在前教格式、目标留空在后等填）**；示例用**别的**评论、JSON key 不带空格。

落到真实 API（messages 结构，摆法甲）：

```python
messages = [
    {"role": "system", "content": "指令 + 2 个示例（到示例为止、不带待分类目标）"},
    {"role": "user",   "content": "电池不耐用"},   # 这次真正要分类的新评论
]
```

⚠️ 搬进 messages 时，**待分类的目标不要留在 system**——它属于 user 那条消息；system 只留指令 + 示例。

## prompt 何时越长反而越差（必答）

**不是「长一定差」，而是「塞了无关 / 冗余内容才差」。** 长但全相关有用（必要的 few-shot、清晰约束）是好的。

塞无关内容的三宗罪：

1. **稀释**：无关内容把核心指令的「浓度」冲淡。
2. **淹没**（lost in the middle）：超长上下文里，真正要紧的指令 / 输入容易被忽略。
3. **成本**：越长 `prompt_tokens` 越多越贵、还更慢；详见 [[sampling-params-and-cost]]。

**few-shot 也别无脑堆几十个**：效果侧有**边际收益递减**（前几个优质示例收益最大）+ 示例分布偏 / 矛盾会带偏；成本侧示例算输入 token、**多轮每轮重发**都在烧钱。→ 给够 + 给对 + 覆盖关键边界的**少量优质示例**。

## 常见坑 / 错误理解 → 正确理解

- ❌ 把 zero/few-shot 的「区别」答成「效果」 → ✅ 区别 = 给几个样例；划边界是 few-shot 的**效果**。
- ❌ 把「格式」算给角色扮演 → ✅ 角色扮演管「怎么说」；**格式归上下文示例 / few-shot**（管「长啥样」）。
- ❌ 把输出 **schema / 格式说明** 当成 **few-shot 示例** → ✅ `{"label":...,"reason":...}` 是格式说明（属清晰指令）；few-shot 是真实的「输入 → 输出」样例（评论 → JSON）。
- ❌ 以为「`user` 这个格子里也装着 system + 历史」 → ✅ `user` 只装用户说的话；整盘 messages = system 消息 + 历史(user/assistant) + 本轮 user，`system` 是独立格子。
- ❌ 搬进 messages 时把待分类目标留在 `system` → ✅ 目标放 `user`，`system` 只留指令 + 示例。
- ❌ 「prompt 越长 / 越详细越好」 → ✅ 相关 + 清晰 > 长；无关内容稀释、淹没、还烧 token。

## 关联

- [[message-roles-and-instruction-hierarchy]]：技巧的内容放进哪个 role；`system` 优先级最高、全局规则不进普通 `user`。
- [[sampling-params-and-cost]]：示例 / 长 prompt 烧的就是 `prompt_tokens`；输入越长越贵、多轮每轮重发。
- [[multi-turn-stateless-memory]]：few-shot 摆法乙 = 伪造 history；多轮每轮重发整盘 messages。
- [[chat-completions-call]]：prompt 最终装进 `messages` 发给 `chat.completions`。

## 来源

- AI-Agent-Learning PR2-01：`notes/stage2/pr2_01_prompt_notes.md`；练习 `daily/2026-06-22.md`（A1–D3 全 PASS）。
- 资料：Hello-Agents 第 3 章 3.2.1 提示工程 (2)-(5)；DeepLearning.AI《Prompt Engineering for Developers》Guidelines。
