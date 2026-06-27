---
type: review
topic: AI-Agent-Learning
status: done
created: 2026-06-27
tags:
  - AI-Agent-Learning
  - 复盘
  - Stage2
  - PASS
---

# 2026-06-27 PR2-01 / PR2-02 动手 PASS 复盘（阶段 2 起步）

> 同日先过 L1-Gate（另见 [[2026-06-27-stage1-l1-gate-pass-review]]），解锁阶段 2 动手后，带做补完 PR2-01、PR2-02 两个动手交付，均 PASS。

## 结论

- **PR2-01 → PASS**：通过标准「有对比和结论」达成。
- **PR2-02 → PASS**：通过标准「输出格式稳定」达成。
- 产物见 [[../../04-Projects/LLM/AI-Agent-Learning/pr2-01-02-handson|PR2-01/02 动手项目页]]。

## 做得好

- prompt 设计全程自己来：3 个递进 prompt（偷懒→清晰→few-shot）、单引号包 instruction 避引号冲突、锁 JSON、控长度，PR2-01 的功夫迁移到 PR2-02 很顺。
- **从「背诵」到「实证」**：亲手跑出 ②③ 输出完全一致，把「prompt 不是越长越好 / few-shot 看任务难度」从口头结论变成真实数据。
- 软约束理解到位：模型版摘要正好 3 条、≤20/≤60 全守住，并能说清「软约束=模型凭语感、没有计数器」。

## 暴露的弱点 / 踩的坑

1. **「漏看点名子项」连续两天重现**（最该警惕）：
   - 昨天 L1-Gate：C1 漏开头 `[SYSTEM]`（4 条答成 3 条）。
   - 今天 PR2-02：`simple_summarize` 说「两处都 strip」只做一处（过滤 strip 了、取值没 strip）。
   - → 对策：看到「两处 / 同时 / 分别 / 各」先在脑子里**数满**再交。
2. **f-string/.format 撞 prompt 里 JSON 花括号**（新工程坑）：静默坏 / KeyError；PR2-Gate 邮件处理器还会遇到。已沉淀进概念卡。
3. **prompt 模板忘嵌 `text`**：写完指令就以为完事，忘把变量正文拼进去。
4. **「代码兜底 ≠ 约束模型」误解**：以为校验代码能约束模型；澄清 prompt=事前软请求、代码=事后硬保证。

## 下一步

- 队列下一个：**PR2-03 分类与路由**（资料 DLAI Inferring + ADP Ch2 Routing）。
- 之后：S-03 上下文工程 → PR2-04 JSON/Schema → PR2-Gate 邮件处理器（把阶段 2 技巧串起来）。

## 关联

- [[2026-06-27-stage1-l1-gate-pass-review|同日 L1-Gate PASS 复盘]]
- [[../../04-Projects/LLM/AI-Agent-Learning/pr2-01-02-handson|PR2-01/02 动手项目页]]
- [[../../02-Concepts/LLM/prompt-engineering-basics|Prompt 基础]]、[[../../02-Concepts/LLM/summarizing-and-transforming|摘要与改写]]
