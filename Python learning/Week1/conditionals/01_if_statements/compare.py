# ============================================================
# CS50P Week 1 — Topic 1: if Statements
# ============================================================
# Key idea: Python's comparison operators produce True or False.
# An `if` block only runs when its condition is True.
#
# Comparison operators:
#   >   greater than
#   <   less than
#   >=  greater than or equal to
#   <=  less than or equal to
#   ==  equal to   (NOTE: double equals — not a single =)
#   !=  not equal to
# ============================================================

x = int(input("What's x? "))
y = int(input("What's y? "))

# A single `if` — only prints when x < y is True.
# If the condition is False, the indented block is skipped entirely.
if x < y:
    print("x is less than y")
