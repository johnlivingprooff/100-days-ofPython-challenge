#!/usr/bin/python3
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L -> ")
pepperoni = input("Do you want pepperoni? Y or N -> ")
cheese = input("Do you want extra cheese? Y or N -> ")

small = 15
med = 20
large = 25

# Small
if size == "S":
    if pepperoni == "Y" and cheese == "Y":
        print(f"Your final Bill is: ${small + 3}.")
    elif pepperoni == "Y":
        print(f"Your final bill is: ${small + 2}")
    elif cheese == "Y":
        print(f"Your final bill is: ${small + 1}")
    if pepperoni == "N" and cheese == "N":
        print(f"Your final Bill is: ${small}.")

# Medium
elif size == "M":
    if pepperoni == "Y" and cheese == "Y":
        print(f"Your final Bill is: ${med + 4}.")
    elif pepperoni == "Y":
        print(f"Your final bill is: ${med + 3}")
    elif cheese == "Y":
        print(f"Your final bill is: ${med + 1}")
    if pepperoni == "N" and cheese == "N":
        print(f"Your final Bill is: ${med}.")

# Large
elif size == "L":
    if pepperoni == "Y" and cheese == "Y":
        print(f"Your final Bill is: ${large + 4}.")
    elif pepperoni == "Y":
        print(f"Your final bill is: ${large + 3}")
    elif cheese == "Y":
        print(f"Your final bill is: ${large + 1}")
    if pepperoni == "N" and cheese == "N":
        print(f"Your final Bill is: ${large}.")
else:
    print("We only have small, medium, and large options")
