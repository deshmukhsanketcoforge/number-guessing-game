# number-guessing-game

A user friendly simple number game that supports multiple difficulty levels and two game modes: Classic and Time Challenge. The program picks a secret number within a range based on the level you choose, and you try to guess it before you run out of attempts (or time).

### Levels

| Level | Number range | Attempts allowed |
|-------|--------------|------------------|
|1. Easy | 1 to 50 | 10 |
|2. Medium | 1 to 100 | 8 |
|3. Hard | 1 to 200 | 10 |

### Modes
**Classic:** Guess the secret number within the allowed attempts. There is no time limit.
**Time Challenge:** Same as Classic, but you must also guess the number within 60 seconds. The remaining time is shown before every guess. If time runs out, the round ends and the secret number is revealed.

After every valid guess, the game tells you if your guess was "too low" or "too high" and how many attempts you have remaining.

> Note: Invalid inputs are not counted towards attempts used. Invalid inputs include strings, empty strings, symbols, out of range numbers, floats, and negative integers.

### Prerequisites:

Make sure following softwares are installed in your system. If not, please check official documentations or YouTube resources on how to install them on your machine.

```txt
Python 3.10+
Git
Github Desktop App
```

Make sure Git is configured using Personal Access Tokens (PAT) or Github Desktop or SSH (via oxygen). If you don't know how to do this please check youtube videos for suitable guide.

> We recommend using Github Desktop, that's what we used for this project. But other methods work perfectly fine too.

### Setup Instructions:

- Clone Github repo located at: https://github.com/deshmukhsanketcoforge/number-guessing-game using Github Desktop (You can do it using SSH or HTTP method as well)
- How to run the program:
Open your preferred code editor
Select "Open Folder" -> Select the cloned github repository
Open "Terminal" and use command

```python
python3 guess.py
```

Choose a level (1-3) when prompted
Choose a mode (1 for Classic, 2 for Time Challenge) when prompted
Start guessing!

> Note: The round ends when you guess the number correctly, run out of attempts, or (in Time Challenge mode) run out of time. A message at the end tells you which of these happened and reveals the secret number if you did not win.

----

## Test Coverage

| # | What I tested | What I did | Expected result | Actual result | Pass? |
|---|---------------|------------|-----------------|---------------|-------|
| 1 | **Classic mode:** guess too low | Set DEBUG_SECRET=42 and guessed 10 | Should print "too low" | got "too low" | Yes |
| 2 | **Classic mode:** guess too high | Set DEBUG_SECRET=42 and guessed 90 | Should print "too high" | got "too high" | Yes |
| 3 | **Classic mode:** correct guess with right attempt count | Set DEBUG_SECRET=42 and guessed 42 on the first attempt in EASY mode | Should print "correct" with a congratulations message, report the attempts used, and the program should exit | Program did exit with "correct" and congratulations message with attempts used | Yes |
| 4 | **Classic mode:** invalid input (letters) | Entered strings (e.g. "abc") as a guess | Should print "invalid input" and the number of attempts left should not change | Number of attempts left did not update for invalid inputs | Yes |
| 5 | **Classic mode:** invalid input (blank entry) | Entered an empty string as a guess | Should print "invalid input" and the number of attempts left should not change | Number of attempts left did not update for invalid inputs | Yes |
| 6 | **Classic mode:** number below range | Entered -1 (low is 0) and other out of range negative integers | Should print an error message with the number of attempts left, and attempts should not change | Received detailed error message with number of attempts left, attempts did not update | Yes |
| 7 | **Classic mode:** number above range | Entered 101 (high is 100) and other out of range positive integers | Should print an error message with the number of attempts left, and attempts should not change | Received detailed error message with number of attempts left, attempts did not update | Yes |
| 8 | **Difficulty level:** EASY range and attempt limit | Chose EASY and read the game header | Range should be `1`-`50` and attempt limit should be `10` | Range boundaries were correct, with attempts limit 10 | Yes |
| 9 | **Difficulty level:** MEDIUM range and attempt limit | Chose MEDIUM and read the game header | Range should be `1`-`100` and attempt limit should be `8` | Range boundaries were correct, with attempts limit 8 | Yes |
| 10 | **Out of attempts:** game ends | Guessed the same incorrect number 10 times in EASY mode | Should print an "out of attempts" message and the program should exit | Program did exit with appropriate message | Yes |
| 11 | **Out of attempts:** secret number revealed | Same run as #11, checked the final message | Should reveal the secret number | Program revealed the secret number | Yes |
| 12 | **Timed Challenge:** timeout ends the game | Started Timed Challenge and waited past the time limit without guessing | Should print "Time up!" and the program should exit | Got the time out message | Yes |
| 13 | **Timed Challenge:** secret number revealed on timeout | Same run as #13, checked the final message | Should reveal the secret number (42) | Secret number was revealed after time out and it was real one | Yes |
| 14 | **Timed Challenge:** correct guess after timeout is rejected | Used DEBUG_SECRET=42, waited past the time limit, then entered 42 | Should print "Time up!" and should NOT say it was correct | Correct guess AFTER timeout said "Time up!" as expected | Yes |
| 15 | **Timed Challenge:** remaining time shown before first guess | Started Timed Challenge and looked at the first prompt | Remaining time should be displayed before the guess prompt | timer was being displayed before each guess on top | Yes |
| 16 | **Timed Challenge:** remaining time shown before every guess | Made 3 wrong guesses and checked each prompt | Remaining time should be displayed before each guess and should decrease between guesses | Time was decreasing with each guess and it "Timed out" after 60 secs | Yes |
| 17 | **Classic mode:** timer not shown | Chose Classic and made a few guesses | Remaining time should not be displayed at any prompt | Timer wasn't visible, only the number of attempts left and low, high or correct output were displayed | Yes |
| 18 | **Classic mode:** program does not get stuck on valid input | Entered a valid integer within range | Should print "too low", "too high" or "correct" without asking for input twice. **Earlier bug:** program got stuck because of multiple input statements. **FIX:** reused the existing input for the int conversion | Program got stuck, fixed by reusing the existing input for int conversion | No |
| 19 | **Classic mode:** program exits after correct guess | Guessed the correct number with 10 attempts available | Should print the correct message and exit. **Earlier bug:** program printed correct but kept running. **FIX:** added a break statement inside the while loop | Program displayed correct guess but did not exit, fixed with a break statement | No |
| 20 | **Classic mode:** attempts used shown on correct guess | Set DEBUG_SECRET=42 and guessed 42 | Should show attempts used instead of attempts left. **FIX:** changed "attempts_left" logic to "attempts_used" | Program terminated but showed attempts left, fixed by switching to attempts_used | No |
| 21 | **Difficulty level:** HARD range and attempt limit | Chose HARD and read the game header | Range should be `1`-`500` and attempt limit should be `10` | Range boundaries were incorrect, with attempts limit 10. **Fix:** Correct the value for high variable and verified by reexcution | No |
| 22 | **Timed Challenge:** remaining time never goes negative | Waited past the time limit in a Timed Challenge, then entered a guess | Should end the game instead of showing negative time. **FIX:** added an if condition to break the while loop | Program went into negative time, fixed by adding a break condition | No |