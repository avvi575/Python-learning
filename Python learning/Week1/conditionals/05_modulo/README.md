# 05 — Modulo `%`

## What is modulo?

`a % b` gives the **remainder** when `a` is divided by `b`.

| Expression | Result | Why |
|-----------|--------|-----|
| `4 % 2` | `0` | 4 ÷ 2 = 2 exactly |
| `7 % 2` | `1` | 7 ÷ 2 = 3 r **1** |
| `10 % 3` | `1` | 10 ÷ 3 = 3 r **1** |
| `15 % 10` | `5` | gives the last digit |

## Parity (even / odd)

```python
if x % 2 == 0:
    print("Even")   # remainder 0 → divisible by 2
else:
    print("Odd")
```

## Common uses beyond parity

- `n % 10` — last digit of `n`
- `n % 100` — last two digits
- Wrapping around a range: `index % length` (used in loops / circular buffers)
