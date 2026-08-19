---
type: concept
topic: Python
status: usable
created: 2026-08-10
updated: 2026-08-19
source:
  - "C:/Users/26823/Desktop/AI-Agent-Learning/daily/2026-08-10.md"
  - "C:/Users/26823/Desktop/AI-Agent-Learning/daily/2026-08-19.md"
  - "C:/Users/26823/Desktop/AI-Agent-Learning/code/stage4/a4_gate_research_summary_agent.py"
tags:
  - Python
  - boolean
  - data-validation
  - AI-Agent-Learning
aliases:
  - Python Truthiness
  - Python 真值判断
  - Python 严格布尔校验
  - is True 与普通判断
  - if not 与 is None
  - Python 对象不存在与假值
---

# Python 真值判断与严格布尔校验

> [!note] 一句话结论
> `if value` 判断“这个值按 Python 规则算不算真”；`value is True` 判断“它是否就是布尔单例 `True`”。普通业务分支通常使用前者；模型、API、JSON 或工具结果的严格布尔合同适合使用后者。
>
> `if not value` 判断“这个对象按真值规则算不算假”；`value is None` 只判断“它是否就是 `None`”。对象真实存在，也可能因自身的 `__bool__()` 或 `__len__()` 返回假值而被 `if not value` 拦截。

## 四种判断解决不同问题

| 写法 | 检查的是什么 | 关键边界 |
| --- | --- | --- |
| `if value` / `if not value` | truthiness（真值）：相当于根据 `bool(value)` 分支 | `1`、非空字符串、非空容器都算真 |
| `value == True` | equality（相等性）：调用值相等规则 | `1 == True` 为 `True`，不能证明类型严格为 `bool` |
| `value is True` / `value is not True` | identity（对象身份）：是否就是布尔单例 `True` | 只有真正的 `True` 能通过严格成功合同 |
| `value is None` / `value is not None` | identity（对象身份）：是否就是单例 `None` | 不会把 `0`、空容器或自定义 falsey 对象误当成 `None` |

可以把它们想成两种门禁：

- truthiness：看起来有通行资格就放行。
- `is True`：必须出示对象身份完全匹配的 `True` 通行证。

## Python 的真值规则

常见 falsy（假值）包括：

```python
False
None
0
0.0
""
[]
{}
set()
```

其他大多数对象都是 truthy（真值），包括容易误判的值：

```python
1
-1
"true"
"false"       # 非空字符串，所以仍然是真值
[0]           # 非空列表
{"ok": False}  # 非空字典
```

因此下面的代码只是在检查真值，并没有验证类型：

```python
if payload.get("ok"):
    continue_work()
```

它会放行 `True`，也会放行 `1`、`"true"`、`"false"` 和非空容器。

## 对象不存在不等于对象是假值

`if not response` 可以理解为先按 `bool(response)` 做真值判断，再把结果取反。Python 对象默认是真值；如果类定义了 `__bool__()`，Python 会使用它的返回值；如果没有 `__bool__()` 但定义了 `__len__()`，长度为 `0` 时对象也是假值。

因此，一个对象可以拥有完整、合法的属性，但仍然是 falsey（假值）：

```python
class ApiResponse:
    def __init__(self) -> None:
        self.status_code = 503
        self.body = {"error": "service unavailable"}

    def __bool__(self) -> bool:
        return False


response = ApiResponse()

assert response is not None
assert bool(response) is False
assert response.status_code == 503
```

这时两种判断会得到不同结果：

```python
if not response:
    print("按对象的真值协议判为假")  # 会执行

if response is None:
    print("根本没有响应对象")        # 不会执行
```

选择依据不是哪种写法“更严格”，而是当前分支真正想问什么：

- 想问“对象是否不存在”，使用 `response is None`。
- 想问“对象按它自己的真值协议是否可用”，才使用 `if not response`。
- 想检查对象的字段、状态码或业务合同，应显式校验那些字段，不要让真值判断替代具体合同。

## 为什么 `== True` 也不严格

