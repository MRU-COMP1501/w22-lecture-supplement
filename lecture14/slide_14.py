def check_caffeine_wrong(caffeine):
    if caffeine > 50:
        print('Good start')
    elif caffeine > 100:
        print('Perfect amount')
    elif caffeine > 200:
        print('TOO MUCH!')
    else:
        print('You need more!')

if __name__ == '__main__':
    check_caffeine_wrong(55)
    check_caffeine_wrong(150)