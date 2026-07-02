---
type: source
topic: DeepSeek share - context engineering, routing, JIT, special tokens
status: processed
source_url: https://chat.deepseek.com/share/tefftbktdjn3xpztg6
created: 2026-07-02
processed: 2026-07-02
compiled_to:
  - ../../02-Concepts/LLM/上下文工程(Context Engineering)
  - ../../02-Concepts/LLM/分类与路由(Classification & Routing)
  - ../../02-Concepts/LLM/API Key 与 SDK
  - ../../02-Concepts/LLM/采样参数与成本(Sampling)
  - ../../02-Concepts/LLM/LLM 本质与幻觉(Hallucination)
  - ../../02-Concepts/LLM/特殊Token(Special Tokens)
tags:
  - Source
  - conversation
  - LLM
  - Agent
  - context-engineering
  - routing
  - JIT
---

# DeepSeek 分享对话：上下文工程、路由与特殊 Token

## 来源说明

- 来源链接：<https://chat.deepseek.com/share/tefftbktdjn3xpztg6>
- 抓取时间：2026-07-02
- 抓取方式：通过分享页接口读取对话内容；整理时只保留可复用结论，不把完整逐字对话并入概念卡。

## 主线主题

这份对话主要围绕两条学习线：

- Agent 上下文工程：Compaction、JIT 上下文、结构化笔记、渐进式披露、路由 + JIT 的组合。
- LLM/API 基础：环境变量与 `.env`、`temperature=0` 的理论和工程口径、Transformer 类型、自回归生成、特殊 token、EOS 与文本结束的区别。

## 已整理去向

- [[../../02-Concepts/LLM/上下文工程(Context Engineering)|上下文工程]]：补充召回/精确度、JIT vs 结构化笔记、JIT 与渐进式披露、引用元数据。
- [[../../02-Concepts/LLM/分类与路由(Classification & Routing)|分类与路由]]：补充“标签 -> 路由 -> JIT”的设计范式，以及四类路由的定位。
- [[../../02-Concepts/LLM/API Key 与 SDK|API Key 与 SDK]]：补充 `.env`、`load_dotenv()`、`os.environ.get()` 与模型名默认值。
- [[../../02-Concepts/LLM/采样参数与成本(Sampling)|采样参数与成本]]：补充 `temperature=0` 的理论/工程差异。
- [[../../02-Concepts/LLM/LLM 本质与幻觉(Hallucination)|LLM 本质与幻觉]]：补充“无法根除，只能降低频率和影响”的工程口径。
- [[../../02-Concepts/LLM/特殊Token(Special Tokens)|特殊Token]]：新增特殊 token、EOS、EOT、API 消息格式与模型内部序列的区别。

## 可复用结论

- Compaction 调参先保召回，再提精确度：先别漏关键决策和未解决问题，再删重复工具输出、旧日志和噪声。
- JIT 是“按需拉取信息”的动作时机；结构化笔记是“长期沉淀信息”的载体。两者可以互相配合。
- JIT 可以看作渐进式披露的一种实现：先给轻量引用，让智能体运行中逐步读取文件、查询或 URL。
- 路由 + JIT 的经典流程是：先从用户输入提取标签，再按标签进入对应路由，最后由该路由决定要检索哪些信息。
- 路由实现不止 LLM 与规则两种；常见还有嵌入路由和专门训练的判别式 ML 路由。
- `load_dotenv()` 负责把 `.env` 写入当前进程环境；`os.environ.get()` 负责从环境变量中取配置；默认值用于没有配置时兜底。
- `temperature=0` 在理论上接近贪心选择，低概率候选不应被采样；但端到端 API 仍可能因实现细节、并行计算或服务路由出现非完全复现。
- 特殊 token 是模型词表里的控制信号，不等于人类可见文本。EOS 是模型侧的“生成到此结束”信号；文本结束只是人类阅读层的语义结束。
