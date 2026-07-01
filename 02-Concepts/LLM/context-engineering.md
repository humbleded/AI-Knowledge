---
type: concept
topic: LLM
status: usable
created: 2026-06-29
source:
  - AI-Agent-Learning S-03
  - Hello-Agents 第9章 上下文工程（9.1~9.2.3 / 9.7）
  - Anthropic：Effective Context Engineering for AI Agents
tags:
  - LLM
  - Agent
  - 上下文工程
  - context-engineering
  - context-rot
  - Compaction
  - JIT
  - 注意力预算
---

# 上下文工程：把「会进窗口的整组 token」当有限资源来策划

## 一句话解释

上下文工程（context engineering）＝**把「这次调用模型时会进入上下文窗口的整组 token」当一种有限资源来策划**。它是提示工程的**演进**：不再只盯「写好一句 prompt」，而是管理「**系统指令 ＋ 工具 ＋ 历史 ＋ 检索 ＋ 这句指令**」的总和。2026 的共识——Agent 失败大多来自**上下文管理**，而非模型本身。

## 提示工程 vs 上下文工程（跨层 / 演进，别混成平级）

| | 提示工程 | 上下文工程 |
|---|---|---|
| 管什么 | 写好「那**一格**指令」（措辞 / 格式 / few-shot） | 策划「**整盒** token」（指令只是其中一格） |
| 关系 | 子集 / 前身 | **包含**提示工程、是它的**升级** |

> ⚠️ **坑①**：把「上下文工程 vs 提示工程」（**跨层 / 演进**，谁包含谁）和「Compaction vs trim」（**同层平级**的两种手段）搞混。前者是「大范畴 vs 其中一格」，后者是「平级的左右手」。

小坑：`prompt` 有**狭义**（你写的指令，本课用这个）/ **广义**（完整 `messages` 输入）两义。判断某内容算不算上下文——**看「是否会进窗口的 token」，别看名字**（`system prompt` 名字带 prompt，但它只是上下文的一格）。

## context rot：为什么上下文是有限资源（核心）

- **context rot（上下文腐蚀）**：窗口里 token 越多，模型**准确回忆信息的能力反而下降**（"针堆找针 needle-in-a-haystack" 基准测出）。
- 由此**结论**：上下文是**有限资源 + 边际收益递减**；模型有一笔**注意力预算（attention budget）**，每个 token 都在花它 → 谨慎筛选放什么。
- 是**性能梯度**、非悬崖（越长越**缓慢**下滑，不是某长度突然崩）。机制：Transformer 每 token 两两关联，n² 增长 → 太长注意力被**摊薄**（见 [[attention]]）；训练语料短序列多、长上下文经验少。

> 现象（context rot）→ 结论（有限资源/递减），别把两者黏一句；「为什么重要」答的是**这个现象**，不是「用什么手段」。

## 有效上下文：最小 ≠ 最短

- 系统提示两极误区：**过度硬编码**（塞脆弱 if-else、难维护）/ **过于空泛**（只给大话、缺具体信号）。
- 「**最小必要信息集**」是**双向平衡**：**下限**别漏关键（别太空 → 误判）、**上限**别注水（别稀释、腐蚀）。所以「最小」**不等于**「最短」。
- 工具走 **MVTS（最小可行工具集）**、few-shot 精选典型（见 [[prompt-engineering-basics]]）；总纲：**信息充分但紧致**。
- 辨析：「过于空泛 vs 过度硬编码」是**写法/刚性**轴，与「太短/太长」**信息量**轴是**表亲非双胞胎**——过度硬编码核心罪是「脆弱难维护」，不只是「长导致腐蚀」。

## ⭐ 五种压缩/筛选手段速查（分层 + 场景）

| 手段 | 怎么做 | 属哪一层 | 适用场景 | 代价 / 风险 |
|---|---|---|---|---|
| **trim / 截断 truncation** | 历史太长按位置删最早的（只留最近 N 条） | 最朴素**基础档** | 简单多轮、对早期信息不敏感 | 按**位置**删、不看重要性 → 误删「旧但重要」 |
| **JIT 及时检索** | 不预载，只放轻量引用（路径/查询/URL），运行时按需读 | **按需检索类** | 资料超大/超窗口（几百页手册、大代码库） | 比预载慢、需好工具与引导否则乱翻 |
| **Compaction 压缩整合** | 接近上限时把对话高保真**总结成摘要**、用摘要**重启新窗口** | **长时程三件套** | 需**长对话连续性**（接力） | ① 额外调一次模型（钱+延迟）② 摘要可能**失真/丢细节** |
| **结构化笔记** | 关键信息写到**上下文外持久存储**（md/TODO），按需拉回 | **长时程三件套** | 有**里程碑/阶段成果**的迭代；记关键字段（订单号/诉求） | 需维护笔记、读写时机设计 |
| **子代理架构** | 主 agent 规划+综合，子 agent 在**干净窗口**深挖、回传 1~2k 摘要 | **长时程三件套** | **复杂研究/分析**、能**并行**探索 | 协调成本、上下文分散、多 agent 风险 |

