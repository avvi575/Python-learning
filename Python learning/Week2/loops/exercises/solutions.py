# ============================================================
# CS50P Week 2 — Exercise Solutions
# ============================================================

# -------------------------------------------------------
# Exercise 1: Countdown
# -------------------------------------------------------
def ex1():
    while True:
        n = int(input("Enter a positive integer: "))
        if n > 0:
            break
    while n > 0:
        print(n)
        n -= 1
    print("Go!")


# -------------------------------------------------------
# Exercise 2: Sum of a List
# -------------------------------------------------------
def ex2():
    numbers = [4, 8, 15, 16, 23, 42]
    total = 0
    for n in numbers:
        total += n
    print("Sum:", total)   # 108


# -------------------------------------------------------
# Exercise 3: FizzBuzz
# -------------------------------------------------------
def ex3():
    for i in range(1, 21):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


# -------------------------------------------------------
# Exercise 4: Student Lookup
# -------------------------------------------------------
def ex4():
    roster = {
        "Hermione": "Gryffindor",
        "Harry": "Gryffindor",
        "Ron": "Gryffindor",
        "Draco": "Slytherin",
        "Luna": "Ravenclaw",
        "Cedric": "Hufflepuff",
    }
    while True:
        name = input("Student name (or 'quit'): ").strip().title()
        if name == "Quit":
            break
        if name in roster:
            print(f"{name} is in {roster[name]}")
        else:
            print("Not found")


# -------------------------------------------------------
# Exercise 5: Pyramid
# -------------------------------------------------------
def get_height():
    while True:
        try:
            n = int(input("Height (1-8): "))
            if 1 <= n <= 8:
                return n
        except ValueError:
            pass


def ex5():
    n = get_height()
    for i in range(1, n + 1):
        print("#" * i)


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
