# ============================================================
# CS50P Week 2 — Topic 4: Lists
# ============================================================
# A `list` is an ordered collection of values.
# Values can be strings, numbers, booleans, other lists — anything.
#
# Syntax:   my_list = [item0, item1, item2]
# Indexing: my_list[0]  → first item  (counting starts at 0!)
#           my_list[-1] → last item
# ============================================================

students = ["Hermione", "Harry", "Ron"]

# -------------------------------------------------------
# Version 1 — manual indexing (verbose)
# -------------------------------------------------------
print("--- Version 1: manual indexing ---")
print(students[0])   # Hermione
print(students[1])   # Harry
print(students[2])   # Ron

# -------------------------------------------------------
# Version 2 — for loop over the list (clean ✅)
# Python reads this as: "for each student in students, print it"
# -------------------------------------------------------
print("\n--- Version 2: for loop ---")
for student in students:
    print(student)

# -------------------------------------------------------
# Useful list facts
# -------------------------------------------------------
print("\n--- Indexing tricks ---")
print("First :", students[0])
print("Last  :", students[-1])   # negative index = from the end
print("Slice :", students[0:2])  # items at index 0 and 1

# -------------------------------------------------------
# Lists are mutable — you can change, add, remove items
# -------------------------------------------------------
print("\n--- Modifying lists ---")
students.append("Neville")        # add to end
print("After append:", students)

students.remove("Ron")            # remove by value
print("After remove:", students)

students.insert(1, "Ginny")       # insert at position
print("After insert:", students)
