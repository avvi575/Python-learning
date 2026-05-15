# ============================================================
# CS50P Week 2 — Topic 6: Dictionaries
# ============================================================
# A `dict` (dictionary) stores KEY → VALUE pairs.
# Keys are unique identifiers; values are the associated data.
#
# Syntax:
#   my_dict = {"key1": value1, "key2": value2}
#   my_dict["key1"]   → value1
#
# Special value: None  →  represents "no value" / absence
# ============================================================

# -------------------------------------------------------
# Part A — Simple dict: name → house
# -------------------------------------------------------
print("=== Part A: Simple dict ===")

students = {
    "Hermione": "Gryffindor",
    "Harry":    "Gryffindor",
    "Ron":      "Gryffindor",
    "Draco":    "Slytherin",
}

# Access a single value by key
print(students["Hermione"])   # Gryffindor

# -------------------------------------------------------
# Iterating a dict — by default you get the KEYS
# -------------------------------------------------------
print("\n--- Keys only ---")
for student in students:
    print(student)

# -------------------------------------------------------
# Access key AND value inside the loop
# -------------------------------------------------------
print("\n--- Keys + values ---")
for student in students:
    print(student, students[student], sep=", ")

# -------------------------------------------------------
# Pythonic: use .items() to unpack both at once
# -------------------------------------------------------
print("\n--- Using .items() (Pythonic) ---")
for name, house in students.items():
    print(f"{name} → {house}")

# -------------------------------------------------------
# Part B — List of dicts: richer data per student
# Use when each record needs multiple fields.
# None = Python's "no value" / null
# -------------------------------------------------------
print("\n=== Part B: List of dicts ===")

students_rich = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry",    "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron",      "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco",    "house": "Slytherin",  "patronus": None},  # None = no patronus
]

for student in students_rich:
    patronus = student["patronus"] if student["patronus"] else "None"
    print(student["name"], student["house"], patronus, sep=", ")

# -------------------------------------------------------
# Common dict operations
# -------------------------------------------------------
print("\n=== Dict operations ===")
d = {"a": 1, "b": 2}

d["c"] = 3              # add a new key-value pair
print("After add:", d)

d["a"] = 99             # update an existing value
print("After update:", d)

del d["b"]              # delete a key
print("After delete:", d)

print("Keys  :", list(d.keys()))
print("Values:", list(d.values()))
print("Has 'a'?", "a" in d)
print("Has 'z'?", "z" in d)