`==` 检查值相等，而 `is` 检查对象身份。Python 中 `bool` 与整数存在继承关系，所以：

```python
1 == True     # True
0 == False    # True

value = 1
value is True  # False
```

如果合同要求“字段必须是布尔值 `True`”，不要用 `value == True` 替代身份检查。

## 严格协议边界的推荐写法

当工具结果合同规定 `ok` 必须严格为布尔值时，可以写：

```python
tool_result = execute_tool_call(...)

if tool_result.get("ok") is not True:
    raise RuntimeError(
        f"工具调用失败: {tool_result.get('error', '无法生成正常候选摘要')}"
    )
```

这段代码的含义是：只有真正的布尔单例 `True` 才能继续。字段缺失时，`.get("ok")` 返回 `None`，也会安全停止。

下面的写法仍然不够严格：

```python
if not tool_result.get("ok", False):
    raise RuntimeError("工具调用失败")
```

它能拒绝字段缺失和明确的 `False`，但 `1`、`"true"`、`"false"`、非空列表和非空字典仍会被当成成功。

## 对照矩阵

| `ok` 的实际值 | `bool(ok)` | `not ok` | `ok is True` | 严格合同是否放行 |
| --- | ---: | ---: | ---: | ---: |
| `True` | True | False | True | 是 |
| `False` | False | True | False | 否 |
| `None` | False | True | False | 否 |
| `1` | True | False | False | 否 |
| `0` | False | True | False | 否 |
| `"true"` | True | False | False | 否 |
| `"false"` | True | False | False | 否 |
| `[]` | False | True | False | 否 |
| `[1]` | True | False | False | 否 |
| `{}` | False | True | False | 否 |
| `{"x": 1}` | True | False | False | 否 |

可以把严格合同写成一个可重复测试的小函数：

```python
def is_strict_success(payload: dict[str, object]) -> bool:
    return payload.get("ok") is True


assert is_strict_success({"ok": True}) is True
assert is_strict_success({"ok": False}) is False
assert is_strict_success({}) is False
assert is_strict_success({"ok": 1}) is False
assert is_strict_success({"ok": "true"}) is False
```

## 什么时候使用哪一种

### 使用普通真值判断

变量由本地可信代码产生，而且语义本来就是“是否为空”或“是否有内容”时，普通写法最自然：

```python
if is_ready:
    start()

if results:
    render(results)
```

### 使用严格身份判断

数据来自模型、API、JSON、配置文件或工具适配层，并且 schema 明确要求布尔类型时，使用：

```python
if payload.get("ok") is not True:
    stop_safely()
```

### 区分三态值

当 `True`、`False`、`None` 分别代表成功、失败、尚未确定时，也应显式使用身份判断：

```python
if value is True:
    handle_success()
elif value is False:
    handle_failure()
elif value is None:
    handle_unknown()
```

## Agent 工具边界中的作用

模型、外部 API 和工具适配器都属于运行时边界。Agent 客户端不能因为一个字段“看起来为真”就继续产生摘要或执行后续动作。

> [!important] 严格不等于每一层重复全部校验
> 严格校验还包括“把检查放在拥有该职责的层”。解析层可以只证明结构存在并保留原始未信任值；执行或 validator 层再检查类型、非空、白名单、Schema 和业务约束。上层抢先检查不属于自己的内容，可能会改变错误分类并切断既定的纠错路径。

例如，一个 Action 解析器只负责区分“响应结构缺失”和“有一个可继续校验的原始 Action”时，可以这样分层：

```python
# 解析层：检查响应或字段是否根本不存在
if response is None:
    raise ToolActionProtocolError("Response must not be empty.")

tool_name = tool_call.function.name
if tool_name is None:
    raise ToolActionProtocolError("Function name must not be None.")

# tool_name 的其他原始值继续透传
return {"tool_name": tool_name}
```

下一层再负责内容合同：

