# CS50P — Week 4: Libraries 🐍

> **Course:** [CS50's Introduction to Programming with Python](https://cs50.harvard.edu/python/)
> **Week:** 4 — Libraries
> **Topics:** `import` · `from` · `random` · `statistics` · `sys` · `sys.argv` · `sys.exit` · `slice` · `pip` · PyPI · APIs · `requests` · `json` · `__name__`

This repository is a personal study reference for CS50P Week 4. Every concept from the lecture has its own folder with annotated code examples.

---

## 📂 Repository Structure

```
Week4/
└── libraries/
    ├── 01_import_random/       # import, from...import, random module
    ├── 02_statistics/          # statistics module, mean, etc.
    ├── 03_sys_argv/            # sys.argv, sys.exit, IndexError
    ├── 04_slice/               # list slicing, sys.argv[1:]
    ├── 05_packages_cowsay/     # pip, PyPI, third-party packages
    ├── 06_apis_requests/       # requests, JSON APIs
    ├── 07_custom_library/      # writing your own module
    ├── exercises/              # Practice problems + solutions
    ├── cheatsheet/             # Quick-reference cheat sheet
    └── README.md
```

---

## 🚀 Quick Start

```bash
# Standard library examples (no install needed)
python3 01_import_random/random_demo.py
python3 02_statistics/statistics_demo.py
python3 03_sys_argv/name.py David

# Install third-party packages first
pip install cowsay requests
python3 05_packages_cowsay/cowsay_demo.py David
python3 06_apis_requests/itunes.py weezer
```

---

## 📚 Topics at a Glance

| # | Topic | Key Concepts | File |
|---|-------|-------------|------|
| 1 | `random` | `import`, `from`, `choice`, `randint`, `shuffle` | `01_import_random/random_demo.py` |
| 2 | `statistics` | `mean`, `median`, `mode` | `02_statistics/statistics_demo.py` |
| 3 | `sys.argv` | command-line args, `sys.exit`, `IndexError` | `03_sys_argv/name.py` |
| 4 | Slices | `list[1:]`, `list[a:b]`, `list[::s]` | `04_slice/slice_demo.py` |
| 5 | Packages | `pip install`, PyPI, `cowsay` | `05_packages_cowsay/cowsay_demo.py` |
| 6 | APIs | `requests.get`, `json.dumps`, JSON parsing | `06_apis_requests/itunes.py` |
| 7 | Custom Library | writing & importing your own module | `07_custom_library/` |

---

## 🔑 Quick Reference

```python
import random                    # full module
from random import choice        # specific function only

random.choice(["heads","tails"]) # random item from list
random.randint(1, 10)            # random int in [1,10]
random.shuffle(my_list)          # shuffle list in place

import sys
sys.argv                         # list of command-line args
sys.argv[0]                      # script name
sys.argv[1]                      # first user-supplied arg
sys.exit("Error message")        # exit program with message

sys.argv[1:]                     # slice: skip first element
```

---

## 📖 Official Resources

- [Lecture Notes](https://cs50.harvard.edu/python/notes/4/)
- [Lecture Video (YouTube)](https://youtu.be/MztLZWibctI)
- [Problem Set 4](https://cs50.harvard.edu/python/psets/4/)
- [Python Docs — random](https://docs.python.org/3/library/random.html)
- [Python Docs — statistics](https://docs.python.org/3/library/statistics.html)
- [Python Docs — sys](https://docs.python.org/3/library/sys.html)
- [PyPI](https://pypi.org/)
- [requests docs](https://docs.python-requests.org/)

---

*Happy coding!* 🎓
