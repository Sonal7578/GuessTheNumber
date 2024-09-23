import random

def guess(x):
    random_num = random.randint(1, x)
    user_guess = 0
    while user_guess != random_num:
        user_guess = int(input(f'Guess a number between 1 and {x}: '))
        if user_guess < random_num:
            print("Sorry, guess again. Too low.")
        elif user_guess > random_num:
            print("Sorry, guess again. Too high.")
    print(f"Congratulations! You've guessed the number {random_num}!")

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # if low and high are the same, we guess that number
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'Yay! The computer guessed your number, {guess}, correctly!')

# Uncomment the game you want to play
# guess(10)
computer_guess(10)
