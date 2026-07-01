---
aliases:
  - http-and-network-basics
type: concept
topic: Network HTTP
status: usable
created: 2026-06-23
tags:
  - Engineering
  - Network
  - HTTP
  - requests
  - timeout
  - AI-Agent-Learning
---

# 一次 HTTP 请求的全链路与三类错误处理

## 一句话

你写 `requests.get(url, timeout=5)` 一行，背后是「DNS → 端口 → TCP → 请求报文 → 响应报文 → 状态码」一整条链；而出错只分三类（请求没发出去 / 服务器返回错误 / 响应解析失败），每一类有各自的发现手段。

## `requests.get()` 背后的 7 步（全景）

| 步 | 发生了什么 | 关键点 |
| --- | --- | --- |
| ① DNS 解析 | 域名 → IP | `socket.gethostbyname` |
| ② 端口定位 | 找到机器后连它的哪个「门」 | `https` 默认 443、`http` 默认 80 |
| ③ 建 TCP 连接 | 和那台机器握手、拉一条可靠管道 | HTTP 基于 TCP |
| ④ 发请求报文 | 把「请求行 + headers + 空行 + body」发过去 | 客户端**先开口** |
| ⑤ 收响应报文 | 收回「状态行 + headers + 空行 + body」 | 服务器不会主动找你 |
| ⑥ 看状态码 | 2xx？还是 4xx/5xx？ | 要**主动**判断 |
| ⑦ timeout 兜底 | 对方不理你时别死等 | 保护**客户端自己** |

## DNS / IP / 端口（定位三件套）

- **DNS** = 互联网的电话簿，把人记得住的**域名**（`example.com`）翻译成机器用的 **IP**（`93.184.216.34`）。
- **IP** = 定位到「哪一台主机/机器」（哪栋楼）。
- **端口** = 定位到「那台机器上的哪个程序/服务」（楼里的哪个房间）。`https` 默认 443、`http` 默认 80，所以代码里看不到端口——`requests` 按 `https://` 自动填了 443。

## HTTP 报文结构（请求 vs 响应）

两者都是**四段式**：`开头一行 + 一堆 headers +（空行）+ body`，区别只在开头那一行。

| | 第一行叫什么 | 装哪三样 |
| --- | --- | --- |
| 请求 | 起始行（request-line） | 方法 + 请求目标 + HTTP 版本（`GET /x HTTP/1.1`） |
| 响应 | 状态行（status-line） | 协议版本 + 状态码 + 状态文本（`HTTP/1.1 200 OK`） |

报文部件 ↔ `requests` 的 `response` 属性：

| 报文部件 | `requests` 里怎么拿 |
| --- | --- |
| 请求行的方法 | `response.request.method` |
| 状态行的状态码 | `response.status_code` |
| 状态行的状态文本 | `response.reason` |
| headers | `response.headers` |
| 响应体 body | `response.text` |

## 状态码

五大类规律（先记这个，再记具体码）：

```text
1xx 信息   2xx 成功   3xx 重定向   4xx 客户端错   5xx 服务端错
```

| 码 | 含义 | 一句话 |
| --- | --- | --- |
| 200 | OK | 成了，东西在响应体里 |
| 301 | Moved Permanently | 资源永久搬家，新地址在响应头 |
| 400 | Bad Request | 请求**语法**本身就不对 |
| 401 | Unauthorized | **没认证**——「你是谁？」先登录/带 token |
| 403 | Forbidden | 认证了但**没权限**——「知道你是谁，但这不归你看」 |
| 404 | Not Found | 地址能到，但**要的东西不存在** |
| 500 | Internal Server Error | 服务器自己内部出错 |

- **401 vs 403**：401 = 服务器不知道你是谁（没认证）；403 = 知道你是谁但权限不够。
- **4xx vs 5xx 谁的锅**：4xx 是客户端的锅（先查请求：参数 → 认证 → 权限）；5xx 是服务端的锅（改请求没用；第三方 API 则稍等重试 + 看对方状态页）。

## 三类错误 + 三层防护（核心）

| 哪一类问题 | 卡在哪 | 代码里怎么发现 |
| --- | --- | --- |
| **① 请求没发出去** | DNS 失败 / 连不上 / 超时 | `except` 抓异常；`resolve_ip` 返回 `None` |
| **② 服务器返回错误** | 状态码 4xx/5xx | 拿到了 `response`，但要**主动看** `status_code` / `ok` |
| **③ 响应解析失败** | 拿到响应后解读内容时 | `response.json()` 处的 `try/except`（此时 `status_code` 可能是 200，看不出） |

对应**三层防护**（健壮调用外部 API 的标准姿势）：

