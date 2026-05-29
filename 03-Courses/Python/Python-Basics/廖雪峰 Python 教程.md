---
type: course-note
topic: Python Basics
status: active
created: 2026-05-28
tags:
  - Python
  - 中文教程
---

# 廖雪峰 Python 教程

来源：

- [模式匹配 match](https://liaoxuefeng.com/books/python/basic/match/index.html)
- [Python 教程主页](https://liaoxuefeng.com/books/python/)

## 为什么有用

廖雪峰 Python 教程适合作为 P0 阶段的中文主线资料。它的优势是中文解释清楚、章节短、适合边读边写小脚本。

## 对应 AI-Agent-Learning 阶段

| 学习内容 | 对应任务 |
|---|---|
| 安装、第一个程序、输入输出 | P0-01 |
| 数据类型、变量、字符串 | P0-02 |
| 条件判断、模式匹配、循环 | P0-03 |
| list、tuple、dict、set | P0-04 |
| 函数、参数、递归 | P0-05 |
| 模块、第三方模块、venv | P0-06 |
| 错误处理、调试、单元测试 | P0-07 |
| 文件读写、序列化 | P0-08 |

## 当前重点：match/case

`match/case` 适合处理“一个值可能对应多种结构或分支”的情况。它比多层 `if/elif` 更像“模式匹配表”，代码可读性更强。

阶段 P0-03 暂时只需要掌握：

- `if/elif/else`：最基础的条件分支。
- `match/case`：当分支很多、匹配对象结构明确时使用。
- `for` / `while`：用循环避免重复写代码。

## 学习建议

- 不要只看文字，每节至少写一个 10-30 行脚本。
- 当前不要被递归卡住；递归放到 P0-05 后再回看。
- 学完一个小节后，优先回答“这个语法解决什么问题？”

## 相关

- [[../AI-Agent-Learning/stage0-python-basics]]
- [[../../../02-Concepts/Python/python-input-print]]
- [[../../../02-Concepts/Python/python-basic-data-types]]

