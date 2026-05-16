# ============================================================
# CS50P Week 3 — Topic 7: pass
# ============================================================
# `pass` is a no-op — it does absolutely nothing.
# It's used as a placeholder when Python requires a statement
# but you don't want to do anything.
#
# In exception handling: `pass` means "ignore this exception
# and continue" — useful when you want silent retry.
# ============================================================

# -------------------------------------------------------
# pass in exception handling — silent retry
# -------------------------------------------------------
print("=== pass in except: silent retry ===")

def get_int(prompt):
    """Keep prompting until valid int; no error message shown."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass    # ← silently ignore, loop again

x = get_int("What's x? ")
print(f"x is {x}")

# -------------------------------------------------------
# pass as a placeholder in functions / classes
# Python requires a body — pass satisfies that requirement
# -------------------------------------------------------
print("\n=== pass as placeholder ===")

def not_implemented_yet():
    pass    # TODO: fill this in later

class EmptyClass:
    pass    # valid empty class definition

not_implemented_yet()   # runs without error
print("Functions and classes with pass are valid Python.")

# -------------------------------------------------------
# pass vs print in except — which to use?
# -------------------------------------------------------
print("\n=== pass vs print in except ===")

print("With message (verbose):")
for attempt in ["42", "cat", "7"]:
    try:
        n = int(attempt)
        print(f"  '{attempt}' → {n}")
    except ValueError:
        print(f"  '{attempt}' → not an integer (told user)")

print("\nWith pass (silent):")
for attempt in ["42", "cat", "7"]:
    try:
        n = int(attempt)
        print(f"  '{attempt}' → {n}")
    except ValueError:
        pass    # silently skip bad values

# -------------------------------------------------------
# Rule of thumb:
#   Use pass when the user re-prompting IS the feedback.
#   Use a print when the user needs to know WHY they failed.
# -------------------------------------------------------