```text
① 每个调用设 timeout        → 防一个卡死拖垮全部（接第一类·超时）
② 每个调用 try/except 接住   → 接第一类（DNS/连接/超时），不让程序崩
③ 主动 check status_code/ok  → 接第二类（4xx/5xx），try/except 抓不到它
```

## 关键认知：`requests` 只对网络层失败抛异常

- `requests` 的任务 = **把请求发出去 + 把回信收回来**，不是「替你判断响应算不算错误」。
- **4xx/5xx**：请求发了、回信也收到了 → 任务成功 → **不抛异常**，正常返回 `response`；「这个状态码算不算错」的判断权交给**开发者**。
- **连不上 / 超时 / DNS 失败**：连回信都没收到，网络层就失败了 → 任务没法完成 → **才抛异常**被 `except` 抓到。
- 推论：**第二类「服务器返回错误」`except` 永远抓不到**，必须主动看 `status_code`/`ok`。

> 反证：若 `requests` 负责判断对错，它判出 404 是错就该抛异常；但它没抛 → 说明它的任务根本不是判断对错。

## timeout 保护的是「客户端」

- 不设 timeout：对方一直不回，你的 Python **死等**在 `requests.get()` 那行，**后续代码永远跑不到**（卡死的是**客户端自己**，不是服务端）。
- 设了 timeout：超时它主动抛 `requests.Timeout`，你能 `catch` 住去重试/报错/降级，程序不至于僵死。
- agent 要连调多个外部 API 时尤其关键——一个卡死就拖垮整条链。

## `except` 顺序：子类在前、基类兜底

```python
try:
    r = requests.get(url, timeout=5)
except requests.Timeout:           # 具体子类在前
    ...
except requests.ConnectionError:   # 具体子类在前
    ...
except requests.RequestException:  # 基类放最后兜底
    ...
```

`requests.RequestException` 是所有 requests 异常的**基类**。若放最前面，会把 `Timeout`/`ConnectionError` 等子类**全部截胡**，后面的 `except` 永远执行不到。

## 最小代码骨架（B0-02）

```python
import socket, requests
from urllib.parse import urlparse

def resolve_ip(hostname):
    try:
        return socket.gethostbyname(hostname)   # 域名 -> IP
    except socket.gaierror:
        return None                              # 失败给个明确信号

def fetch(url):
    hostname = urlparse(url).hostname
    if not hostname:
        print("非法 URL"); return
    ip = resolve_ip(hostname)
    if not ip:
        print("DNS 解析失败"); return            # 第一类：请求没发出去
    try:
        r = requests.get(url, timeout=5)         # timeout 必设
        if r.ok:
            print("成功")
        else:
            print("服务器返回错误（非 2xx）")     # 第二类：主动判断
        print(r.status_code, dict(list(r.headers.items())[:5]), r.text[:500])
    except requests.Timeout:
        print("请求超时")
    except requests.ConnectionError:
        print("连接失败")
    except requests.RequestException as e:
        print(f"请求异常: {e}")
```

## 易错点

- **`requests` 不对 4xx/5xx 抛异常**（最易忘）——第二类错误得主动看 `status_code`/`ok`，或用 `response.raise_for_status()`。
- **timeout 保护的是客户端**，不是服务端（主语别搞反）。
- **`/` vs `//`**：`/` 是真除法得 `float`（`404/100 = 4.04`），`//` 是整除得 `int`（`404//100 = 4`）。按状态码首位分类要用 `//`，否则非整百状态码（如 404）会因 `4.04 == 4` 为 `False` 而漏判。见 [[../Python/类型转换(Type Conversion)]]。
- **`resolve_ip` 失败返回 `None`** 而非抛异常或返回 `""`：`None` 是明确的「失败」信号，调用方一个 `if not ip:` 就能判，且记得后面 `return` 刹车，别 DNS 失败了还往下发请求。

## 来源

- AI-Agent-Learning B0-02：`code/stage0_5/b0_02_http_probe.py`、`daily/2026-06-23.md`
- MDN HTTP（中文）：概述、消息、标头、响应状态码
- Cloudflare：什么是 DNS

## 相关

- [[../Python/HTTP 请求(requests)|Python HTTP 请求：URL、headers、status code 与 JSON（requests 库用法 · P0-09）]]
- [[调试与错误恢复(Triage)|调试与错误恢复：系统化 triage]]（「按错误类型分流」里的网络错/超时）
- [[../Python/异常·调试·测试(Exceptions)|Python 异常、调试与单元测试]]
- [[../LLM/采样参数与成本(Sampling)|采样参数与成本]]（调 API 的成本/超时意识）
- [[../Python/类型转换(Type Conversion)|Python 类型转换]]（`/` vs `//`）
