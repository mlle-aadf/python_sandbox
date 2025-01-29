## https://docs.python.org/3/library/random.html#module-random
import random 


## SHUFFLE()

cards = ["jack", "queen", "king", "ace", "joker"]
random.shuffle(cards)

for card in cards:
    print(card)


## RANDINT()

# number = random.randint(1, 10)
# print(f"number: {number}")


## CHOICE()

# from random import choice

# coin = choice(["heads", "tails"])

# print(f"coin: {coin}")



## IMPORT

# import random

# limbs = ["heads", "tails", "knees", "elbows"]
# limb = random.choice(limbs)

# print(f"limb: {limb}")