try:
    num = float(input('Enter a numerator: '))
    denom = float(input('Enter a denominator: '))
    ratio = num / denom
    some_list = [1, 2]
    index = int(input('Enter a list index: '))
    some_list[index]
except ValueError as e:
    print('Entries must be numbers')
    print(e)
except ZeroDivisionError:
    print('Cannot divide by zero')
except Exception as e:
    print('Something else weird happened')
    print(type(e), e)