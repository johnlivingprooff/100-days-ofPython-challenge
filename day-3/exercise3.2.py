#!/usr/bin/python3


height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

# BMI calculation is weight / height ^2
bmi = round(float(weight) / float(height) ** 2)

if bmi < 18.5:
    print("Your BMI is {}, and you are underweight".format(int(bmi)))
elif 18.5 <= bmi <= 25:
    print(f"Your BMI is {bmi}, and you have a normal weight")
elif 25 < bmi <= 30:
    print(f"Your BMI is {bmi}, and you are slightly overweight")
elif 30 < bmi <= 35:
    print(f"Your BMI is {bmi}, and you are obese")
else:
    print(f"Your BMI is {bmi}, and you are clinically obese")
