---
type: concept
topic: Python
status: seed
created: 2026-05-28
tags:
  - Python
  - 编程基础
---

# Python f-string

f-string 用来把变量方便地放进字符串里。

```python
age = 20
print(f"年龄：{age}")
```

## 解决什么问题

f-string 比字符串拼接更清楚，也能避免字符串和数字直接拼接时报错。

对比：

```python
print("年龄：" + str(age))
print(f"年龄：{age}")
```

第二种更简洁，也更适合输出学习档案、日志、提示信息。

## 相关

- [[python-variables]]
- [[python-basic-data-types]]

