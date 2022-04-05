def find_sorted(nums, target):
    i = 0
    while i < len(nums) and nums[i] <= target:
        if nums[i] == target:
            return i
        print(f'Not at position {i}')
        i += 1

if __name__ == '__main__':
    find_sorted([1, 2, 3, 5, 6, 7], 4)