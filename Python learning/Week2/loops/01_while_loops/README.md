# 01 — `while` Loops

## Structure

```python
while condition:
    body       # runs repeatedly as long as condition is True
```

## How it works

1. Python checks the condition.
2. If `True` → runs the body, then goes back to step 1.
3. If `False` → exits the loop and continues the program.

## The infinite loop trap

```python
i = 3
while i != 0:
    print("meow")   # ❌ i never changes → runs forever
```

**Fix:** always update the variable the condition depends on inside the loop.

## Best practice — start counting from 0

```python
i = 0
while i < 3:
    print("meow")
    i += 1       # i goes 0 → 1 → 2 → condition False → stops
```

## Shorthand operators

| Shorthand | Equivalent |
|-----------|-----------|
| `i += 1`  | `i = i + 1` |
| `i -= 1`  | `i = i - 1` |
| `i *= 2`  | `i = i * 2` |

## Try it

```bash
python3 meow_while.py
```
