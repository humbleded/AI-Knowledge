---
type: concept-index
topic: LLM
status: active
created: 2026-05-28
updated: 2026-06-25
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
- [[api-params-vs-sdk-client-params|API 参数 vs SDK 客户端参数]]：usable，API 参数(`model`/`messages`/`temperature`/`stream`)进请求体发服务器、查 DeepSeek 文档；SDK 客户端参数(`timeout`/`max_retries`)只在本机生效、不进请求体、查 OpenAI SDK 文档（所以 DeepSeek API 文档搜不到 timeout）；timeout 两种写法(client 级/create 级)、timeout+except 才是完整超时保护。
- [[message-roles-and-instruction-hierarchy|消息角色与指令优先级（chain of command）]]：usable，developer/system/user/assistant/tool 的分工、`developer` 高于 `user`、`system` 与 `developer` 的模型/API 版本边界、全局规则应进入供应商支持的应用级指令槽位、上下文窗口≠幻觉。
- [[multi-turn-stateless-memory|多轮对话：接口无状态与客户端记忆]]：usable，服务端不记上一轮，记忆=客户端每轮重发 `[SYSTEM]+history+本轮`（SYSTEM 也每轮发）；append=记不记 / trim=记多久；SYSTEM 固定不裁 vs history 动态会裁。
- [[streaming-output|流式输出：stream=True 与逐 chunk 处理]]：usable，`stream=True`+`for chunk`+`delta.content or ""` 三件套；None 两场景（思考阶段/末块）；推理模型两条流 `reasoning_content`/`content`；拼回完整文本才能进 history；错误 return 字符串而非 None 防毒化。
- [[sampling-params-and-cost|采样参数与成本：temperature/top-k/top-p 与 token 计费]]：usable，写字=抽签(Softmax 分数→概率)；temperature 调差距悬殊度(低=陡=稳, 高=平=野, `k=1`≡`T→0`≡贪心)；top-k 固定/top-p 动态砍名单；DeepSeek 温度表(代码0.0/对话1.3/创意1.5)且数字不跨厂商通用；成本=输入(缓存命中/未命中)+输出(最贵)，`usage` 看用量，history 越长越贵。
- [[prompt-engineering-basics|Prompt 基础：zero/few-shot、角色扮演、上下文示例、CoT]]：usable，四技巧各控一维(角色扮演=怎么说 / 上下文示例=长啥样·格式 / few-shot=划边界+锁格式 / CoT=多步推理)；zero/one/few-shot 唯一区别=给几个样例(≠效果)；指令调优(改模型/训练期) vs few-shot(改 prompt/推理期)；技巧≠role(内容放 system/user)；锁 JSON 三件套模板 + messages 摆法甲/乙；长≠好(相关+清晰)，few-shot 别无脑堆(边际递减+每轮重发烧 token)。
- [[summarizing-and-transforming|摘要与改写：Summarizing(压信息) vs Transforming(换外壳)]]：usable，判据=信息量变不变(摘要=有损压缩变少 / 改写=换语言·语气·格式·纠错信息不变)；控长度三单位(字/词/句)是软约束(模型无计数器·token≠字词)，严格卡死靠代码 `len()` 截；概括(求全·会捎带) vs 提取(求专·更干净)；判断漏重点先定义重点→体检三件套(人工对照/提取反查/聚焦重摘)；转换四类；锁 JSON 摘要 prompt 5 要素清单；真实场景(邮件处理器待办用提取字段兜底、客服历史摘要省 token=「长≠好」同源)。

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
