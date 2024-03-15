#!/usr/bin/python3

def increment(number, by):
    return number + by


result = increment(2,by=1)
print(result)

# Optional parameter

def increment_2(number, by=1):
    return number + by


result_2 = increment_2(2,5)
print(result_2)

print("############################################")
print("Multiple arguments")
print("############################################")

def multiply(*kwargs):
    total = 1
    for kwarg in kwargs:
        print(kwarg)
        total *= kwarg
    return total


print(multiply(1,3,4,45,2))

print("############################################")
print("Double asterisk arguments **args")
print("############################################")

def save_user(**user):
    print(user)
    print(user['name'])


save_user(id=1, name="John", age=22)
