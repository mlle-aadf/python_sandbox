### DEEP THOUGHT
# https://cs50.harvard.edu/python/2022/psets/1/deep/

# Implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything, outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.
# Be sure to vary the casing of your input and “accidentally” add spaces on either side of your input before pressing enter. Your program should behave as expected, case- and space-insensitively.

import re

def main():
    answer = input("What is the answer to the Great Question of Life, the Universe and Everything? ")
    check_answer(answer)
    

def clean_answer(input_answ):
    if input_answ.isdigit():
        return int(input_answ)
    else:
        # Use re.sub() to replace spaces and special characters with an empty string
        cleaned_string = re.sub(r'[^A-Za-z0-9]', '', input_answ)
        lowered_string = cleaned_string.lower()
        return lowered_string

def check_answer(answer):
    cleaned = clean_answer(answer)
    acceptable = {42, "fortytwo"}
    verdict = "Yes" if cleaned in acceptable else "No"
    print(verdict)

main()

# [42] should output: Yes
# [Forty-Two] should output: Yes
# [forty-two] should output: Yes
# [50] should output: No