# ============================================================
# CS50P Week 2 — Topic 5: len() and range(len(...))
# ============================================================
# len() returns the number of items in a list (or string).
# Combining range(len(list)) lets you loop with both the
# index number AND the value at that index.
# ============================================================

students = ["Hermione", "Harry", "Ron"]

# -------------------------------------------------------
# Basic len()
# -------------------------------------------------------
print("Number of students:", len(students))

# -------------------------------------------------------
# range(len(...)) — loop with index + value
# Useful when you need the position number alongside the item
# -------------------------------------------------------
print("\n--- Numbered list (1-based display) ---")
for i in range(len(students)):
    print(i + 1, students[i])   # i+1 so it prints 1, 2, 3 not 0, 1, 2

# -------------------------------------------------------
# Pythonic alternative: enumerate()
# enumerate() gives you (index, value) pairs directly
# -------------------------------------------------------
print("\n--- Same result with enumerate() ---")
for i, student in enumerate(students, start=1):
    print(i, student)

# -------------------------------------------------------
# len() works on strings too
# -------------------------------------------------------
name = "Hermione"
print(f"\nLength of '{name}': {len(name)} characters")

for i, char in enumerate(name):
    print(f"  [{i}] = '{char}'")
