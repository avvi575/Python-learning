# ============================================================
# CS50P Week 4 — Topic 7: Writing Your Own Library
# ============================================================
# This file IS the library (module).
# It defines reusable functions that other files can import.
#
# A module is simply a .py file. When another file does:
#   import sayings
#   from sayings import hello
#
# Python loads THIS file and makes its functions available.
#
# __name__ == "__main__" trick:
#   When you run THIS file directly → __name__ == "__main__"
#   When another file imports it   → __name__ == "sayings"
#
# This lets you put test/demo code that only runs when
# the file is executed directly, NOT when imported.
# ============================================================


def hello(name):
    """Print a greeting."""
    print(f"hello, {name}")


def goodbye(name):
    """Print a farewell."""
    print(f"goodbye, {name}")


def shout(name):
    """Print an emphatic greeting."""
    print(f"HELLO, {name.upper()}!!!")


# -------------------------------------------------------
# This block ONLY runs when you execute sayings.py directly.
# It does NOT run when another file imports sayings.
# -------------------------------------------------------
if __name__ == "__main__":
    print("Running sayings.py directly — showing demo:")
    hello("World")
    goodbye("World")
    shout("World")
