# 06 — Creating Your Own Bool-Returning Functions

## Why write your own function?

Wrapping logic in a named function makes code:
- **Readable** — `if is_even(x)` reads like English
- **Reusable** — call it from anywhere
- **Testable** — easy to unit-test a single function

## Pattern

```python
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

if is_even(x):   # if True → runs; if False → skipped
    print("Even")
```

## Key point

A function that returns `True` or `False` can be used **directly** as a condition in an `if` statement — you don't need `== True`.

```python
# ✅ correct (idiomatic)
if is_even(x):

# ❌ redundant
if is_even(x) == True:
```
