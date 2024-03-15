# Day 01: Introduction to Conditional Statements and Variables

Today, we tackled a fundamental programming concept - conditional statements, by solving a problem on determining whether a number is positive, negative, or zero in Python.

## Challenge:
Write a Python program that takes a user's input of a number and determines whether it is positive, negative, or zero.

Your program should:
- Prompt the user to enter a number.
- Read the user's input as an integer.
- Use an if statement to check if the number is positive, negative, or zero.
- If the number is positive, print "The number is positive."
- If the number is negative, print "The number is negative."
- If the number is zero, print "The number is zero."

## Solution:
```python
user_input = input("Enter a number: ")

input = int(user_input)

if input > 0:
    print("The number is positive")
elif input < 0:
    print("The number is negative")
else:
    print("The number is zero")
