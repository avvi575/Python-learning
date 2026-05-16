# 05 — Loops with `try` / `except`

## The "keep asking" pattern

```python
while True:
    try:
        x = int(input("What's x? "))
    except ValueError:
        print("Not an integer. Try again.")
    else:
        break   # only reached if try succeeded

print(f"x is {x}")   # guaranteed to be a valid int
```

## How control flows

```
loop starts
  ↓
try: attempt int(input(...))
  ├─ ValueError raised? → except runs → loop again ↑
  └─ No exception?      → else runs  → break → exit loop
                                                ↓
                                         print(f"x is {x}")
```

## Key insight

- `except` runs → no `break` → loop repeats
- `else` runs → `break` → loop exits
- After the loop, `x` is **guaranteed** to hold a valid value

## Silent vs. noisy retry

```python
except ValueError:
    print("Not an integer")   # noisy — user sees message

except ValueError:
    pass                       # silent — just re-prompts
```

Which to use depends on UX. Noisy is friendlier; silent is cleaner for some interfaces.
