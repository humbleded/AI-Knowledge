---
type: concept
topic: MCP
status: usable
created: 2026-06-04
updated: 2026-06-04
aliases:
  - Model Context Protocol
  - MCP
tags:
  - MCP
  - Agent
  - ToolCalling
---

# Model Context Protocol

MCP 是让 AI application 连接外部系统的开放协议。它解决的问题不是“模型怎么推理”，而是“AI 应用如何用统一方式访问数据、工具和工作流”。

## 核心理解

- AI application 或 agent 本身不应该为每个外部系统都写一套私有接入方式。
- MCP 把外部能力包装成标准接口，让不同 client 可以连接不同 server。
- Server 侧负责暴露能力，例如文件、数据库、搜索、业务 API、专用 prompt 或 workflow。
- Client 侧负责发现、调用和展示这些能力。
- 学 MCP 时要同时看协议角色、传输方式、权限边界和调试工具。

## 和 Tool Calling 的关系

Tool Calling 更像模型或应用内部的一种“调用工具”机制；MCP 更像外部能力的标准接入层。一个 MCP server 可以把多个 tool、resource 或 prompt 暴露给支持 MCP 的 client。

## 适合什么时候用

- 需要让多个 AI client 复用同一套外部能力。
- 需要把本地文件、数据库、浏览器、GitHub、设计工具或内部系统接给 Agent。
- 工具能力需要独立部署、调试、授权和版本化。
- 不想把所有外部系统集成逻辑都写死在单个应用里。

## 学习检查点

- 能画出 host、client、server 的关系。
- 能解释 tools、resources、prompts 的差异。
- 能写一个最小 MCP server 并用 Inspector 调试。
- 能说明一个 tool 的权限风险和确认策略。

## 相关

- [[README|MCP 概念卡]]
- [[../../01-Maps/MCP/mcp-official-docs-map|MCP Official Docs Map]]
- [[../../01-Maps/AI Agent 学习资源地图]]
- [[../../raw/articles/mcp-official-docs-intro|MCP official raw source]]
