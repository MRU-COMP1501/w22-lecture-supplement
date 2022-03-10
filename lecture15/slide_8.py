def roulette_colour(num):
    if num % 2 == 0: # even
        if num < 11:
            return 'black'
        elif num < 19:
            return 'red'
        elif num < 29:
            return 'black'
        else:
            return 'red'
    else: # odd
        if num < 11:
            return 'red'
        elif num < 19:
            return 'black'
        elif num < 29:
            return 'red'
        else:
            return 'black'

def roulette_colour_alternate(num):
    if num % 2 == 0: # even
        if num < 11 or num >= 19 and num < 29:
            return 'black'
        if num >= 11 and num < 19 or num >= 29:
            return 'red'
    else: # odd
        if num < 11 or num >= 19 and num < 29:
            return 'red'
        if num >= 11 and num < 19 or num >= 29:
            return 'black'

if __name__ == '__main__':
    for num in range(1, 37):
        print(f'Pocket {num}: {roulette_colour(num)}, '
              f'{roulette_colour_alternate(num)}')