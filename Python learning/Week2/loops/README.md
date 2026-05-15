# CS50P — Week 2: Loops 🐍

> **Course:** [CS50's Introduction to Programming with Python](https://cs50.harvard.edu/python/)
> **Week:** 2 — Loops
> **Topics:** `while` · `for` · `list` · `range` · `continue` · `break` · `len` · `dict` · `None`

This repository is a personal study reference for CS50P Week 2. Every concept from the lecture has its own folder with annotated code examples.

---

## 📂 Repository Structure

```
Week2/
└── loops/
    ├── 01_while_loops/         # while, infinite loops, i += 1
    ├── 02_for_loops/           # for, range(), _ placeholder, string repetition
    ├── 03_user_input_validation/  # while True, continue, break, return
    ├── 04_lists/               # list creation, indexing, iterating
    ├── 05_length/              # len(), range(len(...))
    ├── 06_dictionaries/        # dict, key-value, list of dicts, None
    ├── 07_mario_patterns/      # nested loops, print_column, print_square
    ├── exercises/              # Practice problems + solutions
    ├── cheatsheet/             # Quick-reference cheat sheet
    └── README.md
```

---

## 🚀 Quick Start

```bash
python3 01_while_loops/meow_while.py
python3 02_for_loops/meow_for.py
python3 07_mario_patterns/mario.py
```

---

## 📚 Topics at a Glance

| # | Topic | Key Concepts | File |
|---|-------|-------------|------|
| 1 | `while` Loops | condition, `i += 1`, infinite loop | `01_while_loops/meow_while.py` |
| 2 | `for` Loops | `range()`, `_`, string repetition | `02_for_loops/meow_for.py` |
| 3 | Input Validation | `while True`, `break`, `continue`, `return` | `03_user_input_validation/get_number.py` |
| 4 | Lists | indexing, `for x in list` | `04_lists/hogwarts_list.py` |
| 5 | Length | `len()`, `range(len(...))` | `05_length/length_demo.py` |
| 6 | Dictionaries | `dict`, key-value pairs, `list` of `dict`s, `None` | `06_dictionaries/hogwarts_dict.py` |
| 7 | Mario Patterns | nested loops, rows & columns | `07_mario_patterns/mario.py` |

---

## 🔑 Quick Reference

| Syntax | What it does |
|--------|-------------|
| `while condition:` | Repeat while condition is True |
| `i += 1` | Shorthand for `i = i + 1` |
| `for i in range(n):` | Loop n times (0 to n-1) |
| `for _ in range(n):` | Loop n times, variable unused |
| `for item in list:` | Iterate over every item |
| `break` | Exit the loop immediately |
| `continue` | Skip to next iteration |
| `len(list)` | Number of items in list |
| `dict["key"]` | Access value by key |

---

## 📖 Official Resources

- [Lecture Notes](https://cs50.harvard.edu/python/notes/2/)
- [Lecture Video (YouTube)](https://youtu.be/-7xg8pGcP6w)
- [Problem Set 2](https://cs50.harvard.edu/python/psets/2/)
- [Python Docs — Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
- [Python Docs — Dicts](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)

---

*Happy coding!* 🎓
