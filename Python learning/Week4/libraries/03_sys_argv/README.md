# 03 — Command-Line Arguments: `sys.argv` & `sys.exit`

## `sys.argv`

A **list** of strings: everything the user typed on the command line.

```
python3 name.py David Carter
```

| Index | Value |
|-------|-------|
| `sys.argv[0]` | `"name.py"` — always the script name |
| `sys.argv[1]` | `"David"` — first user argument |
| `sys.argv[2]` | `"Carter"` — second user argument |

## Validation patterns

```python
# catch missing argument
try:
    print(sys.argv[1])
except IndexError:
    print("Too few arguments")

# check count with len()
if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print(sys.argv[1])
```

## `sys.exit()` — cleanest approach ✅

```python
import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")    # prints message, exits immediately
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

# Only reaches here when args are valid
print("hello, my name is", sys.argv[1])
```

`sys.exit()` separates error-checking from program logic — code after the guards runs only when input is valid.

## Try it

```bash
python3 name.py              # → Too few arguments
python3 name.py David        # → hello, my name is David
python3 name.py David Carter # → Too many arguments
```
