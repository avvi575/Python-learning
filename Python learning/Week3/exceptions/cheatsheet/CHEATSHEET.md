# CS50P Week 3 — Exceptions Cheat Sheet

## Error Types

| Error | Cause | Example |
|-------|-------|---------|
| `SyntaxError` | Bad code syntax — caught before running | `print("hi)` |
| `ValueError` | Right type, wrong value | `int("cat")` |
| `NameError` | Variable used before assignment | `print(x)` (x never set) |
| `ZeroDivisionError` | Division by zero | `10 / 0` |
| `TypeError` | Wrong type for operation | `"hi" + 5` |
| `IndexError` | List index out of range | `items[99]` |
| `KeyError` | Missing dict key | `d["missing"]` |

---

## Full try / except / else Structure

```python
try:
    x = int(input("What's x? "))   # attempt risky code
except ValueError:
    print("Not an integer")         # runs on failure
else:
    print(f"x is {x}")             # runs on success only
```

### When each block runs

| Block | When |
|-------|------|
| `try` | Always (attempted) |
| `except` | Only if exception was raised |
| `else` | Only if NO exception was raised |

---

## Loops + try — Input Validation Pattern

```python
while True:
    try:
        x = int(input("What's x? "))
    except ValueError:
        print("Not an integer. Try again.")
    else:
        break       # only breaks if try succeeded

# x is guaranteed valid here
print(f"x is {x}")
```

---

## The Reusable get_int() Function

```python
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass    # silent retry
```

Usage anywhere:
```python
age   = get_int("Your age? ")
score = get_int("Score? ")
```

---

## pass — Silent No-Op

```python
except ValueError:
    pass    # do nothing, loop continues
```

Use `pass` when re-prompting IS the user feedback.
Use `print(...)` when the user needs to know why they failed.

---

## Catching Multiple Exceptions

```python
try:
    result = int(input("n: ")) / int(input("d: "))
except ValueError:
    print("Enter integers only")
except ZeroDivisionError:
    print("Can't divide by zero")
```

---

## Inspect Exception Details

```python
except ValueError as e:
    print(f"Error: {e}")              # message
    print(f"Type: {type(e).__name__}") # class name
```

---

## raise — Throw Your Own Exception

```python
def get_age(prompt):
    n = get_int(prompt)
    if n < 0 or n > 120:
        raise ValueError(f"Invalid age: {n}")
    return n
```

---

## Common Pitfalls

| Mistake | Fix |
|---------|-----|
| Too much code inside `try` | Only wrap the line that can fail |
| `print(x)` after `except` block | Move it to `else` — x may be undefined |
| Bare `except:` with no error type | Always name the specific exception |
| `SyntaxError` inside `try` | Can't be caught — fix the syntax |
