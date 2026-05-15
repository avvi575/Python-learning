# CS50P Week 1 — Conditionals Cheat Sheet

## Comparison Operators

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `==` | equal to | `3 == 3` | `True` |
| `!=` | not equal to | `3 != 4` | `True` |
| `<`  | less than | `2 < 5` | `True` |
| `>`  | greater than | `5 > 2` | `True` |
| `<=` | less than or equal | `3 <= 3` | `True` |
| `>=` | greater than or equal | `4 >= 5` | `False` |
| `%`  | modulo (remainder) | `7 % 3` | `1` |

---

## if / elif / else

```python
if condition_1:
    # runs when condition_1 is True
elif condition_2:
    # runs when condition_1 False AND condition_2 True
else:
    # runs when ALL above conditions are False
```

**Rules:**
- Only ONE branch runs — the first True one.
- `else` has no condition; it's the fallback.
- You can have as many `elif`s as you need.

---

## Boolean Operators

### `or` — at least one must be True
```python
if x < 0 or x > 100:
    print("Out of range")
```

### `and` — both must be True
```python
if score >= 90 and score <= 100:
    print("Grade: A")
```

### Chained comparisons (Python only)
```python
if 90 <= score <= 100:   # same as above, more readable
    print("Grade: A")
```

---

## Modulo (%)

```python
n % 2 == 0   # even
n % 2 != 0   # odd
n % 10       # last digit of n
```

---

## Bool-returning functions

```python
def is_even(n):
    return n % 2 == 0   # ✅ most Pythonic

if is_even(x):          # use directly — no == True needed
    print("Even")
```

---

## Ternary expression

```python
label = "Even" if n % 2 == 0 else "Odd"
# equivalent to:
# if n % 2 == 0:
#     label = "Even"
# else:
#     label = "Odd"
```

---

## match statement (Python 3.10+)

```python
match variable:
    case value_1:
        ...
    case value_2 | value_3:   # OR with pipe
        ...
    case _:                   # wildcard / catch-all
        ...
```

---

## Common Pitfalls

| Mistake | Fix |
|---------|-----|
| `if x = 5` | `if x == 5` — single `=` is assignment |
| `if is_even(x) == True` | `if is_even(x)` — the bool IS the condition |
| Three separate `if`s for mutually exclusive cases | Use `elif` / `else` to short-circuit |
| Using `match` on Python < 3.10 | Check: `python3 --version` |
