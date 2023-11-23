#!/usr/bin/python3

print("Welcome to the Love Calculator!")
name1 = input("What's your name?\n")
name2 = input("What's their name?\n")

# True Love -> lower
lower_name1 = name1.lower()
lower_name2 = name2.lower()

# calculator
true = 0
love = 0

for i in lower_name1:
    if i == 't' or i == 'r' or i == 'u' or i == 'e':
        true += 1
for i in lower_name2:
    if i == 't' or i == 'r' or i == 'u' or i == 'e':
        true += 1
for j in lower_name1:
    if j == 'l' or j == 'o' or j == 'v' or j == 'e':
        love += 1
for j in lower_name2:
    if j == 'l' or j == 'o' or j == 'v' or j == 'e':
        love += 1

# print(f"True: {true}\nLove: {love}")

score = str(true) + str(love)
# print(score)

if int(score) < 10 or int(score) > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif 40 < int(score) <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
