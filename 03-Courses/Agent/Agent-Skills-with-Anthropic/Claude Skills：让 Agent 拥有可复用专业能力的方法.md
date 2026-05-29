---
type: course-note
topic: Agent Skills with Anthropic
status: seed
created: 2026-05-28
tags:
  - AI-Agent
  - Claude
  - Skills
  - MCP
  - Claude-Code
aliases:
  - Claude Skills 中文手册整理
  - Agent Skills with Anthropic
source:
  - https://agentskillsdev.com/
  - https://www.deeplearning.ai/short-courses/agent-skills-with-anthropic/
  - https://claude.com/docs/skills/overview
---

# Claude Skills：让 Agent 拥有可复用专业能力的方法

> [!summary]
> Claude Skills 是一种把“可复用工作流程、专业知识、脚本、模板和参考资料”打包给 Agent 使用的方法。它的价值不是多写一段提示词，而是把某类任务沉淀成一个可迁移、可维护、可按需加载的能力包。

## 资料来源

- 中文整理：[Agent Skills Dev 中文手册](https://agentskillsdev.com/)
- 官方课程：[DeepLearning.AI - Agent Skills with Anthropic](https://www.deeplearning.ai/short-courses/agent-skills-with-anthropic/)
- 官方文档：[Claude Skills overview](https://claude.com/docs/skills/overview)

## 一句话理解

Claude Skills 可以理解成 Agent 的“专业能力插件包”：

- 普通 Prompt：临时告诉 Agent 怎么做。
- Claude Skill：把“怎么做”沉淀成固定目录、说明文档、脚本、模板和资料。
- MCP：让 Agent 连接外部工具、服务或数据源。
- Subagent：让某个独立 Agent 承担专门任务。

如果一个任务会反复出现，并且有稳定流程，就适合做成 Skill。

## Skill 的基本结构

一个 Skill 通常是一个文件夹，核心入口是 `SKILL.md`：

```text
my-skill/
  SKILL.md
  scripts/
  references/
  assets/
```

- `SKILL.md`：告诉 Agent 什么时候使用这个 Skill、任务流程是什么、有哪些约束。
- `scripts/`：放可执行脚本，适合重复、确定性强、容易出错的步骤。
- `references/`：放长文档、规范、案例、API 说明，按需加载。
- `assets/`：放模板、图片、样例文件等素材。

## 渐进式披露

Claude Skills 的关键机制是“渐进式披露”：

1. Agent 先看到 Skill 的名称和简短描述。
2. 命中任务时，再读取 `SKILL.md`。
3. 只有需要时，才继续读取 `references/`、`scripts/`、`assets/`。

这样做的好处是节省上下文窗口：不用一开始把所有资料塞给模型，而是在任务推进时逐步取用。

## Skills、Tools、MCP、Subagents 的区别

| 类型 | 解决的问题 | 更适合什么时候用 |
|---|---|---|
| Skill | 复用专业流程和知识 | 任务步骤稳定、需要领域规范、会反复使用 |
| Tool | 执行一个具体动作 | 查询、计算、读写文件、调用接口 |
| MCP | 连接外部系统和数据源 | 需要数据库、邮件、GitHub、浏览器、私有服务等能力 |
| Subagent | 分离任务上下文和职责 | 需要研究、审查、实现、测试等角色分工 |

> [!tip]
> 可以把 Skill 看成“做事的方法”，Tool/MCP 看成“能调用的手”，Subagent 看成“分工的同事”。

## 什么时候值得做成 Skill

适合：

- 你已经重复做过 3 次以上的任务。
- 任务有固定步骤、格式、检查标准。
- 需要引用一组长期维护的资料。
- 输出质量依赖某些领域经验或隐性规则。
- 希望 Agent 每次都按同一套流程完成。

不适合：

- 只是一次性的简单问题。
- 任务规则还没稳定。
- 一句话 Prompt 就能说清楚。
- 主要价值是调用某个外部 API，此时更像 Tool 或 MCP。

## 可沉淀的个人 Skill 方向

结合我的学习路径，可以优先整理这些 Skill：

1. `ai-agent-learning-review`
   - 用来检查每日学习任务、代码、问答和 PASS/RETRY。

2. `mcp-project-review`
   - 用来判断一个项目是不是 MCP Server、Client、Host 或 Tool。

3. `dotnet-vue-fullstack-debug`
   - 用来检查 `.NET WebAPI + Vue` 登录、接口、跨域、端口和运行状态。

4. `obsidian-knowledge-note`
   - 用来把网页、课程、源码阅读整理成知识库卡片。

5. `code-review-with-tests`
   - 用来做代码审查、定位风险、补最小测试、给出验证结果。

## 我的 Skill 设计模板

```markdown
---
name: skill-name
description: 什么时候使用这个 Skill。要具体到任务触发条件。
---

# Skill Name

## 目标

这个 Skill 要稳定完成什么结果。

## 适用场景

- 场景 1
- 场景 2

## 工作流程

1. 先读取哪些文件或资料。
2. 再执行哪些检查或动作。
3. 最后输出什么格式。

## 输出标准

- 必须包含什么。
- 不应该包含什么。
- 如何判断完成。

## 常见错误

- 错误 1：如何避免。
- 错误 2：如何避免。

## 可选资源

- `references/xxx.md`
- `scripts/xxx.py`
```

## 学习顺序

建议按这个顺序学习，而不是从所有细节开始：

1. 先理解 Skill 是什么，以及它和 Prompt 的区别。
2. 再理解 `SKILL.md` 和文件夹结构。
3. 接着理解渐进式披露，明白为什么不要把所有内容写进一个大文件。
4. 然后比较 Skills、Tools、MCP、Subagents。
5. 最后自己做一个小 Skill，比如“把课程网页整理成知识库笔记”。

## 相关笔记

- [[../../../01-Maps/AI 知识库总地图]]
- [[../../../06-Prompts/整理笔记提示词]]
- [[../../../08-Memory/知识库长期记忆规则]]

## 可执行行动

- [ ] 阅读中文手册 L0-L3，重点理解概念和区别。
- [ ] 阅读 L5，整理“创建自定义 Skill”的步骤。
- [ ] 阅读 L7，整理 Claude Code 中 Skills 的使用方式。
- [ ] 写一个自己的 `obsidian-knowledge-note` Skill 草稿。
- [ ] 把这个 Skill 用在 3 篇网页整理任务上，观察是否稳定。

## 我的判断

Claude Skills 值得放进知识库，不只是因为它是一个新功能，而是因为它代表一种重要的 Agent 工程方法：

> 把一次性的提示词，升级成可复用、可维护、可组合的工作流资产。

这和 MCP、Subagents、Context Engineering 放在一起，能形成一条完整主线：让 Agent 不只是“会聊天”，而是能在具体环境里按稳定流程完成工作。
