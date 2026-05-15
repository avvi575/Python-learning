# ============================================================
# CS50P Week 2 — Topic 3: User Input Validation
# ============================================================
# A very common Python pattern: keep asking the user for input
# until they give you something valid.
#
# Key keywords introduced here:
#   continue  →  skip the rest of this iteration, go back to top
#   break     →  exit the loop immediately
#   return    →  exit a function and send a value back
# ============================================================


# -------------------------------------------------------
# Version 1 — while True + continue + break
# -------------------------------------------------------
def demo_v1():
    """Keep prompting until user gives a non-negative number."""
    while True:
        n = int(input("What's n? "))
        if n < 0:
            continue    # bad input → jump back to top of loop
        else:
            break       # good input → exit the loop

    for _ in range(n):
        print("meow")


# -------------------------------------------------------
# Version 2 — simpler: just break on the good condition
# (continue is redundant here — the else only runs when bad)
# -------------------------------------------------------
def demo_v2():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break       # only break when input is valid

    for _ in range(n):
        print("meow")


# -------------------------------------------------------
# Version 3 — best: factor into functions (most readable)
# get_number() uses `return` which also exits the while loop!
# -------------------------------------------------------
def main():
    meow(get_number())


def get_number():
    """Prompt until a positive integer is given, then return it."""
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n    # return exits the function AND the loop


def meow(n):
    for _ in range(n):
        print("meow")


main()

# -------------------------------------------------------
# Summary of loop control keywords:
#
#   continue  →  skip to the NEXT iteration
#   break     →  EXIT the loop entirely
#   return    →  exit the FUNCTION (also exits any loop inside it)
# -------------------------------------------------------
