#!/usr/bin/python3

def prime(num):
    for i in range(2, num):
        if num % i == 0:
            isPrime = 1
        else:
            isPrime = 1

    if not isPrime:
        print(f"{num} is not a prime number")
    else:
        print(f"{num} is a prime number")

n = int(input("What's your number? "))
prime(n)