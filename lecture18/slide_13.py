# Write a function using a while loop that prompts 
# the user to enter any number. 
# If a non-numeric string is entered 
# (e.g. 'five' or '1.0.1'), 
# inform them that their input is invalid and 
# prompt to try again.

def get_valid_number():
    text = input('Enter a number: ') # priming read
    invalid = True # boolean sentinel
    while invalid:
        try:
            num = float(text)
            invalid = False
        except:
            print('Input is invalid')
            text = input('Enter a number: ') # internal read
    return num

def get_valid_number_break():
    text = input('Enter a number: ') # priming read
    while True:
        try:
            num = float(text)
            break
        except:
            print('Input is invalid')
            text = input('Enter a number: ') # internal read
    return num

if __name__ == '__main__':
    print(get_valid_number())
    print(get_valid_number_break())