# Goal: modify the pig latin translator program from lecture to
# translate an entire sentence instead of just a word

def translate_to_pig(word):
    # take the first letter, put it on the end
    # then add "ay"
    # word[1:] is the same as word[1:len(word)]
    pig_word = word[1:] + word[0] + 'ay'
    return pig_word

def translate_sentence(sentence):
    # loop through all the words in the sentence by splitting on whitespace.
    # Note: this does not handle punctuation!
    result = ''
    for word in sentence.split():
        result += translate_to_pig(word) + ' '
    
    return result

def main():
    input_str = input('What would you like to translate? ')
    print(f'"{input_str}" in pig latin is:')
    print(translate_sentence(input_str))

main()