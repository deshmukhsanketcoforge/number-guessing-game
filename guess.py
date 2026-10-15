import random
import time

# ---------- Settings ----------
DEBUG_SECRET = None   # For testing, set to a number such as 42. Set back to None before your final commit.
TIME_LIMIT = 60       # Seconds allowed in Time Challenge mode

print("Welcome to the Number Guessing Game")

# ---------- Choose a level ----------
# Goal: keep asking until the player picks a valid level, then set the range and attempt limit.

# Range unspecified for feature 1: classic mode so using fixed range
low = 0
high = 100

# Unpecified attempts for feature 1: classic mode so using 3 for now
attempts_left = 3

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

while attempts_left > 0:
    guess = input(f"Guess a number between {low} to {high}: ")

    # user input should be all digits, if not ask again
    if not guess.isdigit():
        print("Please enter a valid whole number (e.g. 1, 2)")
        print(f"You have {attempts_left} more attempts to guess!!")
        continue

    # convert user input to int (as default is string input)
    guess = int(input())

    # user input is valid but out of range
    if (guess < low) or (guess > high):
        print("Please enter a number within valid range {low} to {high}")
        print(f"You have {attempts_left} more attempts to guess!!")
        continue

    if guess == secret:
        print("correct")
    elif guess < secret:
        print("too low")
    else:
        print("too high")

    # player lost one attempt
    attempts_left -= 1
    
    print(f"You have {attempts_left} more attempts to guess!!")

# ---------- End of round ----------
# Goal: show the result that matches how the round ended.