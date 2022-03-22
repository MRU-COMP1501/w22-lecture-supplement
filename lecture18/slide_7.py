def get_valid_input():
    # make sure the word has 5 letters
    text = input('Enter a 5 letter word: ')
    while len(text) != 5:
        print('I said 5 letter word')
        text = input('Enter a 5 letter word: ')
    return text

if __name__ == '__main__':
    print(get_valid_input())