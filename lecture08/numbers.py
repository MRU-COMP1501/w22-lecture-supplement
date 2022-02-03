def average(num1, num2):
    avg = (num1 + num2) / 2
    return avg

def main():
    x = float(input('Enter the first number: '))
    y = float(input('Enter the second number: '))
    xy_avg = average(x, y)
    print(f'The average is {xy_avg}')

main()