# 04 — Lists

## Creating a list

```python
students = ["Hermione", "Harry", "Ron"]
```

## Indexing (zero-based!)

```python
students[0]    # "Hermione"  — first item
students[-1]   # "Ron"       — last item
students[1:3]  # ["Harry", "Ron"]  — slice
```

## Iterating

```python
for student in students:
    print(student)   # prints each name, one per line
```

## Common list methods

| Method | What it does |
|--------|-------------|
| `list.append(x)` | Add `x` to the end |
| `list.remove(x)` | Remove first occurrence of `x` |
| `list.insert(i, x)` | Insert `x` at position `i` |
| `list.sort()` | Sort in place |
| `list.pop()` | Remove and return last item |
| `len(list)` | Number of items |

## Key rule

> Lists are **zero-indexed**: the first item is at index `0`, not `1`.
