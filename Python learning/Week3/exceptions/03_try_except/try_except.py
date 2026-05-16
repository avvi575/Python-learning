# ============================================================
# CS50P Week 3 — Topic 3: try / except
# ============================================================
# `try` lets you attempt risky code.
# `except` specifies what to do if a particular error occurs.
#
# Structure:
#   try:
#       <risky code>
#   except <ErrorType>:
#       <recovery code>
#
# Best practice: put the FEWEST possible lines inside try —
# only the line(s) that could actually raise the exception.
# ============================================================

# -------------------------------------------------------
# Version 1 — Too much code inside try (not ideal)
# Both lines are inside try, but only the first can fail.
# -------------------------------------------------------
print("=== Version 1: too much inside try ===")
try:
    x = int(input("What's x? "))
    print(f"x is {x}")          # this line can't raise ValueError
except ValueError:
    print("x is not an integer")

# -------------------------------------------------------
# Version 2 — Minimal try (better practice ✅)
# Only the line that could fail is inside try.
# BUT: this has a NameError bug if the except runs!
# (x is undefined if int() failed)
# -------------------------------------------------------
print("\n=== Version 2: minimal try (has NameError bug) ===")
try:
    x = int(input("What's x? "))   # ONLY this can raise ValueError
except ValueError:
    print("x is not an integer")

# print(f"x is {x}")  ← NameError if the except block ran!
# Solution: use else (see Topic 4)

# -------------------------------------------------------
# Catching multiple exception types
# -------------------------------------------------------
print("\n=== Catching multiple exceptions ===")
try:
    value = int(input("Enter a number to divide 100 by: "))
    result = 100 / value
    print(f"100 / {value} = {result}")
except ValueError:
    print("That's not a number.")
except ZeroDivisionError:
    print("Can't divide by zero!")

# -------------------------------------------------------
# Catching any exception (broad catch — use sparingly)
# -------------------------------------------------------
print("\n=== Broad except (use carefully) ===")
try:
    x = int(input("One more number: "))
    print(f"Got: {x}")
except Exception as e:
    # `as e` binds the exception object so you can inspect it
    print(f"Something went wrong: {type(e).__name__}: {e}")
