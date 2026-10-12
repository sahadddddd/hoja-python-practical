# Computer generates a random number between (1 - 100)
# Player keeps guessing.
# At the end show-->Attempts = 6
# Program tells:Too High,Too Low,Correct!
# functions:generate_number(),get_guess(),check_guess(),play_game(),main()

import random

def generate_number():
    return  random.randint(1,100)


def get_guess():
    guess=int(input("enter a number between(1,100):"))
    return guess


def check_guess(guess,secret_number):
    if guess > secret_number:
        print("too high!")
        return False
    elif guess<secret_number:
        print("too low!")
        return False
    else:
        print("correct")
        return True


def play_game():
    secret_number=generate_number()
    attempt=0

    while True:
        guess=get_guess()
        attempt+=1

        if check_guess(guess,secret_number):
            print("attempts:",attempt)
            break


def main():
    print("welcome to number guessing game")
    print("guess a number between 1-100")
    play_game()
main()




