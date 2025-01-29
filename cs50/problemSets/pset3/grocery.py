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

def main():
    grocery_list ={}
    while True:
        try:
            # prompt user for input
            item = input("- ").lower()

            if item == "..": # workaround for 'ctrl+d' to exit
                raise Exception("EOF Error")
            elif item in grocery_list:
                grocery_list[item] += 1
            else:
                grocery_list[item.lower()] = 1
        # if program exit, 
        except Exception:
            # print items_list
            print(f"list: {grocery_list}")
            for item in sorted(grocery_list.keys()):
                print(f"{grocery_list[item]} {item.upper()}")
            break

main()