import math
import slide_17

def main():
    order = 50
    if slide_17.check_free_delivery(order):
        print('Yay, free!')
    else:
        print('Not yet')

if __name__ == '__main__':
    main()