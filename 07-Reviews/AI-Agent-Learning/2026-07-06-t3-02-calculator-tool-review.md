---
type: review
topic: AI-Agent-Learning T3-02
status: pass
created: 2026-07-06
tags:
  - AI-Agent-Learning
  - Agent
  - Tool-Calling
  - PASS
---

# 2026-07-06 T3-02 计算器工具 PASS 复盘

## 判定

**T3-02 PASS**

## 验证

- `CALCULATOR_SCHEMA` 包含 `name/description/parameters`。
- 参数 key 为 `operation/a/b`。
- 7 组函数测试全 PASS：加、减、乘、除、除零、非法操作、非数字。
- 交互入口能打印调用参数和结果。

## 学到的稳定概念

- [[../../02-Concepts/Agent/工具定义与执行协议(Tool Definition)|工具定义与执行协议]]
- [[../../02-Concepts/LLM/函数调用(Function Calling)|函数调用 / Tool Calling]]

## 关键问题闭环

1. 为什么数学题不能完全交给模型口算？
   - 模型擅长生成文本，本质是预测 token；精确计算应交给确定性程序工具。
2. 工具参数如何校验？
   - `operation` 白名单；`a/b` 转 `float`；除零返回稳定错误。
3. 工具报错如何返回？
   - 成功：`{"ok": True, "result": ...}`。
   - 失败：`{"ok": False, "error": ...}`。

## 今日易错点

- `getTool("Weather")` 找不到工具时最终返回 `None`，不是 `{}`。
- 工具菜单由客户端提供，Observation 由客户端回填；不要说成模型自己查工具或改上下文。
- 回答工具返回结构时要按真实代码字段 `ok/result/error`，不要临时改名。

## 下一步

进入 `T3-03 文件工具`：练习文件读取工具、沙箱目录限制、长文件截断/摘要和敏感路径拒绝。

