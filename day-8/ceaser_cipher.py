#!/usr/bin/python3

def ceaser(text, shift, direction):
    n_text = ""
    if direction == "decode":
            shift *= -1
    for letter in text:
        if letter.isalpha():
            idx = alphabet.index(letter)
            idx_n = (idx + shift) % 26
            n_text += alphabet[idx_n]
        else:
             n_text +=letter
    print(f"Here's the {direction}d result: {n_text}")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from art import logo
print(logo)

end_cipher = False
while not end_cipher:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    ceaser(text, shift, direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if restart == "no":
         end_cipher = True
         print("Goodbye!")
