---
aliases:
  - structured-outputs
type: concept
topic: LLM
status: usable
created: 2026-06-30
updated: 2026-09-08
source:
  - AI-Agent-Learning PR2-04
  - AI-Agent-Learning PR2-Gate
  - C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-07-23.md
  - C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-08-22.md
  - OpenAI Structured Outputs 官方文档
  - DeepSeek JSON Output 官方文档
tags:
  - LLM
  - structured-output
  - json-mode
  - schema
  - json_object
  - DeepSeek
---

# 结构化输出（Structured Outputs）：让模型吐出程序能吃的 JSON

## 一句话解释

结构化输出用于让程序按约定字段读取模型结果。必须分开检查三件事：**能否解析、字段与类型是否符合规则、内容是否有依据**。输出模式能约束前两项的程度取决于接口；合法结构不保证事实正确或缺信息时不编造。[[提示工程基础(Prompt Engineering)|提示词和示例]]可以引导结果，但不能替代格式约束与代码校验。

## 两档强度：JSON 模式 vs 严格 Schema

| 档 | 名字 | 保证什么 | 不保证什么 |
|---|---|---|---|
| 弱档 | **JSON 模式**（`json_object`） | 在正常取得完整正文时，约束合法 JSON 输出 | 自定义必填字段、类型、取值与内容真实性；仍需处理空正文和截断 |
| 强档 | **严格 Schema**（`json_schema` + `strict`） | 支持的接口在正常完成且没有拒答时，按已接受的结构规则限制字段、类型、枚举和额外字段 | 事实正确、业务判断正确与任务一定完成；拒答和不完整响应需单独处理 |

> 原文：**only Structured Outputs ensure schema adherence**（只有严格 Schema 保证贴合结构；JSON 模式只保证是合法 JSON）。

## schema 锁的 4 件事

1. **必填字段（required）**
2. **字段类型（types）**
3. **不许多余字段（`additionalProperties: false`）**
4. **枚举值（enum）**——只能从固定集合选，防乱编（如 priority 只能 `高/中/低`）

> enum 在严格模式下是**硬约束**（约束解码 constrained decoding：生成时把非法 token 概率**归零**，物理上选不到「特急」）——不是「提高概率」。对比：**enum / top-k ＝ 硬归零；temperature ＝ 软压低（仍 >0）**。见 [[采样参数与成本(Sampling)]]。

## 处理异常输出：查 3 处

1. 响应外壳与 `finish_reason`：`length` 表示被 `max_tokens` **截断**；安全过滤、资源不足、缺失 / 未知结束原因都不能按正常 JSON 处理。
2. 意外工具调用 / `message.refusal`：按当前接口支持的字段及本地处理规则分支，不能继续读成业务 JSON；不能假定所有厂商都有同样的拒答字段。
3. `message.content`：非流式 schema 中可以为 nullable；只有确认它是**非空字符串**后，才交给 `json.loads()`。

## DeepSeek 本任务落地：普通回答 JSON 模式

开关 `response_format={'type': 'json_object'}`。三条硬要求：
1. prompt 里必须出现 `"json"` 这个词
2. prompt 里给一段 JSON 格式样例（**双引号**！单引号不是合法 JSON）
3. 按预期输出设置足够的 `max_tokens`，并检查实际结束状态；设置预算本身不保证不会截断。

坑：偶尔返回**空 content** → `loads` 前 `if not content` 兜底。

> 本任务采用的 `json_object` 不强制自定义结构，因此用“提示写清字段、样例和缺失值规则 + Python 代码校验”拦住不合格结果。这是生成后的检查，不能等同于生成时的严格结构限制，也不会自动补出厂商的拒答信号。项目在 2026-09-07 核验的 DeepSeek Tool Calls 另有 `/beta` strict 模式，约束的是工具调用参数；不能据普通回答 JSON 模式推断该厂商所有接口都没有严格模式。本轮重新提取该页未成功，版本事实沿用该次本地核验记录，使用前仍按官方页复查。

## 🔑 最大的坑：`response_format=json_object` ≠ 返回 dict

`response.choices[0].message.content` **不是永远都有字符串**：非流式响应 schema 允许它为 nullable，DeepSeek JSON Output 也提醒可能偶发空正文。客户端必须先完成“响应外壳 → `finish_reason` → 无意外 Tool Action → 非空字符串正文”的守门；只有通过后，才把 `content` 当 `str` 交给 `json.loads()`。即使拿到语法合法 JSON，`json_object` 也不保证外层一定是业务所需的 `dict`，更不保证字段要求；解析后仍要检查外层类型、精确键、字段类型 / 值和业务约束。

## 工程链路：JSON 字符串 -> dict -> 校验 -> 文件 JSON

