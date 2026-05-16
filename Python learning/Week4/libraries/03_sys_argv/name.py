# ============================================================
# CS50P Week 4 — Topic 3: Command-Line Arguments with sys
# ============================================================
# sys.argv is a LIST of everything the user typed on the
# command line when running the script.
#
#   python3 name.py David Carter
#           ↑        ↑     ↑
#   argv[0]="name.py"  argv[1]="David"  argv[2]="Carter"
#
# argv[0] is ALWAYS the script name.
# User-supplied arguments start at argv[1].
#
# sys.exit(msg) — prints msg to stderr and exits immediately.
# ============================================================

import sys

# -------------------------------------------------------
# Version 1 — No validation (crashes if arg missing)
# -------------------------------------------------------
# print("hello, my name is", sys.argv[1])   # IndexError if no arg!

# -------------------------------------------------------
# Version 2 — Catch IndexError with try/except
# -------------------------------------------------------
print("=== Version 2: try/except IndexError ===")
try:
    print("hello, my name is", sys.argv[1])
except IndexError:
    print("Too few arguments")

# -------------------------------------------------------
# Version 3 — Validate with len() + if/elif
# -------------------------------------------------------
print("\n=== Version 3: len() checks ===")
if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("hello, my name is", sys.argv[1])

# -------------------------------------------------------
# Version 4 — sys.exit() separates validation from logic ✅
# sys.exit() stops the program immediately with a message.
# Code after the if-block only runs when args are valid.
# -------------------------------------------------------
print("\n=== Version 4: sys.exit() (cleanest) ===")
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

print("hello, my name is", sys.argv[1])

# -------------------------------------------------------
# Inspect sys.argv
# -------------------------------------------------------
print(f"\nsys.argv contents: {sys.argv}")
print(f"Script name:       {sys.argv[0]}")
if len(sys.argv) > 1:
    print(f"First user arg:    {sys.argv[1]}")

# -------------------------------------------------------
# Run this script as:
#   python3 name.py               → "Too few arguments"
#   python3 name.py David         → "hello, my name is David"
#   python3 name.py David Carter  → "Too many arguments"
# -------------------------------------------------------
