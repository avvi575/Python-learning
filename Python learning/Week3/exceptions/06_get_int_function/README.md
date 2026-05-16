# 06 — The `get_int(prompt)` Pattern

## The final, reusable function

```python
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass
```

## Why this is powerful

The caller never needs to worry about error handling:

```python
age    = get_int("Your age? ")
height = get_int("Height in cm? ")
score  = get_int("Score (0-100)? ")
```

All validation is encapsulated inside `get_int`.

## Progression of versions

```python
# Version 1 — break then return (verbose)
def get_int(prompt):
    while True:
        try:
            x = int(input(prompt))
        except ValueError:
            print("Not an integer")
        else:
            break
    return x

# Version 2 — return in else (no break needed)
def get_int(prompt):
    while True:
        try:
            x = int(input(prompt))
        except ValueError:
            print("Not an integer")
        else:
            return x

# Version 3 — return in try (most concise ✅)
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass
```

## Design principle

> Pass the prompt as a parameter — it makes the function reusable for any question, not just one hardcoded scenario.
