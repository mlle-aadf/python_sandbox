### JUST SETTING UP MY TWITTER
# https://cs50.harvard.edu/python/2022/psets/2/twttr/

# Implement a program that prompts the user for a string of text and then outputs that same text but with all the vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.

# For example:
# Input: Twitter
# Output: Twttr

def main():
    text = input("What's your tweet?")
    print(vowel_check(text))
    
    testCases()

def vowel_check(text):
    vowels = {"a","e","i","o","u"}
    tweet=""
    for char in text:
        if char.lower() in vowels:
            tweet += ""
        else:
            tweet += char
    return tweet

# Test cases:
# [Twitter] should output: Twttr
# [CS50] should output: CS50
# [Hello, World!] should output: Hll, Wrld!
def testCases():
    cases = {"Twitter", "CS50", "Hello, World!"}
    for case in cases:
        print(f"Test case: {case}")
        print(f"output: {vowel_check(case)}")

if __name__ == "__main__":
    main()