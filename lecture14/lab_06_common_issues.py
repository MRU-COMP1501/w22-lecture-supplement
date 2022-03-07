from word_list import VALID_WORDS

def word_in_list():
    """Check for word in list, not equality"""

    word = 'debug'
    if word in VALID_WORDS:
        print(f'{word} is in the list!')

    # This is not the same thing!
    if word == VALID_WORDS:
        print(f'{word} is the same list as VALID_WORDS')
    else:
        print("This probably isn't the comparison you wanted")


if __name__ == '__main__':
    word_in_list()
    
    # redefine input as input - only works in global scope
    input = input('What is your name? ')
    print(f'You entered {input}')

    input = input('What is your quest? ')
    print(f'You entered {input}')
