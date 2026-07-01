---
aliases:
  - python-venv-pip-env
type: concept
topic: Python project environment
status: active
created: 2026-06-10
tags:
  - Python
  - venv
  - pip
  - dotenv
---

# Python 项目环境管理：venv、pip 与 .env

## 核心结论

`venv`、`pip` 和 `.env` 共同解决的是项目环境管理问题：

- `venv` 让一个项目拥有独立的 Python 环境和第三方包目录。
- `pip install` 会把包安装到当前 Python 环境的 `site-packages`。
- `.env` 适合保存本地配置示例或开发配置，真实 API Key 不应该写死在 `.py` 代码里。

## venv 解决什么

虚拟环境的价值是隔离依赖。

如果所有项目都共用全局 Python，项目 A 升级了某个包，项目 B 可能突然坏掉。使用 `.venv` 后，每个项目可以有自己的解释器入口、`pip` 和 `site-packages`。

常见命令：

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
```

## pip 安装到哪里

`pip` 跟随当前 Python 环境。

激活 `.venv` 后：

```powershell
pip install python-dotenv requests
python -m pip show python-dotenv
```

`Location` 应指向当前项目下的 `.venv\Lib\site-packages`。

为了避免 `pip` 和 `python` 指向不同环境，优先使用：

```powershell
python -m pip install 包名
```

## .env 与 API Key

`.env` 用来把配置从代码里分离出来。例如：

```text
TEST_VARIABLE=hello_stage0
```

Python 中可以用 `python-dotenv` 加载：

```python
from dotenv import load_dotenv

load_dotenv()
```

注意：

- `.env` 不等于安全保险箱。
- 真实 API Key、token、密码不要写死在代码里。
- 公开仓库通常提交 `.env.example`，而把真实 `.env` 加入 `.gitignore`。

## 常见检查

```powershell
where python
python --version
python -m pip show requests
python -c "import requests; print(requests.__version__)"
```

如果包明明安装了却无法导入，先检查当前终端使用的 `python` 是否来自项目 `.venv`。

## 来源

- AI-Agent-Learning P0-06：`code/stage0/p0_06_env_check.py`
- AI-Agent-Learning daily：`daily/2026-06-10.md`
- 廖雪峰 Python 教程：模块、安装第三方模块、venv、requests

## 相关

- [[README|Python 概念卡]]
- [[../../03-Courses/Python/AI-Agent-Learning/stage0-python-basics]]
- [[../../04-Projects/Python/AI-Agent-Learning/p0-06-env-check]]
- [[../../07-Reviews/AI-Agent-Learning/2026-06-10-stage0-p0-06-pass-review]]
