---
type: concept
topic: Python functools.partial
status: usable
created: 2026-06-13
updated: 2026-06-13
tags:
  - Python
  - 函数
  - functools
  - 偏函数
  - AI-Agent-Learning
---

# Python 偏函数 functools.partial 与默认参数

`functools.partial` 把一个已有函数的部分参数“冻结”住，派生出一个**新的可调用对象**。它可以像函数一样调用，和默认参数解决的是类似问题（少传几个参数），但机制完全不同。

```python
from functools import partial

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)   # 不改 power，派生出新的可调用对象
cube   = partial(power, exponent=3)

square(5)   # 25
cube(5)     # 125
```

## 一句话区分

- **默认参数**：定义函数时写进函数签名；如果想改已有函数的默认值，通常需要改源码或重新包装。
- **partial**：运行时、包在外面、不改原函数、同一个原函数可派生任意多个预设版本。

正因为 partial **不去修改原函数**，它只能返回一个**新的可调用对象**来承载“被冻结的参数”这份状态。

## 三个检查点

| 检查点 | 要点 |
|---|---|
| 参数合并规则 | `g(*args)` 实际执行 `f(冻结位置参数, *args, 冻结关键字参数)` |
| partial 的本质 | 新建一个对象，存 `func + 冻结 args + 冻结 kwargs`，**原函数一字未动** |
| 与默认参数的根本区别 | 默认值必须写进**函数源码/签名**（你得拥有它）；partial 不碰源码，在外面包一层 |

## partial 为什么返回新函数

partial 的本质是“包装 + 记住参数”。它需要一个对象来装下原函数和冻结的参数，又不能污染原函数，所以新建一个 `partial` 对象。内部大致是这样工作的（伪代码）：

```python
class partial:
    def __init__(self, func, *args, **kwargs):
        self.func = func          # 记住原函数
        self.args = args          # 记住冻结的位置参数
        self.kwargs = kwargs      # 记住冻结的关键字参数

    def __call__(self, *more_args, **more_kwargs):
        # 调用时把冻结的参数和这次传的参数合并，再转发给原函数
        return self.func(*self.args, *more_args,
                         **{**self.kwargs, **more_kwargs})
```

可以亲手验证“不改原函数 / 新对象 / 存了 func”这三件事：

```python
def greet(greeting, name):
    return f"{greeting}, {name}!"

hi = partial(greet, "Hi")

hi("Tom")          # "Hi, Tom!"
hi is greet        # False —— 是新对象，不是 greet 本身
hi.func is greet   # True  —— 内部记住的 func 就是原来的 greet
```

## 默认参数做不到、partial 能做的场景

`round` 是内置函数，签名 `round(number, ndigits=None)`，**你改不了它的源码**。想让它默认保留 2 位小数：

```python
round2 = partial(round, ndigits=2)
round2(3.14159)   # 3.14
```

要把默认值改成 `ndigits=2`，这个 `2` 必须写进 `round` 的签名里——而 `round` 是 C 写的内置函数，你没有权限改。所以默认参数这条路走不通。不管用 `partial`，还是用 `def round2(number, ndigits=2): return round(number, ndigits)`，做的都是同一件事：**新建一个包装层转发给 `round`，`round` 本身不变**。这正是 partial 必须返回新可调用对象的根本原因。

## 两个踩过的坑

**坑 1：参数合并的方向**——冻结的位置参数排在**最左边**，调用时传入的参数接在**后面**，不是反过来。

```python
def f(a, b, c):
    return (a, b, c)

g = partial(f, 1, c=9)   # 冻结 a=1（第一个位置参数）、c=9

g(2)      # f(1, 2, c=9) → (1, 2, 9)
```

**坑 2：`got multiple values` 报错**——下面这行不是“参数太多”，而是 `c` 被赋值了两次。

```python
g(2, 5)   # 展开成 f(1, 2, 5, c=9)
#           位置参数 a=1, b=2, c=5 已经填满，c=9 又重复赋一次 c
# → TypeError: f() got multiple values for argument 'c'
```

对比另一种报错，分清两者：

```python
f(1, 2, 5, 9)      # 全位置参数、数量超了
# → TypeError: f() takes 3 positional arguments but 4 were given

f(1, 2, 5, c=9)    # 数量没超，是 c 被赋值两次
# → TypeError: f() got multiple values for argument 'c'
```

> 小结论：想冻结靠后的参数，用关键字形式（`exponent=2`）比位置形式（`partial(power, 2)` 冻结的是第一个参数）更安全、更不容易踩坑。

## 关联

- [[python-functions]]
- [[python-f-string]]
- [[python-exceptions-debugging-testing]]
