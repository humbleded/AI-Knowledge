---
aliases:
  - prompt-engineering-basics
type: concept
topic: LLM
status: usable
created: 2026-06-24
updated: 2026-09-08
source:
  - AI-Agent-Learning PR2-01
  - AI-Agent-Learning A4-02 正式复核（2026-07-15）
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

写 prompt 就是把任务、格式和边界交代清楚。角色说明引导表达侧重，输入输出示例展示预期结果，分步提示帮助拆解任务；这些都是引导，不能保证格式、事实或推理正确。判断重点是相关、清晰，以及实际任务上的效果。

## 四个技巧，各控什么维度（最重要的一张表）

| 技巧 | 怎么用 | 主控维度（一句话） |
|---|---|---|
| **角色扮演** role-playing | 给出「你是 Python 讲师」等角色 | 引导风格、语气和解释侧重，不增加真实知识 |
| **上下文示例** in-context example | 给「输入 → 输出」样例 | 示范格式和风格，不提供硬性格式保证 |
| **few-shot** 少样本 | 给多个、且覆盖不同情况的样例 | 帮助理解边界，错误或不相关示例也可能带偏 |
| **CoT** 思维链提示 | 要求分步分析或提供必要步骤 | 可能帮助多步任务；是否有效取决于模型和任务，不保证推理正确 |

> 上下文示例按数量可分为 one-shot 和 few-shot；一个示例不能因为放在上下文里就叫 few-shot。二者都可展示格式和任务边界。
> 口诀：**角色扮演管「怎么说」，上下文示例/few-shot 管「长啥样 + 边界」，CoT 管「怎么想」。**

## zero / one / few-shot：唯一区别 = 给几个样例

| | 给几个样例 | 主要作用 |
|---|---|---|
| zero-shot | 0 个 | 直接下命令、靠模型泛化；边界全凭它自己猜 |
| one-shot | 1 个 | 照葫芦画瓢，主要教**格式** |
| few-shot | 多个、覆盖不同情况 | 帮助理解任务边界和差别，是否更准要实际比较 |

⚠️ **区别 ≠ 效果**：三者唯一的【区别】是「给几个样例」；「划清边界」是 few-shot 带来的【效果】，别把效果当区别答。

## Instruction Data / Instruction Tuning / Prompting：对象、过程和当前输入

这三个词不在同一层：

| 概念                             | 它是什么                     | 是否改变参数 | 是否自动影响后续请求                    |
| ------------------------------ | ------------------------ | ------ | ----------------------------- |
| Instruction Data               | “指令/输入 → 理想回答或动作结构”的训练样本 | 数据本身不会 | 不会；只存着数据不等于训练完成               |
| Instruction Tuning             | 使用指令数据继续训练模型的过程          | 会      | 效果保存在**新模型权重**中；后续请求必须实际调用该模型 |
| Prompting                      | 推理时发送的当前输入               | 不会     | 不会；后续请求仍需重新提供必要输入             |
| Few-shot / In-context Learning | 在当前 Prompt 中放少量示例        | 不会     | 不会；示例不再发送时，效果不会自动保留           |

典型判断：

```text
整理 6000 条“用户请求 -> 正确 Tool Call JSON” = Instruction Data
用这 6000 条数据训练并保存 agent-tools-v2 = Instruction Tuning
原模型每次请求临时带 3 条示例 = Few-shot Prompting / In-context Learning
```

所以，不能只说“微调后所有请求都受益”。更精确的说法是：能力写入了**微调后那个模型版本**，请求若仍调用原模型，就不会自动获得这次训练效果。

### 指令调优 vs few-shot：改模型，还是改这次输入

| | 指令调优 Instruction Tuning | few-shot |
|---|---|---|
| 改模型本身？ | **改**（更新模型权重） | **不改** |
| 发生在 | **训练阶段** | **推理时** |
| 持久性 | 保存在微调模型中；请求必须调用它 | 只在当前上下文有效，下次不带就没有 |
| 代价 | 训练、评估和模型版本维护 | 每次都带例子，占 `prompt_tokens` |

- 指令调优通常改善按要求完成任务的能力，但不是 zero-shot 存在的前提；原始 GPT-3 也做过 zero-shot 测试。
- 本课使用的是面向对话和指令的具体模型版本；不能由 DeepSeek、Qwen 等系列名推断所有版本训练方式相同，也不能保证一句命令就完成任务。

## 技巧 ≠ role（system / user / assistant）

两个独立维度，别叠混：

- **维度一·技巧**（内容「怎么写」）：角色扮演 / 上下文示例 / CoT。
- **维度二·role**（内容「放进哪个格子」）：`system` / `user` / `assistant`。

技巧不「是」role，但**技巧的内容可以放进某个 role**：

- 角色说明可按用途放在合适的消息中；本课将长期行为要求放在 `system`，将本轮任务放在 `user`。服务端怎样处理优先级取决于接口，不能把消息角色当作格式或事实保证。详见 [[消息角色与指令优先级(Instruction Hierarchy)]]。
- few-shot 示例可以直接写进一条说明，也可以组织成 `user`/`assistant` 示例对话。本课无状态 API 每次只看到实际发送的输入；客户端初始化一次不代表后续请求无需携带必要规则和示例。

## 实战模板：引导 JSON 输出的 few-shot prompt

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

## ⚠️ 工程坑：f-string / `.format()` 撞 prompt 里的 JSON 花括号

引导 JSON 的 prompt 里既有 JSON 示例的 `{}`、又想用变量嵌入正文时，**别无脑 f-string**：

