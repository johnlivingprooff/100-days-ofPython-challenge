#!/usr/bin/python3
"""The Number Guessing game"""
import random


NUM = random.randint(1, 101)
# print(NUM)

print("Welcome to the Number Guessing Game!")
print("Can you guess the number I'm thinking of?\nIt's between 1 and 100")
difficulty = input("Choose difficulty level: [Type 'easy' or 'hard'] -> ").lower()

def easy():
    """Difficulty: is easy"""
    game_over = False
    attempts = 10

    while attempts >= 1 and not game_over:
        print(f"You have {attempts} attempts left to guess the number")
        guess = int(input("Make a guess: "))
        if guess == NUM:
            print(f"You got it right! {NUM} is the right answer")
            return
        elif guess < NUM:
            print(f"Too Low\nGuess Again")
            attempts -= 1
        elif guess > NUM:
            print(f"Too High\nGuess Again")
            attempts -= 1
    
        if attempts == 0:
            print(f"You're out of guesses, you lose")
            if input("Play Again? ['yes' or 'no']: ").lower() == 'yes':
                attempts = 10
            else:
                game_over = True


def hard():
    """Difficulty: is hard"""
    game_over = False
    attempts = 5

    while attempts >= 1 and not game_over:
        print(f"You have {attempts} attempts left to guess the number")
        guess = int(input("Make a guess: "))
        if guess == NUM:
            print(f"You got it right! {NUM} is the right answer")
            return
        elif guess < NUM:
            print(f"Too Low\nGuess Again")
            attempts -= 1
        elif guess > NUM:
            print(f"Too High\nGuess Again")
            attempts -= 1
    
        if attempts == 0:
            print(f"You're out of guesses, you lose")
            if input("Play Again? ['yes' or 'no']: ").lower() == 'yes':
                attempts = 5
            else:
                game_over = True


if difficulty == "easy":
    easy()
    

elif difficulty == "hard":
    hard()
    
