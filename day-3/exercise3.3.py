#!/usr/bin/python3
print("Is _______ a leap year? Get your answer")
year = int(input("which Year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year")
        print("Not Leap Year")
    else:
        print("Leap Year")
else:
    print("Not Leap Year")