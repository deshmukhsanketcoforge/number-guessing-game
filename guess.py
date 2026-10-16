from ast import While
import random
import time

# ---------- Settings ----------
DEBUG_SECRET = None             # For testing, set to a number such as 42. Set back to None before your final commit.
TIME_LIMIT = 60                 # Seconds allowed in Time Challenge mode
is_correct_guess = False        # flag to track if the player guessed correctly
is_time_up = False              # flag to track if the player ran out of time
attempts_used = 0               # track the number of attempts used

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

mode = None

while True:
    mode = input("Choose a mode:\n1. Classic\n2. Time Challenge\nEnter your choice (1-2): ").strip().lower()

    if mode in ["1", "2"]:
        break
    else:
        print("Invalid choice. Please enter 1 or 2.\n")

start_time = int(time.time())  # record the start time of the round

# ---------- Set up the round ----------
# Goal: pick the secret number (use DEBUG_SECRET when it is not None) and start the clock.

if DEBUG_SECRET is not None:
    secret = DEBUG_SECRET
else:
    secret = random.randint(low, high)

# ---------- Guess loop ----------
# Goal: keep asking for guesses until the player wins, runs out of attempts, or runs out of time.

while attempts_allowed > attempts_used:
    if mode == "2":  # Time Challenge mode
        time_left = TIME_LIMIT - (int(time.time()) - start_time)
        if time_left <= 0:
            is_time_up = True
            break
        print(f"You have {time_left} seconds remaining.")

    guess = input(f"\nGuess a number between {low} to {high}: ")

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
        if mode == "2":  # Time Challenge mode
            time_left = TIME_LIMIT - (int(time.time()) - start_time)
            if time_left <= 0:
                is_time_up = True
                break
        is_correct_guess = True
        print("correct")
        break
    elif guess < secret:
        print("too low\n")
    else:
        print("too high\n")

    print(f"You have {attempts_allowed - attempts_used} attempts remaining.")

# ---------- End of round ----------
# Goal: show the result that matches how the round ended.

if is_time_up:
    print(f"Time's up! The secret number was: {secret}. Better luck next time!")
elif is_correct_guess:
    print(f"Congratulations! You guessed the secret number {secret} correctly, in {attempts_used} attempts!")
else:
    print(f"Game Over! Unfortunately you ran out of attempts. The secret number was: {secret}. Better luck next time!")