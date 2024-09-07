#The task is to implement a guessing game where the computer has a secret number and we are trying to guess that number
import random
random_number = {}
def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}:'))
        if guess < random_number:
            print('Sorry, guess again. Too low')
        elif guess > random_number:
            print('Sorry, guess again. Too High')

guess(50)
print(f'Awesome!! You have guessed the number {random_number} correctly')