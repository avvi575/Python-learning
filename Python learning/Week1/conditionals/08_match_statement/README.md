# 08 — `match` Statement (Python 3.10+)

## Syntax

```python
match expression:
    case pattern_1:
        ...
    case pattern_2:
        ...
    case _:          # wildcard — matches anything (like else)
        ...
```

Python evaluates each `case` in order and executes the **first** match, then stops (no fall-through).

## OR inside a case — the `|` operator

```python
match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
```

## When to prefer `match` over `if/elif`?

| Situation | Prefer |
|-----------|--------|
| Checking one variable against many exact values | `match` |
| Complex boolean logic (`and`, `or`, ranges) | `if/elif` |
| Fewer than 3 branches | `if/elif` |

## Requirements

`match` was introduced in **Python 3.10**. Check your version with `python3 --version`.
