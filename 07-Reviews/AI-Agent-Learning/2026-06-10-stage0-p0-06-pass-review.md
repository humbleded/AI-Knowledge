---
type: review
topic: AI-Agent-Learning Stage0 P0-06
status: pass
created: 2026-06-10
date: 2026-06-10
tags:
  - AI-Agent-Learning
  - Python
  - 复盘
  - PASS
---

# 2026-06-10 阶段 0 复盘：P0-06

## 当日完成

- P0-06 模块、第三方包、venv：PASS

原始每日记录：

- [2026-06-10.md](file:///C:/Users/26823/Desktop/AI-Agent-Learning/daily/2026-06-10.md)

## 已掌握

- 能建立项目虚拟环境 `.venv`。
- 能在虚拟环境中安装 `python-dotenv` 和 `requests`。
- 能用 `.env` 保存本地测试配置。
- 能用 `python-dotenv` 读取 `TEST_VARIABLE=hello_stage0`。
- 能解释虚拟环境、`pip install` 安装位置和 API Key 不硬编码的原因。

## 验证摘要

已用 `.venv\Scripts\python.exe` 运行 `code/stage0/p0_06_env_check.py`。脚本能定位项目根目录，确认 `.env` 存在，并读取到 `TEST_VARIABLE=hello_stage0`。

额外验证 `python-dotenv` 和 `requests` 均可导入，且安装位置在当前项目虚拟环境下。

## 主要问题

没有阻塞问题。

可继续强化：

1. 在脚本中打印 `requests.__version__`，让第三方包验证更直接。
2. 新增 `.env.example`，只保存示例环境变量，后续真实 API Key 不进入代码仓库。

## 下一步

进入 P0-07：异常、调试、单元测试。

下一份代码应关注：

- 用 `try/except` 处理除零和非数字输入。
- 不要把所有异常都吞掉。
- 写最少 3 个测试样例，覆盖正常输入和异常输入。

## 相关

- [[../../02-Concepts/Python/python-venv-pip-env]]
- [[../../03-Courses/Python/AI-Agent-Learning/stage0-python-basics]]
- [[../../04-Projects/Python/AI-Agent-Learning/p0-06-env-check]]
