---
type: project-note
topic: T3-02 Calculator Tool
status: pass
created: 2026-07-06
source:
  - C:\Users\26823\Desktop\AI-Agent-Learning\code\stage3\t3_02_calculator_tool.py
  - C:\Users\26823\Desktop\AI-Agent-Learning\daily\2026-07-06.md
tags:
  - Agent
  - Tool-Calling
  - AI-Agent-Learning
---

# T3-02 计算器工具

## 目标

实现一个最小计算器工具，用来练习 Agent 工具的四件事：

1. 定义工具 schema。
2. 校验参数。
3. 真实执行计算。
4. 打印调用参数和结果。

## 产物

- 执行区代码：`C:\Users\26823\Desktop\AI-Agent-Learning\code\stage3\t3_02_calculator_tool.py`

核心结构：

```python
CALCULATOR_SCHEMA = {
    "name": "calculator_tool",
    "description": "进行精确的加、减、乘、除运算。",
    "parameters": {
        "operation": "操作类型，只能是 add/sub/mul/div",
        "a": "第一个数，数字或可转成数字的字符串",
        "b": "第二个数，数字或可转成数字的字符串",
    },
}
```

## 验证结果

2026-07-06 实跑通过：

| 输入 | 结果 |
|---|---|
| `add 3 5` | `{"ok": True, "result": 8.0}` |
| `sub 10 4` | `{"ok": True, "result": 6.0}` |
| `mul 3 5` | `{"ok": True, "result": 15.0}` |
| `div 10 2` | `{"ok": True, "result": 5.0}` |
| `div 10 0` | `{"ok": False, "error": "除数不能为 0"}` |
| `plus 3 5` | `{"ok": False, "error": "不支持的操作：plus"}` |
| `add abc 5` | `{"ok": False, "error": "参数必须是数字"}` |

交互入口也能打印调用参数和结果：

```text
调用参数：operation=mul, a=3, b=5
计算结果：{'ok': True, 'result': 15.0}
```

## 关键结论

- 模型适合判断“该用计算器”，不适合完全口算精确数学。
- 真实计算由客户端程序执行，不能把模型生成 Action 当成计算结果。
- 工具要把失败包装成稳定结构，方便用户理解，也方便后续程序判断。

## 相关

- [[../../../../02-Concepts/Agent/工具定义与执行协议(Tool Definition)]]
- [[../../../../02-Concepts/LLM/函数调用(Function Calling)]]
- [[../../../../07-Reviews/AI-Agent-Learning/2026-07-06-t3-02-calculator-tool-review]]

