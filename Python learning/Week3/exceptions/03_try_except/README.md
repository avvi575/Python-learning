# 03 — `try` / `except`

## Structure

```python
try:
    x = int(input("What's x? "))   # risky line
except ValueError:
    print("x is not an integer")   # runs if ValueError raised
```

## Best practice: minimize the `try` block

Only put the **specific line(s) that could fail** inside `try`. Everything else stays outside.

```python
# ❌ Too much inside try
try:
    x = int(input("x? "))
    print(f"x is {x}")      # this line can't raise ValueError

# ✅ Minimal try
try:
    x = int(input("x? "))
except ValueError:
    print("Not an integer")
```

## Catching multiple exceptions

```python
try:
    result = 100 / int(input("Divisor: "))
except ValueError:
    print("Not a number")
except ZeroDivisionError:
    print("Can't divide by zero")
```

## Inspect the exception with `as`

```python
except ValueError as e:
    print(f"Error detail: {e}")
```

## What NOT to do

```python
except:          # ← catches everything including KeyboardInterrupt
    pass         #   makes bugs very hard to find
```

Always name the specific exception you expect.
