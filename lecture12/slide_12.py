def sum_of_squares(nums):
    result = 0
    for num in nums:
        result += num ** 2
    return result

def sum_of_odd_squares(nums):
    result = 0
    for num in nums:
        if num % 2 == 1:
            result += num ** 2
    return result

def main():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f'Sum of squares is: {sum_of_squares(nums)}')
    print(f'Sum of odd squares is: {sum_of_odd_squares(nums)}')

main()