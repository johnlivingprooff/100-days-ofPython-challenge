#!/usr/bin/python3


height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

# BMI calculation is weight / height ^2
bmi = int(weight) / float(height) ** 2
print("Your BMI is {}".format(int(bmi)))