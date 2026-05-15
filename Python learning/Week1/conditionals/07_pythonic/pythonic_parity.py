# ============================================================
# CS50P Week 1 — Topic 7: Pythonic Coding
# ============================================================
# "Pythonic" = writing code the way experienced Python
# programmers would write it: concise, readable, idiomatic.
#
# Three progressively more Pythonic versions of is_even().
# ============================================================


def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")


# -------------------------------------------------------
# Version A — verbose (works, but not Pythonic)
# -------------------------------------------------------
def is_even_v1(n):
    if n % 2 == 0:
        return True
    else:
        return False


# -------------------------------------------------------
# Version B — ternary expression (inline if/else)
# Reads almost like a sentence: "return True if ... else False"
# -------------------------------------------------------
def is_even_v2(n):
    return True if n % 2 == 0 else False


# -------------------------------------------------------
# Version C — most Pythonic ✅
# `n % 2 == 0` already evaluates to True or False directly.
# No need to wrap it in an if at all!
# -------------------------------------------------------
def is_even(n):
    return n % 2 == 0


main()


# -------------------------------------------------------
# Ternary expression cheat-sheet (inline if/else):
#
#   value_if_true  if  condition  else  value_if_false
#
# Examples:
#   label = "Even" if n % 2 == 0 else "Odd"
#   abs_x = x if x >= 0 else -x
# -------------------------------------------------------
