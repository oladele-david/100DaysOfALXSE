#!/usr/bin/python3

print("Hello World!")

your_temperature = input("What is your temperature? ")
temperature = int(your_temperature)

if temperature > 30:
    print(f"The temperature is {temperature}")
else:
    print(f"The temperature is cool at {temperature}")