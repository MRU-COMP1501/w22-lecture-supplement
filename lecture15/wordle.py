from word_list import VALID_WORDS

import random

# NOTE: Colours may not work on all terminals! Git Bash appears
# to not support this, so try powershell or Command Prompt
GREEN = '\u001b[42;1m\u001b[30;1m'
YELLOW = '\u001b[43;1m\u001b[30;1m'
RESET = '\u001b[0m'

def green(txt):
    return GREEN + txt + RESET

def yellow(txt):
    return YELLOW + txt + RESET

# Write the solution here
# Write a function that takes a guess word 
# and a goal word then returns a new version of guess where:

# Letters in the correct position are green
# Letters that are in goal but in the incorrect position are yellow
# All other letters are unchanged
def check_word(guess, goal):
    result = ''
    for i in range(len(goal)):
        letter = guess[i]
        if letter == goal[i]:
            result += green(letter)
        elif letter in goal:
            result += yellow(letter)
        else:
            result += letter

    return result

def main():
    goal = random.choice(VALID_WORDS)
    guess = input('Enter a guess: ')
    print(check_word(guess, goal))

if __name__ == '__main__':
    main()