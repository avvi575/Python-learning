# ============================================================
# CS50P Week 3 — Topic 4: The else Clause
# ============================================================
# try/except/else — the FULL structure:
#
#   try:
#       <risky code>
#   except <Error>:
#       <runs if exception WAS raised>
#   else:
#       <runs ONLY if NO exception was raised>
#
# `else` solves the NameError bug from Topic 3:
# code that depends on `x` goes in `else`, so it only
# runs when `x` was successfully assigned.
# ============================================================

# -------------------------------------------------------
# The problem without else
# -------------------------------------------------------
print("=== Problem: NameError risk ===")
try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")

# print(f"x is {x}")  ← DANGEROUS: NameError if except ran

# -------------------------------------------------------
# The fix: use else ✅
# Code in else only runs when try succeeded — x is guaranteed
# -------------------------------------------------------
print("\n=== Solution: try / except / else ===")
try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")
else:
    # Only reaches here if int(input(...)) succeeded
    print(f"x is {x}")    # x is definitely defined here

# -------------------------------------------------------
# Full flow illustration
# -------------------------------------------------------
print("\n=== Full flow with three outcomes ===")
try:
    numerator   = int(input("Numerator: "))
    denominator = int(input("Denominator: "))
    result = numerator / denominator
except ValueError:
    print("Please enter integers only.")
except ZeroDivisionError:
    print("Denominator cannot be zero.")
else:
    # Only runs if NO exception occurred above
    print(f"Result: {numerator} / {denominator} = {result:.4f}")

# -------------------------------------------------------
# Summary of try / except / else:
#
#   try      → attempt the risky operation
#   except   → handle the failure
#   else     → handle the success (x is safely defined here)
# -------------------------------------------------------
