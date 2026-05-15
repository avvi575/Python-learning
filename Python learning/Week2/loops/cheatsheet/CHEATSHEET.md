# CS50P Week 2 — Loops Cheat Sheet

## `while` Loop

```python
i = 0
while i < 3:
    print("meow")
    i += 1        # ← MUST update or loop runs forever
```

---

## `for` Loop + `range()`

```python
for i in range(3):       # 0, 1, 2
    print(i)

for _ in range(5):       # _ = "I don't use this variable"
    print("hello")

# range() variants
range(n)         # 0 to n-1
range(a, b)      # a to b-1
range(a, b, s)   # a to b-1, step s
range(5, 0, -1)  # 5, 4, 3, 2, 1  (countdown)
```

---

## Loop Control

```python
continue   # skip rest of this iteration → back to top
break      # exit the loop entirely
return     # exit the function (also exits any loop inside)
```

### Input validation pattern
```python
while True:
    n = int(input("Enter positive n: "))
    if n > 0:
        break
```

### In a function (cleanest)
```python
def get_number():
    while True:
        n = int(input("n? "))
        if n > 0:
            return n     # validates AND returns
```

---

## Lists

```python
items = ["a", "b", "c"]

items[0]          # "a"   — first (zero-indexed)
items[-1]         # "c"   — last
len(items)        # 3

for item in items:          # iterate values
    print(item)

for i in range(len(items)): # iterate with index
    print(i, items[i])

for i, item in enumerate(items, start=1):  # Pythonic ✅
    print(i, item)

items.append(x)    # add to end
items.remove(x)    # remove first occurrence
items.insert(i,x)  # insert at position i
```

---

## Dictionaries

```python
d = {"key1": "val1", "key2": "val2"}

d["key1"]          # "val1"
d["key3"] = "val3" # add/update
del d["key1"]      # delete
"key2" in d        # True — check existence

for k in d:             # keys only
for k, v in d.items():  # keys + values ✅
```

### List of dicts
```python
students = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]
for s in students:
    print(s["name"], s["house"])
```

### `None` — no value
```python
{"patronus": None}   # key exists, value is absent
```

---

## Nested Loops (Mario)

```python
for i in range(rows):
    for j in range(cols):
        print("#", end="")   # no newline
    print()                  # end of row
```

### String tricks
```python
print("#" * 4)         # "####"
print("hi\n" * 3, end="")  # three lines
```

---

## Common Pitfalls

| Mistake | Fix |
|---------|-----|
| Forgetting `i += 1` in `while` | Always mutate the condition variable |
| Using `=` instead of `==` in condition | `while i == 0` not `while i = 0` |
| Off-by-one: `range(1, n)` misses `n` | Use `range(1, n+1)` if you need to include `n` |
| Accessing `dict["key"]` that doesn't exist | Use `d.get("key", default)` to avoid KeyError |
