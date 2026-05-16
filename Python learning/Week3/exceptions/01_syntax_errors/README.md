# 01 — Syntax Errors

## What is a SyntaxError?

A `SyntaxError` means Python cannot even *parse* your code. It is detected **before** the program runs — nothing executes at all.

## Common causes

| Mistake | Example |
|---------|---------|
| Missing closing quote | `print("hello)` |
| Missing colon | `if x > 0` |
| Mismatched brackets | `[1, 2, 3` |
| Assignment in condition | `if x = 5:` |

## How to fix

Read the error message carefully — Python tells you the **line number** and points to the problem with `^`. Fix the code, save, and re-run.

## Key rule

> `SyntaxError` cannot be caught with `try/except`. You must fix it in your source code.
