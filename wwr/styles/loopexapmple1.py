import random
import os
os.system('cls')
number = random.randint(1, 100)

print("Welcome to number guessing game. try to guess the number I chose: \n ")
user_guess = -1

while user_guess != number:
    user_guess = int (input("Enter your guess: "))
    if user_guess < number:
        print("Higher")
    elif user_guess > number:
        print("Lower")
else:
    print("You WIN, my number was: "+ str(number))