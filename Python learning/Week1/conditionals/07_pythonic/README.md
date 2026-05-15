# 07 — Pythonic Style

## What does "Pythonic" mean?

Writing code in the style that experienced Python developers consider clean and idiomatic. It usually means: **fewer lines, clearer intent**.

## Progression: verbose → Pythonic

```python
# Version A — verbose
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

# Version B — ternary expression
def is_even(n):
    return True if n % 2 == 0 else False

# Version C — most Pythonic ✅
def is_even(n):
    return n % 2 == 0   # the comparison itself is already True/False
```

## Ternary (inline) expression

```
result = value_if_true  if  condition  else  value_if_false
```

```python
label  = "Even" if n % 2 == 0 else "Odd"
status = "pass" if score >= 50 else "fail"
```

## Rule of thumb

> If your function does nothing except return `True` or `False` based on a single expression, just `return` that expression directly.
