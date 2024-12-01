import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

guess_not_reached = True
def easy_mode():
    attempt = 10
    print("You have 10 attempts remaining to guess the number.")
    guess_not_reached = True
    while guess_not_reached:
        attempt -= 1
        guess = int(input("Make a guess: "))
        if (guess != think_num) and (guess > think_num):
            print("Too high\nGuess again.")
            print(f"You have {attempt} attempts remaing to guess the number.")
        elif (guess != think_num) and (guess < think_num):
            print("Too low\nGuess again")
            print(f"You have {attempt} attempts remaing to guess the number.")
            if attempt == 0:
                guess_not_reached = False
                print("You've run out of guess, you lose.")
        elif guess == think_num:
            guess_not_reached = False
            print(f"You got! the answer was {think_num}")


def hard_mode():
    attempt = 5
    print("You have 5 attempts to remaining to guess the number.")
    guess_not_reached = True
    while guess_not_reached:
        attempt -= 1
        guess = int(input("Make a guess: "))
        if (guess != think_num) and (guess > think_num):
            print("Too high\nGuess again.")
            print(f"You have {attempt} attemps remaining to guess the number.")
        elif (guess != think_num) and (guess < think_num):
            print("Too low\nGuess again.")
            print(f"You have {attempt} attempts remaining to guess the number.")
            if attempt == 0:
                guess_not_reached = False
                print("You've run out of guess, you lose.")
        elif guess == think_num:
            guess_not_reached = False
            print(f"You got it! The answer was {think_num}")


numbers = []

print("Welcome to the Number Guessing Game!")
#
# for num in range(1, 101):
#     numbers += [num]
# # print(numbers)
# think_num = random.choice(numbers)
# # print(think_num)

# OR

think_num = random.randint(1, 100)
# print(think_num)
print("I'm thinking of a number between 1 and 100.")

game_level = input("choose a difficulty. Type 'easy' or 'hard': ").lower()

if game_level == "easy":
    easy_mode()
elif game_level == "hard":
    hard_mode()