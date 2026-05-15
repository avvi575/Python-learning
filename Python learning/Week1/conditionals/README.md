# CS50P — Week 1: Conditionals 🐍

> **Course:** [CS50's Introduction to Programming with Python](https://cs50.harvard.edu/python/)
> **Week:** 1 — Conditionals
> **Topics:** `if` · `elif` · `else` · `or` · `and` · `bool` · `match`

This repository is a personal study reference for CS50P Week 1. Every concept from the lecture has its own folder with annotated code examples, so you can quickly revisit and run each idea independently.

---

## 📂 Repository Structure

```
cs50p-week1-conditionals/
│
├── 01_if_statements/          # Basic if, comparison operators
├── 02_control_flow/           # if → elif → else chains
├── 03_or_operator/            # Combining conditions with or
├── 04_and_operator/           # Combining conditions with and, chained comparisons
├── 05_modulo/                 # % operator and parity
├── 06_custom_functions/       # Building your own bool-returning functions
├── 07_pythonic/               # Ternary expressions, idiomatic Python
├── 08_match_statement/        # match / case (Python 3.10+)
│
├── exercises/                 # Practice problems with solutions
├── cheatsheet/                # Quick-reference cheat sheet
└── README.md
```

---

## 🚀 Quick Start

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/cs50p-week1-conditionals.git
cd cs50p-week1-conditionals

# Run any example — Python 3.10+ recommended (needed for match)
python3 01_if_statements/compare.py
```

---

## 📚 Topics at a Glance

| # | Topic | Key Concept | File |
|---|-------|-------------|------|
| 1 | `if` Statements | `>`, `<`, `==`, `!=`, `>=`, `<=` | `01_if_statements/compare.py` |
| 2 | Control Flow | `if` → `elif` → `else` | `02_control_flow/compare_flow.py` |
| 3 | `or` Operator | Combining two conditions | `03_or_operator/or_demo.py` |
| 4 | `and` + Chained | `and`, `60 <= score < 70` | `04_and_operator/grade.py` |
| 5 | Modulo | `%` for even/odd | `05_modulo/parity.py` |
| 6 | Custom Functions | `return True / False` | `06_custom_functions/parity_fn.py` |
| 7 | Pythonic Style | `return n % 2 == 0` | `07_pythonic/pythonic_parity.py` |
| 8 | `match` Statement | `case`, `\|`, `case _` | `08_match_statement/hogwarts.py` |

---

## 🔑 Operator Reference

| Operator | Meaning |
|----------|---------|
| `>`  | Greater than |
| `<`  | Less than |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |
| `==` | Equal to (comparison) |
| `!=` | Not equal to |
| `%`  | Modulo (remainder) |
| `or` | True if either condition is True |
| `and`| True only if both conditions are True |

---

## 📖 Official Resources

- [Lecture Notes](https://cs50.harvard.edu/python/notes/1/)
- [Lecture Video (YouTube)](https://youtu.be/_b6NgY_pMdw)
- [Problem Set 1](https://cs50.harvard.edu/python/psets/1/)
- [Python Docs — Control Flow](https://docs.python.org/3/tutorial/controlflow.html)

---

*Happy coding!* 🎓
