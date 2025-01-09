### this is a comment
"""
these lines
are also
comments
"""

### FUNCTIONS
# print("Hello World")

# *** printing quotes ""
# print('Hello, "friend"')
# print('Hello, \"friend\"')


### ARGUMENTS
# argument1="first argument"
# argument2="second argument"
# argument3="third argument"

# print(argument1, argument2, argument3, sep=", ",end=".")


### VARIABLES
name=input("What's your name? ")
# print(name)

# + concatenates
# print("Hello, " + name)

# f"{variable}"
# print(f"Hello, {name}")


### STR STRING METHODS

# .strip() removes whitespace
stripped=name.strip()
# print(f"Hello, {stripped}")

# .capitalize() Capitalization string method
capital=name.capitalize()
print(f"Hello, {capital}")

# .title()  Title String Method
title=name.title()
print(f"Hello, {title}")

# chaining functions
chain=name.strip().capitalize().title()
print(f"Hello, {chain}")        

# split name variable into multiple variables, where " "
first, last = chain.split(" ")
print(f"Nice to meet you, {first} {last}")