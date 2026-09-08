---
type: review
topic: Workbench Knowledge Sync Check
status: usable
created: 2026-09-08
source:
  - tools/check_vault.py
tags:
  - 知识库
  - Review
  - AI-Agent-Learning
---

# 工作台同步后的知识库检查

本次新增统一工作台项目页，并更新课程接力、学习原则、路线与相关索引。原始来源为学习执行区已有 daily 和实际代码，不重复复制 raw，不为尚未完成的 R6 单元新增掌握结论。

检查复用 `tools/check_vault.py` 的原有规则；通过内存包装将 `Path.rglob` 的候选限定为 `git ls-files --cached --others --exclude-standard -z` 中的现存文件，排除所有隐藏目录和 Claude 命名路径，未读取或修改这些目录。规则检查内容包括断链、frontmatter、重要页面索引、raw 来源与编译链接、生成文件跟踪；不修改检查器或保存一次性运行脚本。

严格检查通过：229 个 Markdown、2198 个内部链接；0 个断链、0 个缺 frontmatter、0 个重要页面索引遗漏、0 个错误、0 个警告。

可复用的材料已合并到 [[../../04-Projects/Agent/AI-Agent-Learning/workbench-knowledge-agent|工作台项目页]] 与 [[../../03-Courses/Agent/AI-Agent-Learning/README|课程索引]]。本次未进行全库概念内容评审或每周种子页扩写，既有历史记录保留；版本敏感结论由项目页指向本次实际版本和来源。

相关索引：[[README|知识库维护索引]]、[[../../index|全局索引]]、[[../../log|维护日志]]。

检查过程中发现 Git 清单里的 transformer.md 与 Windows 实际文件名 Transformer.md 大小写不同；文件清单按实际解析路径统一后复跑通过，没有为此改写已有概念页。
