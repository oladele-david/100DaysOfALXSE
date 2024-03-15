# Day 02: Introduction to Functions and FizzBuzz Challenge

Today, I delved into the world of functions in Python, exploring their definition, implementation, and usage. Additionally, I put my newfound knowledge to the test by solving the classic FizzBuzz challenge.

## Topics Covered:
1. **Functions:**
    - Writing custom functions in Python.
    - Understanding the difference between parameters and arguments.
    - Exploring different types of functions: those that perform a task and those that calculate and return a value.
    - Handling different numbers of arguments in functions.
    - Scope of variables within functions.
  
2. **FizzBuzz Challenge:**
    - Description of the FizzBuzz game.
    - Rules for FizzBuzz: If a number is divisible by both 3 and 5, return "FizzBuzz"; if divisible by 3, return "Fizz"; if divisible by 5, return "Buzz"; otherwise, return the number itself.

## FizzBuzz Solution:
```python
#!/usr/bin/python3
"""
Exercise: Fizz Buzz
Description: Fizz Buzz game
Rules: If a number is divisible by both 3 and 5 return "FizzBuzz",
If a number is divisible by 3 return "Fizz" else if its divisible by 5 return "Buzz"

"""

def fizz_buzz(input):
    """
    Fizz Buzz game
    this function will print the numbers divisible by both 3 and 5 
    :param input: int
    :return: mixed value
    """
    if input % 3 == 0 and input % 5 == 0:
        return "FizzBuzz"
    elif input % 3 == 0:
        return "Fizz"
    elif input % 5 == 0:
        return "buzz"
    else:
        return input


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:
    print(f"{number} is => {fizz_buzz(number)}")
