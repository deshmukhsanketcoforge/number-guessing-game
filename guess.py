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

# there is not attempt limit for featue 1: classic mode
attempts_used = 0

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

while True:
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
    attempts_used += 1

    if guess == secret:
        print("correct")
        print(f"You guessed the secret number {secret} in {attempts_used} attempts!")
        break
    elif guess < secret:
        print("too low\n")
    else:
        print("too high\n")

# ---------- End of round ----------
# Goal: show the result that matches how the round ended.