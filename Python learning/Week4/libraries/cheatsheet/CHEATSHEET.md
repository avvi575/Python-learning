# CS50P Week 4 — Libraries Cheat Sheet

## Import Styles

```python
import random                    # full module → use as random.choice(...)
from random import choice        # specific → use as choice(...) directly
from random import choice, randint  # multiple specific imports
```

---

## `random` Module

```python
import random

random.choice(seq)         # random item from list/string
random.randint(a, b)       # random int, INCLUSIVE of both a and b
random.shuffle(lst)        # shuffle list IN PLACE (returns None!)
random.random()            # float in [0.0, 1.0)
random.uniform(a, b)       # float in [a, b]
random.sample(seq, k)      # k unique random items (no repeats)
```

---

## `statistics` Module

```python
import statistics

statistics.mean(data)      # arithmetic average
statistics.median(data)    # middle value
statistics.mode(data)      # most frequent value
statistics.stdev(data)     # standard deviation (sample)
```

---

## `sys` Module

```python
import sys

sys.argv            # list: ["script.py", "arg1", "arg2", ...]
sys.argv[0]         # always the script name
sys.argv[1]         # first user argument
sys.argv[1:]        # slice: all user args (skip script name)
len(sys.argv)       # number of items in argv

sys.exit("msg")     # print msg to stderr and quit immediately
sys.exit(0)         # quit with success (exit code 0)
sys.exit(1)         # quit with error (exit code 1)
```

---

## Slices

```python
lst[start:stop:step]

lst[1:]      # skip first element
lst[:3]      # first 3 elements
lst[-3:]     # last 3 elements
lst[2:5]     # index 2,3,4
lst[::2]     # every 2nd element
lst[::-1]    # reversed copy
```

Works on lists, strings, and tuples. Creates a **new** copy.

---

## `pip` & PyPI

```bash
pip install <package>        # install
pip install pkg1 pkg2        # install multiple
pip list                     # show installed packages
pip show <package>           # info about a package
pip uninstall <package>      # remove
pip install --upgrade <pkg>  # update
```

---

## `requests` + JSON (API calls)

```python
import requests, json

response = requests.get("https://api.example.com/endpoint")
data = response.json()               # JSON → Python dict/list
print(json.dumps(data, indent=2))    # pretty-print

# Access nested data
for item in data["results"]:
    print(item["trackName"])
```

---

## Writing Your Own Module

```python
# mymodule.py
def greet(name):
    print(f"hello, {name}")

if __name__ == "__main__":
    greet("World")   # only runs when executed directly
```

```python
# main.py
from mymodule import greet
greet("David")
```

---

## `__name__` Explained

| Situation | `__name__` value |
|-----------|-----------------|
| `python3 mymodule.py` (run directly) | `"__main__"` |
| `import mymodule` (imported) | `"mymodule"` |

Use `if __name__ == "__main__":` to protect code that should only run when the file is the entry point.

---

## Common Pitfalls

| Mistake | Fix |
|---------|-----|
| `random.shuffle(lst)` assigned to variable | It returns `None` — use it, then read `lst` |
| `sys.argv[1]` with no arg supplied | Check `len(sys.argv)` first |
| Importing a module not installed | `pip install <module>` first |
| Running `say.py` without `sayings.py` in same folder | Keep custom modules in the same directory |
