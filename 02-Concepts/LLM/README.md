---
type: concept-index
topic: LLM
status: active
created: 2026-05-28
updated: 2026-07-02
tags:
  - LLM
  - 概念卡
---

# LLM 概念卡

## 训练基础

- [[反向传播(Backprop)]]：usable，理解计算图和梯度传播。
- [[梯度下降(Gradient Descent)]]：usable，理解如何用梯度更新参数。

## 语言建模基础

- [[分词(Tokenization)]]：usable，理解文本如何变成 token ID。
- [[特殊Token(Special Tokens)]]：usable，理解 EOS/EOT、角色边界、API 消息格式与模型内部 token 序列的区别。
- [[嵌入(Embedding)]]：usable，理解 token/position 如何变成向量表示。
- [[自回归生成(Autoregressive)]]：usable，理解下一个 token 预测和生成循环。
- [[LLM 本质与幻觉(Hallucination)|LLM 本质与幻觉]]：usable，LLM=预测下一个最可能 token；幻觉是"只求像、不求真"的天生副作用(最可能≠最真实)，靠 RAG 等缓解。

## Transformer 基础

- [[注意力机制(Attention)]]：usable，理解 Q/K/V、causal mask 和上下文读取。
- [[Transformer]]：usable，理解 GPT 类模型的基本 block。

## 调用与工程

- [[API Key 与 SDK|API Key 与 SDK：调用模型的门禁卡和快递柜台]]：usable，理解 key、模型名、SDK 和环境变量的分工。
- [[调用 chat.completions|调用 LLM：chat.completions 与取回复]]：usable，传 `messages`、取 `response.choices[0].message.content`，含 key/`load_dotenv`、错误提示、封装复用等易错点。
- [[API 参数与 SDK 客户端参数|API 参数 vs SDK 客户端参数]]：usable，API 参数(`model`/`messages`/`temperature`/`stream`)进请求体发服务器、查 DeepSeek 文档；SDK 客户端参数(`timeout`/`max_retries`)只在本机生效、不进请求体、查 OpenAI SDK 文档（所以 DeepSeek API 文档搜不到 timeout）；timeout 两种写法(client 级/create 级)、timeout+except 才是完整超时保护。
- [[消息角色与指令优先级(Instruction Hierarchy)|消息角色与指令优先级（chain of command）]]：usable，developer/system/user/assistant/tool 的分工、`developer` 高于 `user`、`system` 与 `developer` 的模型/API 版本边界、全局规则应进入供应商支持的应用级指令槽位、上下文窗口≠幻觉。
- [[多轮对话与无状态记忆(Stateless Memory)|多轮对话：接口无状态与客户端记忆]]：usable，服务端不记上一轮，记忆=客户端每轮重发 `[SYSTEM]+history+本轮`（SYSTEM 也每轮发）；append=记不记 / trim=记多久；SYSTEM 固定不裁 vs history 动态会裁。
- [[流式输出(Streaming)|流式输出：stream=True 与逐 chunk 处理]]：usable，`stream=True`+`for chunk`+`delta.content or ""` 三件套；None 两场景（思考阶段/末块）；推理模型两条流 `reasoning_content`/`content`；拼回完整文本才能进 history；错误 return 字符串而非 None 防毒化。
- [[采样参数与成本(Sampling)|采样参数与成本：temperature/top-k/top-p 与 token 计费]]：usable，写字=抽签(Softmax 分数→概率)；temperature 调差距悬殊度(低=陡=稳, 高=平=野, `k=1`≡`T→0`≡贪心)；top-k 固定/top-p 动态砍名单；DeepSeek 温度表(代码0.0/对话1.3/创意1.5)且数字不跨厂商通用；成本=输入(缓存命中/未命中)+输出(最贵)，`usage` 看用量，history 越长越贵。
- [[提示工程基础(Prompt Engineering)|Prompt 基础：zero/few-shot、角色扮演、上下文示例、CoT]]：usable，四技巧各控一维(角色扮演=怎么说 / 上下文示例=长啥样·格式 / few-shot=划边界+锁格式 / CoT=多步推理)；zero/one/few-shot 唯一区别=给几个样例(≠效果)；指令调优(改模型/训练期) vs few-shot(改 prompt/推理期)；技巧≠role(内容放 system/user)；锁 JSON 三件套模板 + messages 摆法甲/乙；长≠好(相关+清晰)，few-shot 别无脑堆(边际递减+每轮重发烧 token)。
- [[摘要与改写(Summarize & Transform)|摘要与改写：Summarizing(压信息) vs Transforming(换外壳)]]：usable，判据=信息量变不变(摘要=有损压缩变少 / 改写=换语言·语气·格式·纠错信息不变)；控长度三单位(字/词/句)是软约束(模型无计数器·token≠字词)，严格卡死靠代码 `len()` 截；概括(求全·会捎带) vs 提取(求专·更干净)；判断漏重点先定义重点→体检三件套(人工对照/提取反查/聚焦重摘)；转换四类；锁 JSON 摘要 prompt 5 要素清单；真实场景(邮件处理器待办用提取字段兜底、客服历史摘要省 token=「长≠好」同源)。
- [[分类与路由(Classification & Routing)|分类与路由：Classification(给标签) vs Routing(按标签分流)]]：usable，分类是路由前半步(分类给标签→路由按标签 dict/if 分发)；四种路由(LLM/嵌入/规则/ML)，动手规则版(纯代码字面匹配·快但列不全/撞类) vs 模型版(调 LLM 懂语义·非银弹·边界靠 prompt 定义)；真跑 4 难样例规则版 0/4→模型版 2/4；两类错漏判(命中0类)/撞类(命中≥2类被前者抢)用 all_hits+len 自动归因；模型版三件套(只输出标签词+strip+白名单兜底)；固定标签让下游 if 接得住；分类质量=标签定义在 prompt 的清晰度。
- [[上下文工程(Context Engineering)|上下文工程：策划进窗口的整组 token]]：usable，提示工程的**演进**(管整组 token 非一句指令；上下文工程**包含**提示工程=跨层)；**context rot**=token 越多准确回忆越差→上下文是**有限资源+注意力预算**(性能梯度非悬崖)；**最小≠最短**(双向:下限别漏/上限别注水)；**五手段分层**(trim 截断/JIT 检索=基础与按需 ｜ Compaction/结构化笔记/子代理=长时程三件套)+选择经验法则；`trim_history`=truncation 属上下文工程**非**提示工程、与 Compaction(硬删 vs 软压)**平级**；实证真跑 `①100>③50>②25`、②丢名字 ③保名字；坑：`messages=text` 的 400、`history[-0:]`==整表、`split` 按空格不按字。
- [[结构化输出(Structured Output)|结构化输出：让模型吐出程序能吃的 JSON]]：usable，两档强度(JSON 模式 `json_object` 只保证合法 JSON / 严格 Schema `strict` 保证字段齐·类型·不多余·枚举·拒答)；schema 锁 4 件事、enum 硬约束(约束解码归零) vs temperature 软；DeepSeek 只有 `json_object`(三硬要求:含"json"·双引号样例·`max_tokens`；空 content 坑)→prompt 写 schema+代码 `validate` 两头夹；🔑 `json_object`≠dict(content 永远是 str 仍需 `json.loads`)；实证真跑规则版 vs 模型版(自由文本语义抽取·缺字段 `priority:null` 不编造)、真调不可复现(截断/空 content 两种失败)。

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
