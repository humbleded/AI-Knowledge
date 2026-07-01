---
type: project-note
topic: AI-Agent-Learning L1-Gate CLI Chatbot
status: pass
created: 2026-06-27
updated: 2026-06-27
tags:
  - LLM
  - API
  - SDK
  - DeepSeek
  - AI-Agent-Learning
  - Stage1
---

# L1-Gate API 入门闯关：CLI Chatbot

阶段 1 收尾整合关——把 L1-01~04 的能力拼成一个完整可用的命令行聊天机器人。

## 任务

执行区产物：

- `C:\Users\26823\Desktop\AI-Agent-Learning\code\stage1\l1_gate_cli_chatbot.py`（主程序）
- `C:\Users\26823\Desktop\AI-Agent-Learning\code\stage1\l1_03_chat.py`（新增 `build_prompt`、`create` 加 `timeout=30`）
- `C:\Users\26823\Desktop\AI-Agent-Learning\code\stage1\l1_04_stream_chat.py`（client 加 `timeout=30`）
- 设计稿：`notes/stage1/l1_gate_design_draft.md`；每日记录：`daily/2026-06-27.md`

目标：多轮对话 + 流式可开关 + `exit` 退出 + 错误友好提示 + 历史限长。通过标准：演示 5 轮 + 讲清完整调用链路。

## 验证结果

2026-06-27 复核实跑（流式 5 轮）：

```text
开场：stream on
你：我叫三玖，记住我的名字 → 好的，三玖！我已经记住你的名字了…
你：我刚才说我叫什么？只答名字两个字 → 三玖           ← 多轮记忆命中
你：用一句话夸夸这个名字 → 三玖这个名字简洁又独特…
你：我们前面聊了几轮了？ → 已经聊了 3 轮（记名字→问名字→夸名字）  ← history 完整
你：谢谢你 → 不客气呀，三玖…
你：exit → 退出聊天。（exit code 0）
```

另跑非网络冒烟：空输入「输入不能为空，请重新输入。」；API 出错时 `except` 兜成「调用模型失败：…」不崩、不留堆栈，循环继续。

## 完整调用链路（链路题答案）

```text
input("你：") 读到字符串 question
  → build_prompt(history, question) 拼出 [SYSTEM] + history + [{"role":"user","content":question}]
    → 按 stream_mode 分流：stream_answer(messages)（流式）/ call_messages(messages)（非流式）
      → OpenAI SDK 把 messages/model/stream/timeout 打包成 HTTP 请求，发到 base_url
        → DeepSeek 服务端逐 token 生成，通过 SSE 把一小块块 chunk 流回
          → for chunk: delta.content or "" 拼成完整 answer（逐字打印）
            → 成对 append（user + assistant）进 history
              → trim_history 限长（history[-MAX_TURNS*2:]）→ 下一轮重发，模型才「记得」
```

## 5 个整合坑（单个零件都对、拼起来才暴雷 = 整合关的典型陷阱）

1. **失效的 import**：骨架 `from l1_03_chat import build_prompt` 但 l1_03 当时没有 `build_prompt` → 先去 l1_03 把它写出来，import 才成立。
2. **非流式误用 `call_model`（今日新坑）**：`call_model` 只收**字符串**、内部自拼 system+user 两条。把 `build_prompt` 的**列表**喂给它 → ① content 被塞成一个 list、结构畸形；② 丢了 history、模型记不住。必须改 `call_messages(messages)`（收整盘对话）。
3. **历史限长顺序**：必须「**先成对 append（user+assistant）→ 再 trim**」。先 trim 后 append 会让限长晚一轮生效、history 越界（满 6 条时变 8 条），限长形同失效。
4. **错误兜底返回友好字符串、不返回 None**：`except` 返回 `f"调用模型失败：{exc}"`。返回 None 会让 `print` 出 "None"、且 `content=None` 进 history 后下一轮发给 API 报错（content 必须是字符串）→ 雪崩。
5. **超时保护**：`create`/client 加 `timeout=30`（SDK 参数，不在 DeepSeek API 文档里）。timeout 掐表 + except 兜底一起，才是完整超时保护。

## Gate 4 必答（全过）

1. 历史怎么存：服务端无状态；记忆在客户端 messages 列表，每轮重发 `[SYSTEM]+history+question`，`trim_history` 限长。
2. 防 key 泄露：`.env` 存 key → `load_dotenv()` → `os.environ.get`；`.gitignore` 排除 `.env`（实测 `git check-ignore .env` 命中），`!.env.example` 放行模板。
3. 超时/出错表现：`timeout=30` → `APITimeoutError` → `except` 接住 → 友好字符串 → 循环不崩不断。
4. 最影响稳定性的参数：`temperature`（0 = 贪心/argmax，可复现）。

## 通过理由

- 真实 5 轮跑通，多轮记忆稳（第 2 轮答出名字、第 4 轮数出轮数并复述）。
- 流式/非流式两模式、exit、空输入、错误兜底全部按预期。
- 4 必答 + 完整调用链路口头全过；理解 API 参数 vs SDK 客户端参数、SSE。
- 配套练习 15 题全 PASS（C1 漏 [SYSTEM]、C2 限长后果方向 经订正）。

## 相关概念

- [[../../../02-Concepts/LLM/多轮对话与无状态记忆(Stateless Memory)|多轮对话：接口无状态与客户端记忆]]
- [[../../../02-Concepts/LLM/流式输出(Streaming)|流式输出：stream=True 与逐 chunk 处理]]
- [[../../../02-Concepts/LLM/API 参数与 SDK 客户端参数|API 参数 vs SDK 客户端参数]]
- [[../../../02-Concepts/LLM/调用 chat.completions|调用 LLM：chat.completions 与取回复]]
- [[../../../02-Concepts/LLM/采样参数与成本(Sampling)|采样参数与成本]]

复盘：[[../../../07-Reviews/AI-Agent-Learning/2026-06-27-stage1-l1-gate-pass-review|2026-06-27 阶段 1 L1-Gate 复盘]]