```python
text = "正文"
f'格式：{"points":["a"]} 内容：{text}'
# 上面的冒号会被当成格式说明符的分界，运行时可能报 ValueError。
# .format() 中未转义的花括号也会被当成占位符，可能报 KeyError。
```

**解法（从稳到巧）**：

1. **字符串拼接**（最稳）：含 JSON 示例的指令写成固定字符串，变量 `text` 用 `+` 接：`instruction + '\n"""\n' + text + '\n"""'`。
2. f-string 里把 JSON 的 `{` `}` 写成双层 `{{` `}}` 转义（容易漏）。
3. 指令里本身有 `"""` 和 JSON 双引号 `"` 时，包指令的引号用**单引号** `'...'` 避冲突。

## prompt 何时越长反而越差（必答）

**不是「长一定差」，而是「塞了无关 / 冗余内容才差」。** 长但全相关有用（必要的 few-shot、清晰约束）是好的。

塞无关内容的三宗罪：

1. **稀释**：无关内容把核心指令的「浓度」冲淡。
2. **淹没**（lost in the middle）：超长上下文里，真正要紧的指令 / 输入容易被忽略。
3. **成本**：越长 `prompt_tokens` 越多越贵、还更慢；详见 [[采样参数与成本(Sampling)]]。

**few-shot 也别无脑堆几十个**：效果侧有**边际收益递减**（前几个优质示例收益最大）+ 示例分布偏 / 矛盾会带偏；成本侧示例算输入 token、**多轮每轮重发**都在烧钱。→ 给够 + 给对 + 覆盖关键边界的**少量优质示例**。

## 实证：PR2-01 三档 prompt 真跑对比（few-shot 零增益）

同一抽取任务（一段自我介绍 → 6 字段 JSON），写 3 个递进 prompt 真跑 DeepSeek（`json.loads` 自动检测）：

| prompt | 做法 | 真实输出 | `json.loads` |
|---|---|---|---|
| ① 偷懒 | zero-shot、不点字段、不要格式 | Markdown 列表+开场白、多抽字段、值带单位、key 中文 | ✗ 失败 |
| ② 清晰 | 角色+分隔符+点名 6 字段+空 JSON 模板+前后不带文字 | 纯 JSON、6 字段齐 | ✓ 成功 |
| ③ few-shot | ② + 一组填好的样例（用别人的） | **与 ② 完全一致** | ✓ 成功 |

这一次样本中，② 和 ③ 得到相同结果，没有观察到额外示例带来的收益；不能推广为所有规整任务都没有收益，也不能说清晰提示消除了模型的自由输出。需要加入缺失字段、顺序变化等代表性输入，比较格式与内容正确率后再选择。产物：`code/stage2/pr2_01_prompt_cases.md`。

## 常见坑 / 错误理解 → 正确理解

- ❌ 把 zero/few-shot 的「区别」答成「效果」 → ✅ 区别 = 给几个样例；划边界是 few-shot 的**效果**。
- ❌ 把「格式」算给角色扮演 → ✅ 角色扮演管「怎么说」；**格式可由明确说明、示例及输出模式共同约束**，不能归给某一个提示技巧。
- ❌ 把输出 **schema / 格式说明** 当成 **few-shot 示例** → ✅ `{"label":...,"reason":...}` 是格式说明（属清晰指令）；few-shot 是真实的「输入 → 输出」样例（评论 → JSON）。
- ❌ 以为「`user` 这个格子里也装着 system + 历史」 → ✅ `user` 只装用户说的话；整盘 messages = system 消息 + 历史(user/assistant) + 本轮 user，`system` 是独立格子。
- ❌ 搬进 messages 时把待分类目标留在 `system` → ✅ 目标放 `user`，`system` 只留指令 + 示例。
- ❌ 「prompt 越长 / 越详细越好」 → ✅ 相关 + 清晰 > 长；无关内容稀释、淹没、还烧 token。

## 关联

- [[消息角色与指令优先级(Instruction Hierarchy)]]：技巧的内容放进哪个 role；`system` 优先级最高、全局规则不进普通 `user`。
- [[采样参数与成本(Sampling)]]：示例 / 长 prompt 烧的就是 `prompt_tokens`；输入越长越贵、多轮每轮重发。
- [[多轮对话与无状态记忆(Stateless Memory)]]：few-shot 摆法乙 = 伪造 history；多轮每轮重发整盘 messages。
- [[调用 chat.completions]]：prompt 最终装进 `messages` 发给 `chat.completions`。
- [[../../07-Reviews/AI-Agent-Learning/2026-07-15-a4-02-llm-agent-basics-review|A4-02 PASS 复盘]]：训练数据、训练过程与当前上下文的迁移辨析。

## 来源

- AI-Agent-Learning PR2-01：`notes/stage2/pr2_01_prompt_notes.md`；练习 `daily/2026-06-22.md`（A1–D3 全 PASS）。
- 资料：Hello-Agents 第 3 章 3.2.1 提示工程 (2)-(5)；DeepLearning.AI《Prompt Engineering for Developers》Guidelines。
- AI-Agent-Learning A4-02：`daily/2026-07-15.md` F1，Instruction Data / Instruction Tuning / Few-shot 迁移 PASS。
- 2026-09-08 同步 [项目提示词笔记订正](https://github.com/humbleded/AI-Agent-Learning/blob/main/notes/stage2/pr2_01_prompt_notes.md)；保留原实验与历史 PASS，本次维护不作为新作答证据。
