#!/usr/bin/python3
"""
Function Types: here I learn about the different types of functions
"""

def greet(name):
    print(f"Hello {name}")


def new_greeting(name):
    return(f"Hello {name}")


message = new_greeting("John")
print(message)