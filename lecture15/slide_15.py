def sarcastic(text):
    output = ''
    for i in range(len(text)):
        if i % 2 == 0:
            output += text[i].upper()
        else:
            output += text[i]
    return output

if __name__ == '__main__' :
    text = input('Enter text to make sarcastic: ')
    print(sarcastic(text))
