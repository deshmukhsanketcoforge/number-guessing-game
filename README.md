# number-guessing-game

A user friendly simple number game that currently supports classic mode. In Classic mode, user is expcted to guess a number between 0 to 100. 

**Note**: Invalid inputs are not considered towards attempts used. Invalid inputs includes strings, empty strings, symbols, out of range numbers, floats, and negative integers

-----

## Prerequisites:

Make sure following softwares are installed in your system. If not, please check official documentations or YouTube resources on how to install them on your machine.

1. Python 3.10+
2. Git 
3. Github Desktop App

> Make sure Git is configured using Personal Access Tokens (PAT) or Github Desktop or SSH (via oxygen). If you don't know how to do this please check youtube videos for suitable guide.

> We recommend using Github Desktop, that's what we used for this project. But other methods works perfectly fine too.

## Setup Instructions:

1. Clone Github repo located at: https://github.com/deshmukhsanketcoforge/number-guessing-game using Github Desktop (You can do it using SSH or HTTP method as well)

## How to tun the program:

1. Open your preferred code editor
2. Select "Open Folder" -> Select the cloned github repository
3. Open "Terminal" and use command 

> python3 guess.py

**Note:** As per scope of feature 1 Classic mode, the program keeps running until you make correct guess 

----

## Test Coverage

| # | What I tested | What I did | Expected result | Actual result | Pass? |
|---|---------------|------------|-----------------|---------------|-------|
| 1 |Classic mode: input out of range|Used out of range negative and positive integers|Proper error message with number of attempts left| Recived detailed error messgae with number of attempts left|Yes|
| 2 |Classic mode: valid "integer" input within given input|Used valid integer for happy flow test|Should print either "too low", "too high" or "correct"|Program got stuck, due to multiple input statements, FIX: Changed the code by using existing input for int conversion|No|
| 3 |Classic mode: tested for boundary cases for "high" variable|high variable was 100, so tested program for 99, 100, 101|Should get either "too low", "too high" or "correct" for 99, 100 and should get "invalid input" message for 101|Got edge cases covered as per expectations|Yes|
| 4 |Classic mode: tested for boundary cases for "low" variable|low variable was 0, so tested program for -1, 0, 1|Should get either "invalid input" for -1; "too low", "too high" or "correct" for 0 and 1|Got edge cases covered as per expectations|Yes|
| 5 |Classic mode: check number of attempts update for invalid and valid inputs|Tried all invalid inputs (floats, strings, empty strings, outside range, negative numbers)| Number of attempts left should not update for invalid inputs|Number of attempts left did not update for invalid inputs|Yes|
| 6 |Classic mode: check if program exits after correct guess|Increase number of guesses to 10 and planned to use binary search to detrministically find the correct number within 10 attempts and range [0, 100]|Eventually should be able to get the correct guess and program should end with correct message|Program did display correct guess, but did not exit. FIX: added break statement inside while loop|No|
| 7 |Classic mode: test using actual DEBUG_SECRET variable rather than binary search|Set DEBUG_SECRET=42 to check if we are able to validate the result|42 should be correct guess and program should terminate|Program did terminate, but instead of attempts left we need attempts used. Fix: update "attempts_left" logic to be "attempts_used"|No|
| 8 |Difficulty level: check invalid inputs for seelcting difficulty level|Tried giving invalid inputs (empty string, string, any number other than 1,2 or 3)|Program should say "Invalid Input" and keep asking to pick diffculty level until a valid one is picked.|Program did stay in loop to keep asking for valid input|Yes|
| 9 |Difficulty level: check if valid guess exits the program with correct message|Tested with DEBUG_SECRET = 42 and guessed the same number in first attempt with EASY difficulty|Program should say "Correct" and reveal a nice user friendly congratulations message|Program did exit with "correct" and congratulations message|Yes|
| 10 |Difficulty level: in real mode try to guess incorrect 10 times in EASY mode, to see if game ends (due to player ran out of attempt) and reveals secret number|Guessed same "incorrect" number 10 times in EASY mode|Program should exit with proper "out of attempts" message and should reveal the secret number|Program did exit with appropriate message and revealed the secret number|Yes|
| 11 |Difficulty level: Validate range variable values and number of attempts for each mode|Tried with DEBUG_SECRET = 42, and for each mode tested if it takes correct number of attempts for valid/invalid inputs.|Code terminates and reveals secret number|Code terminated and revealed the secret number|Yes|
| 12 |Timed Challenge: Validate if program actually terminates because of TIME OUT, despite correct input|Used DEBUG_SECRET = 42, but didn't guessed it correct for a minute to achieve time out, but then used 42 as correct guess|Program SHOULD NOT say it was correct, as it was given after time out|Program went into negative time. FIX: added if condition to break the while loop|No|
| 13 |Timed Challenge: Validate if correct guess before and after timeout works|with DEBUG_SECRET = 42, waited for timeout and also answered before timeout to see the result|Correct guess AFTER timeout should say "Time up!", Correct guess BEFORE timeout should say "Correct guess" and reveal secret number|Both cases worked as per expectations|Yes|
| 14 |Timed Challenge: Classic mode should not trigger timer|Chose "Classic" mode and saw if it was showing timer after each guess|Timer shouldn't be visible in classic mode, but only number of guesses and low, high or correct should show up|Timer wasn't visible, correct out for "low", "high" and "correct" was being displayed with number of attempts left|Yes|
| 15 |Timed Challenge: Invalid input test for classic or time challenge|Pass invalid input(string, floats, empty strings, out of choice) to see if program keeps asking for valid choice with proper message|Program should stay in loop until valid input is given by the user|Program stayed in loop until user gave one of the valid options|Yes|
| 16 |Timed Challenge: Works along with EASY, MEDIUM and HARD mode|Checked if we are able to play in timed mode for all three difficulty level|Program should satisfy all above test|Program worked fine in all modes with all above tests|Yes|
