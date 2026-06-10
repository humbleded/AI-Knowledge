---
type: review
topic: AI-Agent-Learning Stage0 P0-05
status: pass
created: 2026-06-09
date: 2026-06-09
tags:
  - AI-Agent-Learning
  - Python
  - 复盘
  - PASS
---

# 2026-06-09 阶段 0 复盘：P0-05

## 当日完成

- P0-05 函数、参数、返回值：PASS

原始每日记录：

- [2026-06-09.md](file:///C:/Users/26823/Desktop/AI-Agent-Learning/daily/2026-06-09.md)

## 已掌握

- 能把生成计划和评分答案拆成独立函数。
- 能用参数接收输入，例如 `goal`、`days`、`answer`。
- 能用 `return` 把结果交给调用者。
- 能让 `main()` 负责交互和打印，让核心函数负责处理逻辑。
- 能解释 `return` 和 `print()` 的区别。

## 验证摘要

已运行 `code/stage0/p0_05_plan_functions.py`，脚本能生成 3 天学习计划并输出练习分。函数级检查覆盖了计划长度、中文目标文本、空答案评分、关键词加分和非整数天数提示。

## 主要问题

1. `days <= 0` 当前返回空列表，没有明确告诉用户“计划天数必须是正整数”。
2. `return` 和 `print()` 的回答已抓住方向，但需要记住：普通函数执行完也会回到调用处，关键区别是 `return` 交回值，`print()` 只是显示。

这些问题不影响 P0-05 通过，适合作为后续输入校验和单元测试练习。

## 下一步

进入 P0-06：模块、第三方包、venv。

下一份代码应关注：

- 理解虚拟环境隔离依赖。
- 知道 `pip install` 安装的是项目可用的第三方包。
- 不把 API Key 或敏感配置硬编码到代码里。

## 相关

- [[../../02-Concepts/Python/python-functions]]
- [[../../03-Courses/Python/AI-Agent-Learning/stage0-python-basics]]
- [[../../04-Projects/Python/AI-Agent-Learning/p0-05-plan-functions]]
