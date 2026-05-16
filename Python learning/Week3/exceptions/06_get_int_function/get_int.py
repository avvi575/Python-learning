# ============================================================
# CS50P Week 3 — Topic 6: Creating a Reusable get_int()
# ============================================================
# Abstraction: wrap the validation loop into a function so
# any part of your program can call get_int("prompt") and
# always receive a valid integer back — no error handling needed
# at the call site.
#
# This is one of the most practical patterns in CS50P.
# ============================================================


def main():
    x = get_int("What's x? ")
    print(f"x is {x}")


# -------------------------------------------------------
# Version 1 — break + return x (two-step exit)
# -------------------------------------------------------
def get_int_v1(prompt):
    while True:
        try:
            x = int(input(prompt))
        except ValueError:
            print("Not an integer. Try again.")
        else:
            break       # exit the loop on success
    return x            # return after the loop


# -------------------------------------------------------
# Version 2 — return inside else (cleaner)
# return also exits the loop, so break is not needed
# -------------------------------------------------------
def get_int_v2(prompt):
    while True:
        try:
            x = int(input(prompt))
        except ValueError:
            print("Not an integer. Try again.")
        else:
            return x    # return exits both else AND the loop


# -------------------------------------------------------
# Version 3 — return inside try directly (most concise ✅)
# If int(input(...)) succeeds, return immediately.
# If it raises ValueError, except catches it → loop again.
# -------------------------------------------------------
def get_int(prompt):
    """Prompt user until a valid integer is entered, then return it."""
    while True:
        try:
            return int(input(prompt))   # success → return value
        except ValueError:
            pass                         # failure → loop again silently


# -------------------------------------------------------
# Version 4 — with a custom error message (bonus)
# -------------------------------------------------------
def get_int_verbose(prompt):
    """Like get_int but tells the user what went wrong."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a whole number.")


main()

# -------------------------------------------------------
# Why passing `prompt` as a parameter matters:
#
# ❌ Hardcoded prompt inside the function:
#     def get_int():
#         return int(input("What's x? "))  ← only useful for x
#
# ✅ Prompt as a parameter:
#     def get_int(prompt):
#         return int(input(prompt))        ← reusable anywhere
#
# Usage:
#   age    = get_int("What's your age? ")
#   height = get_int("Height in cm? ")
#   score  = get_int("Enter score: ")
# -------------------------------------------------------
