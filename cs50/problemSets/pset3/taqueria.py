### FELIPE'S TAQUERIA
# https://cs50.harvard.edu/python/2022/psets/3/taqueria/

# Implement a program that enables a user to place an order, prompting them for items, one per line, until the user inputs control-d.
# After each inputted item, display the total cost of all items inputted thus far, prefixed with a dollar sign ($) and formatted to two decimal places.
# Treat the user’s input case insensitively.
# Ignore any input that isn’t an item.
# Assume that every item on the menu will be titlecased.

# Menu:
# {
#     "Baja Taco": 4.25,
#     "Burrito": 7.50,
#     "Bowl": 8.50,
#     "Nachos": 11.00,
#     "Quesadilla": 8.50,
#     "Super Burrito": 8.50,
#     "Super Quesadilla": 9.50,
#     "Taco": 3.00,
#     "Tortilla Salad": 8.00
# }

# For example:
# Input: Burrito
# Output: $7.50
#
# Input: Taco
# Output: $10.50
#
# Input: Super Quesadilla
# Output: $20.00

def main():
    while True:
        try:
            order = input("What can I get for you?")
            
main()