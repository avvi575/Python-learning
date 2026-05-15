# 07 — Mario Patterns & Nested Loops

## Nested loops

A loop inside another loop. The inner loop runs **completely** for each single iteration of the outer loop.

```python
for i in range(3):      # outer: 3 rows
    for j in range(3):  # inner: 3 columns per row
        print("#", end="")
    print()             # newline after each row
```

Output:
```
###
###
###
```

## Key `print()` tricks

```python
print("#", end="")   # no newline → stays on same line
print()              # blank print() → just a newline
print("#" * 4)       # "####"  — string repetition
```

## Abstraction with functions

```python
def print_row(width):
    print("#" * width)

def print_square(size):
    for _ in range(size):
        print_row(size)    # inner loop hidden in print_row
```

Breaking logic into small named functions makes code **readable, testable, reusable**.

## Staircase pattern

```python
for i in range(1, height + 1):
    print(" " * (height - i) + "#" * i)
```

```
   #
  ##
 ###
####
```

## Design principle

> Start with the simplest version that works. Then abstract repeated patterns into functions.
