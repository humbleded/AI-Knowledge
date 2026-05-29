---
type: map
topic: AI-Agent-Learning 关联方案
status: active
created: 2026-05-28
tags:
  - AI-Agent-Learning
  - 知识库
---

# AI-Agent-Learning 关联方案

## 判断

建议关联，但不要把两个目录合并。

`C:\Users\26823\Desktop\AI-Agent-Learning` 是学习执行区，负责每天做任务、写代码、回答 gate 问题、接受 PASS/RETRY 评估。

`D:\AI-Knowledge` 是长期知识库，负责沉淀概念、路线、复盘、提示词和长期记忆。

## 分工

### AI-Agent-Learning

用于保存正在进行的学习材料：

- `tracker\ai-agent-learning-tracker.md`
- `tracker\progress.md`
- `daily\`
- `code\stage0` 到 `code\stage10`
- `notes\stage0` 到 `notes\stage10`
- `repos\`

这里的原则是：可执行、可验证、可判定。

### D:\AI-Knowledge

用于保存长期可复用内容：

- 概念卡片
- 阶段复盘
- 学习地图
- 项目总结
- 长期偏好和重要结论
- 可复用提示词

这里的原则是：可检索、可链接、可复用。

## 推荐连接方式

### 1. 不移动源文件

不要把 `AI-Agent-Learning` 移进 Obsidian vault。它应该继续作为学习工作区和代码工作区。

### 2. 在知识库中建立索引页

在 Obsidian 中保留一个索引，指向学习工作区的重要文件和阶段。

### 3. 每次 PASS 后沉淀

当某个任务或阶段通过后，把结论同步到知识库：

- 新概念 -> `02-Concepts`
- 阶段总结 -> `07-Reviews`
- 项目经验 -> `04-Projects`
- 可复用提示词 -> `06-Prompts`
- 长期规则 -> `08-Memory`

### 4. RETRY 不急着沉淀

如果任务还没通过，只把问题和缺口留在 `AI-Agent-Learning` 的 daily log 或 tracker 里。

通过后再进入长期知识库，避免知识库堆积半成品。

## 推荐同步节奏

```text
每日学习 -> AI-Agent-Learning
每日验证 -> tracker / daily
阶段 PASS -> D:\AI-Knowledge
每周复盘 -> D:\AI-Knowledge\07-Reviews
长期偏好 -> D:\AI-Knowledge\08-Memory
```

## 后续可以自动化

未来可以让 Codex 执行这个流程：

1. 读取 `AI-Agent-Learning\tracker\progress.md`
2. 找到最近通过的任务
3. 读取对应 daily log 和代码
4. 提取概念、问题、经验
5. 写入 `D:\AI-Knowledge`
6. 更新 Obsidian 总地图

## 当前结论

`AI-Agent-Learning` 应该保持为训练场。

`D:\AI-Knowledge` 应该成为长期大脑。

两者通过索引、阶段复盘和 PASS 后沉淀连接，而不是通过文件夹合并连接。
