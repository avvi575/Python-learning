# ============================================================
# CS50P Week 4 — Topic 1: import & the random Module
# ============================================================
# Python ships with a standard library of pre-built modules.
# You unlock them with `import`.
#
# Two styles:
#   import random              → use as random.choice(...)
#   from random import choice  → use as choice(...)  (more specific)
#
# "from" style saves system resources by loading only what you need.
# ============================================================

import random                    # import the whole module

# -------------------------------------------------------
# random.choice(seq) — pick one item at random from a list
# -------------------------------------------------------
print("=== random.choice() ===")
coin = random.choice(["heads", "tails"])
print(f"Coin flip: {coin}")

suit = random.choice(["♠", "♥", "♦", "♣"])
print(f"Random suit: {suit}")

# -------------------------------------------------------
# random.randint(a, b) — random integer in [a, b] INCLUSIVE
# (both endpoints are possible — unlike range which excludes b)
# -------------------------------------------------------
print("\n=== random.randint(a, b) ===")
number = random.randint(1, 10)
print(f"Random number 1-10: {number}")

die = random.randint(1, 6)
print(f"Dice roll: {die}")

# -------------------------------------------------------
# random.shuffle(x) — shuffle a list IN PLACE
# ⚠️ Returns None — it mutates the original list directly
# -------------------------------------------------------
print("\n=== random.shuffle(x) ===")
cards = ["jack", "queen", "king", "ace"]
print(f"Before shuffle: {cards}")
random.shuffle(cards)
print(f"After shuffle : {cards}")   # original list is now shuffled

# -------------------------------------------------------
# from ... import — load only what you need
# -------------------------------------------------------
print("\n=== from random import choice ===")
from random import choice        # now we call choice() directly

result = choice(["rock", "paper", "scissors"])
print(f"Game: {result}")

# -------------------------------------------------------
# Other useful random functions (bonus)
# -------------------------------------------------------
print("\n=== Bonus random functions ===")
print(f"random.random()         → {random.random():.4f}")    # float in [0.0, 1.0)
print(f"random.uniform(1, 5)    → {random.uniform(1, 5):.4f}")  # float in [a, b]
print(f"random.sample(range(10), 3) → {random.sample(range(10), 3)}")  # 3 unique picks
