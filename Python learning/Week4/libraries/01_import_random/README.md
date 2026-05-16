# 01 — `import` & the `random` Module

## Two import styles

```python
# Style 1 — import the whole module
import random
random.choice(["heads", "tails"])   # prefix required

# Style 2 — import a specific function
from random import choice
choice(["heads", "tails"])          # no prefix needed
```

`from` is more specific and slightly more efficient — Python loads only what you request.

## Key `random` functions

| Function | What it does | Example |
|----------|-------------|---------|
| `random.choice(seq)` | Pick one item at random | `choice(["a","b","c"])` |
| `random.randint(a, b)` | Random int **inclusive** of both ends | `randint(1, 6)` → 1–6 |
| `random.shuffle(x)` | Shuffle list **in place** (returns `None`) | `shuffle(cards)` |
| `random.random()` | Float in `[0.0, 1.0)` | `0.7342...` |
| `random.uniform(a, b)` | Float in `[a, b]` | `uniform(1, 5)` |

## ⚠️ `shuffle` returns `None`

```python
cards = ["jack", "queen", "king"]
result = random.shuffle(cards)
print(result)   # None — shuffle mutates the list directly
print(cards)    # the shuffled list
```

## Try it

```bash
python3 random_demo.py
```
