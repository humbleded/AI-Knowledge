---
aliases:
  - python-interpreter
type: concept
topic: Python
status: usable
created: 2026-05-28
updated: 2026-09-20
tags:
  - Python
  - 编程基础
---

# Python Interpreter

## 中文速读

- Python Interpreter（Python 解释器）就是“真正执行 Python 代码的程序”。
- 运行 `.py` 文件时，解释器会从上到下读取代码；遇到错误时，会把错误位置和原因显示成 traceback（报错追踪）。
- 学 AI / Agent 时，经常出问题的不是代码本身，而是“用了哪个 Python 解释器”和“当前工作目录在哪里”。

## 它是什么

Python Interpreter 是负责读取、检查并执行 Python 代码的程序。你写的 `.py` 文件本身只是文本；真正让它运行起来的是解释器。

最常见的运行方式：

```powershell
python script.py
```

这条命令的意思是：让当前命令行能找到的 `python` 解释器去执行 `script.py`。

## 两种常见模式

| 模式 | 适合什么 | 例子 |
|---|---|---|
| 脚本模式 | 运行完整程序，方便保存和反复执行 | `python app.py` |
| 交互模式 / REPL | 临时试一两句代码，输入一句执行一句 | 直接输入 `python` 后再输入 `1 + 1` |

REPL 是 Read-Eval-Print Loop 的缩写，也就是“读取输入、执行、打印结果、再等下一句”。它适合快速试验，不适合保存正式学习产物。

## 为什么对 Agent 学习重要

后面写 API 调用、RAG、工具函数、LangGraph 节点时，经常需要确认：

- 当前是不是在正确的 `.venv` 里运行。
- 安装包的解释器和运行脚本的解释器是不是同一个。
- 命令是在项目根目录运行，还是在别的目录运行。
- 报错来自语法、运行时输入，还是环境依赖。

常用排查命令：

```powershell
python --version
where python
python -m pip --version
```

如果 `python -m pip --version` 显示的路径和你预期的项目 `.venv` 不一致，说明安装依赖和运行代码可能不在同一个环境里。

## 常见误解

- 不是所有电脑上的 `python` 都是同一个解释器；系统 Python、Anaconda、`.venv` 都可能各有一份。
- 双击 `.py` 文件能运行，不代表适合调试；学习阶段优先在 PowerShell 里运行，这样能看到完整报错。
- traceback 最下面通常最接近真正出错的位置；先看最后几行，再往上追调用链。
- 解释器按文件从上到下执行，但函数体内部代码只有在函数被调用时才会真正运行。

## 相关

- [[输入与输出(input & print)]]
- [[环境管理(venv & pip)]]
- [[异常·调试·测试(Exceptions)]]
- [[../../03-Courses/Python/AI-Agent-Learning/stage0-python-basics]]

## 来源 / 证据

- [[../../raw/articles/python-3-official-documentation|Python 3 Official Documentation]]
- [[../../03-Courses/Python/AI-Agent-Learning/stage0-python-basics|阶段 0：Python 与开发环境]]
- [[../../04-Projects/Python/AI-Agent-Learning/p0-01-hello-script|P0-01 第一个脚本]]
- [[../../04-Projects/Python/AI-Agent-Learning/p0-06-env-check|P0-06 venv 与环境检查]]
