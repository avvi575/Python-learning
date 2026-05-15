# ============================================================
# CS50P Week 1 — Topic 6: Creating Your Own Parity Function
# ============================================================
# Functions can return `bool` values (True / False).
# This lets you write expressive conditions like:
#
#   if is_even(x):    ← reads almost like English!
#
# Returning a bool from a function is a very common pattern.
# ============================================================


def main():
    x = int(input("What's x? "))

    # is_even() returns True or False, so it works directly in an if
    if is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even(n):
    """Return True if n is even, False otherwise."""
    if n % 2 == 0:
        return True
    else:
        return False


main()
