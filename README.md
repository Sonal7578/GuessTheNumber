# Number Guessing Game README

## Overview
This Python project is a simple number guessing game that includes two different game modes:
1. **User Guessing Game**: The computer selects a random number, and the user attempts to guess it.
2. **Computer Guessing Game**: The user selects a number, and the computer attempts to guess it based on user feedback.

Both game modes demonstrate the use of Python's control flow structures such as loops, conditionals, and user input.

## Requirements
- Python 3.x
- No external libraries are required as the game uses built-in Python modules.

## How to Use

### Game Modes
There are two modes in this project:
1. **User Guessing Game**: The computer picks a random number within a range, and the user tries to guess it.
2. **Computer Guessing Game**: The user thinks of a number, and the computer guesses it based on user feedback (too high, too low, or correct).

### Functions
1. **`guess(x)`**:
   - Parameters:
     - `x`: The upper bound for the random number the computer generates.
   - Objective: The user has to guess a number between 1 and `x`. The function provides hints whether the guessed number is too high or too low.
   - Example:
     ```python
     guess(10)
     ```

2. **`computer_guess(x)`**:
   - Parameters:
     - `x`: The upper bound for the range in which the user has chosen a number.
   - Objective: The computer tries to guess the number that the user has in mind. The user gives feedback whether the guess is too high (`H`), too low (`L`), or correct (`C`).
   - Example:
     ```python
     computer_guess(10)
     ```

### How to Play

1. **User Guessing Game**:
   - Uncomment the `guess(x)` line in the code (where `x` is any upper bound integer, such as 10).
   - Run the script.
   - The program will ask you to guess a number between 1 and `x`. Based on your input, it will guide you until you guess correctly.

2. **Computer Guessing Game**:
   - Uncomment the `computer_guess(x)` line in the code (where `x` is the upper bound for the number you're thinking of).
   - Run the script.
   - Think of a number between 1 and `x`, and the computer will try to guess it based on your feedback (`H`, `L`, or `C`).

### Example
#### User Guessing Game:
```python
guess(10)
```
- The computer will choose a number between 1 and 10.
- You will try to guess the number based on hints until you get it right.

#### Computer Guessing Game:
```python
computer_guess(10)
```
- You think of a number between 1 and 10.
- The computer will attempt to guess it based on your feedback (`H`, `L`, `C`).

## Customization
- You can change the upper limit of the guessing range by passing different values for `x` in both functions.
- Modify the feedback messages or rules of guessing for a more personalized game experience.

## Running the Game
1. Download or copy the script into a Python environment.
2. Uncomment the desired game mode function call at the bottom of the script.
3. Run the Python file:
   ```bash
   python filename.py
   ```

## License
This project is free to use for educational and personal purposes.

Enjoy the game!