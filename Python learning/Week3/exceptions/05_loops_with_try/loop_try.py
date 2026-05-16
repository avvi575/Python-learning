# ============================================================
# CS50P Week 3 — Topic 5: Loops + try/except
# ============================================================
# Combining while True with try/except/else is the standard
# Python pattern for "keep asking until you get valid input".
#
# Flow:
#   1. Try to get valid input
#   2. If it fails → except handles it → loop continues
#   3. If it succeeds → else breaks out of the loop
# ============================================================

# -------------------------------------------------------
# Version 1 — while True + try/except/else + break
# -------------------------------------------------------
print("=== Version 1: while True + try/except/else + break ===")
while True:
    try:
        x = int(input("What's x? "))
    except ValueError:
        print("x is not an integer. Try again.")
    else:
        break   # only breaks if try succeeded (no exception)

print(f"x is {x}")

# -------------------------------------------------------
# Version 2 — silent retry (no error message to user)
# Uses pass in except — just loops again quietly
# -------------------------------------------------------
print("\n=== Version 2: silent retry ===")
while True:
    try:
        x = int(input("What's x? "))
    except ValueError:
        pass    # silently ignore, loop again
    else:
        break

print(f"x is {x}")

# -------------------------------------------------------
# Why this pattern works:
#
#   while True  → loops forever by default
#   except      → bad input: error message, no break → loops again
#   else        → good input: break exits the loop
#   after loop  → x is guaranteed to be a valid integer
# -------------------------------------------------------
