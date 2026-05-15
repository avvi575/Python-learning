# ============================================================
# CS50P Week 2 — Topic 7: Mario Patterns (Nested Loops)
# ============================================================
# Nested loops = a loop inside another loop.
# Outer loop controls ROWS; inner loop controls COLUMNS.
#
# This section also shows how to abstract patterns into
# reusable functions — a key software design principle.
# ============================================================


# -------------------------------------------------------
# Part 1 — Print a COLUMN (vertical stack of bricks)
# -------------------------------------------------------
def print_column(height):
    """Print a vertical column of # blocks."""
    for _ in range(height):
        print("#")


# -------------------------------------------------------
# Part 2 — Print a ROW (horizontal line of bricks)
# String multiplication: "#" * 4 → "####"
# -------------------------------------------------------
def print_row(width):
    """Print a horizontal row of ? blocks."""
    print("?" * width)


# -------------------------------------------------------
# Part 3 — Print a SQUARE using nested loops
# Outer loop = each row; inner loop = each brick in that row
# print("#", end="") suppresses the newline so bricks stay on one line
# print() at the end of the outer loop adds the row break
# -------------------------------------------------------
def print_square_nested(size):
    """Print a size×size square using explicit nested loops."""
    for i in range(size):           # each row
        for j in range(size):       # each column in this row
            print("#", end="")      # brick — no newline
        print()                     # end of row → newline


# -------------------------------------------------------
# Part 4 — Same square, but using print_row as helper
# Abstraction: the inner loop is hidden inside print_row
# -------------------------------------------------------
def print_square(size):
    """Print a size×size square using print_row helper."""
    for i in range(size):
        print_row(size)             # reuse the row function


def print_row_hash(width):
    """Row of # characters (used by print_square)."""
    print("#" * width)


# -------------------------------------------------------
# Bonus — right-aligned triangle (classic Mario staircase)
# -------------------------------------------------------
def print_staircase(height):
    """Print a right-aligned staircase of given height."""
    for i in range(1, height + 1):
        print(" " * (height - i) + "#" * i)


# -------------------------------------------------------
# Main — run all demos
# -------------------------------------------------------
def main():
    print("=== Column (height=3) ===")
    print_column(3)

    print("\n=== Row (width=4) ===")
    print_row(4)

    print("\n=== Square 3×3 (nested loops) ===")
    print_square_nested(3)

    print("\n=== Square 3×3 (with helper function) ===")
    for _ in range(3):
        print_row_hash(3)

    print("\n=== Staircase (height=4) ===")
    print_staircase(4)


main()
