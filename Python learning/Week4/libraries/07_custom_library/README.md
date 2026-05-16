# 07 — Writing Your Own Library (Module)

## What is a module?

Any `.py` file is a module. You can import it into other files to reuse its functions.

## Creating a module — `sayings.py`

```python
def hello(name):
    print(f"hello, {name}")

def goodbye(name):
    print(f"goodbye, {name}")
```

## Importing your module — `say.py`

```python
from sayings import hello, goodbye   # both files in same folder

hello("David")    # → hello, David
goodbye("David")  # → goodbye, David
```

## `__name__` — the self-awareness trick

```python
# In sayings.py:
if __name__ == "__main__":
    # Only runs when you execute sayings.py directly
    # Does NOT run when another file imports sayings
    hello("World")
```

| How the file is used | `__name__` value |
|----------------------|-----------------|
| `python3 sayings.py` (run directly) | `"__main__"` |
| `import sayings` (imported) | `"sayings"` |

This is the standard Python pattern to protect demo/test code from running on import.

## Try it

```bash
python3 sayings.py          # runs the __main__ block
python3 say.py David        # imports sayings, calls its functions
```