PR2-Gate 把结构化输出接到一个可运行的小工具里，稳定链路是：

```python
todo_dict = json.loads(model_json_string)   # JSON 字符串 -> Python dict
validate_payload(todo_dict)                 # 检查字段齐全、可序列化
result = {"todo": todo_dict, ...}           # 组装内部 dict
json.dump(result, f, ensure_ascii=False, indent=2)  # 写成文件 JSON
```

不要把模型返回的 JSON 字符串直接塞进最终 `result`：

```python
result = {"todo": "{\"sender\": \"张三\"}"}
```

这种结果虽然外层文件仍可能是合法 JSON，但 `todo` 只是**字符串字段**，后续不能写 `result["todo"]["sender"]`。正确做法是先 `json.loads` 成 Python `dict`。

## 弱文本协议：从 Markdown 代码围栏解析 Python 列表

有些教学示例会要求模型返回：

````text
```python
["查询天气", "预订酒店", "安排行程"]
```
````

这只是客户端和模型约定的**文本协议**，不属于 API 强制保证的 Structured Outputs。模型可能漏掉围栏、返回错误语法，或者返回列表以外的对象，因此必须依次完成：

```text
围栏完整性检查
  -> Python 字面量语法解析
  -> 外层类型检查
  -> 元素类型和业务约束检查
```

### `index()` 比链式 `split()` 更明确，但 `find()` 更适合主动兜底

两种常见提取写法：

```python
# 写法 1：明确查找开始和结束位置
start = response_text.index("```python") + len("```python")
end = response_text.index("```", start)
plan_str = response_text[start:end].strip()
```

```python
# 写法 2：依赖切分结果的固定下标
plan_str = response_text.split("```python")[1].split("```")[0].strip()
```

| 异常输入 | `index()` | 链式 `split()` |
|---|---|---|
| 缺少开头围栏 | 抛 `ValueError` | 读取 `[1]` 时抛 `IndexError` |
| 有开头、缺少结束围栏 | 抛 `ValueError` | `[0]` 仍可能拿到剩余全文，格式错误未被明确发现 |
| 可读性 | `start/end` 明确表示边界 | `[1]`、`[0]` 依赖隐含位置 |

如果只在这两种写法中选择，`index()` 更清楚；但模型格式错误属于预期失败分支，使用 `find()` 主动判断通常更稳：

```python
import ast


def parse_plan(response_text: str) -> list[str]:
    marker = "```python"

    start = response_text.find(marker)
    if start == -1:
        return []
    start += len(marker)

    end = response_text.find("```", start)
    if end == -1:
        return []

    plan_str = response_text[start:end].strip()
    if not plan_str:
        return []

    try:
        parsed = ast.literal_eval(plan_str)
    except (ValueError, SyntaxError):
        return []

    if not isinstance(parsed, list) or not parsed:
        return []

    if not all(isinstance(step, str) and step.strip() for step in parsed):
        return []

    return parsed
