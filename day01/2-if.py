#!/usr/bin/python3

"""
Exercise:
Write a Python program that takes a user's input of a number and determines whether it is positive, negative, or zero.

Your program should:
1. Prompt the user to enter a number.
2. Read the user's input as an integer.
3. Use an if statement to check if the number is positive, negative, or zero.
4. If the number is positive, print "The number is positive."
5. If the number is negative, print "The number is negative."
6. If the number is zero, print "The number is zero."

Write the code to achieve this without looking at the solution.
"""

user_input = input("Enter a number: ")
input = int(user_input)

if input > 0:
    print("The number is Positive")
elif input < 0:
    print("The number is negative")
else:
    print("The number is Zero")
