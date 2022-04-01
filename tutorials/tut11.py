from circle import Circle

def get_larger(circ_1, circ_2):
    if circ_1.get_radius() > circ_2.get_radius():
        return circ_1
    else:
        return circ_2

def main():
    circle_1 = Circle(10.5)
    circle_2 = Circle(3)
    print(circle_1)
    print(circle_2)
    print(f'The largest is {get_larger(circle_1, circle_2)}')

if __name__ == '__main__':
    main()