```

### 三个容易漏掉的边界

1. `ast.literal_eval()` 比 `eval()` 安全，因为它不执行任意 Python 代码；但它只负责把合法字面量转成 Python 对象，不保证结果一定是 `list[str]`。
2. `parsed: list[str] = ast.literal_eval(plan_str)` 中的 `list[str]` 只是类型标注，不会在运行时拦住字典、整数或混合元素列表。
3. `all([])` 返回 `True`，所以如果业务要求计划不能为空，必须在 `all()` 前单独检查 `not parsed`。

> [!tip] 可复用判断
> 模型输出应当作不可信外部输入处理：先检查传输/围栏协议，再解析语法，最后验证结构和业务语义。任何一层成功，都不能替代后一层。

如果模型服务支持 JSON mode 或严格 schema，应优先让模型直接返回 JSON，再使用 `json.loads()` 和 schema 校验；Markdown 围栏加 `ast.literal_eval()` 更适合作为教学示例或兼容旧接口的兜底方案。

## 实证：PR2-04 邮件抽取（真跑 DeepSeek）

规则版 `extract_email`（`partition` 解析「标签：值」）vs 模型版 `extract_email_llm`（`json_object` + schema prompt）：

| 输入 | 规则版 | 模型版 |
|---|---|---|
| 结构化邮件（有「标签：」）| ✅ | ✅ |
| 自由文本「张三说下周五前交报告、比较急、记得回复」| ❌ 抽不到 | ✅ 语义抽出（"比较急"→priority 高、"记得回复"→need_reply 是）|
| 缺优先级邮件 | —— | ✅ `priority: null`（**不编造**）|

🔑 模型版价值：**读懂语义再结构化**，规则版对自由文本（没有「标签：」）一个字段都抽不到。

## 实证：PR2-Gate 邮件处理器（阶段 2 收尾）

`code/stage2/pr2_gate_email_processor.py` 把阶段 2 能力串成一条流水线：

1. `simple_summarize(text)` 产出 `points/summary`。
2. `extract_email(text)` 抽取 `todo` dict。
3. `validate_payload(todo)` 做字段和序列化校验。
4. `classify(text)` 产出固定分类标签。
5. `json.dump(result, f, ensure_ascii=False, indent=2)` 保存到 `resources/stage2_email_result.json`。

实跑结果：

- 输出顶层 key：`category/points/summary/todo`。
- `todo` 五字段齐全：`sender/task/deadline/priority/need_reply`。
- 结果文件可被 `json.loads` 重新解析。
- 缺 `deadline` 时抛 `ValueError: 缺失字段: deadline`，坏结果不会落盘。
- `simple_summarize` 从只按 `。` 切，补强为“有换行按行切，否则按句号切”，兼容邮件和普通长文。

## 常见坑 / 错误理解 → 正确理解

- ❌ 开了 `json_object` 拿到的就是 dict → ✅ `content` 可能为空 / nullable；通过响应与非空正文守门后才把它当 **str** 做 `json.loads`，解析结果仍需外层类型与业务 validator。
- ❌ 模型 JSON 字符串可以直接放进最终结果 → ✅ 先 `json.loads` 成 dict，再 `validate_payload`，最后 `json.dump`。
- ❌ JSON 样例照搬 Python 单引号 → ✅ 对象的键和字符串值用双引号；数字、布尔值 `true/false` 和 `null` 不加引号。
- ⚠️ 真调模型**不可复现**：同一封缺字段邮件两次跑出「**截断**（Unterminated string）」和「**空 content**（None）」两种失败 → `except` + `if not content` 兜住不崩（兜底价值实锤）。
- ⚠️ `str.split("：", 1)` 遇无冒号行解包崩 → 用 `str.partition("：")`（总返回 3 段、不崩）。
- ⚠️ 函数体缩进 **4 / 8 空格混用** → `IndentationError: unexpected indent`。

## 关联

- [[提示工程基础(Prompt Engineering)]]：schema 靠 prompt 写清（点名字段 + 样例 + 锁 JSON）。
- [[分类与路由(Classification & Routing)]]：同为「规则版 vs 模型版」；模型版懂语义、规则版认字面。
- [[摘要与改写(Summarize & Transform)]]：都靠 prompt 锁 JSON + 代码兜底。
- [[上下文工程(Context Engineering)]]：真调模型不可复现、兜底必要性同源。
- [[采样参数与成本(Sampling)]]：enum 硬归零 vs temperature 软压低；真实计费看 `usage`。

## 来源

- AI-Agent-Learning PR2-04：产物 `code/stage2/pr2_04_extract_json.py`；预读 `notes/stage2/pr2_04_structured_output_preview.md`；带做与坑 `daily/2026-06-30.md`。
- AI-Agent-Learning PR2-Gate：产物 `code/stage2/pr2_gate_email_processor.py`、`resources/stage2_email_result.json`；复盘 `daily/2026-07-05.md`。
- AI-Agent-Learning A4-04-C1：`daily/2026-07-23.md` 中 Planner 计划解析的五类输入规则、首次 `4/5` 验证和缺少围栏时的 `IndexError` 证据。
- OpenAI《Structured Outputs》、DeepSeek《JSON Output》官方文档（首次检查：2026-06-30）。
- [DeepSeek Chat Completions API](https://api-docs.deepseek.com/zh-cn/api/create-chat-completion/) 与 [DeepSeek JSON Output](https://api-docs.deepseek.com/zh-cn/guides/json_mode/)（复核日期：2026-08-22）：非流式 assistant `content` 可为 nullable，`finish_reason` 有多种终点，JSON Output 仍可能出现空正文。
- AI-Agent-Learning A4-Gate C4b-2c：`daily/2026-08-22.md` 的“响应检查 → JSON 语法解析 → 精确业务校验”执行证据；当时父 Gate 为 `DOING`，后于 2026-08-24 正式 PASS。
- [OpenAI Structured Outputs](https://developers.openai.com/api/docs/guides/structured-outputs)（2026-09-08 复查）：结构约束仍可能有内容错误，拒答和不完整响应另行处理。`finish_reason="length"` 即使碰巧留下可解析的 JSON，也不能当作任务完整完成。
- [项目结构化输出订正](https://github.com/humbleded/AI-Agent-Learning/blob/main/notes/stage2/pr2_04_structured_output_preview.md)及 [DeepSeek Tool Calls](https://api-docs.deepseek.com/guides/tool_calls/)（项目核验日期 2026-09-07）。本轮同步是既有笔记维护，不新增用户作答或课程判定。
