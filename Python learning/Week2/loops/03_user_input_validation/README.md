# 03 — Input Validation: `while True`, `break`, `continue`

## The pattern

```python
while True:           # loop forever...
    n = int(input("What's n? "))
    if n > 0:
        break         # ...until we get valid input
```

## Loop control keywords

| Keyword | Effect |
|---------|--------|
| `continue` | Skip rest of body → jump to top of loop |
| `break` | Exit the loop immediately |
| `return` | Exit the whole function (also breaks any loop) |

## `continue` vs `break`

```python
# continue — skip bad, keep looping
while True:
    n = int(input("n? "))
    if n < 0:
        continue    # re-prompt
    else:
        break

# Simpler — just break on good input
while True:
    n = int(input("n? "))
    if n > 0:
        break
```

## Best practice — wrap in a function

```python
def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n    # return exits both the function AND the loop
```

`return` inside a loop is clean: it validates *and* returns in one step.
