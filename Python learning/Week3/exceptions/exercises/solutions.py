# ============================================================
# CS50P Week 3 — Exercise Solutions
# ============================================================


# -------------------------------------------------------
# Shared helper (used by multiple exercises)
# -------------------------------------------------------
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass


# -------------------------------------------------------
# Exercise 1: Safe Float Input
# -------------------------------------------------------
def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def ex1():
    n = get_float("Enter a decimal number: ")
    print(f"You entered: {n}")


# -------------------------------------------------------
# Exercise 2: Positive Integer Only
# -------------------------------------------------------
def get_positive_int(prompt):
    while True:
        try:
            n = int(input(prompt))
        except ValueError:
            print("That's not an integer.")
        else:
            if n > 0:
                return n
            print("Must be greater than 0.")


def ex2():
    n = get_positive_int("Enter a positive integer: ")
    print(f"Got: {n}")


# -------------------------------------------------------
# Exercise 3: Safe Division
# -------------------------------------------------------
def ex3():
    while True:
        a = get_int("Numerator: ")
        b = get_int("Denominator: ")
        try:
            result = a / b
        except ZeroDivisionError:
            print("Denominator cannot be zero. Try again.")
        else:
            print(f"{a} / {b} = {result:.4f}")
            break


# -------------------------------------------------------
# Exercise 4: Safe List Indexing
# -------------------------------------------------------
def ex4():
    fruits = ["apple", "banana", "cherry", "date"]
    print(f"List: {fruits} (indices 0 to {len(fruits)-1})")
    while True:
        try:
            i = int(input("Enter an index: "))
            print(f"fruits[{i}] = {fruits[i]}")
        except ValueError:
            print("Please enter an integer.")
        except IndexError:
            print(f"Index out of range. Choose 0 to {len(fruits)-1}.")
        else:
            break


# -------------------------------------------------------
# Exercise 5: raise your own exception
# -------------------------------------------------------
def get_age(prompt):
    n = get_int(prompt)
    if n < 0 or n > 120:
        raise ValueError(f"Age must be between 0 and 120, got {n}")
    return n


def ex5():
    while True:
        try:
            age = get_age("Your age: ")
        except ValueError as e:
            print(f"Invalid age: {e}")
        else:
            print(f"Age accepted: {age}")
            break


# -------------------------------------------------------
# Run all
# -------------------------------------------------------
if __name__ == "__main__":
    print("=== Exercise 1 ===")
    ex1()
    print("\n=== Exercise 2 ===")
    ex2()
    print("\n=== Exercise 3 ===")
    ex3()
    print("\n=== Exercise 4 ===")
    ex4()
    print("\n=== Exercise 5 ===")
    ex5()
