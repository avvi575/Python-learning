# ============================================================
# CS50P Week 3 — Topic 2: Runtime Errors
# ============================================================
# Runtime errors happen WHILE the program is running —
# the syntax was fine, but something unexpected occurred.
#
# Common runtime errors in CS50P Week 3:
#
#   ValueError  — right type, wrong value
#                 e.g. int("cat")  → can't convert "cat" to int
#
#   NameError   — using a variable that was never assigned
#                 e.g. print(x) when x was never set
#
#   ZeroDivisionError — dividing by zero
#
#   TypeError   — wrong type for an operation
#                 e.g. "hello" + 5
# ============================================================

# -------------------------------------------------------
# Demo 1 — ValueError
# Uncomment the lines below to SEE the error, then recomment.
# -------------------------------------------------------
# x = int(input("What's x? "))   # type "cat" → ValueError
# print(f"x is {x}")

print("=== Demo 1: ValueError ===")
print('Trying: int("cat")')
try:
    result = int("cat")
except ValueError as e:
    print(f"Caught ValueError: {e}")

# -------------------------------------------------------
# Demo 2 — NameError
# This is the subtle bug from the CS50P lecture:
# if int(input(...)) raises a ValueError, `x` is NEVER
# assigned — so printing x afterward gives NameError.
# -------------------------------------------------------
print("\n=== Demo 2: NameError ===")
print("Trying to use a variable that was never assigned:")
try:
    print(undefined_variable)
except NameError as e:
    print(f"Caught NameError: {e}")

# -------------------------------------------------------
# Demo 3 — ZeroDivisionError
# -------------------------------------------------------
print("\n=== Demo 3: ZeroDivisionError ===")
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Caught ZeroDivisionError: {e}")

# -------------------------------------------------------
# Demo 4 — TypeError
# -------------------------------------------------------
print("\n=== Demo 4: TypeError ===")
try:
    result = "hello" + 5
except TypeError as e:
    print(f"Caught TypeError: {e}")

# -------------------------------------------------------
# Key insight from the lecture:
#
#   x = int(input("What's x? "))   ← if this FAILS,
#   print(f"x is {x}")             ← x was never set → NameError
#
# The assignment `x = ...` only completes if the RIGHT side
# succeeds. If int() raises ValueError, x stays undefined.
# -------------------------------------------------------
