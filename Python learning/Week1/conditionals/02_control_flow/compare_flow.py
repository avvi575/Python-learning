# ============================================================
# CS50P Week 1 — Topic 2: Control Flow, elif, and else
# ============================================================
# Problem with multiple independent `if` checks:
#   All three are evaluated even when the first one is True.
#   That's wasteful — and can cause logical bugs.
#
# Solution: use `elif` and `else` to short-circuit.
#   - `elif`  = "else if"  — only checked when the previous if/elif was False
#   - `else`  = catch-all  — runs when NO previous condition was True
# ============================================================

x = int(input("What's x? "))
y = int(input("What's y? "))

# ❌  Version 1 — three separate ifs (all three are always evaluated)
print("\n--- Version 1: three separate ifs ---")
if x < y:
    print("x is less than y")
if x > y:
    print("x is greater than y")
if x == y:
    print("x is equal to y")

# ✅  Version 2 — elif chains (stops as soon as one is True)
print("\n--- Version 2: if / elif / elif ---")
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
elif x == y:
    print("x is equal to y")

# ✅✅ Version 3 — else as the logical fallback (most efficient)
# If x is not < y AND not > y, it MUST equal y — no need to check.
print("\n--- Version 3: if / elif / else ---")
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")
