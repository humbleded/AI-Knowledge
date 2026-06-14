---
type: review
topic: AI-Agent-Learning P0-Gate L1-01
status: pass
created: 2026-06-14
updated: 2026-06-14
tags:
  - AI-Agent-Learning
  - Python
  - LLM
  - Stage0
  - Stage1
  - P0-Gate
  - L1-01
---

# 2026-06-14 阶段 0 / 阶段 1 复盘：P0-Gate + L1-01

## 判定

- `P0-Gate Python 基础闯关`：PASS。
- `L1-01 API Key 与 SDK`：PASS。

## 验证摘要

P0-Gate：

- `code/stage0/p0_gate_learning_log.py` 通过 `py_compile`。
- 临时 JSON 测试覆盖新增、保存、重新读取、拒绝非整数、拒绝负数、最近 7 条展示。
- 当前 `resources/p0_gate_learning_log.json` 能被 Python 解析。
- 当前 JSON 里有 3 条有效非负测试记录，满足 3 条以上测试记录要求。
- 发现 1 条旧脏数据：`minutes: -5`。脚本已阻止新增负数，旧数据后续清理即可。

L1-01：

- `code/stage1/l1_01_first_call.py` 通过 `py_compile`。
- 用 `.venv\Scripts\python.exe` 运行脚本，成功调用 DeepSeek 并打印模型回复。
- 脚本从 `os.environ.get("DEEPSEEK_API_KEY")` 读取 key。
- 未发现明文 `sk-` 类型密钥。
- 多余的无参数 `client = OpenAI()` 已不存在。

## 稳定结论

- `list[dict]` 适合新手阶段的学习日志：外层列表追加记录，内层字典保存字段。
- CLI 输入边界要先守住：文件不存在、JSON 损坏、非整数输入、负数输入都应有处理。
- API Key 是身份和权限凭证，不是模型本身；模型名决定调用哪个模型。
- SDK 省掉了很多 HTTP 细节，但底层仍然是 HTTP 请求。
- 真实 key 应从环境变量读取，不应硬编码进代码或提交到 GitHub。

## 当天卡点

- `.env` 文件里当前只看到 `TEST_VARIABLE`，`DEEPSEEK_API_KEY` 来自当前 PowerShell 环境；换终端时可能需要重新配置。
- 当前执行区不是 Git 仓库，批改时无法用 Git 状态证明 `.env` 是否会被提交。
- `resources/p0_gate_learning_log.json` 中保留了一条旧负数测试记录，后续统计前应清理。

## 同步内容

- Python 概念卡：[[../../02-Concepts/Python/python-json-learning-log-cli|Python JSON 学习日志 CLI：list[dict] 与输入校验]]
- LLM 概念卡：[[../../02-Concepts/LLM/api-key-and-sdk|API Key 与 SDK：调用模型的门禁卡和快递柜台]]
- Python 项目记录：[[../../04-Projects/Python/AI-Agent-Learning/p0-gate-learning-log|P0-Gate Python 基础闯关]]
- LLM 项目记录：[[../../04-Projects/LLM/AI-Agent-Learning/l1-01-first-call|L1-01 API Key 与 SDK]]
- 阶段 0 页面：[[../../03-Courses/Python/AI-Agent-Learning/stage0-python-basics|阶段 0：Python 与开发环境]]
- 阶段 1 页面：[[../../03-Courses/LLM/AI-Agent-Learning/stage1-llm-api-basics|阶段 1：大模型 API 入门]]

## 下一步

进入 `L1-02 单轮问答`。

重点不是再证明“能调用模型”，而是把单次用户输入、模型输出和错误提示封装成一个更像真实工具的小脚本。
