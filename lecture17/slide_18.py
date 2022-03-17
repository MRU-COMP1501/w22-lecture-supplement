def sentence_finder(text):
    char = text[0]
    result = ''
    index = 1
    while char != '.':
        result += char 
        char = text[index]
        index += 1
    return result

if __name__ == '__main__':
    sentence = sentence_finder(input('Enter text: '))
    print(sentence)