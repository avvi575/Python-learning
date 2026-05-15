# 06 — Dictionaries (`dict`)

## Creating a dict

```python
students = {
    "Hermione": "Gryffindor",
    "Draco":    "Slytherin",
}
```

## Accessing values

```python
students["Hermione"]   # → "Gryffindor"
```

## Iterating

```python
# Keys only (default)
for name in students:
    print(name)

# Keys + values — two ways:
for name in students:
    print(name, students[name])

for name, house in students.items():   # Pythonic ✅
    print(name, house)
```

## List of dicts — richer records

```python
students = [
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Draco", "house": "Slytherin",  "patronus": None},
]
for s in students:
    print(s["name"], s["house"])
```

## `None` — Python's "no value"

```python
{"patronus": None}   # key exists, but has no meaningful value
```

## Common operations

| Operation | Syntax |
|-----------|--------|
| Add/update | `d["key"] = value` |
| Delete | `del d["key"]` |
| Check existence | `"key" in d` |
| All keys | `d.keys()` |
| All values | `d.values()` |
| Key-value pairs | `d.items()` |

## `list` vs `dict`

| Feature | `list` | `dict` |
|---------|--------|--------|
| Access by | Index (number) | Key (any type) |
| Ordered | Yes | Yes (Python 3.7+) |
| Duplicates | Allowed | Keys must be unique |
