# 01 — `if` Statements

## What is an `if` statement?

An `if` statement lets your program **make a decision**. Python evaluates the condition (which is always either `True` or `False`) and only executes the indented block if the result is `True`.

```python
if x < y:
    print("x is less than y")   # runs only when x < y is True
```

## Comparison operators

| Operator | Meaning | Example |
|----------|---------|---------|
| `<`  | less than | `3 < 5` → `True` |
| `>`  | greater than | `5 > 3` → `True` |
| `<=` | less than or equal to | `3 <= 3` → `True` |
| `>=` | greater than or equal to | `4 >= 5` → `False` |
| `==` | equal to | `3 == 3` → `True` |
| `!=` | not equal to | `3 != 4` → `True` |

> ⚠️ **Common mistake:** using `=` (assignment) instead of `==` (comparison).  
> `x = 5` stores the value. `x == 5` checks the value.

## Try it

```bash
python3 compare.py
```

Enter two numbers and watch which branch runs (or doesn't).
