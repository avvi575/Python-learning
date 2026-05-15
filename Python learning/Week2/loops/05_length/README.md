# 05 — `len()` and Indexed Loops

## `len()`

```python
students = ["Hermione", "Harry", "Ron"]
len(students)   # → 3
len("Hello")    # → 5   (works on strings too)
```

## Looping with index + value

```python
# Using range(len(...))
for i in range(len(students)):
    print(i + 1, students[i])

# Output:
# 1 Hermione
# 2 Harry
# 3 Ron
```

## Pythonic alternative: `enumerate()`

```python
for i, student in enumerate(students, start=1):
    print(i, student)
# Same output — cleaner code
```

## When to use each

| Pattern | Use when |
|---------|---------|
| `for item in list` | You only need the value |
| `for i in range(len(list))` | You need the index to modify the list |
| `for i, item in enumerate(list)` | You need both index and value (preferred) |
