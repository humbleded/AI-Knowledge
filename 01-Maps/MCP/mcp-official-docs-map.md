---
type: map
topic: MCP
status: active
created: 2026-06-04
updated: 2026-06-04
aliases:
  - MCP Official Docs Map
tags:
  - MCP
  - Agent
  - 地图
---

# MCP Official Docs Map

这页只做官方 MCP 文档入口和学习顺序，不替代官方文档正文。

## 官方入口

- [What is MCP?](https://modelcontextprotocol.io/docs/getting-started/intro)
- [MCP docs index for LLMs](https://modelcontextprotocol.io/llms.txt)
- [Architecture overview](https://modelcontextprotocol.io/docs/learn/architecture.md)
- [Understanding MCP servers](https://modelcontextprotocol.io/docs/learn/server-concepts.md)
- [Understanding MCP clients](https://modelcontextprotocol.io/docs/learn/client-concepts.md)
- [SDKs](https://modelcontextprotocol.io/docs/sdk.md)
- [Build an MCP server](https://modelcontextprotocol.io/docs/develop/build-server.md)
- [Build an MCP client](https://modelcontextprotocol.io/docs/develop/build-client.md)
- [MCP Inspector](https://modelcontextprotocol.io/docs/tools/inspector.md)
- [Debugging](https://modelcontextprotocol.io/docs/tools/debugging.md)
- [Security best practices](https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices.md)

## 建议阅读顺序

1. 先读 What is MCP，建立边界：MCP 是连接 AI application 和外部系统的开放协议。
2. 读 Architecture，确认 host、client、server、transport 的位置关系。
3. 读 server concepts 和 client concepts，分别理解“暴露能力”和“消费能力”。
4. 选一个 SDK，做最小 server。
5. 用 MCP Inspector 调试，再接入一个真实 client。
6. 最后补安全、授权、远程 server 和 registry。

## 学习产出

- 一张概念卡：[[../../02-Concepts/MCP/MCP(Model Context Protocol)]]
- 一个最小本地 MCP server 项目记录。
- 一份 client/server/host 的架构图或文字说明。
- 一份安全检查清单：哪些 tool 可以执行、哪些资源只读、哪些调用需要用户确认。

## 相关

- [[../../02-Concepts/MCP/README|MCP 概念卡]]
- [[../../01-Maps/AI Agent 学习资源地图]]
- [[../../03-Courses/Agent/AI-Agent-Learning/README]]
- [[../../raw/articles/mcp-official-docs-intro|Raw source]]
