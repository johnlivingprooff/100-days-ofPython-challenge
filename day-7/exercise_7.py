#!/usr/bin/python3
import random

word_list = ["aardvark", "baboon", "camel"]

display = []
chosen_word = random.choice(word_list)
for i in range(0, len(chosen_word)):
    display.append("_")

print(f"the chosen word -> {chosen_word}")

endGame = False

while not endGame:
    guess = input("Guess a letter: ").lower()

    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            display[i] = chosen_word[i]

    print(display)

    if "_" not in display:
        endGame = True
print("You win!")
print()

