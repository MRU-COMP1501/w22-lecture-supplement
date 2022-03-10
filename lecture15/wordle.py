# A bunch of stuff to allow imports from an adjacent directory
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[1] / 'lecture14'))
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

def check_word(guess, goal):
    pass

def main():
    goal = random.choice(VALID_WORDS)
    guess = input('Enter a guess: ')
    print(check_word(guess, goal))

if __name__ == '__main__':
    main()