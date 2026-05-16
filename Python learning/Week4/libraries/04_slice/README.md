# 04 — Slices

## Syntax

```
sequence[start : stop : step]
```

| Part | Default | Meaning |
|------|---------|---------|
| `start` | `0` | First index to include |
| `stop` | end | First index to **exclude** |
| `step` | `1` | How many positions to advance |

## Common patterns

```python
items = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

items[1:]      # skip first → [1,2,3,4,5,6,7,8,9]
items[:3]      # first 3   → [0,1,2]
items[2:5]     # index 2–4 → [2,3,4]
items[::2]     # every 2nd → [0,2,4,6,8]
items[::-1]    # reversed  → [9,8,7,6,5,4,3,2,1,0]
```

## The key CS50P use case — `sys.argv[1:]`

```python
import sys

# sys.argv = ["name.py", "David", "Carter", "Rongxin"]
for name in sys.argv[1:]:       # [1:] skips the script name
    print(f"hello, {name}")
```

## Key rule

> Slices create a **new** list — the original is not modified.

Works on lists, strings, tuples — any sequence.
