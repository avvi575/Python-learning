# ============================================================
# CS50P Week 4 — Topic 2: statistics Module
# ============================================================
# Python's built-in `statistics` module provides functions
# for mathematical statistics on numeric data.
#
# No installation needed — just import it.
# ============================================================

import statistics

scores = [100, 90, 85, 70, 95, 60, 88]
print(f"Scores: {scores}")

# -------------------------------------------------------
# statistics.mean(data) — arithmetic average
# -------------------------------------------------------
print("\n=== mean ===")
avg = statistics.mean(scores)
print(f"Mean: {avg}")

# From the lecture — simple two-value example
print(f"Mean of [100, 90]: {statistics.mean([100, 90])}")

# -------------------------------------------------------
# statistics.median(data) — middle value
# -------------------------------------------------------
print("\n=== median ===")
mid = statistics.median(scores)
print(f"Median: {mid}")

# -------------------------------------------------------
# statistics.mode(data) — most common value
# -------------------------------------------------------
print("\n=== mode ===")
grades = ["A", "B", "A", "C", "A", "B"]
most_common = statistics.mode(grades)
print(f"Most common grade: {most_common}")

# -------------------------------------------------------
# statistics.stdev(data) — standard deviation
# -------------------------------------------------------
print("\n=== stdev ===")
spread = statistics.stdev(scores)
print(f"Standard deviation: {spread:.2f}")

# -------------------------------------------------------
# Practical example: compute average from command-line numbers
# (Preview of sys — see Topic 3)
# -------------------------------------------------------
import sys

print("\n=== Practical: average from command-line ===")
print("Usage:  python3 statistics_demo.py 80 90 100")
print(f"sys.argv: {sys.argv}")

if len(sys.argv) > 1:
    try:
        nums = [float(x) for x in sys.argv[1:]]
        print(f"Average: {statistics.mean(nums)}")
    except ValueError:
        print("Please provide numbers only.")
else:
    print("(No numbers provided on command line — run with args to try!)")
