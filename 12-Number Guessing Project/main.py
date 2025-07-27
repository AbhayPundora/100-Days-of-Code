import random
from art import logo
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ")

def guess_the_number():
    attempts = 0
    if difficulty_level == "easy":
        attempts = 10
    else:
        attempts = 5

    number = random.randint(1,100)

    def compare(msg):
        nonlocal attempts
        print(f"Too {msg}!")
        print("Guess again.")
        attempts -= 1

    while attempts != 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guessed_num = int(input("Make a guess: "))
        if guessed_num > number:
            compare("high")
        elif guessed_num < number:
            compare("low")
        else:
            print(f"You got it! The answer was {number}")
            return

    print(f"You've run out of guesses, you lose! The answer was {number}")
guess_the_number()