# ============================================================
# CS50P Week 4 — Topic 5: Third-Party Packages & pip
# ============================================================
# Python's standard library is powerful, but the real power
# comes from the Python Package Index (PyPI) — hundreds of
# thousands of free, open-source packages.
#
# pip is Python's package manager:
#   pip install <package>    → install
#   pip list                 → see installed packages
#   pip show <package>       → info about a package
#   pip uninstall <package>  → remove
#
# Install before running this file:
#   pip install cowsay
# ============================================================

import sys

# -------------------------------------------------------
# cowsay — a fun package that makes ASCII animals talk
# pip install cowsay
# -------------------------------------------------------
try:
    import cowsay

    if len(sys.argv) == 2:
        name = sys.argv[1]
        print("=== cowsay.cow ===")
        cowsay.cow(f"hello, {name}")

        print("\n=== cowsay.trex ===")
        cowsay.trex(f"hello, {name}")

        print("\n=== cowsay.dragon ===")
        cowsay.dragon(f"ROAR! Hello, {name}!")
    else:
        print("Usage: python3 cowsay_demo.py <name>")
        print("Example: python3 cowsay_demo.py David")

        # Show available characters even without a name arg
        print("\n=== Available cowsay characters ===")
        print(cowsay.char_names)

except ImportError:
    print("cowsay is not installed.")
    print("Run: pip install cowsay")

# -------------------------------------------------------
# How packages work:
#
# 1. pip downloads the package from PyPI (pypi.org)
# 2. Installs it into your Python environment
# 3. You import it just like a standard library module
#
# PyPI has packages for:
#   - Web scraping     (beautifulsoup4, scrapy)
#   - Data science     (numpy, pandas, matplotlib)
#   - Web frameworks   (flask, django, fastapi)
#   - Machine learning (scikit-learn, tensorflow)
#   - APIs / HTTP      (requests, httpx)
#   - Fun stuff        (cowsay, rich, art)
# -------------------------------------------------------
