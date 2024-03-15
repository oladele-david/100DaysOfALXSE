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

