# 02 — Control Flow: `elif` and `else`

## The problem with multiple `if`s

When you write three separate `if` blocks, Python evaluates **all three every time**, even when the first one is already `True`. That's inefficient and can produce unexpected output.

## The `elif` / `else` chain

```
if <first condition>:
    ...
elif <second condition>:
    ...
else:
    ...          ← runs only when ALL above conditions were False
```

Python works **top-to-bottom**, stopping as soon as one branch is taken. This is called **short-circuit control flow**.

## Rule of thumb

> Use `else` when you can logically guarantee the remaining case without checking — it's both faster and clearer.

## Try it

```bash
python3 compare_flow.py
```

All three versions run for the same input so you can compare their behaviour side-by-side.
