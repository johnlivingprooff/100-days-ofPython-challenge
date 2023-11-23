#!/usr/bin/python3
print("Is Your Number Odd/Even?")
num = int(input("What number would you like to check? "))

if num % 2 == 0:
    print(f"{num} is an even number")
elif num % 2 != 0:
    print(f"{num} is an odd number")
else:
    print("Your number should be an integer")
