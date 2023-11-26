#!/usr/bin/python3

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

count = 0
for student in student_heights:
  count += student
avg = round(count / len(student_heights))
print(avg)
