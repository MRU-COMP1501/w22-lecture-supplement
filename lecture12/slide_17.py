FREE_THRESH = 40

def check_free_delivery(order_amount):
    if order_amount < FREE_THRESH:
        return False
    else:
        return True
    
    # print('This only executes if order_amount >= FREE_THRESH')
    return True

def main():
    order_amount = float(input('How much is your order? '))
    print(check_free_delivery(order_amount))

# Conditional execution of main - only run main if this script is run
# directly, not imported (see slide_18.py)
if __name__ == '__main__':
    main()
# main()