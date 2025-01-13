### HOME FEDERAL SAVINGS BANK
# https://cs50.harvard.edu/python/2022/psets/1/bank/

# Implement a program that prompts the user for a greeting. 
# If the greeting starts with "hello", output "$0". 
# If the greeting starts with an "h" (but not "hello"), output "$20". 
# Otherwise, output "$100".

# Be sure to vary the casing of your input and “accidentally” add spaces on either side of your input before pressing enter. 
# Your program should behave as expected, case- and space-insensitively.

def main():
    while True:
        greeting = input("What is your greeting? ").strip().lower()
        if greeting.isdigit() or greeting == "":
            print("Invalid greeting.")
        else:
            print(hello(greeting))
            break

    test_cases()

def test_cases():
    test_cases = ["hello", "Hello", "hi", "hey", "what's up", "Hola"]
    for case in test_cases:
        print(f"Testing: {case}")
        print(f"Output: {hello(case)}")

def hello(greeting):
    if greeting == "hello":
        return "$0"
    elif greeting.startswith("h"):
        return "$20"
    else:
        return "$100"

if __name__ == "__main__":
    main()