#!/usr/bin/python3
#Password Generator Project
import random, sys


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")


choice = "yes"

while choice == "yes":
    password_lenght = int(input("How long should your password be?\n(a strong password is between 8 - 15 chars long) "))
    nr_symbols = 4
    nr_numbers = 3
    nr_letters= password_lenght - nr_numbers - nr_symbols
    if password_lenght >= 8:
        password = []
        for char in range(nr_letters):
            password += random.choice(letters)
        for sym in range(nr_symbols):
            password += random.choice(symbols)
        for num in range(nr_numbers):
            password += random.choice(numbers)

        random.shuffle(password)
        phrase = ""
        for p in password:
            phrase += p

        print(f"Your new Password: {phrase}")
    else:
        print("Your password length should be above 8 chars")
    print()
    choice = (input("Would you like to generate another password? [Yes/No] ")).lower()
    if choice != "yes":
        sys.exit()