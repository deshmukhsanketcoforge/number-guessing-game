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