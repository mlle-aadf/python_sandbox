### GROCERY LIST
# https://cs50.harvard.edu/python/2022/psets/3/grocery/

# Implement a program that prompts the user for items, one per line, until the user inputs control-d.
# Then output the user’s grocery list in all uppercase, sorted alphabetically by item, prefixing each line with the number of times the user inputted that item.
# Treat the user’s input case-insensitively.

# For example:
# Input: apple
# Input: banana
# Input: apple
# Input: carrot
# Output:
# 2 APPLE
# 1 BANANA
# 1 CARROT

# def main():
#     while True:
    
        # prompt user for input
            # if input ctrl+D, 
                # print items_list
            # else
                # if input in items_list 
                    # increment item counter
                # else add item to items_list