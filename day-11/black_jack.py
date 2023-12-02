#!/usr/bin/python3
"""The black jack game"""
import os, random
from art import logo


def deal_card():
    """deals the cards for user/computer"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def scores(cards):
    """Calculates the scores of dealt cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user, computer):
    """Compares the scores of player vs opponent"""
    if user > 21 and computer > 21:
        return "You went over! You lose"
    
    if user == computer:
        return "You Draw!"
    elif user == 0:
        return "You Win, with a Black Jack"
    elif user > 21:
        return " You went over, Opponent wins!"
    elif computer == 0:
        return "Opponent wins with a Black Jack"
    elif computer > 21:
        return "Opponent went over, You Win!"
    elif user > computer:
        return "You Win!"
    else:
        return "You Lose! -_-"


def play():
    """This is the main core of the game"""
    print(logo)

    user = []
    computer = []
    game_over = False

    for _ in range(2):
        user.append(deal_card())
        computer.append(deal_card())

    while not game_over:
        user_score = scores(user)
        computer_score = scores(computer)
    
        print(f"    Your cards: {user}, current score {user_score}")
        print(f"    Computer's first card: {computer[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            deal_again = input("Type 'y' to get another card, type 'n' to pass: ")
            if deal_again == 'y':
                user.append(deal_card())
            else:
                game_over = True

    while 1 < computer_score < 17:
        computer.append(deal_card())
        computer_score = scores(computer)

    print(f"    Your final hand: {user}, final score:{user_score}")
    print(f"    Computer's final hand: {computer}, final score:{computer_score}")
    print(compare(user_score, computer_score))



while input("Do you want to play Black Jack? [Type 'y' or 'n'] ") == "y":
    os.system('clear')
    play()