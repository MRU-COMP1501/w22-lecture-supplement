def swap_adjacent(some_nums):
    # comment out the next line to see it modified in place
    some_nums = some_nums.copy()
    for i in range(1, len(some_nums)):
        prev = some_nums[i - 1]
        if prev < some_nums[i]:
            some_nums[i - 1] = some_nums[i]
            some_nums[i] = prev
    return some_nums

def main():
    nums = [1, 3, 0, 4, 2]
    print('Original:', nums)
    print('Swapped:', swap_adjacent(nums))
    print('After:', nums)

if __name__ == '__main__':
    main()