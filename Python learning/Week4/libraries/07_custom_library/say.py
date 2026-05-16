# ============================================================
# CS50P Week 4 — Topic 7: Using Your Own Library
# ============================================================
# This file IMPORTS from sayings.py (our custom module).
#
# Both files must be in the same directory for this to work.
#
# Run:
#   python3 say.py David
# ============================================================

import sys
from sayings import goodbye, hello, shout

if len(sys.argv) < 2:
    sys.exit("Usage: python3 say.py <name>")

name = sys.argv[1]

# Call functions from our custom sayings module
hello(name)
goodbye(name)
shout(name)
