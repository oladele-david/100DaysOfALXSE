#!/usr/bin/python3
"""
This file is tests and examples on exception handling in Python 3

"""

def read_a_number(number):
    """
    This function reads a number
    :param number:
    :return number:
    """
    try:

        print(int(number))
    except ValueError:
        print("Not a number")


input = input("Enter a number:")

read_a_number(input)