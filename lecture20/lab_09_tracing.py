TARGET = 5
counter = 0

prompt = 'Enter a guess: '
guess = int(input(prompt))
while guess != TARGET:
    counter += 1
    print('Sorry, guess again')
    guess = int(input(prompt))