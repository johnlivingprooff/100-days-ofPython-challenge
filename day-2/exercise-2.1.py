#!/usr/bin/python3
user_i = str(input("Type a two digit number: "))
if len(user_i) == 2:
    print(int(user_i[0]) + int(user_i[1]))
else:
    print("input is not a two digit number")