> **三件套选择经验法则**：要长对话连续性 → **Compaction**；有里程碑/阶段成果的迭代 → **结构化笔记**；复杂研究、能并行 → **子代理**。

## 接回 `trim_history`（朴素裁剪只是最简单的一种）

- `trim_history`（按轮数裁剪历史）＝ **truncation**，属**上下文工程的最朴素基础档**，**不属于提示工程**（提示工程只写指令、**不碰删/压历史**）。
- 它按**位置/新旧**决定删谁、**不看重要性** → 误删「旧但重要」（如开头报的名字）。
- vs Compaction：trim＝**硬删**（旧的直接扔）；Compaction＝**软压**（旧的压成摘要保梗概）。二者**平级**；trim **不在**长时程三件套（硬删丢信息，长时程不够用）。详见 [[multi-turn-stateless-memory]]。

## 实证：S-03 token 对比实验（真跑 DeepSeek）

同一段「8 条对话历史」（第 1 条藏了人名「三玖」），三方案对比：

| 方案 | 条数 | token | 还留着「三玖」? | 含义 |
|---|---|---|---|---|
| ① 全量 full | 8 | 100 | ✅ | 信息全，但最费——长了还会 context rot |
| ② 裁剪 trim | 2 | **25** | ❌ False | **最省，但早期关键信息硬丢** |
| ③ Compaction | 3 | 50 | ✅ True | **花一点 token，换回早期信息的召回** |

真摘要（DeepSeek，prompt 要求「保留人名、30 字内」）：`之前对话摘要：三玖被推荐了《机器学习》西瓜书和《星际穿越》。`

🔑 **结论**：`② False / ③ True` 就是「trim 硬丢、Compaction 保信息」最直观的证据；token `① 100 > ③ 50 > ② 25` 印证三者在「省 token」与「保信息」之间各有取舍。产物：`code/stage2/s03_context_experiment.py`。

## 常见坑 / 错误理解 → 正确理解

- ❌「上下文工程 vs 提示工程」当成和「Compaction vs trim」一样 → ✅ 前者**跨层/演进**（上下文工程包含提示工程），后者**同层平级**。
- ❌「trim 是提示工程的手段」/「不止提示工程也是上下文工程」 → ✅ trim **只**属上下文工程；trim ≠ Compaction（平级）；trim 技术名 **truncation**，是基础档、不在长时程三件套。
- ❌ Compaction 只是「做个摘要」 → ✅ 灵魂是摘要**之后用它重启新窗口**；代价＝① 调模型（钱+延迟）② 摘要**失真/丢细节**。
- ❌ 以为 Compaction「把全量历史都丢进窗口、只减少输出 token」 → ✅ 它把旧历史**替换**成短摘要，**输入 token 是减少的**（③ Compaction < ① 全量）；但 ③ ＝ ②裁剪 + **一条摘要**，摘要 token 恒 >0，故 ③ > ②、**再压也省不过 trim**。（S-03 后续 PR2-04 练习 B3 深化）
- ❌ 把「为什么上下文工程重要」答成「用什么手段」 → ✅ 答的是 **context rot 现象**（token 越多回忆越差）。
- ⚠️ 工程坑 `history[-0:]`＝`history[0:]`＝**整个列表**（`-0==0`）；`keep_recent=0` 会让 trim/compaction 失效返回全部。
- ⚠️ 工程坑 `str.split()` 按**空格**切**不按字**，中文整块算 1 词；`count_tokens` 中英混合会重复计中文、不精确（生产用真 tokenizer，详见 [[tokenization]]）。
- ⚠️ 真调坑 `messages=text`（字符串）→ **400**；`messages` 要 `list of {"role","content"}`（同 [[chat-completions-call]]）；把待总结文本包成 `[{system:总结指令},{user:text}]`。
- ⚠️ 实验设计坑：要演示「裁剪丢早期信息」，关键信息须**只在会被裁的早期出现**——若最近 N 条里复现（如末条复述名字），`name_in_trim` 会假性为 True，演示失效。

## 关联

- [[prompt-engineering-basics]]：上下文工程的**前身**；最小≠最短、few-shot 精选、长≠好同源。
- [[multi-turn-stateless-memory]]：`trim_history` 是这里的朴素裁剪；记忆=每轮重发整盘 messages。
- [[summarizing-and-transforming]]：Compaction 用的就是「摘要＝有损压缩」；锁短靠 prompt 软约束 + 代码兜底。
- [[sampling-params-and-cost]]：上下文越长 `prompt_tokens` 越多越贵、多轮每轮重发。
- [[attention]]：context rot 的架构根因（n² 注意力被摊薄）。
- [[tokenization]]：`count_tokens` 毛估 vs 真 tokenizer。
- [[chat-completions-call]]：真调摘要时 `messages` 结构与 `messages=text` 的 400 坑。

## 来源

- AI-Agent-Learning S-03：笔记 `notes/stage2/s03_context_engineering.md`；实验 `code/stage2/s03_context_experiment.py`；练习 `daily/2026-06-29.md`（15 题全 PASS，6 个易错点）。
- 资料：Hello-Agents 第 9 章《上下文工程》9.1~9.2.3 / 9.7；Anthropic《Effective Context Engineering for AI Agents》。
