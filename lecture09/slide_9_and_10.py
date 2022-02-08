# slide 9
def no_return():
    print('Here be dragons')

# slide 10
def average(num1, num2, score):
    avg = (num1 + num2) / 2
    # print(x) # Error, x is not in scope
    print(score)
    return avg

def main():
    x = no_return()
    print(x)
    y = average(4, 5, x)
    print(y)

main()