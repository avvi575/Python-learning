# 03 — The `or` Operator

## Truth table

| A | B | A `or` B |
|---|---|---------|
| True | True | **True** |
| True | False | **True** |
| False | True | **True** |
| False | False | **False** |

## Usage

```python
if x < y or x > y:
    print("x is not equal to y")
```

`or` is evaluated **left to right** and short-circuits: if the left side is already `True`, Python skips evaluating the right side entirely.

## Tip: choose the simplest operator

Often, a single operator replaces an `or`:

```python
# Verbose
if x < y or x > y: ...

# Cleaner — same result
if x != y: ...
```

Always prefer the version that asks **one clear question**.
