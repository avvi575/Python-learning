# ============================================================
# CS50P Week 1 — Topic 5: Modulo (%)
# ============================================================
# The modulo operator `%` returns the REMAINDER of division.
#
#   4 % 2 == 0   → 4 divides evenly by 2  → Even
#   3 % 2 == 1   → remainder 1             → Odd
#   7 % 3 == 1   → 7 / 3 = 2 remainder 1
#
# Key parity rule:
#   n % 2 == 0   → Even
#   n % 2 != 0   → Odd
# ============================================================

x = int(input("What's x? "))

if x % 2 == 0:
    print("Even")
else:
    print("Odd")

# -------------------------------------------------------
# Extra: explore modulo with different divisors
# -------------------------------------------------------
print(f"\n{x} % 2 = {x % 2}")
print(f"{x} % 3 = {x % 3}")
print(f"{x} % 10 = {x % 10}   ← last digit of {x}")
