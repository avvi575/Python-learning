# ============================================================
# CS50P Week 1 — Topic 4: The `and` Operator & Chained Comparisons
# ============================================================
# `and` requires BOTH conditions to be True.
#
#   True  and True   → True
#   True  and False  → False
#   False and True   → False
#   False and False  → False
#
# Python also supports chained comparisons (unique to Python!):
#   60 <= score < 70   is the same as   score >= 60 and score < 70
# ============================================================

score = int(input("Score (0-100): "))

# -------------------------------------------------------
# Version 1 — explicit `and` (verbose but readable)
# -------------------------------------------------------
print("\n--- Version 1: using `and` ---")
if score >= 90 and score <= 100:
    print("Grade: A")
elif score >= 80 and score < 90:
    print("Grade: B")
elif score >= 70 and score < 80:
    print("Grade: C")
elif score >= 60 and score < 70:
    print("Grade: D")
else:
    print("Grade: F")

# -------------------------------------------------------
# Version 2 — chained comparisons (Pythonic ✅)
# -------------------------------------------------------
print("\n--- Version 2: chained comparisons ---")
if 90 <= score <= 100:
    print("Grade: A")
elif 80 <= score < 90:
    print("Grade: B")
elif 70 <= score < 80:
    print("Grade: C")
elif 60 <= score < 70:
    print("Grade: D")
else:
    print("Grade: F")

# -------------------------------------------------------
# Version 3 — fewest checks (most efficient ✅✅)
# Once we know score >= 90, we don't need an upper bound —
# because elif only runs when the previous condition was False.
# -------------------------------------------------------
print("\n--- Version 3: fewest checks (best) ---")
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
