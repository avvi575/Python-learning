# ============================================================
# CS50P Week 4 — Exercise Solutions
# ============================================================

import random
import statistics
import sys


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass


# -------------------------------------------------------
# Exercise 1: Coin Flip Simulator
# -------------------------------------------------------
def ex1():
    n = get_int("How many flips? ")
    results = [random.choice(["heads", "tails"]) for _ in range(n)]
    heads = results.count("heads")
    tails = results.count("tails")
    print(f"Heads: {heads} | Tails: {tails}")


# -------------------------------------------------------
# Exercise 2: Command-Line Greeter
# -------------------------------------------------------
def ex2():
    if len(sys.argv) < 2:
        sys.exit("Usage: python3 solutions.py <name> [name ...]")
    for name in sys.argv[1:]:
        print(f"hello, {name}!")


# -------------------------------------------------------
# Exercise 3: Statistics Calculator
# -------------------------------------------------------
def ex3():
    if len(sys.argv) < 2:
        sys.exit("Usage: python3 solutions.py <num1> <num2> ...")
    try:
        nums = [float(x) for x in sys.argv[1:]]
    except ValueError:
        sys.exit("Please provide numbers only.")

    print(f"Count:  {len(nums)}")
    print(f"Sum:    {sum(nums)}")
    print(f"Mean:   {statistics.mean(nums):.2f}")
    print(f"Median: {statistics.median(nums):.2f}")
    if len(nums) > 1:
        print(f"Stdev:  {statistics.stdev(nums):.2f}")


# -------------------------------------------------------
# Exercise 4: List Slicer
# -------------------------------------------------------
def ex4():
    data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    print(f"Original:         {data}")
    print(f"First 3:          {data[:3]}")
    print(f"Last 3:           {data[-3:]}")
    print(f"Every other:      {data[::2]}")
    print(f"Reversed:         {data[::-1]}")
    print(f"Index 3 to 7:     {data[3:8]}")


# -------------------------------------------------------
# Exercise 5: calculator module — defined inline here
# (In real usage, this would be a separate calculator.py file)
# -------------------------------------------------------
def add(a, b):       return a + b
def subtract(a, b):  return a - b
def multiply(a, b):  return a * b
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def ex5():
    a, b = 10, 3
    print(f"{a} + {b} = {add(a, b)}")
    print(f"{a} - {b} = {subtract(a, b)}")
    print(f"{a} * {b} = {multiply(a, b)}")
    print(f"{a} / {b} = {divide(a, b):.4f}")
    try:
        divide(a, 0)
    except ValueError as e:
        print(f"Caught: {e}")


# -------------------------------------------------------
# Run all (exercises 2 & 3 use sys.argv, so skip them here)
# -------------------------------------------------------
if __name__ == "__main__":
    print("=== Exercise 1 ===")
    ex1()
    print("\n=== Exercise 4 ===")
    ex4()
    print("\n=== Exercise 5 ===")
    ex5()
    print("\n(Exercises 2 & 3 require command-line args — run separately)")
