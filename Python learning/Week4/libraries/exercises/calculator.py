# ============================================================
# Exercise 5 — calculator.py (custom module)
# ============================================================

def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return a minus b."""
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def divide(a, b):
    """Return a divided by b. Raises ValueError if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


if __name__ == "__main__":
    print("Calculator module demo:")
    print(f"10 + 3  = {add(10, 3)}")
    print(f"10 - 3  = {subtract(10, 3)}")
    print(f"10 * 3  = {multiply(10, 3)}")
    print(f"10 / 3  = {divide(10, 3):.4f}")
