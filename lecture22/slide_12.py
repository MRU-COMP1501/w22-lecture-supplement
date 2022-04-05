def swap_adjacent(some_nums):
    changing = False
    for i in range(1, len(some_nums)):
            prev = some_nums[i - 1]
            if prev < some_nums[i]:
                some_nums[i - 1] = some_nums[i]
                some_nums[i] = prev
                changing = True
    return changing

def sort(nums):
    keep_going = True
    while keep_going:
        print(nums) # debug print
        keep_going = swap_adjacent(nums)

def main():
    nums = [7, 5, 20, 7, 8, 1, 14, 4]
    print(nums)
    sort(nums)

if __name__ == '__main__':
    main()