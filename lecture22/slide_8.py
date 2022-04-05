def find_target(nums, target):
    i = 0
    pos = []
    while i < len(nums):
        if nums[i] == target:
            # return i
            pos.append(i)
        i += 1
    return pos

def count_target(nums, target):
    count = 0
    for i in range(len(nums)):
        if nums[i] == target:
            count += 1
    return count

def main():
    nums = [7, 5, 20, 7, 8, 1, 14, 4]
    target = int(input('Enter the number to search for: '))
    index = nums.index(target)
    my_index = find_target(nums, target)
    print(f'{target} is at index position {index}')
    print(f'{target} is at my_index position {my_index}')

if __name__ == '__main__':
    main()