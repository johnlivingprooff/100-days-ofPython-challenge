#!/usr/bin/python3
import random

names = input("Type in everybody's name, separated by comma: ")
nameList = names.split(", ")
chosen = random.randint(0, len(nameList) - 1)
print(chosen)
print(f"{nameList[chosen]} will handle the bill")
