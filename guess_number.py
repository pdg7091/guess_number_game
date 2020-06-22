import random

number_of_guesses = 0

print('Hello, what is your name?')
name = input()

number = random.randint(1, 20)
print(f'Hello, {name}, I am thinking of a number between 1 and 20.')

while number_of_guesses < 6:
    print('Take a guess.')
    guess = input()
    guess = int(guess)
    number_of_guesses = number_of_guesses + 1

    if guess < number:
        print('Your guess is too low.')

    if guess > number:
        print('Your guess is too high.')

    if guess == number:
        break

if guess == number:
    number_of_guesses = str(number_of_guesses)
    print(
        f'Good job {name}! You guessed my number in {number_of_guesses} guesses!')

if guess != number:
    number = str(number)
    print(f'Sorry {name}, the number I was thinking of was {number}.')
