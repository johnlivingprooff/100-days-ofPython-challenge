#!/usr/bin/python3

row1 = ["⬜", "⬜", "⬜"]
row2 = ["⬜", "⬜", "⬜"]
row3 = ["⬜", "⬜", "⬜"]
map = [row1, row2, row3]
print(f"{map[0]}\n{map[1]}\n{map[2]}")
treasure = input("Where do you want to place the treasure? ")
x = int(treasure[1]) - 1
y = int(treasure[0]) - 1

map[x][y] = "X"
print(f"{map[0]}\n{map[1]}\n{map[2]}")
