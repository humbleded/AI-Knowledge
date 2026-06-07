---
type: source
topic: MCP
status: active
created: 2026-06-04
updated: 2026-06-04
source_url: https://modelcontextprotocol.io/docs/getting-started/intro
source_type: official-docs
tags:
  - Source
  - MCP
  - Agent
---

# MCP Official Docs Intro

## 中文速读

- 这是 Model Context Protocol 的官方入门页，适合先建立“它是什么、解决什么问题、有哪些角色”的整体心智模型。
- 学 MCP 时，重点不是背某个 SDK 的 API，而是先理解 protocol（协议）、client、server、tool、resource 这些稳定概念。
- 真正开始实现前，应重新查看官方文档，因为 spec、SDK 页面和最佳实践仍可能继续变化。

## 关键术语

- `protocol`（协议）：约定 client 和 server 如何交换能力与上下文。
- `client`（客户端）：消费 MCP 能力的一侧，通常是 AI application 或 agent runtime。
- `server`（服务端）：暴露 tools、resources、prompts 等能力的一侧。
- `workflows`（工作流）：通过 MCP 接入的外部步骤、工具链或业务流程。

## Source

- Official page: https://modelcontextprotocol.io/docs/getting-started/intro
- Docs index for LLMs: https://modelcontextprotocol.io/llms.txt
- Retrieved: 2026-06-04

## Why This Source Matters

This is the official introduction to Model Context Protocol. It is a good entry point for the Agent learning route because it explains MCP as a standard way for AI applications to connect to external data sources, tools, and workflows.

## What To Compile Into Wiki

- MCP official navigation -> [[../../01-Maps/MCP/mcp-official-docs-map]]
- Core concept -> [[../../02-Concepts/MCP/model-context-protocol]]
- Agent learning route reference -> [[../../01-Maps/AI Agent 学习资源地图]]

## Do Not Lose

- MCP should be learned as an integration protocol, not as a single library.
- For implementation work, read the current official pages before coding because the spec and SDK pages can change.
