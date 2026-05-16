# ============================================================
# CS50P Week 3 — Topic 1: Syntax Errors
# ============================================================
# A SyntaxError is caught by Python BEFORE your program runs.
# It means you've written something that Python cannot parse
# — like a missing quote, bracket, or colon.
#
# Python reads your entire file first, and if it spots a
# syntax problem, it refuses to run any of it.
#
# ⚠️  These errors CANNOT be caught with try/except —
#     they must be fixed in your source code.
# ============================================================

# -------------------------------------------------------
# Common Syntax Errors (shown as comments — they would
# prevent the file from running if uncommented)
# -------------------------------------------------------

# Missing closing quote:
# print("hello, world)          ← SyntaxError

# Missing colon after if:
# if x > 0                      ← SyntaxError
#     print("positive")

# Mismatched brackets:
# my_list = [1, 2, 3            ← SyntaxError

# Using = instead of == in a condition:
# if x = 5:                     ← SyntaxError (use ==)

# -------------------------------------------------------
# This file is correct — it runs fine ✅
# -------------------------------------------------------
print("This file has no syntax errors!")
print("Python parsed it successfully before running.")

# -------------------------------------------------------
# How to read a SyntaxError message:
#
#   File "hello.py", line 1
#     print("hello, world)
#                         ^
#   SyntaxError: EOL while scanning string literal
#
#   → EOL = End Of Line. Python hit the end of the line
#     before finding the closing quote.
# -------------------------------------------------------
