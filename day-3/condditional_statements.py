#!/usr/bin/python3


print("Welcome to the RollerCoaster Ride!")
start = input("Are you Ready? [Yes/No] ")

if start == "Yes" or start == "yes":
    print("Let's Begin!")
    height = input("What's your height in cm? ")
    if (int(height) >= 120):
        print("You can proceed")
    else:
        print("Sorry, you need to grow taller -_-")
elif start == "No" or start == "no":
    print("Okay, Bye..\nCome back soon!")
else:
    print("Please type 'Yes' or 'No'\nGoodBye..")

