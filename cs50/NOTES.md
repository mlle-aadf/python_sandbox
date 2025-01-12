# DATA TYPES

**int**: Integer
    Example: `x = 5`
**float**: Floating-point number
    Example: `y = 3.14`
**str**: String
    Example: `name = "Alice"`
**bool**: Boolean
    Example: `is_valid = True`
**list**: List
    Example: `numbers = [1, 2, 3, 4, 5]`
**tuple**: Tuple
    Example: `coordinates = (10, 20)`
**dict**: Dictionary
    Example: `person = {"name": "Alice", "age": 30}`
**set**: Set
    Example: `unique_numbers = {1, 2, 3, 4, 5}`
**NoneType**: None
    Example: `value = None`


## Conditional Statements
- Use if, elif, and else for conditional logic.

  ```python
  if x > 0:
      print("Positive")
  elif x == 0:
      print("Zero")
  else:
      print("Negative")
  ```

## Loops
- Use for loops to iterate over a sequence.

  ```python
  for i in range(5):
      print(i)
  ```

  ```python
  for _ in range(5):
      print("Hello")
  ```

- Use while loops for repeated execution as long as a condition is true.

  ```python
  while x > 0:
      print(x)
      x -= 1
  ```


## F-STRINGS
- Formatted String Literals: Embed expressions inside string literals using {}.
    ```python
        name = "Alice"
        age = 30
        print(f"{name} is {age} years old.")
    ```


## UNPACKING
- Unpacking Lists/Tuples: Assign multiple variables at once.

    ```python
        coordinates = (10, 20)
        x, y = coordinates
    ```

- Unpacking with * Operator: Collect multiple items into a list.
 
    ```python
        numbers = [1, 2, 3, 4, 5]
        first, *rest = numbers
    ```
## ENUMERATE
- Iterate over a list and get both the index and the value.

    ```python
        fruits = ["apple", "banana", "cherry"]
        for index, fruit in enumerate(fruits):
            print(index, fruit)
    ```
## ZIP
- Combine multiple iterables into tuples.

    ```python
        names = ["Alice", "Bob", "Charlie"]
        ages = [25, 30, 35]
        for name, age in zip(names, ages):
            print(f"{name} is {age} years old.")
    ```
    
## LAMBDA
- Create small, unnamed functions using [lambda]

    ```python
        add = lambda x, y: x + y
        print(add(2, 3))  # Output: 5   
    ```

## MAP, FILTER, REDUCE
- Map Function: Apply a function to all items in an iterable.
   
    ```python
        numbers = [1, 2, 3, 4, 5]
        squares = list(map(lambda x: x**2, numbers))
    ```

- Filter Function: Filter items in an iterable based on a condition.
   
    ```python
        even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    ```

- Reduce Function: Apply a function cumulatively to the items in an iterable (requires functools).
   
    ```python
        from functools import reduce
        product = reduce(lambda x, y: x * y, numbers)
    ```


## Exception Handling
- Use [try], [except], [else], and [finally] for exception handling.

  ```python
  try:
      result = 10 / 0
  except ZeroDivisionError:
      print("Cannot divide by zero")
  else:
      print("Division successful")
  finally:
      print("This will always execute")
  ```

## File Handling
- Use [open] with statement for file handling.

  ```python
  with open("file.txt", "r") as file:
      content = file.read()
  ```

## SYNTAX
- Single Underscore _: Often used as a throwaway variable name in loops or to indicate that a variable is temporary or insignificant.

  ```python
    for _ in range(5):
        print("Hello")
  ```

- Leading Underscore _var: Indicates that a variable or method is intended for internal use (convention, not enforced).
 
  ```python
    _internal_variable = 42

  ```

- Double Leading Underscore __var: Triggers name mangling to avoid naming conflicts in subclasses.

    ```python
        class MyClass:
        def __init__(self):
            self.__private_variable = 42
    ```

- Trailing Underscore var_: Used to avoid naming conflicts with Python keywords.

    ```python
        class_ = "MyClass"
    ```

- Print with Multiple Arguments: Prints multiple arguments separated by spaces.

    ```python
        print("The value of n is", n)
    ```

- Print with end Parameter: Changes the end character (default is newline).

    ```python
        print("Hello", end=" ")
        print("world!")
        # Output: Hello world!
    ```

- Print with sep Parameter: Changes the separator between arguments (default is space).
    
    ```python
        print("apple", "banana", "cherry", sep=", ")
        # Output: apple, banana, cherry
    ```
   