---
type: project
topic: LLM
status: done
created: 2026-06-27
source:
  - AI-Agent-Learning PR2-01 / PR2-02
tags:
  - LLM
  - prompt
  - 摘要
  - 结构化输出
  - AI-Agent-Learning
  - Stage2
---

# PR2-01 / PR2-02 动手：prompt 对比 + 摘要器

> 阶段 2 前两个动手交付，2026-06-27（L1-Gate 通关同日）补完，均 PASS。
> 概念早已学完（见 [[../../../02-Concepts/LLM/提示工程基础(Prompt Engineering)]]、[[../../../02-Concepts/LLM/摘要与改写(Summarize & Transform)]]），本页记录**动手代码与真跑结果**。

## PR2-01：同一任务 3 个递进 prompt 对比

- 产物：`code/stage2/pr2_01_prompt_cases.md`（对比文档）+ `code/stage2/pr2_01_run_cases.py`（驱动脚本，复用 stage1 `call_model`，对每段输出自动 `json.loads`）。
- 任务：一段「李雷自我介绍」→ 抽 `姓名/年龄/公司/城市/职位/邮箱` 成 JSON。
- 三档 prompt + 真实输出：

| prompt | 做法 | 真实输出 | `json.loads` |
|---|---|---|---|
| ① 偷懒 | zero-shot、不点字段、不要格式 | Markdown 列表+开场白；多抽「编程语言」、城市→「所在地」、值「28岁」带单位、key 中文 | ✗ 失败 |
| ② 清晰 | 角色+`"""`分隔符+点名 6 字段+空 JSON 模板+前后不带文字 | `{"name":"李雷","age":"28",...}` 纯 JSON | ✓ |
| ③ few-shot | ② + 一组填好的张三样例 | 与 ② **完全一致** | ✓ |

- 结论：清晰具体消除模型自由发挥空间；few-shot 在规整任务上**零增益**、纯多花 token → **prompt 不是越长越好、few-shot 看任务难度**。

## PR2-02：长文 → 3 要点 + 1 摘要

- 产物：`code/stage2/pr2_02_summarizer.py`。
  - `simple_summarize(text)`：机械基线，`[s.strip() for s in text.strip().split('。') if s.strip()][:3]`，不用模型。
  - `llm_summarize(text)`：模型版，`instruction`（单引号包，避 `"""`/JSON 双引号冲突）+ `'\n"""\n' + text + '\n"""'` 拼接 → `call_model`。
  - `main`：两版对比 + `json.loads` + 数条数 + 量长度的兜底检查。
- 真跑（远程办公长文）：

| | 机械版 | 模型版 |
|---|---|---|
| 要点 | 整句照搬、啰嗦 | 提炼 10-12 字 |
| 覆盖 | 漏后 2 段 | 覆盖全文 + 平衡点 |
| 格式 | 不能 loads | loads OK、正好 3 条、≤20/≤60 |

- 结论：机械摘要=照搬会漏，模型版才是真摘要 + 可控格式；软约束这次全守住，但仍需代码兜底。

## 踩的坑（动手过程）

1. **f-string/.format 撞 prompt 里 JSON 花括号**：静默把 JSON 示例求值成 dict / KeyError → 改字符串拼接。详见 [[../../../02-Concepts/LLM/提示工程基础(Prompt Engineering)]] 工程坑。
2. **`simple_summarize` 漏「取值也 strip」**：`if s.strip()` 过滤了，但取值仍 `s`，换行没洗掉 → 「漏看点名子项」弱点重现。
3. **prompt 模板忘把 `text` 嵌进去**：只写固定指令，`"""` 里是空的。
4. **「代码兜底 ≠ 约束模型」**：校验跑在返回之后，只能事后把关+补救，不能反向约束 → 详见 [[../../../02-Concepts/LLM/摘要与改写(Summarize & Transform)]]。

## 运行

```text
.venv/Scripts/python.exe code/stage2/pr2_01_run_cases.py
.venv/Scripts/python.exe code/stage2/pr2_02_summarizer.py
```

## 关联

- [[../../../02-Concepts/LLM/提示工程基础(Prompt Engineering)|Prompt 基础]]
- [[../../../02-Concepts/LLM/摘要与改写(Summarize & Transform)|摘要与改写]]
- [[../../../07-Reviews/AI-Agent-Learning/2026-06-27-pr2-01-02-handson-review|本次 PASS 复盘]]

## 来源

- AI-Agent-Learning PR2-01 / PR2-02 动手；`daily/2026-06-27.md` 补记小节。
