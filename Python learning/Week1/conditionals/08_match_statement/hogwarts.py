# ============================================================
# CS50P Week 1 — Topic 8: match Statements  (Python 3.10+)
# ============================================================
# `match` is Python's structural pattern matching.
# It compares one value against multiple `case` patterns
# and runs the first matching block — then stops.
#
# Syntax:
#   match <expression>:
#       case <pattern>:
#           ...
#       case _:           ← wildcard / catch-all (like `else`)
#           ...
# ============================================================

name = input("What's your name? ")

# -------------------------------------------------------
# Version 1 — many elif (repetitive)
# -------------------------------------------------------
print("\n--- Version 1: if / elif chain ---")
if name == "Harry":
    print("Gryffindor")
elif name == "Hermione":
    print("Gryffindor")
elif name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")

# -------------------------------------------------------
# Version 2 — using `or` to collapse repeated branches
# -------------------------------------------------------
print("\n--- Version 2: using or ---")
if name == "Harry" or name == "Hermione" or name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")

# -------------------------------------------------------
# Version 3 — match statement (clearest)
# Each `case` checks whether `name` matches the given string.
# `case _` is the wildcard — catches anything not matched above.
# -------------------------------------------------------
print("\n--- Version 3: match statement ---")
match name:
    case "Harry":
        print("Gryffindor")
    case "Hermione":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")

# -------------------------------------------------------
# Version 4 — match with `|` (OR inside a case)
# The pipe `|` lets one case handle multiple patterns.
# This is the most concise version.
# -------------------------------------------------------
print("\n--- Version 4: match with | ---")
match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
