# ============================================================
# CS50P Week 4 — Topic 4: Slices
# ============================================================
# A slice lets you extract a sub-list (or sub-string) from
# a sequence using the syntax:
#
#   sequence[start : stop : step]
#
#   start  — index to begin (inclusive, default 0)
#   stop   — index to end   (exclusive, default end)
#   step   — how many to skip (default 1)
#
# Slices produce a NEW list — the original is not modified.
# ============================================================

# -------------------------------------------------------
# Basic list slicing
# -------------------------------------------------------
print("=== Basic slicing ===")
items = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Original:       {items}")
print(f"items[2:]       {items[2:]}   ← from index 2 to end")
print(f"items[:5]       {items[:5]}   ← from start to index 4")
print(f"items[2:7]      {items[2:7]}  ← index 2 to 6")
print(f"items[::2]      {items[::2]}  ← every 2nd item (evens)")
print(f"items[1::2]     {items[1::2]} ← every 2nd item (odds)")
print(f"items[::-1]     {items[::-1]} ← reversed")

# -------------------------------------------------------
# The CS50P use case: sys.argv slicing
# sys.argv[0] is always the script name — skip it with [1:]
# -------------------------------------------------------
print("\n=== sys.argv slicing ===")
import sys

# Simulate what sys.argv would look like with multiple names
fake_argv = ["name.py", "David", "Carter", "Rongxin"]
print(f"Full argv:      {fake_argv}")
print(f"argv[1:]:       {fake_argv[1:]}   ← skip the script name")

# Greet each name (skipping argv[0])
print("\nGreeting each name:")
for name in fake_argv[1:]:
    print(f"  hello, my name is {name}")

# -------------------------------------------------------
# Slicing strings (works the same way)
# -------------------------------------------------------
print("\n=== String slicing ===")
text = "Hello, World!"
print(f"text[7:]        '{text[7:]}'")
print(f"text[:5]        '{text[:5]}'")
print(f"text[7:12]      '{text[7:12]}'")
print(f"text[::-1]      '{text[::-1]}'  ← reversed string")

# -------------------------------------------------------
# Slicing does NOT modify the original
# -------------------------------------------------------
print("\n=== Slices are copies ===")
original = [1, 2, 3, 4, 5]
sliced   = original[1:4]
sliced[0] = 99
print(f"original: {original}")   # unchanged
print(f"sliced:   {sliced}")     # only the copy changed
