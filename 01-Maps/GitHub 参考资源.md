---
type: map
topic: GitHub 参考资源
status: active
created: 2026-05-28
tags:
  - GitHub
  - 资源
---

# GitHub 参考资源

## 已安装到 Codex 的 Obsidian Skills

来源：[kepano/obsidian-skills](https://github.com/kepano/obsidian-skills)

已安装：

- `obsidian-markdown`：创建和编辑 Obsidian Flavored Markdown，支持 wikilink、callout、properties 等语法。
- `obsidian-bases`：创建和编辑 Obsidian Bases。
- `json-canvas`：创建和编辑 Obsidian Canvas 文件。
- `defuddle`：从网页提取干净 Markdown，适合把网页资料转入知识库。
- `obsidian-cli`：通过 Obsidian CLI 操作 vault。

说明：安装后需要重启 Codex，新的 skills 才会在之后的对话中被自动识别。

## 值得参考的知识库项目

### kepano/obsidian-skills

用途：让 AI agent 更懂 Obsidian 的 Markdown、Canvas、Bases 和网页清洗。

适合本知识库的用法：

- 让 Codex 更规范地写 Obsidian 笔记。
- 把网页整理成干净 Markdown。
- 后续生成 `.canvas` 学习地图。

### Ar9av/obsidian-wiki

链接：[Ar9av/obsidian-wiki](https://github.com/Ar9av/obsidian-wiki)

用途：受 Karpathy 的 LLM Wiki 模式启发，让 AI agent 构建和维护 Obsidian wiki。

适合本知识库的用法：

- 参考它的 agent + wiki 维护思路。
- 后续可以对比它的目录、命名、自动化方式。
- 不建议现在直接全量采用，先保持当前 vault 简洁。

### Obsidian Hub

链接：[Obsidian Hub](https://github.com/obsidian-community/obsidian-hub)

用途：Obsidian 社区维护的知识库，包含插件、主题、工作流和实践资料。

适合本知识库的用法：

- 查 Obsidian 插件和工作流。
- 参考大型 Markdown vault 的组织方式。

### SoRobby/ObsidianStarterVault

链接：[SoRobby/ObsidianStarterVault](https://github.com/SoRobby/ObsidianStarterVault)

用途：一个 Obsidian starter vault，偏任务、概念、行动组织。

适合本知识库的用法：

- 参考模板和 dashboard 思路。
- 不建议直接套用全部结构，避免知识库变重。

## 当前选择

本知识库先采用轻量路线：

```text
D:\AI-Knowledge
  00-Inbox
  01-Maps
  02-Concepts
  03-Courses
  04-Projects
  05-Papers
  06-Prompts
  07-Reviews
  08-Memory
  Templates
```

原则：先让学习、整理、复盘闭环跑起来，再逐步引入复杂模板、Canvas、Bases 或自动化。
