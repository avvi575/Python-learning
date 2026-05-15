# ============================================================
# CS50P Week 2 — Topic 2: for Loops
# ============================================================
# A `for` loop iterates over a sequence of values — a list,
# a range, a string, etc.
#
# Structure:
#   for variable in sequence:
#       body
#
# Key tool: range(n)  →  produces 0, 1, 2, ..., n-1
# ============================================================

# -------------------------------------------------------
# Version 1 — iterate over an explicit list
# -------------------------------------------------------
print("--- Version 1: explicit list ---")
for i in [0, 1, 2]:
    print("meow")

# -------------------------------------------------------
# Version 2 — use range() instead of a hardcoded list
# range(3) generates [0, 1, 2] on the fly
# -------------------------------------------------------
print("\n--- Version 2: range(n) ---")
for i in range(3):
    print("meow")

# -------------------------------------------------------
# Version 3 — use _ when the loop variable isn't needed
# Convention: _ signals "I don't use this value"
# -------------------------------------------------------
print("\n--- Version 3: _ placeholder ---")
for _ in range(3):
    print("meow")

# -------------------------------------------------------
# Version 4 — string repetition (most concise)
# "meow\n" * 3  produces "meow\nmeow\nmeow\n"
# end=""  suppresses the extra newline print() adds
# -------------------------------------------------------
print("\n--- Version 4: string repetition ---")
print("meow\n" * 3, end="")

# -------------------------------------------------------
# range() variants:
#   range(n)        → 0, 1, ..., n-1
#   range(a, b)     → a, a+1, ..., b-1
#   range(a, b, s)  → a, a+s, a+2s, ... (step s)
# -------------------------------------------------------
print("\n--- range() variants ---")
print("range(5)      :", list(range(5)))
print("range(1, 6)   :", list(range(1, 6)))
print("range(0,10,2) :", list(range(0, 10, 2)))   # even numbers
print("range(5,0,-1) :", list(range(5, 0, -1)))   # countdown
