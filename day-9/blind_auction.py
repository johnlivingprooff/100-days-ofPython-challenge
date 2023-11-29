#!/usr/bin/python3

from art import logo
import sys, os

print(logo)

print("Welcome to the secret auction program.")

auction = {}
more_bidders = "yes"

while more_bidders == "yes":
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))

    def add_bidder(name, bid):
        auction[name] = bid

    add_bidder(name, bid)

    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

    if more_bidders != "no":
        more_bidders = input("Type 'yes' or 'no' !.\n").lower()

    if more_bidders == "yes":
        os.system('clear')

max_bid = 0
max_bidder = ""
for key, value in auction.items():
    if value > max_bid:
        max_bid = value
        max_bidder = key

print(f"The winner is {max_bidder} with a bid of ${max_bid}")