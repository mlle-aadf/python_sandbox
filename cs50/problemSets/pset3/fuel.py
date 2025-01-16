### FUEL GAUGE
# https://cs50.harvard.edu/python/2022/psets/3/fuel/

# Implement a program that prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is an integer, and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank.
# If 1% or less remains, output E instead to indicate that the tank is essentially empty.
# If 99% or more remains, output F instead to indicate that the tank is essentially full.
# If X or Y is not an integer, X is greater than Y, or Y is 0, prompt the user again.
# Be sure to catch any exceptions like ValueError or ZeroDivisionError.


def main():
    while True:
        try:
            fraction_input = input("Input: ")
            percentage = fraction_to_percentage(fraction_input)
        except (IndexError, ValueError, ZeroDivisionError) as e:
            if isinstance(e, IndexError):
                print(e)
            elif isinstance(e, ValueError):
                print("Both X and Y must be integers, where X is less than Y")
            elif isinstance(e, ZeroDivisionError):
                print("Denominator (Y) cannot be 0")
        else:
            print(f"Output: {gauge(percentage)}")
            break
    
def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"
    
def fraction_to_percentage(fraction): 
    if "/" not in fraction:
        raise IndexError("Input must contain '/'")
    x,y =fraction.split("/")
    
    if int(x)/int(y) > 1:
        raise ValueError
    return round((int(x)/int(y))*100)

main()


# For example:
# Input: 1/4
# Output: 25%
#
# Input: 1/2
# Output: 50%
#
# Input: 3/4
# Output: 75%
#
# Input: 1/100
# Output: E
#
# Input: 100/100
# Output: F