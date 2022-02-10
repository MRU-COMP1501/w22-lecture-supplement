def translate_to_pig(word):
    # take the first letter, put it on the end
    # then add "ay"
    # word[1:] is the same as word[1:len(word)]
    pig_word = word[1:] + word[0] + 'ay'
    return pig_word

def main():
    input_str = input('What word would you like to translate? ')
    print(f'{input_str} in pig latin is {translate_to_pig(input_str)}')

main()