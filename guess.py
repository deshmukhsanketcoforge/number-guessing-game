from ast import While
import random
import time

# ---------- Settings ----------
DEBUG_SECRET = None   # For testing, set to a number such as 42. Set back to None before your final commit.
TIME_LIMIT = 60       # Seconds allowed in Time Challenge mode
is_correct_guess = False # flag to track if the player guessed correctly

print("Welcome to the Number Guessing Game")

# ---------- Choose a level ----------
# Goal: keep asking until the player picks a valid level, then set the range and attempt limit.

level = None

while True:
    level = input("Choose a level:\n1. Easy\n2. Medium\n3. Hard\nEnter your choice (1-3): ").strip().lower()

    if level in ["1", "2", "3"]:
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.\n")

# default values for range (used in feature 1: classic mode)
low = 0
high = 100

# default number of attempts
attempts_allowed = 3

if level == "1":
    low = 1
    high = 50
    attempts_allowed = 10
elif level == "2":
    low = 1
    high = 100
    attempts_allowed = 8
elif level == "3":
    low = 1
    high = 200
    attempts_allowed = 10

# ---------- Choose a mode ----------
# Goal: keep asking until the player picks Classic or Time Challenge.

# ---------- Set up the round ----------
# Goal: pick the secret number (use DEBUG_SECRET when it is not None) and start the clock.

if DEBUG_SECRET is not None:
    secret = DEBUG_SECRET
else:
    secret = random.randint(low, high)

# ---------- Guess loop ----------
# Goal: keep asking for guesses until the player wins, runs out of attempts, or runs out of time.

while attempts_allowed > 0:
    guess = input(f"Guess a number between {low} to {high}: ")

    # user input should be all digits, if not ask again
    if not guess.isdigit():
        print("Invalid Integer. Please enter a valid whole number (e.g. 1, 2)\n")
        continue

    # convert user input to int (as default is string input)
    guess = int(guess)

    # user input is valid but out of range
    if (guess < low) or (guess > high):
        print("Out of range integer. Please enter a number within valid range {low} to {high}\n")
        continue

    # valid input format within range, hence counted towards attempts used
    attempts_allowed -= 1

    if guess == secret:
        is_correct_guess = True
        print("correct")
        break
    elif guess < secret:
        print("too low\n")
    else:
        print("too high\n")

    print(f"You have {attempts_allowed} attempts remaining.\n")

# ---------- End of round ----------
# Goal: show the result that matches how the round ended.

if is_correct_guess:
    print(f"Congratulations! You guessed the secret number {secret} correctly!")
else:
    print(f"Game Over! Unfortunately you ran out of attempts. The secret number was: {secret}. Better luck next time!")