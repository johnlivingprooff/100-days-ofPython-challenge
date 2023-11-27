#!/usr/bin/python3
import math

def paint_area(height, width, cover):
    return math.ceil((height * width) / cover)

h = int(input("Wall Height: "))
w = int(input("Wall Width: "))
coverage = 5

area = paint_area(h, w, coverage)
print(f"You need {area} cans of paint")
