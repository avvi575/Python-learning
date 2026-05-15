# 02 — `for` Loops

## Structure

```python
for variable in sequence:
    body
```

## `range()` — the most common sequence

| Call | Values produced |
|------|----------------|
| `range(5)` | 0, 1, 2, 3, 4 |
| `range(1, 6)` | 1, 2, 3, 4, 5 |
| `range(0, 10, 2)` | 0, 2, 4, 6, 8 |
| `range(5, 0, -1)` | 5, 4, 3, 2, 1 |

## The `_` convention

When the loop variable isn't used in the body, name it `_`:

```python
for _ in range(3):
    print("meow")   # _ just counts — we never use its value
```

## String repetition trick

```python
print("meow\n" * 3, end="")
# Prints:
# meow
# meow
# meow
```

## `while` vs `for` — when to use which

| Situation | Use |
|-----------|-----|
| Known number of iterations | `for` |
| Iterating over a list/string | `for` |
| Loop until a condition changes | `while` |
| Input validation ("keep asking") | `while True` |
