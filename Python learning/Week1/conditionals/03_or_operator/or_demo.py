# ============================================================
# CS50P Week 1 — Topic 3: The `or` Operator
# ============================================================
# `or` combines two Boolean expressions.
# The combined result is True when AT LEAST ONE side is True.
#
#   True  or True   → True
#   True  or False  → True
#   False or True   → True
#   False or False  → False
# ============================================================

x = int(input("What's x? "))
y = int(input("What's y? "))

# Version 1 — using `or` to check two conditions at once
print("\n--- Version 1: using or ---")
if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal to y")

# Version 2 — cleaner: just use != directly (same logic, simpler)
print("\n--- Version 2: using != (more Pythonic) ---")
if x != y:
    print("x is not equal to y")
else:
    print("x is equal to y")

# Version 3 — flip the condition entirely
print("\n--- Version 3: check equality first ---")
if x == y:
    print("x is equal to y")
else:
    print("x is not equal to y")
