#!/usr/bin/python3
"""This Module contains a Calculator program"""
from art import logo


#Calculator

#Add
def add(x, y):
    """Adds two numbers"""
    return x + y

#Subtract
def sub(x, y):
    """Subtracts two numbers"""
    return x - y

#Divide
def div(x, y):
    """Divides two numbers"""
    return x / y

#Multiply
def mul(x, y):
    """Multiplies two numbers"""
    return x * y

operations = {
    "+": add,
    "-": sub,
    "/": div,
    "*": mul,
}
def calc():
    print(logo)
    x = float(input("What's the first number? "))

    for key in operations:
        print(key, end="  ")

    print()

    # Calculation
    should_continue = True
    while should_continue:
        user_op = input("Pick an Operation: ")

        y = float(input("What's the next number? "))

        funct = operations[user_op]
        result = funct(x, y)
        print(f"{x} {user_op} {y} = {result}")
        msg = f"Type 'y' to continue calculating with {result}, \
or 'n' to start a new calculation: "
        if input(msg) == "y":
            x = result
        else:
            should_continue = False
            print("---")
            calc()

calc()
