def average_inputs():
    percentage = float(input('Enter the first grade to average: '))
    total = 0
    count = 0

    while percentage >= 0:
        total += percentage
        count += 1
        print(f'Running average: {total / count}')
        percentage = float(input('Enter the next grade to average: '))
    
    print(f'The average is {total / count}')

if __name__ == '__main__':
    average_inputs()