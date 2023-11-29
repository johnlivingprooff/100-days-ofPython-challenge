#!/usr/bin/python3

scores = {
    "Harry": 81,
    "Ron": 78,
    "Bosl": 99,
    "Rach": 64,
    "Seven": 72,
}

grades = {}

for key, value in scores.items():
    if 91 <= value <= 100:
        grades[key] = "Outstanding"
    if 81 <= value <= 90:
        grades[key] = "Exceeds Expectations"
    if 71 <= value <= 80:
        grades[key] = "Acceptable"
    if value <= 70:
        grades[key] = "Fail"

print(grades)
    