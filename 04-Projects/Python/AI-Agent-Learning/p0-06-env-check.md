---
type: project-note
topic: AI-Agent-Learning P0-06
status: pass
created: 2026-06-10
tags:
  - Python
  - AI-Agent-Learning
  - PASS
---

# P0-06 模块、第三方包、venv

## 任务

完成 `code/stage0/p0_06_env_check.py`：

- 建立项目虚拟环境 `.venv`。
- 安装 `python-dotenv` 和 `requests`。
- 在项目根目录创建 `.env`，写入 `TEST_VARIABLE=hello_stage0`。
- 运行脚本并确认能读取环境变量。

源代码位置：

- [p0_06_env_check.py](file:///C:/Users/26823/Desktop/AI-Agent-Learning/code/stage0/p0_06_env_check.py)
- [2026-06-10 daily](file:///C:/Users/26823/Desktop/AI-Agent-Learning/daily/2026-06-10.md)

## 验证结果

已执行：

```powershell
.\.venv\Scripts\python.exe -m py_compile code\stage0\p0_06_env_check.py
.\.venv\Scripts\python.exe code\stage0\p0_06_env_check.py
.\.venv\Scripts\python.exe -c "import dotenv, requests; print(requests.__version__)"
```

关键输出：

```text
.env 是否存在： True
TEST_VARIABLE： hello_stage0
dotenv import OK
requests import OK
```

`python -m pip show` 验证到：

- `python-dotenv` 安装在 `.venv\Lib\site-packages`
- `requests` 安装在 `.venv\Lib\site-packages`

## 通过结论

P0-06 已 PASS。

通过原因：

- `.venv` 存在，且能使用其中的 Python 运行脚本。
- `python-dotenv` 和 `requests` 均安装在虚拟环境中。
- `.env` 能被读取，`TEST_VARIABLE=hello_stage0` 生效。
- 问答能说明 venv 隔离依赖、`pip install` 的安装位置，以及 API Key 不应硬编码。

## 可改进点

- 可以在脚本中额外打印 `requests.__version__`，让第三方包导入检查更直观。
- 可以新增 `.env.example`，只保存示例配置，避免混淆真实密钥和练习变量。

## 相关

- [[../../../02-Concepts/Python/环境管理(venv & pip)]]
- [[../../../03-Courses/Python/AI-Agent-Learning/stage0-python-basics]]
- [[../../../07-Reviews/AI-Agent-Learning/2026-06-10-stage0-p0-06-pass-review]]
