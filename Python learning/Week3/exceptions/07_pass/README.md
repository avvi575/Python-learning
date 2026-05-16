# 07 — `pass`

## What is `pass`?

`pass` is a **no-op** — it does nothing. Python requires a statement wherever a block is expected; `pass` satisfies that requirement without any effect.

## In exception handling — silent retry

```python
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass    # ignore bad input, loop back and ask again
```

The user just gets re-prompted with no explanation.

## As a placeholder

```python
def coming_soon():
    pass   # TODO: implement later

class MyClass:
    pass   # empty class — valid Python
```

## `pass` vs printing a message

| | `pass` | `print(...)` |
|-|--------|-------------|
| User feedback | None — just re-prompts | Explains what went wrong |
| UX feel | Cleaner, minimal | Friendlier, educational |
| Use when | Re-prompting IS the signal | User needs to know why |
