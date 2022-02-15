from random import randint

number = randint(1, 10)
guess = int(input('Guess a number between 1 and 10: '))

if guess == number:
    print('You guessed it!')
else:
    print('Nope, better luck next time.')