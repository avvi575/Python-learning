# 02 — Runtime Errors

## What is a runtime error?

A runtime error (also called an **exception**) happens *while your program is running* — after Python successfully parsed the code.

## Common exceptions

| Exception | Cause | Example |
|-----------|-------|---------|
| `ValueError` | Right type, wrong value | `int("cat")` |
| `NameError` | Variable used before assignment | `print(x)` when `x` never set |
| `ZeroDivisionError` | Division by zero | `10 / 0` |
| `TypeError` | Operation on incompatible types | `"hi" + 5` |
| `IndexError` | List index out of range | `items[99]` on a short list |
| `KeyError` | Dict key doesn't exist | `d["missing"]` |

## The subtle NameError trap

```python
try:
    x = int(input("What's x? "))   # if user types "cat"...
except ValueError:
    print("Not a number")

print(f"x is {x}")   # ← NameError! x was never assigned
```

If `int()` raises `ValueError`, the assignment `x = ...` never completes — so `x` doesn't exist when you try to print it.

**Fix:** print `x` inside the `else` block (see Topic 4).
