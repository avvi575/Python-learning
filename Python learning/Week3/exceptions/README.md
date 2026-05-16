# CS50P — Week 3: Exceptions 🐍

> **Course:** [CS50's Introduction to Programming with Python](https://cs50.harvard.edu/python/)
> **Week:** 3 — Exceptions
> **Topics:** `SyntaxError` · `ValueError` · `NameError` · `try` · `except` · `else` · `pass` · `raise`

This repository is a personal study reference for CS50P Week 3. Every concept from the lecture has its own folder with annotated code examples.

---

## 📂 Repository Structure

```
Week3/
└── exceptions/
    ├── 01_syntax_errors/          # SyntaxError — caught before running
    ├── 02_runtime_errors/         # ValueError, NameError — crash at runtime
    ├── 03_try_except/             # try / except — catching errors gracefully
    ├── 04_else_clause/            # try / except / else — run on success
    ├── 05_loops_with_try/         # while True + try/except/else → keep asking
    ├── 06_get_int_function/       # Full reusable get_int(prompt) pattern
    ├── 07_pass/                   # pass — silently ignore an exception
    ├── exercises/                 # Practice problems + solutions
    ├── cheatsheet/                # Quick-reference cheat sheet
    └── README.md
```

---

## 🚀 Quick Start

```bash
python3 03_try_except/try_except.py
python3 06_get_int_function/get_int.py
```

---

## 📚 Topics at a Glance

| # | Topic | Key Concept | File |
|---|-------|-------------|------|
| 1 | Syntax Errors | Caught before running; fix your code | `01_syntax_errors/syntax_demo.py` |
| 2 | Runtime Errors | `ValueError`, `NameError` crash at runtime | `02_runtime_errors/runtime_demo.py` |
| 3 | `try` / `except` | Catch a specific error, handle it gracefully | `03_try_except/try_except.py` |
| 4 | `else` clause | Runs only when NO exception occurred | `04_else_clause/else_demo.py` |
| 5 | Loops + `try` | `while True` + break on success | `05_loops_with_try/loop_try.py` |
| 6 | `get_int` function | Reusable, prompt-taking integer getter | `06_get_int_function/get_int.py` |
| 7 | `pass` | Silently swallow an exception | `07_pass/pass_demo.py` |

---

## 🔑 Quick Reference

```python
try:
    x = int(input("What's x? "))   # risky code here
except ValueError:                  # what to do if it fails
    print("Not an integer!")
else:
    print(f"x is {x}")             # runs only if NO exception
```

---

## 📖 Official Resources

- [Lecture Notes](https://cs50.harvard.edu/python/notes/3/)
- [Lecture Video (YouTube)](https://youtu.be/LW7g1169v7w)
- [Problem Set 3](https://cs50.harvard.edu/python/psets/3/)
- [Python Docs — Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)

---

*Happy coding!* 🎓
