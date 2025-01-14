### CAMEL CASE TO SNAKE CASE
# https://cs50.harvard.edu/python/2022/psets/2/camel/

# Implement a program that prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case.
# Assume that the user’s input will indeed be in camel case.

def main():
    camelCase = input("Enter a variable name in camel case: ")
    snakeCase = camel_to_snake(camelCase)
    
    print(f"camelCase: {camelCase}")
    print(f"snake_case: {snakeCase}")

def camel_to_snake(camelCase):
    snake_case = ""
    # check if each letter is uppercase
    for char in camelCase:
        # if char is uppercase start new word
        if char.isupper():
            snake_case +="_"+char.lower()
        else:
            snake_case += char

    return snake_case
# Test cases:
# [name] should output: name
# [firstName] should output: first_name
# [preferredFirstName] should output: preferred_first_name

if __name__ == "__main__":
    main()