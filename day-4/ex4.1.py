#!/usr/bin/python3
import random


coin_toss = random.randint(0, 1)
if coin_toss == 0:
    print("Tails")
elif coin_toss == 1:
    print("Heads")

if random.randint(0, 1) == 0:
    print("->Tails")
else:
    print("Heads<-")
