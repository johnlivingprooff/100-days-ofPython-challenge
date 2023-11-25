#!/usr/bin/python3
import random

def choose(n):
    rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''

    if n == 0:
        print(rock)
        return 0
    if n == 1:
        print(paper)
        return 1
    if n == 2:
        print(scissors)
        return 2

print("it's a rock, paper, scissors game!")
fig = int(input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissors\n"))

user = choose(fig)

comp_fig = random.randint(0, 2)
print("Computer chose:")

computer = choose(comp_fig)

if user == computer:
    print("it is a draw!")
elif user == 1 and computer == 0:
    print("You win")
elif user == 0 and computer == 2:
    print("You win")
elif user == 2 and computer == 1:
    print("You lose -_-")
elif user == 0 and computer == 1:
    print("You lose -_-")
elif user == 1 and computer == 2:
    print("You lose -_-")
elif user == 2 and computer == 0:
    print("You win")