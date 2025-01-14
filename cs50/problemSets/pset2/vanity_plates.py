### VANITY PLATES
# https://cs50.harvard.edu/python/2022/psets/2/plates/

# Implement a program that prompts the user for a vanity plate and then validates it based on specific rules:
# All vanity plates must start with at least two letters.”
# Vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.
# Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.
# No periods, spaces, or punctuation marks are allowed.”
# The program should output "Valid" if the plate is valid and "Invalid" otherwise.

# For example:
# Input: CS50
# Output: Valid

def main():
    plate = input("Enter your vanity plate: ")
    
    print(is_valid(plate))
    
    
def is_valid(plate):
    # check if plate starts with at least two letters
    if not plate[:2].isalpha():
        return False
    # check if plate contains 2-6 characters (letters or numbers)
    if len(plate) < 2 or len(plate) > 6:
        return False
    # check if numbers cannot be used in the middle of a plate
    if plate[2:-1].isdigit():
        return False
    # check if the first number used cannot be a '0'
    if plate[2].isdigit() and plate[2] == "0":
        return False
    # check if no periods, spaces, or punctuation marks are allowed
    if not plate.isalnum():
        return False


# Test cases:
# [CS50] should output: Valid
# [CS50P] should output: Invalid
# [CS] should output: Valid
# [CS50CS] should output: Invalid

if __name__ == "__main__":
    main()