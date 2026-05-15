# 04 — The `and` Operator & Chained Comparisons

## Truth table

| A | B | A `and` B |
|---|---|----------|
| True | True | **True** |
| True | False | **False** |
| False | True | **False** |
| False | False | **False** |

## Python's chained comparisons

Python lets you write range checks the mathematical way:

```python
# Other languages need `and`
if score >= 80 and score < 90:

# Python: chain operators directly
if 80 <= score < 90:
```

Both are equivalent — Python evaluates chained comparisons left-to-right.

## Efficiency insight

When using `elif`, the upper bound is **implied** by the previous condition having failed:

```python
if score >= 90:      # covers 90–100
    print("A")
elif score >= 80:    # only reached when score < 90, so covers 80–89
    print("B")
```

Fewer questions = cleaner, faster, more maintainable code.
