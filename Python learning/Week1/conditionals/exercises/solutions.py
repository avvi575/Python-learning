# ============================================================
# CS50P Week 1 — Exercise Solutions
# ============================================================

# -------------------------------------------------------
# Exercise 1: Positive / Negative / Zero
# -------------------------------------------------------
def ex1():
    n = float(input("Enter a number: "))
    if n > 0:
        print("Positive")
    elif n < 0:
        print("Negative")
    else:
        print("Zero")


# -------------------------------------------------------
# Exercise 2: Letter Grade
# -------------------------------------------------------
def ex2():
    score = int(input("Score (0-100): "))
    if score >= 90:
        print("A")
    elif score >= 80:
        print("B")
    elif score >= 70:
        print("C")
    elif score >= 60:
        print("D")
    else:
        print("F")


# -------------------------------------------------------
# Exercise 3: FizzBuzz
# -------------------------------------------------------
def ex3():
    n = int(input("Enter a number: "))
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)


# -------------------------------------------------------
# Exercise 4: Season Classifier
# -------------------------------------------------------
def get_season(month: int) -> str:
    match month:
        case 12 | 1 | 2:
            return "Winter"
        case 3 | 4 | 5:
            return "Spring"
        case 6 | 7 | 8:
            return "Summer"
        case 9 | 10 | 11:
            return "Autumn"
        case _:
            return "Invalid month"


def ex4():
    month = int(input("Month number (1-12): "))
    print(get_season(month))


# -------------------------------------------------------
# Exercise 5: BMI Category
# -------------------------------------------------------
def ex5():
    weight = float(input("Weight (kg): "))
    height = float(input("Height (m): "))
    bmi = weight / height ** 2
    print(f"BMI: {bmi:.1f}")

    if bmi < 18.5:
        print("Underweight")
    elif bmi < 25.0:
        print("Normal")
    elif bmi < 30.0:
        print("Overweight")
    else:
        print("Obese")


# -------------------------------------------------------
# Run all exercises
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
