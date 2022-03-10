ALCOHOLIC = ['beer', 'wine', 'spirits']

def serve_it(order):
    if order in ALCOHOLIC:
        age = float(input('Show me your ID: '))
        if age >= 18:
            print(f"Here's your {order}")
        else:
            print(f"Sorry, you can't have {order}")
    else:
        print(f"Here's your {order}")

def bad_logic_serve_it(order):
    if order in ALCOHOLIC:
        age = float(input('Show me your ID: '))
        if age >= 18:
            print(f"Here's your {order}")
    else:
        print(f"Sorry, you can't have {order}")
        print(f"Here's your {order}")

if __name__ == '__main__':
    serve_it('spirits')
    serve_it('coke')
