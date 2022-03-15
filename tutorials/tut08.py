# Note: wordle problem in lecture15 folder

def dice_rolls(a, b, c):
    if a == b and a == c: 
        return 'print(3 of a kind!)'

    if (a == b) or (a == c) or (b == c):
        return 'a pair!'
    else:
        return 'Roll again!'

if __name__ == '__main__':
    print(dice_rolls(1, 1, 2))
    print(dice_rolls(1, 1, 1))
    print(dice_rolls(1, 3, 2))