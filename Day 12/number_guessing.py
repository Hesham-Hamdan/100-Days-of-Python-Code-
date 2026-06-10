import random


print(
    "Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100"
)

difficulty = input("Choose a difficulty. Type 'e' for 'easy' or 'h' fo 'hard': ")
number = random.randint(0, 100)

if difficulty == "e":
    attemps = 10
else:
    attemps = 5

guess = 0


def compare_two_nums(num1, num2):
    if num1 == num2:
        print("You won")
        return
    elif num1 > num2:
        print("Too high")
    else:
        print("Too low")


while guess != number and attemps > 0:
    print(f"You have {attemps} attemps remaining to guess the number.")
    guess = int(input("Make a guess: "))

    compare_two_nums(guess, number)

    attemps -= 1
    if attemps > 0:
        print("Guess again")

if attemps == 0:
    print("You lost")
