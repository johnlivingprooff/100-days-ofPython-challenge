#!/usr/bin/python3


age = input("what's your current age? ")

inYears = 90 - int(age)
inMonths = inYears * 12
inWeeks = inYears * 52
inDays = inYears * 365

print(f"You have {inDays} days, {inWeeks} weeks, {inMonths} months left :)")
