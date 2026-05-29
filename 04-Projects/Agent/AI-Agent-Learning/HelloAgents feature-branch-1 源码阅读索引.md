---
type: project-note
topic: HelloAgents feature-branch-1
status: seed
created: 2026-05-28
tags:
  - AI-Agent
  - 源码阅读
  - Python
---

# HelloAgents feature-branch-1 源码阅读索引

来源：

- [jjyaoao/HelloAgents feature-branch-1](https://github.com/jjyaoao/HelloAgents/tree/feature-branch-1)
- 本地路径：[HelloAgents-feature-branch-1](file:///C:/Users/26823/Desktop/AI-Agent-Learning/repos/HelloAgents-feature-branch-1/)

## 为什么有用

这个仓库适合 H5 阶段的源码学习。它是一个教学友好的多智能体框架，核心思想是用较少抽象理解 Agent 如何调用工具。

## 阅读重点

优先找这些结构：

- Agent 基类或核心 Agent 类
- LLM 调用封装
- ToolRegistry 或工具注册逻辑
- ReActAgent
- ReflectionAgent
- Memory / RAG / Protocols 如何被抽象成工具
- 示例代码和测试

## 对应学习任务

| 源码阅读目标 | 对应任务 |
|---|---|
| 跑通指定分支 | H5-01 |
| 阅读 Core 层 | H5-02 |
| 阅读 Agents 层 | H5-03 |
| 阅读 Tools 层并新增工具 | H5-04 |
| 阅读 Memory、Context、Protocol | H5-05 |

## 产出要求

读源码时不要只写“看懂了”，每次至少产出：

- 一张模块关系图。
- 一个关键类/函数说明。
- 一个最小运行示例。
- 一个自己新增的小工具或小改动。

