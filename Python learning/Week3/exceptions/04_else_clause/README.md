# 04 — The `else` Clause

## Full structure

```python
try:
    x = int(input("What's x? "))
except ValueError:
    print("Not an integer")   # runs on failure
else:
    print(f"x is {x}")        # runs on success
```

## Why `else` matters

Without `else`, code after the `try/except` block runs **regardless** of whether the exception occurred — which causes a `NameError` if `x` was never assigned:

```python
try:
    x = int(input("x? "))
except ValueError:
    print("Not an integer")

print(f"x is {x}")   # ❌ NameError if except ran — x undefined!
```

With `else`, the print is **guarded** — it only executes when `x` was successfully set:

```python
try:
    x = int(input("x? "))
except ValueError:
    print("Not an integer")
else:
    print(f"x is {x}")   # ✅ safe — only runs if try succeeded
```

## Mental model

| Block | When it runs |
|-------|-------------|
| `try` | Always (attempted) |
| `except` | Only if the specified exception was raised |
| `else` | Only if NO exception was raised |
