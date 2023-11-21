#!/usr/bin/python3
"""Day 2 - #100DaysofPython
For Learning Purposes"""


# User input
bill = input("Welcome to the tip calculator!\nWhat was the total bill? $")
percent = input("What % tip would you like to give? 10, 15 or 12? ")
people = input("How many people will split the bill? ")

# Calculation
final_bill = float(bill) + (float(bill) * (int(percent) / 100))
split = round(final_bill / int(people), 2)

msg = f"Each person should pay: ${split}"
print(msg)

# Calculates any currency
print("---\nNow lets try any currency!")

# User input
print("Don't forget the currency symbol!")
bill = input("What was the total bill? ")
percent = input("What % tip would you like to give? 10, 15 or 12? ")
people = input("How many people will split the bill? ")

# Calculation
final_bill = float(bill[1:]) + (float(bill[1:]) * (int(percent) / 100))
split = round(final_bill / int(people), 2)

msg = f"Each person should pay: {bill[0]}{split}"
print(msg)
