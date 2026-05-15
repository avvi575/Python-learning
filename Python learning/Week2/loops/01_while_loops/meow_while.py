# ============================================================
# CS50P Week 2 — Topic 1: while Loops
# ============================================================
# A `while` loop repeats a block of code as long as its
# condition remains True.
#
# Structure:
#   while <condition>:
#       <body>
#
# ⚠️  If the condition never becomes False → infinite loop!
#     Press Ctrl+C to escape an infinite loop.
# ============================================================

# -------------------------------------------------------
# Version 1 — BROKEN: infinite loop (condition never False)
# -------------------------------------------------------
# i = 3
# while i != 0:
#     print("meow")        # i never changes → runs forever!

# -------------------------------------------------------
# Version 2 — Fixed: decrement i each iteration
# -------------------------------------------------------
print("--- Version 2: count DOWN ---")
i = 3
while i != 0:
    print("meow")
    i = i - 1              # each iteration brings i closer to 0

# -------------------------------------------------------
# Version 3 — Count UP from 1 (more human-readable)
# -------------------------------------------------------
print("\n--- Version 3: count UP from 1 ---")
i = 1
while i <= 3:
    print("meow")
    i = i + 1

# -------------------------------------------------------
# Version 4 — Best practice: start at 0 (programmer style)
# `i += 1` is shorthand for `i = i + 1`
# -------------------------------------------------------
print("\n--- Version 4: start at 0 (Pythonic) ---")
i = 0
while i < 3:
    print("meow")
    i += 1                 # shorthand increment

# -------------------------------------------------------
# Shorthand operators cheat-sheet:
#   i += 1   same as   i = i + 1
#   i -= 1   same as   i = i - 1
#   i *= 2   same as   i = i * 2
#   i //= 2  same as   i = i // 2
# -------------------------------------------------------
