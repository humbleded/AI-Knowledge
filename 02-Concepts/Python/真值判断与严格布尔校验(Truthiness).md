---
type: concept
topic: Python
status: usable
created: 2026-08-10
updated: 2026-08-10
source:
  - "C:/Users/26823/Desktop/AI-Agent-Learning/daily/2026-08-10.md"
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
---

# Python 真值判断与严格布尔校验

> [!note] 一句话结论
> `if value` 判断“这个值按 Python 规则算不算真”；`value is True` 判断“它是否就是布尔单例 `True`”。普通业务分支通常使用前者；模型、API、JSON 或工具结果的严格布尔合同适合使用后者。

## 三种判断解决不同问题

| 写法 | 检查的是什么 | 关键边界 |
| --- | --- | --- |
| `if value` / `if not value` | truthiness（真值）：相当于根据 `bool(value)` 分支 | `1`、非空字符串、非空容器都算真 |
| `value == True` | equality（相等性）：调用值相等规则 | `1 == True` 为 `True`，不能证明类型严格为 `bool` |
| `value is True` / `value is not True` | identity（对象身份）：是否就是布尔单例 `True` | 只有真正的 `True` 能通过严格成功合同 |

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
| 当前 fail-fast 已经实现完整错误恢复 | 它只防止失败工具结果进入正常候选链；重试与安全停止仍需单独实现 |

## 来源与验证

- AI-Agent-Learning `daily/2026-08-10.md`：保留从普通真值判断到严格 identity 校验的订正过程。
- AI-Agent-Learning `code/stage4/a4_gate_research_summary_agent.py`：真实使用 `tool_result.get("ok") is not True` 保护第二次模型调用。
- 决定性验证：R4b `5/5 PASS`，覆盖参数被改写、明确 `False`、字段缺失、`ok=1` 与严格 `True`；C3c topic / relative_path 两条真实 DeepSeek 正常链均通过。

## 相关

- [[基础数据类型(Data Types)|Python 基础数据类型]]
- [[类型转换(Type Conversion)|Python 类型转换与 bool(input(...)) 的坑]]
- [[and-or 短路求值|Python and / or 真值规则与返回原值]]
- [[异常·调试·测试(Exceptions)|Python 异常、调试与测试]]
- [[../Agent/工具定义与执行协议(Tool Definition)|Agent 工具定义与执行协议]]
- [[../../01-Maps/Python/python-official-docs-map|Python Official Docs Map]]