```python
# 执行 / validator 层：判断原始值是否合法
if not isinstance(tool_name, str):
    return {"ok": False, "error": "工具名必须是字符串"}

if not tool_name.strip():
    return {"ok": False, "error": "工具名不能为空"}
```

这里让 `123` 原样进入执行层，不代表认定它合法；只是把“它为何不合法”的判断交给正确的责任层，使系统能生成具体、安全的错误 Observation，且不调用真实工具。如果当前解析器的合同本来就要求输出完整合法的非空字符串，那才应在解析器中使用 `type(...) is str` / `isinstance(...)` 与 `strip()`。

在 AI-Agent-Learning 的 A4-Gate C3c 正常链中，最终采用了 fail-closed（失败时默认关闭）规则：

```text
tool_result.ok is True
→ 回填真实 Observation
→ 发起第二次模型调用
→ 生成候选摘要

其他任何值
→ 抛出 RuntimeError
→ 不发起第二次模型调用
```

这只负责保护当前两轮正常链。失败 Observation 的模型纠错、重试、`max_steps` 和安全停止仍应由后续 Agent 控制器负责，不能把当前快速停止冒充完整恢复机制。

## 错误理解与订正

| 错误理解 | 正确结论 |
| --- | --- |
| 给 `.get()` 设置默认 `False` 就等于严格布尔校验 | 它只解决字段缺失；普通真值判断仍会放行 `1`、非空字符串和非空容器 |
| `value == True` 能证明 value 是布尔值 | `1 == True` 为 True；严格合同应使用 `value is True` |
| `if value` 只会让布尔值通过 | `if value` 检查 truthiness，很多非布尔对象也会通过 |
| `if not response` 等于“没有响应对象” | 它检查真值；真实存在的对象也可能通过 `__bool__()` 或 `__len__()` 表现为假。只检查缺失应使用 `response is None` |
| 严格模式要求解析层也对 `tool_name` 做类型与 `strip()` 校验 | 严格模式要求职责清晰；若解析层只提取原始 Action，内容校验应留给执行 / validator 层，否则可能截断纠错链 |
| 当前 fail-fast 已经实现完整错误恢复 | 它只防止失败工具结果进入正常候选链；重试与安全停止仍需单独实现 |

## 来源与验证

- [Python 官方文档：Truth Value Testing](https://docs.python.org/3/library/stdtypes.html#truth-value-testing)：对象默认是真值；类可通过 `__bool__()` 返回 `False`，或通过 `__len__()` 返回 `0`，使实例表现为假值。
- [Python 官方文档：Identity comparisons](https://docs.python.org/3/reference/expressions.html#is-not)：`is` / `is not` 检查两个名称是否指向同一个对象；`None` 是单例。
- AI-Agent-Learning `daily/2026-08-10.md`：保留从普通真值判断到严格 identity 校验的订正过程。
- AI-Agent-Learning `daily/2026-08-19.md`：记录 `if not response` 对 falsey 合法属性对象的误判，以及 Action parser 与 `execute_tool_call()` 的结构 / 内容职责边界；C4b-1 子单元已收口，但父 A4-Gate 仍为 `DOING`。
- AI-Agent-Learning `code/stage4/a4_gate_research_summary_agent.py`：真实使用 `tool_result.get("ok") is not True` 保护第二次模型调用。
- 决定性验证：R4b `5/5 PASS`，覆盖参数被改写、明确 `False`、字段缺失、`ok=1` 与严格 `True`；C3c topic / relative_path 两条真实 DeepSeek 正常链均通过。

## 相关

- [[基础数据类型(Data Types)|Python 基础数据类型]]
- [[类型转换(Type Conversion)|Python 类型转换与 bool(input(...)) 的坑]]
- [[and-or 短路求值|Python and / or 真值规则与返回原值]]
- [[异常·调试·测试(Exceptions)|Python 异常、调试与测试]]
- [[../Agent/工具定义与执行协议(Tool Definition)|Agent 工具定义与执行协议]]
- [[../../01-Maps/Python/python-official-docs-map|Python Official Docs Map]]
