# Initialize result to 0
# For each number in the list:
#     square the number and add it to result
# Return the result

def sum_of_squares(nums):
    result = 0
    for num in nums:
        result += num ** 2
        # totally fine to write 
        # result = result + num ** 2
    return result

def main():
    nums = [1, 3, 5, 7, 9]
    print(f'Sum of squares is: {sum_of_squares(nums)}')

main()