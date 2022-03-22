def elements(symbols, nums):
    index = 0
    while index < len(nums) and nums[index] > 0:
        print(symbols[index], nums[index], index)
        index += 1
    
    if index < len(nums) - 1:
        print('Invalid index encountered at position', index)
    

if __name__ == '__main__':
    symbols = ['H', 'He', 'Li', 'Be', 'B', 'B', 'C', 'N', 'O']
    nums = [1, 2, 3, 4, 5, 0, 6, 7, 8]
    elements(symbols, nums)